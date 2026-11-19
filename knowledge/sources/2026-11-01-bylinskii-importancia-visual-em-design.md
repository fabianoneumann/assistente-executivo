---
titulo: "Learning Visual Importance for Graphic Designs and Data Visualizations"
tipo: paper
autor: "Zoya Bylinskii, Nam Wook Kim, Peter O'Donovan, Sami Alsheikh, Spandan Madan, Hanspeter Pfister, Fredo Durand, Bryan Russell, Aaron Hertzmann"
url: "https://arxiv.org/abs/1708.02660"
publicado_em: 2017-08-08
capturado_em: 2026-11-01
licenca: "Licença não exclusiva de distribuição do arXiv (arxiv.org/licenses/nonexclusive-distrib/1.0/, indicada na página do arXiv); a versão dos anais do UIST 2017 (DOI 10.1145/3126594.3126653) é da ACM, com copyright. Entra só a ficha."
areas: [agent-engineering, content-design]
tags: [visual-importance, saliency, visual-hierarchy, graphic-design, eye-tracking, bubbleview, human-agreement, retargeting, design-feedback, adobe]
---

Ficha de estudo, em palavras próprias; sem texto integral. arXiv: v1 em 08/08/2017, a única versão; publicado nos anais do UIST 2017 (Quebec, outubro de 2017). Autores do MIT CSAIL, Harvard SEAS e Adobe. Texto extraído do PDF com `pdftotext`; as Tabelas 1 a 3 lidas no texto extraído. Lido para a rodada investigativa, pelo D1 (hierarquia): é a referência clássica de mapa de "importância" para design gráfico, distinto da saliência de foto, e validado contra cliques, anotações e olhar de pessoas.

## 1. A pergunta

Saber onde as pessoas olham e clicam num design dá pista de como ele é percebido e de onde está o conteúdo importante. Modelos de saliência feitos para fotos vão mal em visualizações e designs. Os autores treinam redes que preveem, a partir só da imagem (sem o arquivo vetorial), a **importância relativa** de cada região de um design gráfico ou de uma visualização de dados, e mostram aplicações: recorte para outro formato, miniatura e retorno imediato numa ferramenta de design.

## 2. Os dados de importância

- **Design gráfico:** o conjunto GDI (O'Donovan et al.), 1.078 designs do Flickr; 35 pessoas por design marcaram com máscara as regiões importantes, sem definição do que é "importante"; as máscaras são somadas.
- **Visualizações:** 1,4 mil visualizações do MASSVIS com cliques coletados pelo BubbleView (a pessoa vê a imagem borrada e clica para revelar pequenas regiões; cerca de 15 pessoas por imagem, com descrição obrigatória para garantir exploração).
- **Cliques contra olhar:** nas visualizações com rastreamento ocular (cerca de 16 pessoas, 10 segundos), os elementos mais clicados são também os mais olhados (Spearman de 0,96 por elemento, no exemplo da Figura 6). Nos designs, cliques e máscaras do GDI apontam regiões parecidas; as máscaras dão importância uniforme ao elemento inteiro, os cliques não.

## 3. O modelo e a validação

- Rede totalmente convolucional, uma para designs e uma para visualizações, com perda equivalente à divergência KL; 0,1 s por imagem em GPU.
- **Visualizações (Tabela 1):** contra os cliques, correlação de mapa (CC) de 0,69 contra 0,57 do melhor modelo de saliência de foto (DeepGaze). **Contra o olhar (Tabela 2):** CC de 0,54, perto do DeepGaze (0,53), abaixo do que os próprios cliques preveem do olhar (0,79). No exemplo da Figura 6, o modelo acerta a ordem de importância dos elementos em relação ao olhar (Spearman de 0,96).
- **Design gráfico (Tabela 3, R² contra o GDI):** 0,576, contra 0,539 da versão automática do modelo do O'Donovan e 0,462 de uma combinação de quatro modelos de saliência; a versão do O'Donovan com anotação manual de texto, rosto e pessoa chega a 0,754, e somar as duas a 0,769. **Por elemento:** Spearman médio de 0,56 entre a importância prevista e a anotada para os elementos de cada design de teste.
- **O que o modelo aprendeu:** títulos de visualização muito bem; em designs, texto e elementos maiores e mais centrais como mais importantes.
- **Aplicações:** recorte e miniatura guiados pela importância, avaliados por centenas de pessoas no MTurk, ficam iguais ou melhores que os métodos de referência, inclusive saliência de foto; um protótipo atualiza o mapa enquanto o designer move elementos.

## 4. Limites declarados

O modelo é tão bom quanto os dados: nas visualizações há forte viés para o texto, tanto no modelo quanto nas pessoas, que pode não valer para outros tipos e tarefas; os cliques não são uniformes no elemento e podem cortar texto no recorte.

## 5. Tudo o mais que ensina

- **Importância não é qualidade:** o mapa diz para onde a atenção vai, não se a hierarquia está certa. Leitura nossa: o uso para o juiz é comparar o mapa previsto com a hierarquia pretendida (o título que a peça manda ler primeiro deveria ser o mais importante), o "teste de apertar os olhos" do D1 feito por um modelo de atenção, e não por uma nota.
- **Modelos de saliência feitos para foto vão mal em visualização** (Haass et al., citados), e métodos de saliência de página web costumam usar o DOM como entrada; este modelo usa só a imagem.
- **Métricas de saliência:** a correlação de mapa (CC) trata erro para mais e para menos igualmente; a KL pune mais deixar de prever uma região importante, e os autores desaconselham usá-la sozinha para comparar modelos.
- **Fonte de 2017:** modelos de atenção mais recentes para interfaces existem (não abertos nesta rodada); o valor aqui é o desenho do problema e a validação.
