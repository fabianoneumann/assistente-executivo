"""Teste sem rede do `conta_citacoes.py`: os casos que têm de contar e os que têm de ficar fora.

  python -X utf8 .claude/skills/research/scripts/teste_conta_citacoes.py
"""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import conta_citacoes as cc  # noqa: E402

falhas = []


def confere(nome, obtido, esperado):
    if obtido != esperado:
        falhas.append(f"{nome}: esperado {esperado!r}, veio {obtido!r}")


# licença
LIVRES = [
    "CC BY 4.0 (indicada na página do arXiv)",
    "CC BY-SA 4.0 (Wikipedia); ficha em palavras próprias em cima e o texto integral embaixo",
    "Creative Commons Atribuição-SemDerivações 3.0 Brasil (CC BY-ND 3.0 BR)",
    "CC0-1.0, no repositório (API do GitHub, 2026-11-07)",
    "MIT, no repositório",
    "Apache 2.0 (arquivo LICENSE do repositório)",
    "página sem nota de licença; obra do governo federal dos EUA, sem copyright nos EUA (17 U.S.C. §105)",
    "lei federal, texto oficial no portal do Planalto, sem direito autoral: Lei 9.610/1998, art. 8º, IV",
    "CC BY 4.0 (indicada na página do arXiv, para o preprint; a versão publicada na PNAS tem CC BY-NC-ND 4.0)",
    # 21/11: o "\bGPL\b" não pegava LGPL nem AGPL, e "CC 0" separado não casava com CC0 (achado)
    "LGPL-3.0, no repositório (API do GitHub)",
    "AGPL-3.0 (arquivo LICENSE do repositório)",
    "GPL-3.0, no repositório",
    "CC 0 1.0 (indicada no rodapé da documentação)",
    "CC-0, no repositório",
]
PROTEGIDAS = [
    None,
    "",
    "todos os direitos reservados (post do Instagram, sem licença aberta)",
    "CC BY-NC-SA 4.0 (indicada na página do arXiv); só a ficha",
    "Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 (CC BY-NC-ND), escrita na página do PMC",
    "© BMJ Publishing Group (aberto no PMC, PMC3240751, sem licença Creative Commons): só a ficha",
    "protegido (rodapé das três páginas: '© Quaternius'); as páginas dizem que os modelos são CC0",
    "em dúvida: a revista declara hoje CC BY 4.0 no DOAJ, mas o PDF de 1994 não traz licença",
    "licença não exclusiva do arXiv (arxiv.org/licenses/nonexclusive-distrib/1.0/); entra só a ficha",
    "sem LGPL nem outra licença aberta declarada",   # a licença negada na mesma frase não conta
    "ACC 0 é o nome do produto; todos os direitos reservados",   # "ACC 0" não é CC0
]
for lic in LIVRES:
    confere(f"livre: {lic[:50]}", cc.eh_livre(lic), True)
for lic in PROTEGIDAS:
    confere(f"protegida: {str(lic)[:50]}", cc.eh_livre(lic), False)

# citações
CASOS = [
    # (nome, linha do corpo, quantas contam)
    ("aspas retas", 'O autor diz que "a medida certa vem antes de qualquer ajuste fino".', 1),
    ("aspas curvas", 'Segundo ela, “we recommend generating at least one thousand ideas first”.', 1),
    ("aspas angulares", 'A frase: «o roteiro é a planta baixa do filme inteiro».', 1),
    ("curta demais", 'Ele chama isso de "loop rápido de verificação".', 0),
    ("números não são palavras", 'O banner dizia "From 16.06 till 24.06".', 0),
    ("título depois de ano", 'Ver Wang et al. 2023 ("Large language models are not fair evaluators").', 0),
    ("título depois de 'artigo'", 'O artigo "A Scientific Approach to Brand Name Development" abre o site.', 0),
    ("'o artigo diz que' é citação", 'O artigo diz que "any proxy metric will eventually be exploited by optimization".', 1),
    ("título em itálico", 'O livro *"The Non-Designer\'s Design Book, fourth edition"* traz.', 0),
    ("exemplo de prompt", 'Um prompt de exemplo: "reescreva começando cada frase com a letra A".', 0),
    ("segundo exemplo herda", 'O pedido ("reescreva começando cada frase com a letra A"; "explique de novo como se eu tivesse cinco anos").', 0),
    ("termo técnico", 'A chamada o chama de "transformador de linguagem baseado em texto".', 0),
    ("código em linha", 'O comando `"git worktree add ../x -b nova origin/master"` cria.', 0),
    ("texto de link", 'Ver [“Kanban: Successful Evolutionary Change for Your Business”](https://x.y).', 0),
]
for nome, linha, n in CASOS:
    texto = f"---\ntitulo: \"x\"\n---\n\n{linha}\n"
    confere(f"cita: {nome}", len(cc.citacoes(texto)), n)

# blocos, código, seções e repetição
corpo = "\n".join([
    "---", 'licenca: "todos os direitos reservados"', "---", "",
    "## O que a fonte recomenda", "",
    "> The first line of the quote block",
    "> and the second line, which is joined to the first one.", "",
    "```", '"uma frase entre aspas dentro do bloco de código não conta"', "```", "",
    'Ele repete: "we have to keep the AI on the leash".',
    'E de novo: "keep the AI on the leash, always and forever".',
    'Mais uma vez: "we have to keep the AI on the leash".', "",
    'A ficha tem a seção "O que a fonte recomenda", com esse nome.', "",
    '**Conferência lado a lado:** "Em uma frase, a ficha resume tudo o que importa".', "",
    "## Referências", "",
    '- Barthes, "Introduction à l\'analyse structurale des récits du monde".', "",
    "## Texto integral", "",
    '"qualquer coisa aqui embaixo não conta como citação da ficha".',
])
cits = cc.citacoes(corpo)
confere("bloco + duas falas distintas (a repetida conta uma vez)", len(cits), 3)
confere("o bloco junta as linhas", cits[0][1], 18)

# tradução: português numa ficha de fonte em inglês sai à parte
trad = "\n".join([
    "---", "---",
    'A autora: "readability was the most crucial factor for comparing the names".',
    'E ainda: "participants were given four minutes to come up with names".',
    'O sistema respondeu "sempre volte da página de resultados para a busca".',
])
cand = cc.candidatos(trad)
confere("tradução: duas em inglês contam", sum(1 for a in cand if a[3] == "cita"), 2)
confere("tradução: a em português sai à parte", sum(1 for a in cand if a[3] == "traduzida"), 1)
pt = "\n".join(["---", "---",
                'A autora: "a cena só anda quando alguém quer alguma coisa nela".',
                'E: "o leitor perdoa quase tudo menos uma página sem rumo".'])
confere("fonte em português: contam", len(cc.citacoes(pt)), 2)

# mede: livre some, protegida conta, pago marcado
with tempfile.TemporaryDirectory() as d:
    livre = Path(d) / "livre.md"
    livre.write_text('---\nlicenca: "CC BY 4.0"\n---\n\n"uma citação longa o bastante para contar aqui"\n', encoding="utf-8")
    confere("mede: livre fica fora", cc.mede(livre), None)
    prot = Path(d) / "prot.md"
    prot.write_text('---\nlicenca: "todos os direitos reservados (cópia distribuída por um curso pago)"\n---\n\n'
                    '"uma citação longa o bastante para contar aqui"\n', encoding="utf-8")
    m = cc.mede(prot)
    confere("mede: protegida conta", m["citacoes"], 1)
    confere("mede: curso pago é pago", m["pago"], True)
    vazia = Path(d) / "vazia.md"
    vazia.write_text('---\nlicenca:\n---\n\ntexto\n', encoding="utf-8")
    confere("mede: licenca vazia conta como ausente", cc.mede(vazia)["licenca"], "ausente")
    aberta = Path(d) / "aberta.md"
    aberta.write_text('---\nlicenca: "todos os direitos reservados"\ntitulo: "um título longo o bastante para contar"\n\ncorpo\n',
                      encoding="utf-8")
    campos, corpo = cc.frontmatter(aberta.read_text(encoding="utf-8"))
    confere("frontmatter sem fechamento: lê os campos", campos.get("licenca"), "todos os direitos reservados")
    confere("frontmatter sem fechamento: o corpo começa depois dos campos", corpo, 3)

if falhas:
    print("FALHOU:")
    for f in falhas:
        print("  " + f)
    sys.exit(1)
print(f"ok: {len(LIVRES) + len(PROTEGIDAS) + len(CASOS) + 12} conferências")
