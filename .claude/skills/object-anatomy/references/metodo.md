# O método: as regras R1 a R22

As regras do objeto que é a explicação e se move, tiradas por engenharia reversa do Anatomy (https://github.com/wheresryan22/anatomy, MIT, © 2026 Ryan, commit `1482e84`) e reescritas como regras nossas, em palavras próprias. Cada regra diz se se faz **à mão** (com o código desta skill e o que se escreve na peça) ou se **depende do kit**, que não se instala nem roda aqui (só como prova, isolado e com o ok de quem pediu: é código de terceiro). O que é do projeto (o traço, as cores, os caminhos) não está aqui: está em [`projeto.md`](projeto.md).

## 1. Antes do desenho: a verdade e o tamanho

**R1. Medir o tamanho antes de começar.** O porte se mede pelo papel do desenho: o objeto de conceito numa tela parada de carrossel tem de 15 a 25 peças; o objeto herói de vídeo, de 40 a 80, e a tela em vídeo do carrossel conta como vídeo (com menos peças, o objeto em vídeo sai pobre); acima disso, propor a versão menor a quem chamou, sem começar a grande. À mão.

**R2. A verdade primeiro.** Os números e o comportamento reais do que se explica (tamanhos, contagens, limiares, a ordem do que acontece, a direção do fluxo), cada um com a fonte aberta, antes do objeto. O desenho também tem de ser verdadeiro, não só o texto. Nesta skill, os fatos chegam de quem chama, nas fichas com fonte; o que não tem fonte se diz no relatório como "sem fonte" e não se desenha como se tivesse. À mão.

## 2. O objeto

**R3. O objeto é a explicação.** Uma coisa física, típica e reconhecível para o público, cujo funcionamento é o conceito, com uma peça para cada termo do conceito. Caixas com setas só quando o conceito já é um diagrama (um ciclo, uma linha do tempo, um fluxo entre aparelhos): aí não há objeto, e a skill devolve. Essa pergunta é o passo 0 do `SKILL.md` (o filtro: coisa física real, com anatomia e fonte do interior), antes da R4. À mão.

**R4. Dizer numa frase o que se move e o que o movimento significa.** Se a frase não sai, o objeto não mapeia: a skill para e devolve, sem geometria. A frase vai ao `objeto.md` antes de qualquer traço. É a correspondência dita que a analogia pede para funcionar (a síntese de metáfora visual e demonstração, em `knowledge/content-design/`, quando a base a tiver). À mão.

**R5. Copiar o acabamento de uma referência, nunca o objeto.** À mão.

**R6. O objeto inventado (o genérico de um tipo real, não o aparelho que só existe no desenho, que o passo 0 barra) é ilustração, não documento.** Ele nunca toma o lugar da máquina real da época no conteúdo que documenta a época; a máquina real se desenha pela ficha, com fonte. À mão.

## 3. A lista de peças antes da geometria

**R7. A lista de peças por grupo, antes de desenhar:** base (placa, pés, parafusos, régua), estrutura (colunas, trilhos, batentes), mecanismo (carro, molas, êmbolo, ponteiro), controles (botão, manivela) e o assunto, que é a peça acesa. Cada peça com a função dela no conceito; peça sem função sai. "Most of the quality is decided there." À mão.

**R8. Toda peça se apoia noutra.** Nada flutua: a bola fica no fundo da canaleta, o braço sai de uma face. No `pecas.json`, o apoio é um encosto (dentro da tolerância) com a peça de baixo. À mão.

## 4. O mundo, a câmera e a geometria

**R9. O mundo em unidades e a câmera escolhida.** x e y no chão, z para cima, cerca de 1 px por unidade; azimute de 45° por padrão (35 a 60° para mostrar o lado comprido), elevação de 30° (mais alta para olhar dentro de algo aberto). A face que carrega o mecanismo vira para quem lê, e a parte que precisa de espaço fica do lado oposto ao texto. A projeção são cinco linhas (`scripts/iso.js`, `camera`). À mão.

**R10. Geometria calculada uma vez, por código, nunca a olho.** Todo caminho parado se calcula num script; o que se move se constrói uma vez em repouso e se desloca; só se reconstrói a cada quadro o que muda de forma. Nada de `path` escrito à mão. À mão (as peças torneadas com sombreado contínuo, os tubos e os cabos ordenáveis são do kit).

**R11. Pintar de trás para a frente, de baixo para cima; partir o que abraça outra peça** (a mola em volta da haste vira metade de trás, haste, metade da frente). A ordem se escreve à mão até umas 30 peças sem cruzamento difícil; acima disso, ou com cascas uma dentro da outra, a ordem se prova por medida (a profundidade por pixel, amostrada, é um substituto à mão; a ordem medida e acertada sozinha é do kit). À mão até o limite; a prova automática, kit.

**R12. Esconder o que fica atrás.** Cada peça se preenche com o papel (opaco), sem aresta transparente nem linha oculta tracejada; a alternativa (cortar as linhas pela silhueta das da frente e deixar o papel aparecer) é gosto de quem chama, salvo quando o projeto já a decidiu (`projeto.md`). À mão.

## 5. Palavras e números

**R13. Palavras fora do desenho.** No máximo um rótulo gravado numa face; o resto na margem, com o rótulo do projeto, só para a peça que o texto nomeia. À mão.

**R14. Um modelo só move as peças e gera os números.** Toda posição, todo ângulo e todo número da tela saem do mesmo modelo puro, lido por `window.quadro(t)`; nenhum número é digitado à parte. Conte o que se desenha e tire o número da lista (desenhar 11 e escrever 8 é o erro clássico). À mão.

## 6. Movimento

**R15. Movimento calmo, por tempo, nunca por quadro.** Suavização exponencial (τ de 0,1 a 0,3 s) ou mola de verdade; evento único com ataque e queda (o `envelope` do `iso.js`), nunca um valor que vai a 1 num quadro; troca de cor com envelope próprio, mais lento que o da forma; quadro pré-calculado anda no máximo 0,25 px por passo; na página interativa, `dt` limitado a 1/30 s. A palavra que troca na tela também entra e sai com envelope. Pare no estado aberto o tempo de ler o arranjo (a imagem parada ganha da animação no arranjo espacial); o leve anda mais rápido que o pesado; linear só no que é mecânico; câmera parada contra o objeto que se move (as sínteses de princípios de motion design e de linguagem de câmera virtual, em `knowledge/generative-media/`). À mão.

**R16. Vista explodida pelos conjuntos reais:** cada um no sentido em que sai na oficina, quem está por fora sai primeiro e volta por último, o que está enfiado em outro compartilha o movimento. O desenho, à mão; a prova de que nada atravessa nada em cada quadro, pelo `intersecao.py` (à mão, no plano) ou pelo kit (em 3D).

**R17. Movimento reduzido:** num artifact ou página interativa, um quadro parado representativo, e a figura ainda responde. No post não se aplica. À mão.

## 7. As conferências (como ler cada uma em [`conferencias.md`](conferencias.md))

**R18. Zoom de 4× em cada junta, e ler cada recorte.** "The owner finds faults by zooming in, so you zoom in first." A ordem: linha que entra em algo, cruzamento na ordem errada, ponta pousada no contorno de outra linha, peça afundada ou solta, textura que para no meio. À mão (o `juntas.py`).

**R19. Toda linha termina em algo** (um traço, um ponto, um contorno, ou some em degradê); nenhuma para no ar. A versão reduzida é a ponta da seta no alvo; a inteira (toda ponta de traço do desenho) se mede no navegador, com 1 px até outro traço ou preenchimento pintado depois, a marca curta (até 7 px) enraizada a 2 px, e a ponta declarada livre passando. À mão (o algoritmo é curto; o `juntas.py` recorta as pontas para ler).

**R20. Interseção e profundidade provadas por medida:** nada atravessa nada em repouso, desmontado e em cada quadro da explosão; nenhuma ponta sem apoio. "A zero audit is necessary, not sufficient." À mão no plano, pelo `intersecao.py`; a prova em 3D com a ordem de pintura, kit.

**R21. A folha de quadros em câmera lenta:** todo vídeo passa por uma folha de quadros tirados do MP4 e pela diferença entre quadros seguidos, sem salto, sem troca súbita de cor, sem corte. À mão (o `saltos.py` e o `ffmpeg`).

**R22. A passada de detalhe não se traz** (encher, a 4×, todo canto vazio com peças verdadeiras): contraria o "um dominante por tela" e o enfeite que custa atenção.

## Anti-padrões (de figuras reprovadas)

A pilha abstrata (placas soltas fazendo de "camadas"; a saída é gaveta, bandeja em rack, cartão num suporte); a laje grande e lisa; a mobília de planta técnica (cota, hachura, balão numerado, aresta oculta tracejada); a linha que para no ar; o aramado (caixa transparente); cor em toda parte; texto no desenho; copiar a referência; o cano atravessando cano (só se vê a 4×); a textura que para no meio (esmaece no fim, não para de uma vez); o efeito que estoura ou é cortado; acertar um close-up a olho, que quebra outro (meça antes de olhar).
