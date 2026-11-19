"""Testa, sem rede e sem ffmpeg, a parte do roteiro do video_do_story.py: a conta frase a frase do tempo
de leitura e a legenda revisada do vídeo com voz.

1. A frase abaixo da régua (`caracteres ÷ 17` s, piso de 0,3 s por palavra) dá AVISO; a que cabe, não.
2. Frase a frase, não a soma: as três frases de uma linha (separadas por " / ") que cabem sozinhas passam, mesmo que
   somadas não caibam.
3. A linha sem trecho em segundos ("o vídeo todo") e as outras tabelas do roteiro ficam de fora; a marcação do
   markdown (==, **, *) não conta como caractere.
4. O vídeo com voz (a `funcao` de câmera ou `voz: true`) sem "legenda: ..., revisada" dá AVISO; com ela, ou sem voz, não.
5. A linha de comando: --roteiro sem valor ou com arquivo que não existe sai com 2; só o roteiro sai com 0.

Uso: python -X utf8 teste_video_do_story.py (de qualquer pasta)."""
import importlib.util, io, pathlib, sys, tempfile
from contextlib import redirect_stderr, redirect_stdout

AQUI = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("video_do_story", AQUI / "video_do_story.py")
vs = importlib.util.module_from_spec(spec); spec.loader.exec_module(vs)
ROOT = AQUI.parents[3]

falhas = []


def confere(nome, ok):
    print(("ok  " if ok else "FALHA ") + nome)
    if not ok:
        falhas.append(nome)


def roteiro(corpo, fm="estagio: rascunho"):
    d = tempfile.mkdtemp(prefix="teste-vds-")
    p = pathlib.Path(d) / "roteiro.md"
    p.write_text(f"---\n{fm}\n---\n\n# x\n\n{corpo}\n", encoding="utf-8", newline="\n")
    return p


TABELA = """| Tempo | Na tela | O que se mexe |
|---|---|---|
| o vídeo todo | *(no topo, pequeno)* terça, 18h | fixa |
| 0–7 s | O assunto que eu venho adiando aprender: fazer um ==vídeo curto e animado==, para ensinar bem. | nada |
| 12,6–18 s | Com tanto para testar, quem me ajuda a escolher a ordem são os leitores e os meus grupos de estudos. | x |
| 43,5–52 s | Terça, 18h: como uma ideia antiga virou a ferramenta que quase todo mundo usa hoje no trabalho. / n.º 3 da série de exemplo / Às 18h, no post, me conta qual é o assunto que você vem adiando. | parada |

| Critério | Nota |
|---|---|
| 0–1 s | uma frase muito longa que não é do vídeo e não deveria contar nunca, de jeito nenhum, em lugar nenhum |
"""

t = vs.tempos_do_roteiro(TABELA)
confere("a tabela de tempo: 5 frases (a linha do vídeo todo e a outra tabela fora)", len(t) == 5)
confere("a marcação sai do texto", t[0][2] == "O assunto que eu venho adiando aprender: fazer um vídeo curto e animado, para ensinar bem.")
confere("a abertura tem 90 caracteres", len(t[0][2]) == 90)
confere("o trecho com vírgula", (t[1][0], t[1][1]) == (12.6, 18.0))
av = vs.conferir_roteiro(roteiro(TABELA))
confere("só a segunda frase fica abaixo da régua", len(av) == 1 and "Com tanto para testar" in av[0] and "pede 6 s" in av[0])
aviso = [f for f in t if f[0] == 43.5]
confere("frase a frase: as três da última linha passam sozinhas", all(vs.pede(f) <= b - a for a, b, f in aviso))
confere("e somadas não passariam (a soma não é a régua)", sum(vs.pede(f) for _, _, f in aviso) > 52 - 43.5)
confere("o piso por palavra vale quando pesa mais", vs.pede("a b c d e f g h i j") == 3.0)
confere("tabela sem frase abaixo: nenhum aviso",
        vs.conferir_roteiro(roteiro("| Tempo | Legenda |\n|---|---|\n| 0–3 s | Uma frase curta. |\n")) == [])
confere("a coluna Legenda também se lê", len(vs.tempos_do_roteiro("| Tempo | Quem | Legenda |\n|---|---|---|\n| 0–1 s | eu | Frase. |\n")) == 1)
confere("a tabela sem a coluna Tempo fica de fora", vs.tempos_do_roteiro("| Cena | Na tela |\n|---|---|\n| 0–1 s | Frase longa demais. |\n") == [])

# a legenda revisada no vídeo com voz
camera = "funcao: vídeo falando para a câmera"
confere("câmera sem legenda revisada: aviso", any("legenda revisada" in x for x in vs.conferir_roteiro(roteiro("texto", camera))))
confere("câmera com legenda queimada, revisada: nada", vs.conferir_roteiro(roteiro("**legenda:** queimada, revisada", camera)) == [])
confere("voz: true sem legenda: aviso", any("legenda revisada" in x for x in vs.conferir_roteiro(roteiro("texto", "voz: true"))))
confere("legenda sem revisão não basta", any("legenda revisada" in x for x in vs.conferir_roteiro(roteiro("legenda: adesivo", "voz: sim"))))
confere("sem voz, a legenda não se pede", vs.conferir_roteiro(roteiro("texto", "funcao: aviso")) == [])

# o roteiro ao lado do MP4
p = roteiro("x")
(p.parent / "images").mkdir()
confere("o roteiro uma pasta acima do MP4", vs.roteiro_ao_lado(p.parent / "images" / "story-01.mp4") == p.parent / "roteiro.md")
confere("sem roteiro por perto, None", vs.roteiro_ao_lado(pathlib.Path(tempfile.mkdtemp()) / "a" / "b.mp4") is None)

# a linha de comando
with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
    sem_valor = vs.main(["--roteiro"])
    nao_existe = vs.main(["--roteiro", str(p.parent / "nao-existe.md")])
    so_roteiro = vs.main(["--roteiro", str(roteiro(TABELA))])
confere("--roteiro sem valor sai com 2", sem_valor == 2)
confere("--roteiro de arquivo que não existe sai com 2", nao_existe == 2)
confere("só o roteiro sai com 0 (aviso não barra)", so_roteiro == 0)

print(f"\n{len(falhas)} falha(s)" if falhas else "\ntudo ok")
sys.exit(1 if falhas else 0)
