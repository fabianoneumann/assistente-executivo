---
titulo: "Audio understanding - Gemini API"
tipo: artigo
autor: "Google AI for Developers"
url: "https://ai.google.dev/gemini-api/docs/audio"
capturado_em: 2026-11-11
areas: [generative-media, agent-engineering]
tags: [audio-understanding, gemini, multimodal, api-pricing, audio-evaluation]
licenca: "em dúvida: as páginas do Google for Developers costumam declarar CC BY 4.0 no rodapé, mas o HTML baixado não traz a declaração; tratado como protegido, ficha em palavras próprias, sem o integral"
---

# Google: o que o Gemini faz com áudio, pela documentação da API

Ficha da página de documentação do Gemini sobre entender áudio, baixada em 2026-11-11 (os exemplos de código citam o `gemini-3.8-flash`). O HTML salvo declara como canônica a página `https://aistudio.google.com/docs/audio`: a `url` acima é o endereço que a busca devolveu, e a documentação responde também, como endereço oficial, no AI Studio. Fonte curta: organizada pelo que serve a quem quer usar o modelo para ouvir um arquivo (o que entra, o que ele faz, o que se perde no caminho), e não pela ordem da página.

## O que entra

- Formatos: WAV, MP3, AIFF, AAC, OGG, FLAC, MPEG, M4A, L16, Opus, A-law, mu-law e WebM.
- O arquivo vai junto do pedido ou, se o pedido passar de 20 MB, pela Files API; há uma chamada para contar os tokens antes.
- **Até 9,5 horas de áudio por pedido.**

## O que o modelo faz, segundo a página

- Descrever, resumir ou responder perguntas sobre o áudio; transcrever e traduzir; separar quem fala; detectar emoção na fala e na música; analisar trechos marcados por tempo (o exemplo pede marcas no formato minuto:segundo).
- **Entende sons que não são fala** (o exemplo dado: canto de pássaro, sirene).
- Para fala em tempo real, a página manda para a Live API; para transcrição dedicada, para o Speech-to-Text do Google Cloud.

## O que se perde no caminho

- **O áudio é reduzido a 16 kbps** (é o que a página escreve) e **os canais viram um só**: o modelo não ouve o estéreo e ouve uma versão de baixa resolução do arquivo.
- **Cada segundo de áudio conta 32 tokens** (um minuto, 1.920).
