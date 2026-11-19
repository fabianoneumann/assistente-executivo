---
titulo: "Launch recordings from the command line | Recorder | 5.1.8"
tipo: artigo
autor: "Unity Technologies (documentação oficial)"   # a página não tem assinatura; o rodapé diz 'Copyright © 2026 Unity Technologies'
url: "https://docs.unity3d.com/Packages/com.unity.recorder@5.1/manual/CommandLineRecorder.html"
publicado_em: null   # a página não traz data
capturado_em: 2026-11-13
licenca: "protegido (rodapé: 'Copyright © 2026 Unity Technologies'; sem licença de conteúdo declarada no texto lido); nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [unity, unity-recorder, video-capture, command-line, csharp, batch-rendering]
---

# Unity Recorder 5.1: gravar pela linha de comando, com o Editor aberto e em Play

Nota de fato: o tutorial do manual do Recorder que monta a gravação pela linha de comando, com os passos numa lista, porque a ordem é o método, e tabelas do que cada parte do código faz, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a página é protegida, e o código dela não se copia aqui, só se descreve. É fonte técnica curta, por isso nota de fato, na ordem da página (o `README.md` desta pasta, item 2, a exceção da página técnica); a medida da cópia é a do `parafrase.py` e a da conta lado a lado.

**Proveniência.** Página do manual do pacote Recorder, https://docs.unity3d.com/Packages/com.unity.recorder@5.1/manual/CommandLineRecorder.html, servida como versão 5.1.8, baixada com `curl` em 13/11/2026 e lida no texto do bloco `<article>` (1.358 palavras, de "Launch recordings from the command line" a "Batch recording"), conferido no HTML; sha256 (hash omitido) (como registra o `protegidas.json` da rodada, é o hash do texto do bloco, não do arquivo HTML); Wayback http://web.archive.org/web/20240922084701/https://docs.unity3d.com/Packages/com.unity.recorder@5.1/manual/CommandLineRecorder.html, de 2024. Título conferido no `<title>`: "Launch recordings from the command line | Recorder | 5.1.8". Lida a página inteira. No HTML servido, o código da função `ExecuteCommandLine` termina no meio da chamada a `SetRecordingInfo`, e o texto segue com "Now, your CommandLineRecorder should look like this." sem o resto do código; a página "Unity Editor command line arguments", ligada, não foi aberta.

**Conferência lado a lado** (2026-11-13, pela régua do item 2 do `README.md` desta pasta). Conferência automática: o `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês) contra `unity-recorder-linha-de-comando.txt` (o texto do bloco, na cópia de trabalho), com 32 unidades medidas (20 de prosa, 12 de célula com texto), 1 colada, que são nomes em inglês (Samples, Package Manager), fatos sem outra grafia, e 0 trechos de 3 ou mais seguidas. Na leitura lado a lado, segue a fonte a unidade que traduz uma frase dela, junta duas ou funde três ou mais na ordem dela, e conta como unidade que segue a fonte a célula que o script partiu em pedaços da mesma frase: 18 de 23 unidades do corpo (de "Em uma frase" em diante), 18 de 32 com as 9 do cabeçalho de proveniência, que não tratam do conteúdo. A maior sequência de unidades seguidas que seguem a fonte na ordem dela é de 15, dos passos ao preparo do comando: a página é técnica e lista fatos, e a ficha segue a ordem dela pela exceção do item 2; não há texto argumentativo do autor na página.

## Em uma frase

Tutorial oficial que grava pela linha de comando com um preset do Recorder e um script em C# na cena: o comando abre a Unity com `-projectPath` e `-executeMethod`, o script entra em Play, grava o intervalo de quadros pedido e sai do Play; para muitas gravações, um arquivo de lote ou um script de PowerShell chama o comando várias vezes.

## Os passos, na ordem da página

1. Criar presets de configuração do Recorder, um por tipo ou variante de saída, com nomes claros para chamar depois. O exemplo é um preset de filme em Full HD (FHD 1080, 1920 × 1080): abrir a janela do Recorder, adicionar um Movie recorder, escolher a resolução, salvar como preset pelo ícone de preset e nomeá-lo `HDMovieRecorderSettings.preset`.
2. Criar um MonoBehaviour `CommandLineRecorder` e prendê-lo a um GameObject da cena.
3. Escrever as funções que carregam o preset, iniciam a gravação e param no fim (tabela abaixo).
4. Escrever as funções chamáveis de fora, que leem os argumentos e entram em Play.
5. Preparar o projeto e chamar o comando.
6. Para gravar em lote, montar uma fila de comandos.

## O que cada parte do script faz

| Parte | O que faz, pela página |
|---|---|
| Campos `m_startFrame`, `m_endFrame`, `m_presetPath` | o primeiro e o último quadro e o caminho do preset, serializados para não se perderem ao entrar em Play |
| `RecorderController` | começa e para a gravação |
| `LoadRecorderSettingsFromPreset` | carrega o preset pelo caminho, acha por reflexão o tipo de configuração (um `MovieRecorderSettings`, por exemplo), cria a instância e aplica o preset |
| `StartRecording` | cria a configuração a partir do preset, fixa 60 quadros por segundo, monta um `RecorderControllerSettings` com o intervalo de quadros e chama `PrepareRecording` e `StartRecording` |
| `OnEnable` | roda uma vez ao entrar em Play e inicia a gravação |
| `Update` | a cada quadro em Play; quando o controlador não grava mais, para e sai do Play com `EditorApplication.ExitPlaymode()` |
| `GetCommandLineArgs` | lê `-startFrame`, `-endFrame` e `-presetPath` da linha de comando |
| `SetRecordingInfo` | guarda os três valores no MonoBehaviour e salva os assets |
| `ExecuteCommandLine` | estática e pública, a chamada de fora: confere os três argumentos (erro se faltar um), acha o `CommandLineRecorder` da cena e passa os valores; a busca usa `FindObjectsByType` com uma forma para a Unity 6000.4 ou mais nova e outra para as anteriores |
| Mais exemplos | nos Samples do pacote Recorder, pelo Package Manager |

## O comando

| Item | Fato |
|---|---|
| Preparar | tirar os recorders da janela do Recorder, fechá-la, salvar e fechar o projeto, entrar pelo terminal na raiz do projeto |
| Estrutura | `<executável da Unity> -projectPath <projeto> -executeMethod <função> <parâmetros próprios>` |
| Exemplo no Windows (PowerShell) | `& 'C:\Program Files\Unity\Hub\Editor\2023.2.0b4\Editor\Unity.exe' -projectPath . -executeMethod CommandLineRecorder.ExecuteCommandLine -startFrame 0 -endFrame 10 -presetPath 'Assets/HDMovieRecorderSettings.preset'` |
| Exemplos de macOS e Linux | os mesmos argumentos, com o executável de cada sistema (versões 2023.1.10f1 e 2023.2.0b2 nos exemplos) |
| `-batchmode` ou `-nographics` | não aparecem em nenhum exemplo |
| O que acontece | a Unity abre e começa a gravar |
| No fim | a Unity sai do Play; o filme novo fica na pasta Recordings, na raiz do projeto |
| Erro comum | um NullRefException no console: o `-presetPath` está errado; ele vai entre aspas, só com barras normais (também no Windows), começando por `Assets` |

## O que a fonte recomenda

Preparar um preset por saída, com nome claro, e expor uma função estática que lê os quadros e o preset da linha de comando; antes de chamar, limpar a janela do Recorder e fechar o projeto. Para muitas gravações, um script de lote que chama o mesmo comando com presets diferentes, e o script do tutorial pode ganhar mais parâmetros.

## Citações

- "When you execute the command, Unity opens and start the recording."
- "Use this setup to enable batch recording via a job queue of many command lines targeting different recordings."

## Lacuna

A página não diz se a gravação funciona com `-batchmode` ou sem placa de vídeo, nem se a janela da Unity fica aberta durante a gravação; não diz como a Unity fecha ao fim (o script sai do Play, e o texto não fala em sair do programa). Não diz com que versões da Unity o Recorder 5.1 funciona, que formatos o Movie recorder grava, nem se a resolução vertical (1080 × 1920) serve. O código da `ExecuteCommandLine` está cortado no HTML servido.
