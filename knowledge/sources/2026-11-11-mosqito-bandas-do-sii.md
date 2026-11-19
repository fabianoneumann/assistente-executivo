---
titulo: "MoSQITo: dados das bandas do índice de inteligibilidade da fala (SII, ANSI S3.5-1997)"
tipo: instrumento
autor: "Eomys e colaboradores do MoSQITo (biblioteca Python de qualidade sonora)"
url: "https://github.com/Eomys/MoSQITo/blob/master/mosqito/sq_metrics/speech_intelligibility/sii_ansi/_band_procedure_data.py"
capturado_em: 2026-11-11
areas: [generative-media]
tags: [speech-intelligibility, sii, frequency-bands, masking, audio-mixing]
licenca: "Apache-2.0 (a licença do repositório Eomys/MoSQITo no GitHub); o integral está na url, com a atribuição; lido no commit d990c33f94f1"
---

# MoSQITo: os pesos das bandas do índice de inteligibilidade da fala

Ficha do arquivo de dados da implementação do índice de inteligibilidade da fala (SII) da norma ANSI S3.5-1997 na biblioteca MoSQITo, e do passo de audibilidade do arquivo `_main_sii.py` ao lado, lidos como texto em 2026-11-11 (commit d990c33f94f1). É uma implementação de terceiros da norma, que não foi aberta (a norma é paga).

## Ficha

- **O que é o SII:** um índice de 0 a 1 de quanto da fala chega audível a quem ouve, somando, banda a banda, a importância da banda vezes a audibilidade dela. A norma tem quatro jeitos de dividir o espectro (21 bandas críticas, 17 bandas críticas de contribuição igual, 18 terços de oitava e 6 oitavas), cada um com a sua tabela de importância.
- **A importância por oitava** (centros de 250 Hz a 8 kHz): 0,0617, 0,1671, 0,2373, 0,2648, 0,2142 e 0,0549. As oitavas de 1, 2 e 4 kHz (de 710 a 5.680 Hz) somam cerca de 0,72 do total; a de 250 Hz, 0,06.
- **Em terços de oitava,** o peso sobe de 0,008 em 160 Hz até o máximo de 0,090 em 2 kHz e cai para 0,019 em 8 kHz.
- **A audibilidade de cada banda** (passo 7 do `_main_sii.py`): `(nível da fala - nível do ruído ou da máscara + 15) / 30`, limitada entre 0 e 1. A banda é inaudível quando a fala está 15 dB abaixo da máscara e conta inteira quando está 15 dB acima.
- **O que fica de fora do arquivo:** o espectro padrão da fala em esforço normal, o ruído interno de referência e a função de transferência para o tímpano estão no mesmo arquivo (abaixo); a distorção por nível alto e o espalhamento da máscara estão no `_main_sii.py`, não copiado aqui.
