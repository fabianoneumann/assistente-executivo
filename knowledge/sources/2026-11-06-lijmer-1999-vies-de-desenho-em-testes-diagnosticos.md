---
titulo: "Empirical Evidence of Design-Related Bias in Studies of Diagnostic Tests"
tipo: paper
autor: "Jeroen G. Lijmer, Ben Willem Mol, Siem Heisterkamp, Gouke J. Bonsel, Martin H. Prins, Jan H. P. van der Meulen, Patrick M. M. Bossuyt"
url: "https://jamanetwork.com/journals/jama/fullarticle/191668"
publicado_em: 1999
capturado_em: 2026-11-06
areas: [agent-engineering]
tags: [spectrum-bias, case-control, diagnostic-accuracy, study-design, publication-bias]
licenca: "JAMA, protegida; texto lido na página da editora, no Chrome. Só a ficha: o integral fica na url"
---

# Lijmer e outros 1999 (JAMA): o quanto falhas de desenho inflam a acurácia diagnóstica

Estudo observacional em JAMA, 282(11), 1999, sobre testes diagnósticos em medicina. Lido na página da editora. O integral está na `url`.

## Pergunta

Quanto as falhas de desenho, de coleta e de relato mudam a acurácia que um estudo de teste diagnóstico relata. A hipótese dos autores era que as estimativas viriam exageradas nos estudos que não cumprem os padrões de método. Eles partem de um problema prático: poucos estudos cumprem todos os critérios, e os pesos usados até ali para ponderar as falhas vinham de consenso, não de dados.

## Método

- **Busca:** meta-análises de testes diagnósticos em MEDLINE, EMBASE, Cochrane e DARE, de janeiro de 1996 a dezembro de 1997. Exigiam busca sistemática, ao menos 5 estudos e sensibilidade e especificidade de cada estudo. De 26 artigos, 15 saíram (7 sem busca sistemática, 8 sem a lista de valores), e ficaram 11.
- **Amostra:** os 11 artigos davam 18 meta-análises separadas e 193 estudos publicados. Nove não serviram (4 só com resumo, 5 sem tabela 2×2 possível). Sobraram 184 estudos e 218 avaliações de teste.
- **Leitura:** um autor extraiu as características num formulário, um segundo pontuou de forma independente, e a discordância ia a consenso ou a um terceiro. As notas de 20 estudos mudaram depois do consenso.
- **Medida:** razão de chances diagnóstica (DOR), a chance de resultado positivo em doentes dividida pela de não doentes, que junta sensibilidade e especificidade num número.
- **Modelo:** regressão linear ponderada, de efeitos fixos, adaptada do modelo de curva ROC resumida. A variável dependente é o log da DOR, com dois parâmetros por meta-análise (a DOR comum e o limiar) e 9 covariáveis, uma por característica, avaliadas ao mesmo tempo. O antilog da covariável é a DOR relativa (RDOR): acima de 1, o estudo sem o critério relata acurácia maior que o estudo com ele. Células zero recebem 0,5.

## Definições de falha

- **Caso-controle:** avaliar o teste em pacientes já sabidamente doentes e num grupo separado de pessoas normais, no lugar de uma população clínica relevante, que cubra o espectro da doença esperado no uso. O desenho considerado ótimo é a comparação cega e prospectiva numa série consecutiva dessa população.
- **Seleção:** inclusão não consecutiva nem aleatória.
- **Verificação parcial:** mais de 10% do grupo não passa pelo teste de referência.
- **Referência diferencial:** testes de referência diferentes para resultados positivos e negativos.
- **Sem cegamento:** ler um teste sabendo o resultado do outro.
- **Relato:** dados coletados de forma retrospectiva, e descrição insuficiente do teste, da referência ou da população (idade, proporção entre os sexos ou distribuição de sintomas, dois deles).

## Quantos estudos em cada classe (Tabela 2, N = 218)

| Característica | Classes |
|---|---|
| Espectro | população clínica 213; **caso-controle 5** |
| Verificação | completa 106; referências diferentes 48; parcial 54 |
| Interpretação | cega 70; não cega 148 |
| Seleção | consecutiva 97; não consecutiva 121 |
| Coleta | prospectiva 98; desconhecida 92; retrospectiva 28 |
| Detalhe do teste | suficiente 195; insuficiente 23 |
| Detalhe da referência | suficiente 138; insuficiente 80 |
| Detalhe da população | suficiente 132; insuficiente 86 |

Só 15 das 218 (6,8%) cumpriram os 8 critérios, e 64 (30%), 6 ou mais.

## Resultados (RDOR, IC de 95% quando o texto dá)

- **Caso-controle contra população clínica: 3,0 (2,0 a 4,5).** Foi o maior efeito.
- **Referências diferentes: 2,2 (1,5 a 3,3).**
- **Verificação parcial: 1,0.** Em média, a mesma DOR da verificação completa.
- **Sem cegamento: 1,3 (1,0 a 1,9).**
- **Sem critérios do teste descritos: 1,7 (1,1 a 2,5).**
- **Sem descrição da população: 1,4 (1,1 a 1,7).**
- **Inclusão não consecutiva:** não mudou a estimativa de forma significativa.
- **Coleta retrospectiva:** sem associação, comparada à prospectiva ou desconhecida. As duas últimas foram juntadas porque, na análise univariada, não mostrada, a desconhecida ficou perto da prospectiva.
- **Sem detalhe do corte da referência:** DOR cerca de 30% menor, a única no sentido contrário.

## O que os autores dizem do mecanismo e dos limites

- Atribuem o efeito do caso-controle ao espectro: sem os doentes de quadro leve, os que dão mais trabalho ao teste, as duas medidas sobem.
- A referência diferencial depende da qualidade dos testes: uma referência boa para os positivos e fraca para os negativos superestima as duas medidas. Se a fraca falha em achar verdadeiros negativos, pode subestimar. O exemplo é a proteína C reativa na apendicite aguda, em que os casos de proteína baixa não vão à cirurgia e o seguimento não pega as infecções leves que se resolvem sozinhas.
- A verificação parcial sem efeito pode vir da definição usada, que conta também o paciente não verificado por acaso.
- O efeito pequeno do cegamento depende da referência: com referência objetiva não se espera efeito, e com referência subjetiva pode ser maior.
- As falhas de relato parecem marcar outras falhas de método; os autores dizem que não está claro como levam à superestimação.
- Limitar a amostra a meta-análises recentes pode ter mudado a frequência das características, não necessariamente o tamanho relativo dos efeitos, dizem.
- **Viés de publicação:** só entraram estudos publicados; se os de boa qualidade ou de resultado animador se publicam mais, as associações podem estar infladas. Propõem um registro central de protocolos de pesquisa diagnóstica.

## Tudo o mais que ensina

- **Tradução em pontos:** um estudo com referências diferentes, sem cegamento e sem descrever o teste superestimaria a DOR em média 5 vezes, o que equivale a relatar sensibilidade e especificidade de cerca de 84% quando as duas deveriam ser 70%. A diferença cai com sensibilidade e especificidade mais altas e com poucas falhas menores.
- **Uso prático:** ao ler um estudo, é difícil pesar as falhas contra a evidência; os resultados servem para avaliar a literatura e pedem relato explícito de como os pacientes foram selecionados, como a doença foi verificada e como se interpretaram o teste e a referência.
- **Trabalhos anteriores:** quatro meta-análises tinham examinado o efeito das características, todas sobre um teste só, com resultados divergentes sobre verificação parcial e cegamento.
- "Studies using a case-control design tended to overestimate the DOR 3-fold compared with studies with a clinical cohort."
