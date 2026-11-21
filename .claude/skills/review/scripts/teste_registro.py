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

# A reserva, a colisão da reserva e a série de lotes.
com_reserva = [f"2026-11-21 | registro 1 | {L}", "Reserva do registro 2: o kit (marca aa)"]
_, nd = registro.ler_registros(com_reserva)
res = registro.ler_reservas(com_reserva)
caso("a reserva ocupa o número: o próximo é o 3", registro.proximo_numero(nd.values(), res) == 3)
caso("a reserva não conta como registro", list(nd.values()) == [1])

# reservar(): a primeira tentativa colide (outra sessão reservou o mesmo número antes), cancela a perdida e a
# segunda passa (re-revisão).
issue_falsa = [f"2026-11-21 | registro 1 | {L}"]
postados = []


def postar(corpo):
    if not postados:  # outra sessão chega antes, com o mesmo número
        issue_falsa.append("Reserva do registro 2: outra sessão (marca 0f0f)")
    issue_falsa.append(corpo)
    postados.append(corpo)


n_res = registro.reservar("270", "a minha revisão", ler=lambda _: list(issue_falsa), postar=postar,
                          esperar=lambda: None)
caso("a reserva que colide tenta o número seguinte", n_res == 3)
caso("a reserva perdida é cancelada com a marca dela",
     len(postados) == 3 and postados[1].startswith("Cancelada a reserva do registro 2 (marca ")
     and registro.MARCA.search(postados[0]).group(1) in postados[1])
caso("a reserva vencedora traz o trabalho e a marca", "a minha revisão" in postados[-1] and "(marca " in postados[-1])
caso("colidiu: um registro já com o número conta como colisão",
     registro.colidiu([f"2026-11-21 | registro 2 | {L}", "Reserva do registro 2: x (marca 01)"], 2, "01"))
caso("colidiu: a reserva única e sem registro é nossa",
     not registro.colidiu(["Reserva do registro 2: x (marca 01)"], 2, "01"))

# A reserva que demora a aparecer: a primeira releitura não a vê, a segunda vê; não se cancela.
atrasada, posts2, leituras = [], [], [0]


def ler_atrasado(_):
    leituras[0] += 1
    return list(atrasada) if leituras[0] != 2 else [c for c in atrasada if not c.startswith("Reserva")]


def postar2(corpo):
    atrasada.append(corpo)
    posts2.append(corpo)


n2 = registro.reservar("270", "y", ler=ler_atrasado, postar=postar2, esperar=lambda: None)
caso("a reserva que demora a aparecer se relê, sem cancelar", n2 == 1 and len(posts2) == 1)

# O cancelamento: a reserva cancelada sai das abertas, mas o número continua usado.
canc = [f"2026-11-21 | registro 1 | {L}", "Reserva do registro 2: z (marca 0a)",
        "Cancelada a reserva do registro 2 (marca 0a): a revisão não rodou"]
caso("a reserva cancelada sai das ativas", registro.ler_reservas(canc) == [])
caso("o número cancelado não volta a ser oferecido",
     registro.proximo_numero([1], registro.ler_reservas(canc, com_canceladas=True)) == 3)
caso("o cancelamento sem marca cancela todas as reservas do número, e só dele",
     [r[1] for r in registro.ler_reservas(["Reserva do registro 5: a (marca 01)", "Reserva do registro 5: b (marca 02)",
                                            "Reserva do registro 6: c (marca 03)", "Cancelada a reserva do registro 5"])] == [6])
caso("o cancelamento com marca tira só a reserva daquele número",
     [r[1] for r in registro.ler_reservas(["Reserva do registro 2: a (marca aa)", "Reserva do registro 3: b (marca aa)",
                                            "Cancelada a reserva do registro 2 (marca aa)"])] == [3])
caso("o lote se lê com ou sem acento e em maiúscula",
     registro.ler_lotes(["Lote da serie do registro 7: x", "LOTE DA SÉRIE DO REGISTRO 7: y"]) == {7: 2})

serie = [f"2026-11-21 | registro 4 | série: lotes de citações | {L[8:]}",
         "Lote da série do registro 4: lote 2, 0 achados", "Lote da série do registro 4: lote 3, 1 achado"]
_, nd_s = registro.ler_registros(serie)
caso("o lote não vira registro: a série conta um só", list(nd_s.values()) == [4])
caso("os lotes se contam pela série", registro.ler_lotes(serie) == {4: 2})
caso("o campo \"skill e etapa\" da série casa", bool(registro.SERIE.match("série: lotes")))

print(f"\n{len(FALHAS)} falha(s)")
sys.exit(1 if FALHAS else 0)
