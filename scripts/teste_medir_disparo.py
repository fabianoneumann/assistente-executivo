"""Testa o medir_disparo.py sem o CLI de verdade: um `claude` falso (este mesmo arquivo, com --falso <cenário>)
imprime os eventos do stream-json de cada cenário, e a retomada roda sobre um projeto mínimo numa pasta temporária.
Cobre o "result" com erro contado como resposta, a saída sem "result", a rodada que falhou nunca refeita e a rodada
de outra descrição reaproveitada.

Uso: python -X utf8 scripts/teste_medir_disparo.py   (de qualquer pasta; sai com erro se algum caso falhar)
"""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
from pathlib import Path

CENARIOS = {
    "skill": [{"type": "assistant", "message": {"content": [
        {"type": "tool_use", "name": "Read", "input": {"file_path": "index.md"}}]}},
        {"type": "assistant", "message": {"content": [
            {"type": "tool_use", "name": "Skill", "input": {"skill": "piece-creation"}}]}}],
    "sem_skill": [{"type": "result", "subtype": "success", "is_error": False}],
    "erro": [{"type": "result", "subtype": "error_during_execution", "is_error": True}],
    "sucesso_com_erro": [{"type": "result", "subtype": "success", "is_error": True}],
    "turnos": [{"type": "result", "subtype": "error_max_turns", "is_error": True}],
    "sem_result": [],
}

if len(sys.argv) > 2 and sys.argv[1] == "--falso":  # o claude falso
    for ev in CENARIOS[sys.argv[2]]:
        print(json.dumps(ev), flush=True)
    sys.exit(0)

spec = importlib.util.spec_from_file_location("medir_disparo", Path(__file__).with_name("medir_disparo.py"))
md = importlib.util.module_from_spec(spec)
spec.loader.exec_module(md)
falhas: list[str] = []


def caso(nome: str, ok: bool, detalhe: str = "") -> None:
    print(("ok    " if ok else "FALHA ") + nome + (f" ({detalhe})" if detalhe and not ok else ""), flush=True)
    if not ok:
        falhas.append(nome)


def rodar(cenario: str) -> dict:
    popen = md.subprocess.Popen
    md.subprocess.Popen = lambda cmd, **kw: popen([sys.executable, __file__, "--falso", cenario], **kw)
    try:
        return md.uma_rodada("pedido", Path(tempfile.gettempdir()), None, 30, "claude")
    finally:
        md.subprocess.Popen = popen


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    r = rodar("skill")
    caso("1. chama a skill depois de um Read: a skill e a ferramenta antes", r["skill"] == "piece-creation"
         and r["antes"] == ["Read"] and r["respondeu"], str(r))
    r = rodar("sem_skill")
    caso("2. termina sem skill (result success): respondeu, sem skill", r["respondeu"] and r["skill"] is None, str(r))
    for c in ("erro", "sucesso_com_erro"):
        r = rodar(c)
        caso(f"3. result com erro ({c}): não conta como resposta", not r["respondeu"], str(r))
    r = rodar("turnos")
    caso("4. limite de turnos sem skill: o modelo decidiu, conta como resposta", r["respondeu"]
         and r["fim"] == "limite de turnos sem skill", str(r))
    r = rodar("sem_result")
    caso("5. o CLI fecha sem o evento result: não conta como resposta", not r["respondeu"], str(r))

    # a retomada: a rodada que respondeu se pula, a que falhou roda de novo, e outra descrição refaz tudo
    with tempfile.TemporaryDirectory(prefix="teste-disparo-") as t:
        tmp = Path(t)
        raiz = tmp / "projeto"
        (raiz / ".claude/skills/x").mkdir(parents=True)
        skill_md = raiz / ".claude/skills/x/SKILL.md"
        skill_md.write_text("---\nname: x\ndescription: faz x\n---\n", encoding="utf-8")
        casos = tmp / "casos.json"
        casos.write_text(json.dumps([{"query": "faz x", "should_trigger": True},
                                     {"query": "faz y", "should_trigger": False}]), encoding="utf-8")
        saida = tmp / "saida"
        chamadas: list[str] = []
        respostas = {"faz x": {"skill": "x", "antes": [], "fim": "chamou skill", "segundos": 0, "respondeu": True},
                     "faz y": {"skill": None, "antes": [], "fim": "timeout", "segundos": 0, "respondeu": False}}
        original = md.uma_rodada
        md.uma_rodada = lambda q, *a: (chamadas.append(q), dict(respostas[q]))[1]
        argv = ["--skill", "x", "--casos", str(casos), "--saida", str(saida), "--rodadas", "1", "--raiz", str(raiz)]

        def roda() -> int:
            sys.argv = ["medir_disparo.py", *argv]
            try:
                md.main()
            except SystemExit as e:
                return e.code
            return 0
        try:
            rc = roda()
            caso("6. primeira rodada: as duas rodam, e a do timeout vai para sem_resposta (código 2)",
                 sorted(chamadas) == ["faz x", "faz y"] and rc == 2, f"{chamadas}, código {rc}")
            chamadas.clear()
            respostas["faz y"] = {"skill": None, "antes": [], "fim": "terminou sem skill", "segundos": 0,
                                  "respondeu": True}
            rc = roda()
            res = json.loads((saida / "resumo.json").read_text(encoding="utf-8"))
            caso("7. de novo: só a que falhou roda; o resumo fecha 2 de 2 (código 0)",
                 chamadas == ["faz y"] and rc == 0 and res["acertos"] == 2 and res["sem_resposta"] == 0,
                 f"{chamadas}, código {rc}, {res.get('acertos')}")
            chamadas.clear()
            roda()
            caso("8. de novo, sem mudar nada: nenhuma roda", chamadas == [], str(chamadas))
            skill_md.write_text("---\nname: x\ndescription: faz x e mais\n---\n", encoding="utf-8")
            roda()
            caso("9. a descrição mudou: as duas rodam de novo", sorted(chamadas) == ["faz x", "faz y"], str(chamadas))
        finally:
            md.uma_rodada = original

    linhas = md.resumir([{"query": "q", "should_trigger": False}],
                        {md.chave("q", n, "v"): {"skill": s, "respondeu": True} for n, s in
                         enumerate(["x", None, "plugin:x"])}, "x", 3, "v")
    caso("10. resumir: 2 de 3 rodadas chamaram (o nome com prefixo de plugin conta), não devia: erro",
         linhas["casos"][0]["taxa"] == 2 / 3 and linhas["casos"][0]["passou"] is False, str(linhas["casos"][0]))
    print("TODOS OK" if not falhas else f"{len(falhas)} FALHA(S): {falhas}")
    sys.exit(1 if falhas else 0)


if __name__ == "__main__":
    main()
