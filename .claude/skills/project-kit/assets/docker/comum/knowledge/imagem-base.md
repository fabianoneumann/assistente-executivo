# A imagem e a imagem base

Como a imagem do serviço se constrói, se publica e se vigia. Vale porque este projeto publica imagem. **Ler quando:** for mexer no `Dockerfile`, cortar uma versão, ou quando a vigilância abrir ou comentar uma issue `[imagem-base]`.

## Como a imagem nasce

- **O `Dockerfile` da raiz** constrói a imagem que se instala. A base é a tag flutuante da linha do runtime, e todo build é com `--pull`: sem ele, o Docker usa a base do cache, e a imagem sai com um runtime de semanas antes.
- **O runtime não leva o gerenciador de pacote** (o `npm` e companhia, ou o `pip`): ele só executa o serviço, e o que ninguém executa ali só soma falha na varredura. A conferência no fim do `Dockerfile` derruba o build se ele voltar.
- **A procedência:** o build recebe a versão e o commit (`VERSAO` e `COMMIT`), e o `/health` os devolve. É assim que uma instalação diz o que roda.
- **Sem root:** o serviço roda com um usuário sem privilégio.
- **O CI constrói a imagem em todo PR** (o job `imagem` do `ci.yml`), sobe o contêiner e confere o `/health`: a verificação que mora no build precisa do build no CI. Ele não publica nada.

## Como se publica

O `publicar-imagem.yml` roda no push da tag de versão (`versao-e-dependencias.md`): confere que a tag é anotada e está no `{{BASE}}`, e publica `ghcr.io/<dono>/<repositório>:vX.Y.Z`. **A imagem publicada é imutável:** a que já existe não se reconstrói. O pacote nasce privado e herda o acesso do repositório. Voltar à versão anterior é baixar a imagem dela, e não reconstruir um commit antigo.

## Como se vigia

O Dependabot não vigia esta camada: no contêiner, ele só propõe versão, sem alerta de segurança. O `vigiar-imagem.yml` roda toda segunda (e à mão), contra a imagem do Release "Latest", com duas perguntas:

1. **O runtime está atrás de uma versão nova da mesma linha?** No Node, pela lista oficial de versões (`nodejs.org/dist/index.json`), que marca as de segurança; no Python, pelas versões publicadas da linha no `python.org`, porque na linha só de segurança toda versão nova é de segurança. A varredura não é a fonte disso: o runtime da imagem oficial é um binário, e não um pacote do sistema.
2. **O Trivy acha falha alta ou crítica com correção disponível?** O que não tem correção não tem ação, e fica para quando tiver.

**Quem é avisado:** cada imagem com achado tem uma issue `[imagem-base] <nome>`, atribuída ao responsável quando o workflow o tem. A rodada seguinte só comenta quando algo mudou (achado novo, achado que saiu, imagem limpa); o estado fica em comentários HTML no histórico da issue. Fechar é da triagem; a issue fechada só reabre com achado novo. A falha da própria rodada (rede, login, download) deixa o job vermelho e não abre issue.

**O ruído permanente se tira da varredura, na lista `IGNORAR` do `vigiar_imagem.py`, com o motivo escrito ao lado:** o pacote que só roda na partida, sem entrada de rede, ou a ferramenta de build que a imagem leva e não executa. Sem isso, a issue nunca fica limpa e ninguém mais a lê.

## Quando vira versão de correção

A triagem é um comentário na issue, com o veredito. A pergunta é a mesma das dependências: chega a quem, com que severidade, e há instalação nesta versão? Falha alta ou crítica no serviço exposto, ou versão de segurança do runtime numa API que o projeto usa, com instalação na versão → versão de correção. **Não há mudança de código a fazer:** a versão nova constrói do zero, com a base do dia; é cortar a tag. **Antes de cortar, conferir que a imagem oficial já traz a correção** (`docker run --rm --pull always <a base> --version`): a lista do Node e a do Python publicam a versão antes de a imagem oficial ser reconstruída, e a versão cortada nesse intervalo sai com o runtime velho. Depois, conferir o `/health` da instalação e disparar o vigia à mão, que comenta "limpa".

## O que a vigilância não vê

- **Só a "Latest".** A instalação que ficou numa versão anterior deixa de ser vigiada; o achado da "Latest" vale como indício para ela, que é mais velha.
- **A imagem de terceiros** (o banco, uma ferramenta num compose), se o projeto tiver: entra no vigia quando entrar no projeto, com a regra de como cada uma se corrige.
- **A falha corrigida entre duas rodadas semanais** passa sem aviso até a rodada seguinte.
