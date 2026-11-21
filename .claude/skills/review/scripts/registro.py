"""Número do próximo registro de uso na issue de reavaliação da skill `review`, e se é hora de propor a reavaliação.

Uso, da raiz do projeto: python -X utf8 .claude/skills/review/scripts/registro.py <número da issue>
                         python -X utf8 .claude/skills/review/scripts/registro.py <número da issue> --reservar "<o trabalho>"

- **--reservar** posta "Reserva do registro N: <trabalho>" antes da revisão, relê a issue e, se outra sessão
  reservou ou registrou o mesmo número antes, cancela a sua ("Cancelada a reserva do registro N (marca ...)") e
  reserva o seguinte; o número reservado, mesmo cancelado, conta como usado. A linha do registro leva esse número;
  a reserva sem registro aparece como aviso até virar registro ou ser cancelada. Por quê: sessões em paralelo
  tiravam o mesmo número.
- **A série:** o lote repetido de uma mesma issue, com a mesma régua e o mesmo nível, abre um registro cujo campo
  "skill e etapa" começa por "série"; os lotes seguintes entram como comentário "Lote da série do registro N: ..."
  e não são registro (contam um só para o gatilho).
- **O "a ver" vencido** se completa antes de postar o próximo registro. Se o projeto decidir uma data para tirar o
  campo do formato quando ainda sobrarem vencidos, ela vai em PRAZO_A_VER (vazio por padrão).

O formato tem 14 campos (`references/registro.md`); registro com outro número de campos ganha aviso. O campo "o que
veio depois" é o antepenúltimo; ele começa por "nada" ou diz "a ver" até ganhar complemento, e o resto ganha aviso
(o resultado da re-revisão vai na observação, não nele).

Roda igual no Bash, no PowerShell e no prompt do Windows: a busca fica aqui dentro, não nas aspas do shell.
Conta só os comentários no formato do registro ("AAAA-MM-DD | registro N | ..."), porque a issue também
recebe comentários que não são registro. Aceita o registro colado entre crases, com marcador ou negrito na frente,
em qualquer linha do comentário, e a data de dois dias ("2026-01-14/15"). Precisa do `gh` autenticado.
"""
import datetime
import json
import re
import secrets
import subprocess
import sys
import time

# Antes da data, aceita crase, negrito, marcador de lista e espaços; procura no começo de cada linha, não no meio
# dela, para não contar um comentário que só cite um registro. A citação em markdown (">") fica de fora: a resposta
# que cita um registro, cortado ou não, não é registro. A data pode ser de dois dias.
REGISTRO = re.compile(r"^[ \t`*-]*(\d{4}-\d{2}-\d{2}(?:/\d{1,2})? \| registro (\d+)\b[^\n]*)", re.M)
PROPOSTA = re.compile(r"^[\s`*>-]*Reavaliação proposta")  # marca da proposta feita
COMPLEMENTO = re.compile(r"^[ \t`*-]*Complemento do registro (\d+)\b", re.M)  # em qualquer linha
# Número repetido se corrige com outro comentário, sem editar o publicado:
# "Correção de numeração: ... é o **registro N**" renumera o registro repetido mais recente antes dele.
CORRECAO = re.compile(r"^[\s`*>-]*Correção de numeração:.*?\*\*registro (\d+)\*\*", re.S)
A_VER = re.compile(r"^a ver\b|\ba ver$")  # no começo ou no fim do campo
NADA = re.compile(r"^nada\b")
CAMPOS_DO_FORMATO = (14,)
# O PR citado em "skill e etapa" fecha como MERGED; lido como estado ilegível, o "a ver" venceria sem aviso.
FECHADA = ("CLOSED", "MERGED")
GATILHO = 15  # a partir deste registro, propor a reavaliação
RESERVA = re.compile(r"^[ \t`*-]*Reserva do registro (\d+)\b[^\n]*", re.M)
MARCA = re.compile(r"\(marca ([0-9a-f]+)\)")
# "Cancelada a reserva do registro N (marca ...)": com a marca, cancela só aquela reserva; sem ela, todas as do N.
CANCELA = re.compile(r"^[ \t`*-]*Cancelada a reserva do registro (\d+)\b([^\n]*)", re.M)
LOTE = re.compile(r"^[ \t`*-]*Lote da s[ée]rie do registro (\d+)\b", re.M | re.I)
SERIE = re.compile(r"^s[ée]rie\b", re.I)  # o campo "skill e etapa" do registro que abre a série
# A data, se o projeto a decidir, em que o campo "o que veio depois" sai do formato quando ainda sobrarem vencidos.
PRAZO_A_VER = None


def ler_reservas(corpos, com_canceladas=False):
    """As reservas, na ordem dos comentários: [(índice do comentário, número, linha, marca ou None)]. Sem
    `com_canceladas`, tira as que um "Cancelada a reserva do registro N" cancelou; com ele, devolve todas, porque o
    número cancelado continua usado (não volta a ser oferecido)."""
    todas = []
    for i, c in enumerate(corpos):
        for m in RESERVA.finditer(c):
            mm = MARCA.search(m.group(0))
            todas.append((i, int(m.group(1)), m.group(0), mm.group(1) if mm else None))
    if com_canceladas:
        return todas
    por_marca, por_numero = set(), set()
    for c in corpos:
        for m in CANCELA.finditer(c):
            mm = MARCA.search(m.group(2))
            if mm:
                por_marca.add((int(m.group(1)), mm.group(1)))
            else:
                por_numero.add(int(m.group(1)))
    return [r for r in todas if r[1] not in por_numero and (r[1], r[3]) not in por_marca]


def ler_lotes(corpos):
    """Quantos lotes cada série recebeu: {número do registro que abriu a série: lotes}."""
    lotes = {}
    for c in corpos:
        for m in LOTE.finditer(c):
            n = int(m.group(1))
            lotes[n] = lotes.get(n, 0) + 1
    return lotes


def proximo_numero(numeros, reservas):
    """O maior número usado, entre registros e reservas, mais um."""
    return max(list(numeros) + [r[1] for r in reservas], default=0) + 1


def ler_registros(corpos):
    """As linhas de registro de todos os comentários, em ordem, e o número de cada uma, já com as correções de
    numeração. Devolve (linhas, numero_de): linhas[u] = (índice do comentário, a linha a partir da data)."""
    linhas, numero_de, vistas = [], {}, set()
    for i, c in enumerate(corpos):
        achados = list(REGISTRO.finditer(c))
        if achados:
            for m in achados:
                linha = m.group(1).rstrip().rstrip("`")
                # A repostagem (a mesma linha do número em diante, mesmo com a data acertada) conta uma vez só.
                # Limites conhecidos: a repostagem de um registro que uma "Correção de numeração" renumerou leva o
                # número novo e conta de novo (reposte com o número antigo, ou não reposte); e a correção só se lê
                # num comentário próprio, que começa por ela, como o formato pede.
                chave = linha.split(" | ", 1)[1] if " | " in linha else linha
                if chave in vistas:
                    continue
                vistas.add(chave)
                linhas.append((i, linha))
                numero_de[len(linhas) - 1] = int(m.group(2))
            continue
        m = CORRECAO.match(c)
        if m:
            antes = list(numero_de)
            usados = [numero_de[u] for u in antes]
            repetidos = [u for u in antes if usados.count(numero_de[u]) > 1]
            if repetidos:
                numero_de[max(repetidos)] = int(m.group(1))
    return linhas, numero_de


USO = ("uso: python -X utf8 .claude/skills/review/scripts/registro.py <número da issue> [--reservar \"<o trabalho>\"]\n"
       "(o número sem #: no Bash e no PowerShell, o # sem aspas vira comentário)")


def ler_comentarios(issue):
    """Os corpos dos comentários da issue, em ordem; sai com a mensagem se o gh não responder."""
    try:
        saida = subprocess.run(["gh", "issue", "view", issue, "--json", "comments"],
                               capture_output=True, text=True, encoding="utf-8")
    except OSError:
        sys.exit("o gh não foi encontrado: instale o GitHub CLI e autentique com `gh auth login`")
    if saida.returncode != 0:
        sys.exit("o gh falhou: " + saida.stderr.strip())
    try:
        return [c["body"] for c in json.loads(saida.stdout)["comments"]]
    except (ValueError, KeyError, TypeError):
        sys.exit("o gh respondeu sem a lista de comentários esperada; rode de novo ou confira o `gh auth status`")


def situacao(corpos, numero, marca):
    """"nossa" (a reserva com `marca` ficou com o número), "perdeu" (um registro já tem o número, ou outra reserva
    ativa dele veio antes) ou "sumiu" (a nossa ainda não aparece na leitura: a API pode demorar)."""
    _, numero_de = ler_registros(corpos)
    if numero in numero_de.values():
        return "perdeu"
    nossa = next((r[0] for r in ler_reservas(corpos) if r[1] == numero and r[3] == marca), None)
    if nossa is None:
        return "sumiu"
    if any(r[1] == numero and r[0] < nossa for r in ler_reservas(corpos)):
        return "perdeu"
    return "nossa"


def colidiu(corpos, numero, marca):
    """A reserva que leva `marca` não ficou com o número (perdeu, ou ainda não aparece)."""
    return situacao(corpos, numero, marca) != "nossa"


def reservar(issue, trabalho, tentativas=3, ler=ler_comentarios, postar=None, esperar=None, releituras=3):
    """Posta a reserva do próximo número e confere, relendo a issue, que nenhuma outra sessão o pegou antes; se
    pegou, cancela a sua e reserva o seguinte. A reserva que ainda não aparece se relê até `releituras` vezes,
    com uma espera entre elas, antes de ser dada por perdida (e cancelada). Devolve o número reservado. `ler`,
    `postar` e `esperar` se trocam no teste. Limite: duas
    sessões que postam no mesmo instante e releem antes de a outra reserva aparecer na API ainda podem ficar com o
    mesmo número; a "Correção de numeração" cobre esse caso raro."""
    if postar is None:
        def postar(corpo):
            r = subprocess.run(["gh", "issue", "comment", issue, "--body", corpo],
                               capture_output=True, text=True, encoding="utf-8")
            if r.returncode != 0:
                sys.exit("o gh não postou a reserva: " + r.stderr.strip())
    if esperar is None:
        def esperar():
            time.sleep(2)
    for _ in range(tentativas):
        corpos = ler(issue)
        _, numero_de = ler_registros(corpos)
        numero = proximo_numero(numero_de.values(), ler_reservas(corpos, com_canceladas=True))
        marca = secrets.token_hex(8)
        postar(f"Reserva do registro {numero}: {trabalho} (marca {marca})")
        estado = "sumiu"
        for k in range(releituras):
            estado = situacao(ler(issue), numero, marca)
            if estado != "sumiu":
                break
            if k < releituras - 1:
                esperar()
        if estado == "nossa":
            return numero
        postar(f"Cancelada a reserva do registro {numero} (marca {marca}): "
               + ("outra sessão ficou com o número." if estado == "perdeu" else "a reserva não apareceu na releitura."))
    sys.exit(f"a reserva colidiu {tentativas} vezes (sessões em paralelo?): rode de novo")


def estado_da_issue(numero):
    """OPEN, CLOSED, MERGED (PR) ou "?" (gh falhou): uma chamada por número citado, só para os registros "a ver"."""
    try:
        saida = subprocess.run(["gh", "issue", "view", numero, "--json", "state"],
                               capture_output=True, text=True, encoding="utf-8")
    except OSError:
        return "?"
    if saida.returncode != 0:
        return "?"
    try:
        return json.loads(saida.stdout).get("state", "?")
    except ValueError:
        return "?"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    args = sys.argv[1:]
    if not args or not args[0].lstrip("#").isdigit():
        sys.exit(USO)
    issue = args[0].lstrip("#")
    if len(args) == 3 and args[1] == "--reservar" and args[2].strip():
        numero = reservar(issue, args[2].strip())
        print(f"#{issue}: reservado o registro {numero}; a linha do registro leva esse número")
        return
    if len(args) != 1:
        sys.exit(USO)
    corpos = ler_comentarios(issue)
    linhas, numero_de = ler_registros(corpos)
    numeros = list(numero_de.values())
    # "a ver" sem complemento: o campo "o que veio depois" é o antepenúltimo, diz "a ver" no começo ou no fim, e
    # nenhum comentário começa por "Complemento do registro N:". Vencido: a issue do trabalho, citada como #N em
    # "skill e etapa", já fechou. Registro fora dos 14 campos ganha aviso: o campo errado seria lido em silêncio.
    complementados = {int(m.group(1)) for c in corpos for m in COMPLEMENTO.finditer(c)}
    a_ver, vencidos, formato_errado, sem_estado, estranhos, fora_do_padrao = [], [], [], [], [], []
    estado_issue = {}
    for u, (_, linha) in enumerate(linhas):
        n_reg = numero_de[u]
        campos = [x.strip() for x in linha.split(" | ")]
        if len(campos) not in CAMPOS_DO_FORMATO:
            formato_errado.append(f"{n_reg} ({len(campos)} campos)")
        if n_reg in complementados or len(campos) < 3:
            continue
        depois = campos[-3].lower()
        if A_VER.search(depois):
            a_ver.append(n_reg)
            issues_trab = sorted(set(re.findall(r"#(\d+)", campos[2])), key=int)
            for issue_trab in issues_trab:
                if issue_trab not in estado_issue:
                    estado_issue[issue_trab] = estado_da_issue(issue_trab)
            fechadas = [i for i in issues_trab if estado_issue[i] in FECHADA]
            abertas = [i for i in issues_trab if estado_issue[i] == "OPEN"]
            sem_estado += [i for i in issues_trab if estado_issue[i] == "?"]
            estranhos += [i for i in issues_trab if estado_issue[i] not in FECHADA + ("OPEN", "?")]
            if fechadas:
                vencidos.append(f"{n_reg} (#{', #'.join(fechadas)} fechada{'s' if len(fechadas) > 1 else ''}"
                                + (f"; #{', #'.join(abertas)} aberta{'s' if len(abertas) > 1 else ''}: confira" if abertas else "") + ")")
        elif len(campos) in CAMPOS_DO_FORMATO and not NADA.match(depois):
            # Nem "nada" nem "a ver", e sem complemento: o resultado da re-revisão vai na observação, e o registro
            # sairia do acompanhamento. Um "Complemento do registro N:" cala o aviso.
            fora_do_padrao.append(n_reg)
    proposta = any(PROPOSTA.match(c) for c in corpos)
    # O número sai do maior já usado, não da contagem: com um registro faltando ou fora do formato,
    # a contagem daria um número que já existe. O gatilho, ao contrário, é pela contagem.
    # As reservas também ocupam número (o reservado e ainda sem linha fica "aberto").
    reservas = ler_reservas(corpos)
    todas_reservas = ler_reservas(corpos, com_canceladas=True)
    proximo = proximo_numero(numeros, todas_reservas)
    reservados_abertos = sorted({r[1] for r in reservas} - set(numeros))
    cancelados = sorted({r[1] for r in todas_reservas} - {r[1] for r in reservas} - set(numeros))
    n = len(numeros)
    print(f"#{issue}: {n} registro{'' if n == 1 else 's'}; o próximo é o registro {proximo} "
          "(antes da revisão, reserve-o com --reservar)")
    if reservados_abertos:
        print("aviso: reserva sem registro: " + ", ".join(map(str, reservados_abertos))
              + " (a linha do registro leva o número reservado; se a revisão não rodou, poste \"Cancelada a reserva do "
              "registro N\")")
    series = sorted(numero_de[u] for u, (_, linha) in enumerate(linhas)
                    if len(linha.split(" | ")) > 2 and SERIE.match(linha.split(" | ")[2].strip()))
    lotes = ler_lotes(corpos)
    if series:
        print("séries (um registro para o gatilho): " + ", ".join(
            f"registro {s} com {1 + lotes.get(s, 0)} lote{'s' if lotes.get(s, 0) else ''}" for s in series))
    orfaos = sorted(set(lotes) - set(series))
    if orfaos:
        print("aviso: lote de série que não existe: registro " + ", ".join(map(str, orfaos))
              + " (o registro que abre a série começa o campo \"skill e etapa\" por \"série\")")
    repetidos = sorted({x for x in numeros if numeros.count(x) > 1})
    if repetidos:
        print("aviso: número repetido (sessões em paralelo?): " + ", ".join(map(str, repetidos))
              + "; poste um comentário \"Correção de numeração: ... é o **registro N**\" para o mais novo, com o "
              "próximo número livre (o comentário publicado não se edita), e rode de novo")
    faltando = sorted(set(range(1, proximo)) - set(numeros) - set(reservados_abertos) - set(cancelados))
    if faltando:
        print("aviso: não achei o registro " + ", ".join(map(str, faltando))
              + " (apagado ou fora do formato?); confira na issue")
    if a_ver:
        print("\"a ver\" sem complemento: registro " + ", ".join(map(str, sorted(set(a_ver))))
              + " (o complemento vem o mais tardar quando a issue do trabalho revisado fechar, ou, sem issue, na "
              "validação da pessoa ou na reavaliação)")
    if vencidos:
        print("aviso: complemento vencido: registro " + ", ".join(vencidos) + "; poste \"Complemento do registro N:\""
              f" de cada um antes de postar o registro {proximo}")
        if PRAZO_A_VER and datetime.date.today() >= PRAZO_A_VER:
            print(f"aviso: passou {PRAZO_A_VER:%d/%m/%Y} com complementos vencidos: o campo \"o que veio depois\" "
                  "sai do formato (decisão do projeto): tire-o do registro.md e do formato")
    if sem_estado:
        print("aviso: não consegui ler o estado de #" + ", #".join(sorted(set(sem_estado), key=int)) + " (gh falhou?)")
    if estranhos:
        print("aviso: estado inesperado de " + ", ".join(f"#{i} ({estado_issue[i]})" for i in sorted(set(estranhos), key=int))
              + "; confira se a issue ou o PR fechou")
    if fora_do_padrao:
        print("aviso: \"o que veio depois\" fora do padrão: registro " + ", ".join(map(str, fora_do_padrao))
              + " (o campo é o que a pessoa pediu ou corrigiu depois e o que uma etapa posterior da mesma skill achou, "
              "\"nada\" ou \"a ver\"; o resultado da re-revisão vai na observação); se ele traz mesmo o que veio depois "
              "e a revisão não pegou, poste \"Complemento do registro N:\" com o que veio depois, que cala o aviso")
    if formato_errado:
        print("aviso: registro fora do formato (14 campos): " + ", ".join(formato_errado)
              + "; confira os separadores \" | \"")
    if n + 1 >= GATILHO and not proposta:
        print(f"a partir do registro {GATILHO}: propor à pessoa a reavaliação com os números, e marcar na issue "
              f"com um comentário que começa por \"Reavaliação proposta\"")
    elif proposta:
        print("a reavaliação já foi proposta nesta issue")


if __name__ == "__main__":
    main()
