---
name: visual-form
description: >-
  Monta a forma de uma peça a partir do texto travado e da escaleta: o HTML das telas (`slides.html` ou `stories.html`) no design system da série, as imagens do banco ou da `image-gen`, as conferências em código, as alternativas de forma e a I2 contra as publicadas, até a prévia, sem trocar as palavras aprovadas. USE quando a criação de peças chegar à forma, ou quando a pessoa pedir para montar as telas, ajustar o layout, deixar uma tela mais forte, mais calma ou mais limpa, refazer a forma de um carrossel ou de uma sequência de Stories, ou rodar a I2, mesmo que não diga "forma". NÃO use para gerar só uma imagem (`image-gen`), o mecanismo que se move (`object-anatomy`), escrever ou mudar o texto (`piece-script`), a peça inteira (`piece-creation`), exportar ou publicar (`slides-export`) nem para interface de site ou app (`frontend-design`).
---

# visual-form

A forma das telas de uma peça: o HTML no design system, as imagens, as conferências, as alternativas e a I2, até a prévia. Roda no contexto principal, sem subagente próprio, porque conversa com as paradas de quem pede e com o roteiro travado. O que se isola continua isolado: o objeto que se move vai à `object-anatomy`, e a I2 roda num agente que não fez a forma.

**A regra que não muda: a forma nunca troca palavra.** O texto aprovado fica como está, também no ajuste de layout; o pedido que muda o texto volta ao roteiro (a `piece-script`), e um corte de texto só aparece como alternativa explícita, com o antes e o depois, para a pessoa escolher.

**Antes de começar:** leia as abertas e as apontadas em [`licoes.md`](./licoes.md) desta pasta, e o [`references/projeto.md`](./references/projeto.md), com o que muda de projeto para projeto (as réguas de cada formato, as pastas, os caminhos das outras skills, os comandos). Quando esta skill e o design system da série discordarem, vale o design system, e a diferença vai ao relatório.

## Entra

| O quê | De onde |
|---|---|
| O texto | **no carrossel,** o `texto.md` travado, com a linha "Texto travado em" no `refinamentos.md`; sem a trava, pare e diga que falta, porque a forma não começa sobre texto aberto. **Nos Stories narrativos e de resposta,** a seção "Os Stories" do `roteiro.md`, que chega "a travar": o ok vem na leitura da prévia, e então quem conduz a peça chama a `piece-script` para gravar a linha da trava. **No Story avulso,** o `roteiro.md` que a `piece-creation` escreveu, validado na simulação |
| A escaleta, com a coluna **Aparece** | a `escaleta.md` (ou o roteiro dos Stories), da `piece-script`: o que cada tela mostra, com o arquivo quando já existe |
| Os conceitos e as imagens | o `conceitos-e-imagens.md` (no carrossel da série): a função de cada imagem, a tela-par, o tamanho previsto do dominante, o incremento declarado |
| O formato | carrossel da série, carrossel avulso (com a identidade escolhida na primeira mesa), sequência de Stories ou Story avulso |
| O pedido da pessoa, quando é ajuste | a tela e o movimento ("mais forte", "mais calma", "limpa"): o vocabulário em [`references/criterio.md`](./references/criterio.md) |

## Sai

- O `slides.html` (ou o `stories.html`) na pasta da peça, o `assets/` com o que foi usado e o `prompts.md` de cada imagem gerada; a versão anterior a cada passada em `versions/`.
- As conferências da forma em 0 ERRO, com os AVISOs lidos.
- As **alternativas de forma**, só onde o processo do formato já tem a parada da forma (no carrossel; nos Stories não há essa parada, e a skill não cria mesa nova).
- No carrossel da série, a **I2** e a lista das telas que voltam, validada por script, com os arquivos em `medida/` da peça.
- A **prévia** da peça inteira ao lado da prévia da peça anterior do mesmo tipo, no mesmo acabamento, para a parada que a `piece-creation` conduz.
- O bloco da forma no `refinamentos.md` da peça: o que entrou, o que saiu, as lições aplicadas, os desvios avisados, as conferências, a I2 e o que vai à leitura da pessoa como sinal. Nos Stories, no `roteiro.md`, as seções que o README dos Stories dá à forma ("Passadas", com a prévia de cada passada, e "Artefatos gerados", com cada imagem que foi ao banco). A seção "Estado da criação" não é desta skill: é da `piece-creation`.

## O fluxo

1. **Ler as entradas e as lições:** as desta skill, as de forma do arquivo de lições das peças (o `projeto.md` diz onde), com as aplicadas anotadas no `refinamentos.md`, as da `slides-export` e da `image-gen`, e as regras do formato no `projeto.md`. No carrossel, confira que o texto está travado.
2. **Montar a partir de um publicado do mesmo tipo:** copie o `slides.html` publicado mais recente do mesmo tipo (na série nova, o post de exemplo; nos Stories, o modelo do `projeto.md`) e troque o texto, os desenhos e as anotações que mudam. O CSS da peça só posiciona: valor novo de cor, letra ou tamanho é decisão de série (o `projeto.md` diz onde). O texto vem do travado, colado, sem reescrever.
3. **As imagens, primeiro do banco:** a coluna **Aparece** nomeia o arquivo quando ele existe (o `assets/` das peças, o banco de imagens que o `projeto.md` aponta); só o que falta vai à `image-gen`, que escolhe o gerador pela tabela dela e confere a imagem antes de devolver, com o `prompts.md` na pasta. Cada imagem, do banco ou gerada, se confere contra o texto da tela que ela ilustra (a ordem de uma sequência, o sentido da seta, a letra inventada) antes de entrar. **O traço segue as regras de desenho da série** (o que se faz a lápis, o que se faz a caneta, o objeto que se move; o `projeto.md` aponta onde estão).
4. **O objeto que se move vai à `object-anatomy`** (o objeto que é a explicação e funciona, se monta ou se separa), e só se passa no filtro dela (o passo 0: coisa física real, com anatomia e fonte do interior); senão, a tela é diagrama a caneta ou desenho parado, e a escaleta é avisada. A caixa padrão é a tela inteira (a menor, pela regra da `object-anatomy`). Faça três coisas:
   - **Chame a skill com o pedido inteiro,** porque o subagente não vê a conversa: o conceito (o texto travado da tela), a pasta da peça, o formato (tela parada, tela em vídeo do carrossel ou cena dos Stories, com os segundos) e as fichas com fonte dos números do objeto (na base, pela `research`, antes da chamada); quando a forma já sabe, a caixa (x, y, largura e altura em px) e o número da tela.
   - **Leia a devolução:** o estado (pronto, falta lastro, a R4 não fecha, não passou numa conferência), o `object/objeto.md`, o `confere.json` e o `relatorio.md`. "A R4 não fecha": o objeto volta à escaleta, e a forma não o troca. "Falta lastro": a lista vai à `research`. As escolhas de gosto e a lista do "sem fonte" vão à parada da forma; a seção "Lição para a skill" vai ao `licoes.md` da `object-anatomy`, na mesma entrega.
   - **Encaixe sem escalar,** pelo contrato do encaixe do `references/projeto.md` da `object-anatomy`: o HTML carrega `object/iso.js` e `object/geometria.js` por `<script src>`, chama `OBJETO.monta(svg)` no `svg` da tela e `OBJETO.quadro(t)` do próprio `window.quadro`; o texto travado vai em volta. O que precisar mudar na geometria volta à skill. Depois do encaixe, as conferências de novo (o passo 6, o `juntas.py` na tela encaixada, e o `saltos.py` e a folha de quadros no MP4), com os números no `refinamentos.md`.
5. **Os sete passos da Robin Williams** (*Design para quem não é designer*, caps. 6 e 12), na peça inteira e não tela a tela: (1) limpar, e escolher uma ou duas fontes; (2) o ponto focal, pelo propósito e pelo lugar onde a peça aparece; (3) proximidade; (4) alinhamento, uma borda forte e uma segunda para a hierarquia, reforçando a que já existe; (5) repetição, reforçando o que já se repete; (6) contraste, nunca tímido; (7) conferir, revendo a repetição e o lado do alinhamento à luz do contraste. Os passos 1 a 4 são a estrutura; 5 a 7, o acabamento. Na série, o design system já resolve boa parte do 1 e do 5: o trabalho é não desfazê-lo.
6. **As conferências da forma em 0 ERRO:** o `conferir_telas.py` e o `medir_blocos.py` desta skill (os comandos e a tabela de achados em [`references/conferencias.md`](./references/conferencias.md); nos Stories, com o `stories.html`). Corrija cada ERRO pela posição, nunca pelo texto, e rode de novo. Os AVISOs ficam para depois do passo 7. A exportação (`slides-export`) chama estas conferências antes da foto, e o `--upload` barra o ERRO.
7. **A leitura crítica antes dos números:** com a peça renderizada e antes de ler os AVISOs e as medidas, olhe cada tela ao lado da tela-par publicada e escreva a **lista de defeitos** (tela, elemento, o que falta ou está errado, a gravidade, a correção), não uma nota, pelo protocolo do [`references/criterio.md`](./references/criterio.md). Só então leia os AVISOs, o `mede_forma.py` e a ocupação contra a tela-par (a tela meio vazia é a crítica mais frequente de quem julga a forma). Classifique cada desvio (token que falta, implementação avulsa, conceito, defeito local) e corrija o que é da forma; o que é de conceito volta à escaleta.
   **A passada de enriquecimento da forma,** no carrossel: a skill `base-enrichment`, camada forma, com o texto travado declarado, só sobre a forma; o que pedir texto vai à leitura da pessoa como sinal, e as sugestões ganham destino no `refinamentos.md`.
8. **As alternativas, na parada da forma** (só no carrossel): elas mudam a primeira decisão (o que conduz a tela: o título, a imagem, o número), não o detalhe de uma versão só; onde a quantidade de texto pesa, uma versão que explica com texto e outra que mostra com imagem. O que é regra chega à mesa já conferido; só vai à pessoa o que é gosto e direção de arte (`decisions/mesas-de-design.md`). A mesa segue o formato que a `piece-creation` descreve (o comentário por item, "nenhuma destas / outra"); quando a pessoa já trouxe a escolha, siga com ela.
9. **A I2, no carrossel da série, validada por script antes da prévia:** com 0 ERRO e depois da parada da forma, pelo [`references/i2.md`](./references/i2.md): o material pelo `prepara_i2.py` e o `folha_de_contato.py`, o pedido num agente que não fez a forma, as medidas pelo `mede_forma.py`, e a trava pelo `trava_i2.py` (a regra antiga e a (b)). Voltam só as telas que o script devolve, até duas voltas; o resto vai à leitura da pessoa como sinal. Nos Stories, a comparação com a sequência anterior do mesmo tipo é só sinal, sem trava. Na primeira peça da série, sem publicada do mesmo tipo, a I2 não roda (fica "não se aplica, sem tela-par").
10. **A prévia,** a peça inteira ao lado da prévia da peça anterior do mesmo tipo, no mesmo render, na mesma resolução e com as fontes carregadas (export com `--out-dir` fora da pasta da peça, sem `--upload`; nos Stories, com `--previa`). Entregue o caminho e o que vai à leitura da pessoa; a pergunta "superou a anterior?" e as marcas são da `piece-creation`.

## Conferência antes de entregar

- [ ] Nenhuma palavra fora do texto: no carrossel, o AVISO `texto_fora_do_travado` do `conferir_telas.py` sem achado (ou a diferença declarada como alternativa à pessoa). **Nos Stories,** o mesmo AVISO lê a seção "Os Stories" do `roteiro.md`; a diferença que vem da legenda de um vídeo ou de um rótulo descrito em prosa no roteiro é esperada e se lê, não se corrige. No Story avulso, sem essa seção, compare à mão com o texto do roteiro e diga no registro que foi à mão.
- [ ] 0 ERRO no `conferir_telas.py` e no `medir_blocos.py`, com os AVISOs lidos e o destino de cada um no `refinamentos.md`.
- [ ] Cada imagem conferida contra o texto da tela, com o prompt no `prompts.md`; o banco consultado antes de gerar.
- [ ] O objeto encaixado sem escalar, com as conferências de novo na peça (quando houve objeto).
- [ ] No carrossel da série, o `trava_i2.py` rodado sobre a I2 da versão final, e as voltas registradas.
- [ ] Os desvios do design system avisados no `refinamentos.md`, uma linha por desvio, com o `data-intencional` ou o `data-sangria` no HTML.

## Pronto quando

A prévia está pronta para a parada da pessoa: o HTML com 0 ERRO e o texto intacto, as imagens conferidas, a I2 com a lista curta das telas que voltaram e o porquê (no carrossel da série), e o bloco da forma no `refinamentos.md`. O portão e a exportação com `--upload` não são desta skill.

## Nunca

- Trocar, cortar ou acrescentar palavra do texto travado; mudar o arco ou o conceito de uma tela (volta à `piece-script`).
- Exportar com `--upload` (o fechamento da peça é da `slides-export`, com a peça pronta) ou publicar. O que as regras das outras pastas mandam subir no caminho sobe como elas dizem: a imagem gerada vai ao banco pela `image-gen`, e a prévia de cada passada dos Stories, pelo README deles.
- Mudar a geometria do objeto da `object-anatomy` ou escalar o desenho dela.
- Fazer a I2 no próprio contexto de quem fez a forma, ou voltar uma tela que o `trava_i2.py` não devolveu.
- Criar uma parada que o processo do formato não tem.

**Ao terminar:** se houve falha, contorno ou acerto que vale lembrar, registre em [`licoes.md`](./licoes.md) desta pasta, na mesma entrega (formato em `decisions/licoes-das-skills.md`); a lição da peça vai ao arquivo de lições das peças, na etapa da forma.
