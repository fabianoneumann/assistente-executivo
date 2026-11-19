"""Teste do registro.py sem rede: as linhas de registro em qualquer linha do comentário, a data de dois dias,
o comentário que só cita um registro, a correção de numeração e a repostagem.

    python -X utf8 .claude/skills/review/scripts/teste_registro.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import registro  # noqa: E402

FALHAS = []


def caso(nome, cond):
    print(("ok     " if cond else "FALHOU ") + nome)
    if not cond:
        FALHAS.append(nome)


L = "c | d | e | f | g | h | i | j | k | a ver | m | n"  # os 12 campos depois da data e do número
corpos = [
    f"2026-01-14 | registro 1 | {L}",
    f"2026-01-14 | registro 2 | {L}\n\n2026-01-14 | registro 3 | {L}",  # o segundo registro na segunda linha
    f"2026-01-14/15 | registro 4 | {L}",  # a data de dois dias
    "Comentário que só cita o 2026-01-14 | registro 9 no meio da linha.",
    f"`2026-01-15 | registro 5 | {L}`",  # entre crases
    f"2026-01-15 | registro 5 | outra sessão | {L[4:]}",  # número repetido, de outro trabalho
    "Correção de numeração: o segundo 5 é o **registro 6**",
    f"2026-01-15 | registro 4 | {L}\n\n(Repostado.)",  # a repostagem do 4, com a data acertada
]
linhas, numero_de = registro.ler_registros(corpos)
nums = [numero_de[u] for u in range(len(linhas))]
caso("lê a segunda linha do comentário e a data de dois dias", nums[:4] == [1, 2, 3, 4])
caso("não conta o comentário que só cita um registro no meio da linha", 9 not in nums)
caso("a correção de numeração renumera o repetido mais recente", nums == [1, 2, 3, 4, 5, 6])
caso("a linha entre crases sai sem a crase do fim", not linhas[4][1].endswith("`"))
caso("a repostagem com a data acertada conta uma vez só", nums.count(4) == 1)
caso("depois da repostagem, o próximo número é o seguinte ao maior", max(nums) + 1 == 7)
citado = registro.ler_registros([f"> 2026-01-16 | registro 3 | {L}"])[0]
caso("a linha citada em markdown (\">\") não conta como registro", citado == [])
comp = {int(m.group(1)) for m in registro.COMPLEMENTO.finditer("Complemento do registro 1: nada.\n\nComplemento do registro 2: nada.")}
caso("dois complementos no mesmo comentário contam os dois", comp == {1, 2})
caso("cada linha tem os 14 campos do formato", all(len(l.split(" | ")) in registro.CAMPOS_DO_FORMATO for _, l in linhas))
caso("o \"a ver\" está no antepenúltimo campo", all(l.split(" | ")[-3] == "a ver" for _, l in linhas))

print(f"\n{len(FALHAS)} falha(s)")
sys.exit(1 if FALHAS else 0)
