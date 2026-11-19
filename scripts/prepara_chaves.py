#!/usr/bin/env python3
"""Prepara o arquivo das chaves a partir do exemplo, sem ler nem mostrar valor nenhum.

Uso, da raiz do repositório:
  python -X utf8 scripts/prepara_chaves.py                          # cria o .env a partir do .env.example
  python -X utf8 scripts/prepara_chaves.py --settings               # cria o .claude/settings.local.json do exemplo
  python -X utf8 scripts/prepara_chaves.py --skill research         # cria e diz que linhas a research pede
  python -X utf8 scripts/prepara_chaves.py --settings --skill image-gen

Só cria quando o destino não existe: nunca sobrescreve, e nunca lê nem imprime um destino que já existe
(diz que ele já existe e sai com 0). As linhas que se indicam vêm do exemplo, de que o arquivo novo é cópia
exata. Quem cola a chave é a pessoa, no editor dela; o Claude nunca abre o arquivo preenchido.

O que cada skill pede vem da tabela do `scripts/confere_ambiente.py`, a fonte única.
Código de saída: 0 criado ou já existente; 2 uso errado (skill desconhecida) ou exemplo ausente.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "scripts"))
import confere_ambiente  # noqa: E402

ALVOS = {
    # opção: (o exemplo, o destino, como se acha a linha da variável no exemplo)
    "env": (".env.example", ".env", lambda nome, linha: linha.startswith(nome + "=")),
    "settings": (".claude/settings.local.example.json", ".claude/settings.local.json",
                 lambda nome, linha: linha.strip().startswith(f'"{nome}"')),
}


def variaveis(skill: str) -> list[tuple[str, str]]:
    """(nome, papel) de cada variável que a skill usa, na ordem da tabela, sem repetir."""
    r = confere_ambiente.SKILLS[skill]
    grupos = [
        ("obrigatória", list(r.get("chaves", []))),
        ("obrigatória, basta uma do grupo", [c for g in r.get("uma_de", []) for c in g]),
        ("liga o modo completo", [c for c, _ in r.get("frentes", {}).values()]),
        ("só para subir ao bucket, com --upload", list(r.get("upload", []))),
        ("opcional", list(r.get("chaves_opc", []))),
    ]
    vistos: dict[str, str] = {}
    for papel, nomes in grupos:
        for c in nomes:
            vistos.setdefault(c, papel)
    return list(vistos.items())


def linha_no_exemplo(exemplo: Path, nome: str, casa) -> int | None:
    for i, linha in enumerate(exemplo.read_text(encoding="utf-8-sig").splitlines(), start=1):
        if casa(nome, linha):
            return i
    return None


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--settings", action="store_true",
                    help="cria o .claude/settings.local.json (bloco env) no lugar do .env")
    ap.add_argument("--skill", help="depois de criar, diz que variáveis esta skill pede e em que linha preencher")
    ap.add_argument("--raiz", type=Path, default=RAIZ, help=argparse.SUPPRESS)  # para o teste
    a = ap.parse_args(argv)

    if a.skill and a.skill not in confere_ambiente.SKILLS:
        print(f"[ERRO] skill desconhecida: {a.skill}. Conhecidas: {', '.join(confere_ambiente.SKILLS)}.")
        return 2

    rel_ex, rel_dest, casa = ALVOS["settings" if a.settings else "env"]
    exemplo, destino = a.raiz / rel_ex, a.raiz / rel_dest
    if not exemplo.is_file():
        print(f"[ERRO] falta o exemplo {rel_ex} na raiz do repositório: sem ele, não há de onde criar o {rel_dest}.")
        return 2

    criado = False
    if destino.exists():
        print(f"[OK] o {rel_dest} já existe; abra no seu editor. Este script não o lê nem o altera.")
        if a.settings:
            print(f"  Se ele ainda não tem o bloco \"env\", copie o bloco do {rel_ex} para dentro dele.")
    else:
        destino.parent.mkdir(parents=True, exist_ok=True)
        try:
            with open(destino, "xb") as f:  # "x": não cria por cima de um arquivo que apareceu no meio-tempo
                f.write(exemplo.read_bytes())
        except FileExistsError:
            print(f"[OK] o {rel_dest} já existe; abra no seu editor. Este script não o lê nem o altera.")
        else:
            criado = True
            print(f"[OK] criado o {rel_dest}, cópia do {rel_ex} (fora do git). Abra no seu editor e troque o "
                  "marcador COLE_... pelo valor, só nas linhas das skills que você vai usar.")

    if a.skill:
        nomes = variaveis(a.skill)
        if not nomes:
            print(f"A skill {a.skill} não pede chave.")
        else:
            print(f"A skill {a.skill} usa, no {rel_dest}:")
            for nome, papel in nomes:
                if criado:
                    n = linha_no_exemplo(exemplo, nome, casa)
                    onde = f"linha {n}" if n else "linha não encontrada no exemplo: acrescente-a"
                else:  # o arquivo existente não se lê: a linha dele pode ser outra
                    onde = f"procure a linha {nome}=" if not a.settings else f"procure \"{nome}\" no bloco \"env\""
                print(f"  - {nome} ({papel}): {onde}")
    print("Cole a chave no seu editor, nunca na conversa com o Claude. Depois, reinicie a sessão do Claude Code e "
          "confira: python -X utf8 scripts/confere_ambiente.py" + (f" --skill {a.skill}" if a.skill else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
