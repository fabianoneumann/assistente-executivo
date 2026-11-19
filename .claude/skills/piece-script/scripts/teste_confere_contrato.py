"""Teste negativo do confere_contrato.py, sem rede: uma escaleta limpa de cada nível dá 0 ERRO, e cada defeito plantado
(um por regra) é pego pelo código certo. Rodar a cada mudança no script ou nos rótulos de references/contrato.md.

Uso: python -X utf8 teste_confere_contrato.py
"""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import confere_contrato as cc  # noqa: E402

N2 = """# Escaleta: teste

**Fontes, por sigla** (o número depois dos dois-pontos é a linha):
- **WZ** `knowledge/sources/2026-10-28-critic-autocorrecao-com-ferramentas.md`; **R** `../rascunho.md`

## A cabeça

**Nível:** N2, o do carrossel.

**Realidade da peça:** fato.

**Objetivo:** salvar.

**Regras conferidas:** a série; nenhuma lição registrada.

**Critério de escolha:** não se aplica, porque não é Stories de véspera.

**Story line:** algo acontece, algo deve ser feito, algo se faz.

**Fecho:** de x a y, pois z.

**Em jogo:** confiar no que não entendeu.

**Padrão de ordem:** o da série.

## As telas

### Tela 1. Gancho
- **Função:** abre.
- **Diz:** o título.
- **Fonte:** WZ:35.
- **Aparece:** a foto.
- **Valor:** do nome ao paradoxo.
- **Promete:** a resposta. **Paga em:** tela 2.
- **Puxa a próxima:** "mas quem era ele? →"

### Tela 2. A resposta
- **Função:** paga.
- **Diz:** a resposta.
- **Fonte:** WZ:36, R:4.
- **Aparece:** o diagrama.
- **Valor:** da dúvida à resposta.
- **Promete:** não se aplica, porque é a última.
- **Paga em:** não se aplica, porque não promete.
- **Puxa a próxima:** não se aplica, porque é a última tela.

## O pé

### Plantas e pagamentos
| Planta | Paga |
|---|---|
| a resposta | tela 2 |

### Não escolhidos
- **A2, o outro ângulo** (R:3) → a irmã, tela 4.
- **A3** fica fora, porque não serve a peça nenhuma.

### Representação
não se aplica, porque não há pessoa retratada.

### Exemplos
não se aplica, porque a peça não ensina procedimento.

### Enriquecimento
a camada arco, sem sugestão nova.

### Ironia
não se aplica, porque não há ironia.

### Para ir além
o artigo de 1966.

### Riscos
nenhum.
"""

N1 = """# Escaleta: resposta

**Fontes, por sigla**:
- **R** `../rascunho.md`

**Nível:** N1, Stories de resposta.

**Realidade da peça:** fato.

**Objetivo:** responder; o pedido único é mandar a pergunta.

**Regras conferidas:** o README dos Stories.

**Critério de escolha:** três respostas, pela ordem de chegada.

**Story line:** não se aplica, porque a resposta não tem arco.

**Fecho:** de dúvida a resposta, pois o leitor perguntou.

**Em jogo:** não se aplica, porque fora do N1.

**Padrão de ordem:** não se aplica, porque fora do N1.

### Story 1
- **Função:** a pergunta.
- **Diz:** a pergunta do seguidor.
- **Fonte:** a resposta 2, sobre o preço (references/stories.md: o número ou o tema, sem o @).
- **Aparece:** a caixinha.
- **Valor:** não se aplica, porque fora do N1.
- **Puxa a próxima:** "e a resposta? →"

### Plantas e pagamentos
não se aplica, porque não há promessa.

### Não escolhidos
não se aplica, porque fora do N1.

### Representação
não se aplica, porque não há pessoa retratada.

### Exemplos
não se aplica, porque fora do N1.

### Enriquecimento
não se aplica, porque fora do N1.

### Ironia
não se aplica, porque não há ironia.

### Para ir além
não se aplica, porque fora do N1.

### Riscos
nenhum.
"""

# (descrição, texto base, troca (antigo, novo), código esperado)
CASOS = [
    ("sem nível", N2, ("**Nível:** N2, o do carrossel.", "**Nível:** o do carrossel."), "CT-NIVEL"),
    ("campo do nível ausente", N2, ("**Em jogo:** confiar no que não entendeu.\n", ""), "CT-AUSENTE"),
    ("campo fora do nível sumiu (N2)", N2, ("**Critério de escolha:** não se aplica, porque não é Stories de véspera.\n", ""), "CT-SUMIU"),
    ("campo fora do nível sumiu (N1, unidade)", N1, ("- **Valor:** não se aplica, porque fora do N1.\n", ""), "CT-SUMIU"),
    ("campo fora do nível sumiu (N1, pé)", N1, ("### Para ir além\nnão se aplica, porque fora do N1.\n", ""), "CT-SUMIU"),
    ("campo a definir", N2, ("**Fecho:** de x a y, pois z.", "**Fecho:** a definir na forma."), "CT-VAZIO"),
    ("não se aplica sem motivo", N2, ("### Ironia\nnão se aplica, porque não há ironia.", "### Ironia\nnão se aplica"), "CT-NSA-MOTIVO"),
    ("não se aplica dentro do nível", N2, ("- **Valor:** do nome ao paradoxo.", "- **Valor:** não se aplica, porque é capa."), "CT-NSA-DENTRO"),
    ("Promete e Paga em num rótulo só", N2, ("- **Promete:** a resposta. **Paga em:** tela 2.", "- **Promete e Paga em:** a resposta, na tela 2."), "CT-PROMETE"),
    ("Fonte sem ficha", N2, ("- **Fonte:** WZ:35.", "- **Fonte:** o livro dele."), "CT-FONTE"),
    ("não escolhido sem destino", N2, ("- **A2, o outro ângulo** (R:3) → a irmã, tela 4.", "- **A2, o outro ângulo** (R:3), a ver."), "CT-ESCOLHIDO"),
    ("sigla sem linha (aviso)", N2, ("- **Fonte:** WZ:35.", "- **Fonte:** WZ."), "AV-LINHA"),
    # os casos de borda (18/11)
    ("rótulo vazio não engole o próximo", N2, ("**Objetivo:** salvar.", "**Objetivo:**"), "CT-VAZIO"),
    ("nível só dentro de uma unidade (sem cabeça)", N2,
     ("**Nível:** N2, o do carrossel.\n", ""), "CT-NIVEL"),
    ("tabela só com o cabeçalho", N2, ("| a resposta | tela 2 |\n", ""), "CT-VAZIO"),
    ("promete e o Paga em não se aplica", N2,
     ("- **Promete:** a resposta. **Paga em:** tela 2.",
      "- **Promete:** a resposta. **Paga em:** não se aplica, porque paga noutra peça."), "CT-PROMETE"),
    ("não escolhido sem a unidade (só a peça)", N2,
     ("- **A2, o outro ângulo** (R:3) → a irmã, tela 4.", "- **A2, o outro ângulo** (R:3) → a irmã."), "CT-ESCOLHIDO"),
    ("não escolhido no terceiro ponto da lista", N2,
     ("- **A3** fica fora, porque não serve a peça nenhuma.",
      "- **A3** fica fora, porque não serve a peça nenhuma.\n- **A4** vai para depois."), "CT-ESCOLHIDO"),
    ("sigla que não é ficha (aviso)", N2, ("- **Fonte:** WZ:35.", "- **Fonte:** R:4."), "AV-FICHA"),
    ("rótulo Fontes no lugar de Fonte (aviso)", N2, ("- **Fonte:** WZ:35.", "- **Fontes:** WZ:35."), "AV-ROTULO"),
    ("critério de escolha nos Stories de véspera", N2,
     ("**Objetivo:** salvar.", "**Objetivo:** a véspera do post; o pedido único é votar."), "CT-NSA-DENTRO"),
    ("N1 sem fonte nenhuma", N1,
     ("- **Fonte:** a resposta 2, sobre o preço (references/stories.md: o número ou o tema, sem o @).", "- **Fonte:** o print."),
     "CT-FONTE"),
]

# o que não pode acusar: (descrição, texto base, troca)
LIMPOS = [
    ("o destino 'aqui, tela N' sem seta", N2, ("- **A2, o outro ângulo** (R:3) → a irmã, tela 4.",
                                              "- **A2, o outro ângulo** (R:3): aqui, tela 2, pela escolha de quem decide.")),
    ("o destino pela função da tela", N2, ("- **A2, o outro ângulo** (R:3) → a irmã, tela 4.",
                                          "- **A2, o outro ângulo** (R:3): no post B, na tela 'como funciona'.")),
    ("'não é véspera' no critério não faz o critério obrigatório", N2, ("x", "x")),
    ("a escaleta com CRLF", N2, ("\n", "\r\n")),
]


def roda(texto, pasta, nome):
    p = Path(pasta) / nome
    p.write_text(texto, encoding="utf-8")
    return cc.confere(str(p))


def main():
    falhas = 0
    with tempfile.TemporaryDirectory(dir=str(Path(__file__).resolve().parent)) as d:
        for nome, base in (("N2 limpa", N2), ("N1 limpa", N1)):
            ach = roda(base, d, "limpa.md")
            erros = [a for a in ach if a["nivel"] == "ERRO"]
            print(("ok   " if not ach else "FALHA") + f" {nome}: {len(erros)} ERRO, {len(ach) - len(erros)} AVISO")
            for a in ach:
                print(f"       {a['codigo']} {a['onde']}: {a['msg']}")
            falhas += bool(ach)
        for desc, base, (velho, novo) in LIMPOS:
            ach = [a for a in roda(base.replace(velho, novo), d, "limpo.md") if a["nivel"] == "ERRO"]
            print(("ok   " if not ach else "FALHA") + f" limpo: {desc}" + ("" if not ach else f"; veio {[a['codigo'] for a in ach]}"))
            falhas += bool(ach)
        # o bloco de siglas fecha na linha em branco: um rótulo depois dele não vira sigla
        sig = cc.siglas(["**Fontes, por sigla**:", "", "**Objetivo** x", "", "**Objetivo:** y"])
        print(("ok   " if "Objetivo" not in sig else "FALHA") + " siglas: o bloco vazio não pega o negrito seguinte")
        falhas += "Objetivo" in sig
        for i, (desc, base, (velho, novo), codigo) in enumerate(CASOS, 1):
            assert velho in base, f"caso {i}: o trecho a trocar não existe no texto base"
            ach = roda(base.replace(velho, novo, 1), d, f"caso{i}.md")
            pegou = any(a["codigo"] == codigo for a in ach)
            print(("ok   " if pegou else "FALHA") + f" {i:2}. {desc}: espera {codigo}"
                  + ("" if pegou else f"; veio {[a['codigo'] for a in ach]}"))
            falhas += not pegou
    print("TODOS OK" if not falhas else f"{falhas} FALHA(S)")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
