// O ponto de entrada do serviço. O primeiro endpoint é o de saúde, que o smoke do CI chama.
import { createServer, type IncomingMessage, type ServerResponse } from 'node:http'

export function responder(req: IncomingMessage, res: ServerResponse): void {
  if (req.url === '/health') {
    res.writeHead(200, { 'content-type': 'application/json' })
    res.end(JSON.stringify({ status: 'ok' }))
    return
  }
  res.writeHead(404).end()
}

if (import.meta.main) {
  const porta = Number(process.env.PORT ?? 3000)
  createServer(responder).listen(porta)
}
