# A vida pessoal e os mapas

O assistente cobre também a vida pessoal (finanças, saúde e os mapas de autoconhecimento e de direção), no mesmo repositório do trabalho. Este arquivo diz como essa parte se organiza e por quê. As regras de cada pasta estão nos READMEs de `finance/`, `health/` e `maps/`.

## 2026-11-18 — Um modelo só, com as pastas e o método, sem os registros

**Decisão:** o modelo traz `finance/`, `health/` e `maps/` desde o clone, cada uma com o README do método e o roteiro do que preencher, mas **nenhum arquivo de registro**: o `overview.md` das finanças, o plano de treino, o diário, o exame e o retrato de cada mapa nascem no primeiro registro, criados pelo assistente quando você relatar a primeira informação que pertence a eles.

**Motivo:** a pasta com README e sem conteúdo é intenção gravada como estrutura. O arquivo em branco esperando ser preenchido fica vazio por meses e passa a parecer obrigação; o arquivo que nasce no primeiro registro já nasce com dado. O README fica, porque é ele que diz ao assistente onde cada coisa vai quando chegar.

## As três famílias de framework

- **Diagnóstico:** Roda da Vida, Big Five, SWOT, Ikigai. Retrato datado, refeito de tempos em tempos; o valor está na série.
- **Direção:** Vision Board, Matriz EREC, OKR. A intenção, com o destino dito e, no OKR, com um alvo que se mede.
- **Execução** (Eisenhower, GTD, Pomodoro): **não entram nos mapas.** São ferramentas de operar o dia, e não de orientar; o papel delas é das tarefas do dia a dia, fora dos mapas.

**OKR, o conceito sim, a forma engessada não:** o resultado-chave só com alvo e fonte de medição; o objetivo em prosa. Forma que dá trabalho demais faz parar de usar.

## Os cuidados de privacidade

- **O repositório privado vem antes do primeiro registro pessoal.** No "Use this template" se escolhe Private; quem criou público muda em Settings antes de escrever. O histórico do git guarda o que foi commitado mesmo depois de apagado. O `scripts/confere_dados.py`, rodado antes do push e com o `gh` logado, para quando acha registro pessoal num repositório com remoto público, e diz como mudar; sem o `gh` ou sem o login dele, sai com o código 3 ("não conferiu") e diz o que falta; com remoto fora do GitHub, só avisa. Antes do primeiro registro, a conferência é à mão.
- **Espaço sensível:** o psicológico, a saúde e os mapas. O assistente não diagnostica, não estima traço de personalidade pela conversa e incentiva o apoio profissional.
- **O quadro é local:** o `maps/board/` abre no navegador e não se publica em link, porque junta as áreas mais íntimas numa página só.
- **Terceiro pelo papel:** o familiar, o médico, quem paga ou recebe entra como "a mãe", "a médica", "o sócio", e não pelo nome.
- **O documento fora do git:** o laudo, o extrato e a fatura, se guardados, vão para `originals/`, que o `.gitignore` tira.
- **Cada item diz de quem é:** a leitura do assistente fica "a testar" ou "proposta" até você assumir.

## Os frameworks e as fontes

Cada guia de `maps/guides/` diz o que o mapa é, quando usar e onde preencher, e atribui a origem:

- **Roda da Vida:** atribuída a Paul J. Meyer (Success Motivation Institute, anos 1960). "Wheel of Life" aparece como marca de terceiro; o modelo usa o nome descritivo em português, sem o ®, e o desenho é próprio.
- **Big Five:** só pelo **IPIP-NEO-120** (John A. Johnson, itens do International Personality Item Pool, de domínio público). Inventários de distribuição controlada ou comerciais não entram, porque o modelo é público.
- **Ikigai:** o diagrama de quatro círculos é de Marc Winn (2014), sobre um diagrama de Andrés Zuzunaga; o modelo desenha o seu, do zero, sem copiar a imagem de ninguém.
- **Matriz EREC:** atribuída ao livro *A Estratégia do Oceano Azul* (Kim e Mauborgne), sem usar o nome do livro como nome do mapa, porque "Blue Ocean Strategy" aparece como marca dos autores no site deles.
- **SWOT, Vision Board e OKR:** conceitos difundidos, com a origem dita no guia.

**O guia é curto de propósito:** o que o mapa pergunta e onde ele mora. O exercício guiado (o passo a passo, as perguntas de cada etapa, a leitura do resultado) do Ikigai, da SWOT e da Matriz EREC é do curso que acompanha este modelo.

**A ordem segue a dependência:** o Vision Board primeiro, porque é o destino contra o qual os outros medem; o Ikigai como síntese dos anteriores; a EREC a partir do Ikigai. O detalhe está em `maps/README.md`.

**Revê se:** alguém usar o modelo só para o trabalho e as pastas pessoais atrapalharem (a saída é um segundo repositório a partir do mesmo modelo), ou se um mapa novo pedir uma família que não está aqui.
