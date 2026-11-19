"""Número do próximo registro de uso na issue de reavaliação da skill `review`, e se é hora de propor a reavaliação.

Uso, da raiz do projeto: python -X utf8 .claude/skills/review/scripts/registro.py <número da issue>

O formato tem 14 campos (`references/registro.md`); registro com outro número de campos ganha aviso. O campo "o que
veio depois" é o antepenúltimo; ele começa por "nada" ou diz "a ver" até ganhar complemento, e o resto ganha aviso
(o resultado da re-revisão vai na observação, não nele).

Roda igual no Bash, no PowerShell e no prompt do Windows: a busca fica aqui dentro, não nas aspas do shell.
Conta só os comentários no formato do registro ("AAAA-MM-DD | registro N | ..."), porque a issue também
recebe comentários que não são registro. Aceita o registro colado entre crases, com marcador ou negrito na frente,
em qualquer linha do comentário, e a data de dois dias ("2026-01-14/15"). Precisa do `gh` autenticado.
"""
import json
import re
import subprocess
import sys

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


USO = ("uso: python -X utf8 .claude/skills/review/scripts/registro.py <número da issue>\n"
       "(o número sem #: no Bash e no PowerShell, o # sem aspas vira comentário)")


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
    if len(args) != 1 or not args[0].lstrip("#").isdigit():
        sys.exit(USO)
    issue = args[0].lstrip("#")
    try:
        saida = subprocess.run(["gh", "issue", "view", issue, "--json", "comments"],
                               capture_output=True, text=True, encoding="utf-8")
    except OSError:
        sys.exit("o gh não foi encontrado: instale o GitHub CLI e autentique com `gh auth login`")
    if saida.returncode != 0:
        sys.exit("o gh falhou: " + saida.stderr.strip())
    corpos = [c["body"] for c in json.loads(saida.stdout)["comments"]]
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
    proximo = max(numeros, default=0) + 1
    n = len(numeros)
    print(f"#{issue}: {n} registro{'' if n == 1 else 's'}; o próximo é o registro {proximo}")
    repetidos = sorted({x for x in numeros if numeros.count(x) > 1})
    if repetidos:
        print("aviso: número repetido (sessões em paralelo?): " + ", ".join(map(str, repetidos))
              + "; poste um comentário \"Correção de numeração: ... é o **registro N**\" para o mais novo, com o "
              "próximo número livre (o comentário publicado não se edita), e rode de novo")
    faltando = sorted(set(range(1, proximo)) - set(numeros))
    if faltando:
        print("aviso: não achei o registro " + ", ".join(map(str, faltando))
              + " (apagado ou fora do formato?); confira na issue")
    if a_ver:
        print("\"a ver\" sem complemento: registro " + ", ".join(map(str, sorted(set(a_ver))))
              + " (o complemento vem o mais tardar quando a issue do trabalho revisado fechar, ou, sem issue, na "
              "validação da pessoa ou na reavaliação)")
    if vencidos:
        print("aviso: complemento vencido: registro " + ", ".join(vencidos) + "; poste \"Complemento do registro N:\"")
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
