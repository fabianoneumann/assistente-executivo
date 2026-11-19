import { strict as assert } from 'node:assert'
import { spawn } from 'node:child_process'
import { createServer } from 'node:http'
import type { AddressInfo } from 'node:net'
import { test } from 'node:test'

import { responder } from '../src/servidor.ts'

test('o /health responde ok', async () => {
  const servidor = createServer(responder).listen(0)
  try {
    const { port } = servidor.address() as AddressInfo
    const resposta = await fetch(`http://127.0.0.1:${port}/health`)
    assert.equal(resposta.status, 200)
    assert.deepEqual(await resposta.json(), { status: 'ok' })
  } finally {
    servidor.close()
  }
})

test('smoke: o servidor sobe de verdade e responde', async () => {
  const porta = 3900 + Math.floor(Math.random() * 90)
  const filho = spawn(process.execPath, ['src/servidor.ts'], { env: { ...process.env, PORT: String(porta) } })
  try {
    let resposta: Response | undefined
    for (let i = 0; i < 50 && !resposta; i++) {
      resposta = await fetch(`http://127.0.0.1:${porta}/health`).catch(async () => {
        await new Promise((r) => setTimeout(r, 200))
        return undefined
      })
    }
    assert.equal(resposta?.status, 200)
  } finally {
    filho.kill()
  }
})
