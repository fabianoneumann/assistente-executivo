// O ponto de entrada do serviço. O primeiro endpoint é o de saúde, que o smoke do CI chama.
import { createServer, type IncomingMessage, type ServerResponse } from 'node:http'

export function responder(req: IncomingMessage, res: ServerResponse): void {
  if (req.url === '/health') {
    // A instalação declara o que roda: a versão e o commit chegam do build (VERSAO e COMMIT). Vazios, num build à mão
    // ou fora da imagem, saem null, e ninguém mente sobre a procedência.
    res.writeHead(200, { 'content-type': 'application/json' })
    res.end(
      JSON.stringify({
        status: 'ok',
        versao: process.env.VERSAO || null,
        commit: process.env.COMMIT || null,
      }),
    )
    return
  }
  res.writeHead(404).end()
}

if (import.meta.main) {
  const porta = Number(process.env.PORT ?? 3000)
  createServer(responder).listen(porta)
}
