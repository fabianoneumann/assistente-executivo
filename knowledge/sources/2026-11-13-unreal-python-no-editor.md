---
titulo: "Scripting the Unreal Editor Using Python"
tipo: artigo
autor: "Epic Games (documentação oficial do Unreal Engine)"   # a página não tem assinatura de pessoa
url: "https://dev.epicgames.com/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python"
publicado_em: null   # sem data visível; o título diz "Unreal Engine 5.9 Documentation"; o HTML tem carimbos created_at e updated_at de 2026-11-10 de um bloco, que datam o bloco, não a página
capturado_em: 2026-11-13
licenca: "protegido (documentação da Epic Games; nenhum aviso de direitos nem licença de conteúdo no HTML baixado, cujo rodapé é montado no navegador; tratada como protegida); nota de fato em palavras próprias, sem o integral"
areas: [generative-media]
tags: [unreal-engine, python, command-line, headless, automation, editor-scripting, mcp]
---

# Unreal Engine 5.9: Python no Editor, dos jeitos de rodar um script à API `unreal`

Nota de fato: tabelas do que a página da documentação diz sobre o Python no Unreal Editor, uma seção por parte da página, na ordem dela, com prosa só para dizer o que a fonte é, o que ela recomenda e o que falta. Não há integral: a página é protegida. É fonte técnica longa que lista fatos (o que cada jeito de rodar faz, o que cada caminho aceita), então as seções e as linhas seguem a ordem da página, sem reordenar (o `README.md` desta pasta, item 2, e Passo 7, item 1, da `research`); a medida da cópia é a do `parafrase.py` e a da conta lado a lado, com a maior sequência declarada.

**Proveniência.** Página de dev.epicgames.com, baixada com `curl` em 13/11/2026 e lida no texto do bloco `<article>` (4.888 palavras, de "Why Python?" a "Using Python with AI Agents"), conferido no HTML; sha256 (hash omitido) (como registra o `protegidas.json` da rodada, é o hash do texto do bloco, não do arquivo HTML); Wayback http://web.archive.org/web/20251215170752/https://dev.epicgames.com/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python, anterior à versão lida. Título conferido no `<title>`: "Scripting the Unreal Editor Using Python | Unreal Engine 5.9 Documentation". Lida a página inteira nesta captura (o rótulo do Passo 5 registrava só as seções de linha de comando e do `init_unreal.py`); as imagens, a referência da API e as páginas ligadas ("Using Python with AI Agents", "Scripting and Automating the Unreal Editor") não foram abertas.

**Conferência lado a lado** (2026-11-13, pela régua do item 2 do `README.md` desta pasta). Conferência automática: o `parafrase.py` saiu com o código 3 (ficha em português, fonte em inglês) contra `epic-python-editor-scripting.txt` (o texto do bloco, na cópia de trabalho), com 66 unidades medidas (16 de prosa, 50 de célula com texto), 0 coladas e 0 trechos de 3 ou mais seguidas. Na leitura lado a lado, segue a fonte a unidade que traduz uma frase dela, junta duas ou funde três ou mais na ordem dela, e conta como unidade que segue a fonte a célula que o script partiu em pedaços da mesma frase: 52 de 58 unidades do corpo (de "Em uma frase" em diante), 52 de 66 com as 8 do cabeçalho de proveniência, que não tratam do conteúdo. A maior sequência de unidades seguidas que seguem a fonte na ordem dela é de 52, de "Por que Python" a "Python com agentes de IA": a página é técnica e lista fatos, e a ficha segue a ordem dela pela exceção do item 2; o texto argumentativo da abertura (por que Python) ocupa duas células seguidas.

## Em uma frase

O Python do Unreal vem num plugin do Editor, com o Python 3.11.8 embutido, roda só no Editor (nunca no jogo), pode ser disparado do console, do menu, da linha de comando (em que o Editor fecha ao fim do script), da inicialização do projeto e de Blueprints só de Editor e enxerga pela API `unreal` quase tudo o que o C++ expõe aos Blueprints.

## Por que Python, e para quê

| Item | O que a página diz |
|---|---|
| A razão de fundo | o Python virou a língua comum dos pipelines de produção e da troca entre programas 3D, em mídia e entretenimento |
| Para quem começa | fácil de aprender, com interface própria pelo PySide e muitos módulos livres |
| Usos citados | pipelines de assets que ligam o Editor a outros programas 3D; automatizar tarefa de asset, como gerar LODs de malhas estáticas; dispor conteúdo num nível por procedimento; controlar o Editor por interface feita em Python |

## Preparar o projeto

| Item | Fato |
|---|---|
| Plugin | Python Editor Script Plugin, em Edit > Plugins > Scripting |
| Por projeto | o plugin se liga em cada projeto, separado |
| Plugin recomendado junto | Editor Scripting Utilities, com APIs simplificadas para tarefas comuns |
| Depois de ligar | reiniciar o Editor |
| Python embutido | 3.11.8, sem instalar Python à parte |
| Por que 3.11.8 | faz parte da VFX Reference Platform atual |
| Outra versão | a variável `UE_PYTHON_DIR` apontando para outra instalação, e o motor recompilado do código-fonte |

## Os jeitos de rodar

**Onde o Python existe:** só no Unreal Editor. Não roda com o projeto em execução em nenhum modo (Play In Editor, Standalone Game, executável empacotado), então serve para automatizar o Editor e para pipelines de assets, não como linguagem de jogo.

| Jeito | Como | O que a página diz dele |
|---|---|---|
| Console em modo Python, no Output Log | trocar a barra do console para Python (também pela tecla de crase) | o único jeito de rodar linha a linha; Shift + Enter separa linhas; o nome de um arquivo roda o arquivo, com argumentos depois; o `print` sai no Output Log |
| Comando `py` | no console em modo Cmd, `py "C:\MyScripts\my_script.py"` | roda o resto da linha como Python; não usar no `ExecCmd` da linha de comando ao abrir o Editor, porque o script pode rodar antes de o nível inicial carregar |
| Menu File | Execute Python Script, ou a lista Recent Python scripts | a lista relê o arquivo do disco, então roda a versão editada |
| Linha de comando, opção 1: Editor inteiro | `UnrealEditor-Cmd.exe "<projeto>.uproject" -ExecutePythonScript="<script>.py"` | abre o Editor inteiro, o projeto e o nível inicial, e roda o script quando tudo carregou; para script que mexe em conteúdo ou em nível demorado; pede os plugins Editor Scripting Utilities e Python Editor Script no projeto |
| Linha de comando, opção 2: commandlet | `UnrealEditor-Cmd.exe "<projeto>.uproject" -run=pythonscript -script=<arquivo ou código>` | rápido, pode rodar sem abrir a interface do Editor; aceita o caminho de um script ou comandos Python, com `\n` para quebrar linha; não carrega nível sozinho, então o script começa com `unreal.get_editor_subsystem(unreal.LevelEditorSubsystem).load_level(...)`; pede o Python Editor Script Plugin |
| Arquivo `init_unreal.py` | em `Content/Python` do projeto ou do plugin | roda sozinho toda vez que o Editor abre, para o código de inicialização que todos do projeto precisam; os plugins que trazem ferramentas em Python para agentes de IA registram as ferramentas por ele |
| Scripts de inicialização | Project Settings > Plugins > Python > Startup scripts | rodam a cada abertura do projeto, depois de o nível inicial carregar por inteiro; pedem reiniciar o Editor ao mudar |

**Nas duas opções de linha de comando,** o Editor fecha logo depois de rodar o script, e os argumentos do script vêm depois do nome dele.

## Python em Blueprints só de Editor

| Nó (Python > Execution) | O que faz |
|---|---|
| Onde funciona | só em classes de Blueprint só de Editor (Editor Utility Widgets, Editor Utility Blueprints), nunca nas que existem no jogo, como uma derivada de Actor |
| Execute Python Script | roda o código Python escrito no nó; é o jeito recomendado, no lugar de criar em Python um BlueprintFunctionLibrary (BPFL) |
| O BPFL feito em Python | dá problema ao salvar ou carregar asset, porque o tipo gerado é transitório, e saiu do suporte oficial |
| Pinos do Execute Python Script | entradas e saídas próprias, que viram variáveis no script; as entradas valem antes de rodar, as saídas se leem depois |
| Retorno | verdadeiro se rodou; falso, com o erro no Output Log; não roda arquivo, só código |
| Execute Python Command | roda código ou arquivo, e decide sozinho qual dos dois recebeu |
| Execute Python Command (Advanced) | o mesmo, com o modo de execução: Execute File (trata a entrada como arquivo), Execute Script (como código) e Evaluate Script (avalia e devolve o valor em Command Result) |
| Escopo do arquivo | Public (global, enxerga e pode redefinir o que já existe) ou Private (isolado); a página diz que o Private é o mais seguro |
| Command Result | o valor, no Evaluate Script; `None`, no Execute File e no Execute Script; o erro, quando falha |

## Caminhos do Python no Editor

| Item | Fato |
|---|---|
| Onde o `import` e o caminho relativo procuram | as pastas de `sys.path` |
| Pastas que o Editor põe sozinho | `Content/Python` do projeto; `Content/Python` da instalação do motor; `Content/Python` de cada plugin ligado; `Documents/UnrealEngine/Python` do usuário (no Windows, dentro da pasta `Documents` do usuário) |
| Acrescentar pastas | em Project Settings > Plugins > Python > Additional Paths (e reiniciar); pela variável `UE_PYTHONPATH` (ou `PYTHONPATH`, com o isolamento desligado); direto no `sys.path`; ou pelo C++, com `IPythonScriptPlugin::GetAdditionalPathsInterface()` |
| Regras do caminho pelo C++ | um dono por caminho; absoluto e já existente; `AddAdditionalPath` devolve falso se o caminho é inválido ou já está no `sys.path` |
| Ponto de montagem opcional | dá nome estável aos tipos gerados pelo Python (como `/MyPlugin/Python/Extra/MyClass_PY.MyClass`) |
| Limpeza dos tipos gerados | automática quando o plugin dono sai, se o dono nomeia o plugin e o ponto fica dentro de `/<Plugin>/Python`; tirar o caminho não descarrega módulo nem limpa tipo |
| Acrescentar caminho | não cria montagem de conteúdo nem roda script de inicialização |
| Isolamento | o interpretador roda isolado por padrão (o `-I` do Python); o ajuste fica em Project Settings > Plugins > Python > Isolate Interpreter Environment |
| `UE_PYTHONPATH` | sempre lida, com ou sem isolamento; tem o papel do `PYTHONPATH` e não deve ser mexida por programa de terceiros |

## A API `unreal`

| Item | Fato |
|---|---|
| Onde fica | no módulo `unreal`, importado no começo do script |
| O que expõe | quase tudo o que o C++ expõe aos Blueprints no Editor |
| Como se forma | não vem gerada de antemão: reflete o que existe nos Blueprints naquele Editor, inclusive o que plugins ligados e C++ do projeto expõem |
| Tipos simples | convertidos entre Python e o nativo quando preciso |
| Listas, conjuntos e dicionários | viram array, set e map do Unreal; o que volta é classe do Unreal com a mesma API do tipo Python |
| Herança | a mesma dos tipos nativos; `isinstance()` e `type()` funcionam |
| Nomes | as classes com o nome dos Blueprints (sem o prefixo U ou T); funções e propriedades em `snake_case` minúsculo (`unreal.StaticMeshActor.get_actor_transform()`); valores de enumeração em `SNAKE_CASE` maiúsculo |
| Parâmetros | por posição ou por nome, em qualquer ordem |

| Expor C++ ao Python | Fato |
|---|---|
| Quando a função aparece no Python | `UFUNCTION` com `BlueprintCallable` ou `BlueprintEvent`, ou com o metadado `PythonCallable` |
| `PythonCallable` | para API de script do Editor que não deve aparecer nos grafos de Blueprint |
| O que impede a exposição, mesmo com `PythonCallable` | `ScriptNoExport`, `BlueprintGetter`, `BlueprintSetter`, `BlueprintInternalUseOnly`, `CustomThunk`, `NativeMakeFunc`, `NativeBreakFunc` |
| Para Python e para agentes de IA | os dois especificadores juntos, como `meta = (PythonCallable, AICallable, AIAccessMode = "Read")`; o `AICallable` remete à página do Unreal MCP |

| Blueprints e structs no Python | Fato |
|---|---|
| Classe de Blueprint | ganha um tipo Python próprio, subclasse do pai nativo (um Actor Blueprint `BP_MyActor` aparece como `BP_MyActor_C`, subclasse de `unreal.Actor`), com as propriedades e funções do Blueprint |
| User Defined Struct | ganha um tipo próprio, subclasse de `unreal.StructBase` |
| Até a 5.8 | o Python via a classe de Blueprint como o pai nativo mais próximo, e a struct como `unreal.StructBase` |
| Voltar ao jeito antigo | `Engine.Python.WrapBlueprintClassesOnDemand` e `Engine.Python.WrapUserDefinedStructsOnDemand` em falso (o padrão é verdadeiro) |
| Script que funciona nos dois | o que usa `isinstance()` com classe nativa, ou `get_editor_property()` para ler variável de Blueprint |
| Script da 5.8 que pode quebrar na 5.9 | o que compara `type(obj)` com classe nativa ou depende do nome do tipo |

| Outros comportamentos | Fato |
|---|---|
| Carregar nível | `LevelEditorSubsystem.load_level` recebe `UnsavedChangesPolicy`; no padrão, `Fail`, dá erro nomeando os pacotes com mudança não salva; `Save` salva antes de carregar |
| Gerar PCG | por `ExecuteGraphInstance` com uma fonte de execução; `Generate` e `GenerateLocal` do `PCGComponent` não existem no Python |
| Áudio | os subsistemas de script do editor de áudio estão no Python |
| Referência da API | a Unreal Editor Python API Reference, que não lista tudo o que plugins expõem; dá para gerar uma versão local pelo readme de `Engine\Plugins\Experimental\PythonScriptPlugin\SphinxDocs` |

## Boas práticas

| Prática | O que a página diz |
|---|---|
| Assets | sempre pela API do Unreal (`unreal.EditorAssetLibrary`, `unreal.AssetTools`), nunca por `os.rename` ou `shutil.move` no disco, porque o projeto guarda referências internas que se quebram |
| Propriedades simples | as marcadas `BlueprintReadOnly` ou `BlueprintReadWrite` se leem e se mudam como atributo do objeto |
| Propriedades de editor | as marcadas `ViewAnywhere` ou `EditAnywhere` se leem e se mudam por `get_editor_property()` e `set_editor_property()`; a lista de cada classe está na referência da API |
| Por que `set_editor_property()` | ele dispara o código de antes e depois da edição, como o painel Details faz; mudar o atributo direto não dispara, e o resultado pode ser outro |
| Exemplo | o `play_on_open` de `unreal.MediaPlayer` |
| Tipos do Unreal | usar os do Unreal (`unreal.Vector` para coordenadas), otimizados para o motor |
| Mensagens | `unreal.log()`, `unreal.log_warning()` e `unreal.log_error()`, no Output Log; o `print()` passa pelo `unreal.log()` |
| Desfazer | `unreal.ScopedEditorTransaction("<nome>")` junta várias operações numa entrada só do histórico; só vale para o que a interface também desfaz (importar modelo, por exemplo, não) |
| Operação lenta | o Editor fica bloqueado enquanto o script roda; `unreal.ScopedSlowTask` mostra o progresso e o botão de cancelar (`make_dialog`, `should_cancel`, `enter_progress_frame`) |

## Python com agentes de IA

| Item | Fato |
|---|---|
| Por onde | o Unreal MCP, o servidor MCP do Editor |
| O que o agente faz | roda scripts Python do Editor |
| O que se escreve | ferramentas (toolsets) e skills de agente em Python que ampliam o que o agente faz no Editor |

## O que a fonte recomenda

Para automatizar o Editor de fora, a linha de comando: o Editor inteiro quando o script precisa do nível carregado, o commandlet quando a pressa conta, com o nível carregado à mão no começo do script. Dentro do script, mexer em asset e em propriedade só pela API (`set_editor_property()`, `EditorAssetLibrary`), juntar as mudanças numa transação e mostrar o progresso nas operações longas; e, para quem atualiza da 5.8, conferir os scripts que comparam tipos de Blueprint.

## Citações

- "the Python environment is only available in Unreal Editor, not when your project is running in Unreal Engine in any mode"
- "In both approaches, Unreal Editor shuts down immediately after running your Python script."
- "This approach runs quickly and can run your scripts in headless mode, without opening the Unreal Editor UI."

## Lacuna

A página não diz se o commandlet ou o `-ExecutePythonScript` rodam sem placa de vídeo, nem se dá para disparar um render da Movie Render Queue de dentro deles; não trata do Sequencer. Não diz quanto tempo o Editor leva para abrir na opção 1, nem como o script recebe os argumentos que vêm depois do nome dele. As imagens (o console em modo Python, os nós, o Output Log) não foram vistas.
