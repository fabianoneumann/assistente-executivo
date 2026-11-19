# Assinatura do Claude em ferramentas de terceiros: o que sai do plano

A pergunta que volta a cada ferramenta nova que usa Claude por baixo (Hermes Agent, OpenClaw e similares): dá para usar a cota do Pro/Max em vez de pagar API? As regras mudam: reconferir a página de autenticação antes de decidir.

Fontes: *Claude Code — Legal and compliance (autenticação e uso de credenciais)*, de Anthropic (documentação oficial do Claude Code) (https://code.claude.com/docs/en/legal-and-compliance) (regra da Anthropic) e *Hermes Agent — LLM and Model Providers (trechos sobre assinatura e Anthropic)*, de Documentação oficial do Hermes Agent (Nous Research) (https://hermes-agent.nousresearch.com/docs/integrations/providers) (como o Hermes cobra). Relaciona-se com [[claude-code-sem-supervisao]], onde o mesmo corte aparece no Agent SDK.

## A regra

A página de legal e compliance do Claude Code separa dois usos:

- **Login com a conta Claude (OAuth)** é "intended exclusively" para assinantes e para o "ordinary use of Claude Code and other native Anthropic applications". Os limites anunciados do Pro e do Max supõem uso "ordinary, individual".
- **Quem constrói produto ou serviço**, inclusive com o Agent SDK, usa chave de API. A Anthropic "does not permit third-party developers to offer Claude.ai login into their own applications, or to route requests through Free, Pro, or Max plan credentials", nem "collect, store, or intermediate Claude.ai credentials or session tokens".
- Fica ressalvado o usuário que entra com a própria assinatura no **binário do Claude Code sem modificação**, inclusive quando uma plataforma hospeda o Claude Code.
- A Anthropic pode aplicar a regra "without prior notice".

## O teste prático: quem chama o modelo

| Como a ferramenta chega ao Claude | O que paga | Situação |
|---|---|---|
| Roda **dentro** do Claude Code (servidor MCP, plugin, channel, skill, `claude -p`) | a cota do plano | uso previsto pela regra |
| Chama a API com o seu login do Claude | créditos extras, quando a Anthropic aceita | é o que a regra restringe |
| Chama a API com chave do Console | por token, na chave | permitido |
| Passa por gateway próprio (Nous Portal, OpenRouter) | a assinatura ou os créditos do gateway | fora da conta Anthropic |

Por isso um servidor MCP de mensageria ou um channel do Claude Code usam o plano, e o Hermes não.

## O caso Hermes

A documentação do Hermes é franca sobre o resultado:

- **Max:** o login funciona só com **créditos de uso extra comprados**, e "all Hermes usage bills as 'extra usage' even while your included Max allowance sits untouched".
- **Pro:** o caminho não existe; a alternativa é `ANTHROPIC_API_KEY`, por token.
- O Hermes **lê o armazenamento de credenciais do Claude Code** ("borrowed Claude Code login", "reads Claude Code credential files automatically"). Não cabe a esta página julgar se isso cai no "collect, store, or intermediate" da regra; fica anotado como ponto de atrito.
- O caminho que o Hermes recomenda é o Nous Portal, que cobra na assinatura da Nous.

No repositório do Claude Code, a issue 40014 relata o login do plano drenando créditos extras em vez da cota, e a 48320, que propunha um provedor chamando `claude -p` para usar a cota, foi fechada como duplicada, sem implementação.

## Promessas a desconfiar

O site hermesagents.net, que se declara feito por fã e sem vínculo com a Nous Research, descreve um `hermes proxy` que exporia a sessão do Claude Pro como endpoint compatível com OpenAI. O comando não aparece na documentação oficial, e o que ele descreve é exatamente o roteamento que a regra proíbe. Promessa de "usar Claude pelo plano em qualquer ferramenta" pede esse teste: se a chamada não sai do binário do Claude Code, ela não é cota do plano.
