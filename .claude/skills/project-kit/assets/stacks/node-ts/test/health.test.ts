import { strict as assert } from 'node:assert'
import { spawn } from 'node:child_process'
import { createServer } from 'node:http'
import type { AddressInfo } from 'node:net'
import { test } from 'node:test'

import { responder } from '../src/servidor.ts'

async function health(): Promise<{ status: number; corpo: unknown }> {
  const servidor = createServer(responder).listen(0)
  try {
    const { port } = servidor.address() as AddressInfo
    const resposta = await fetch(`http://127.0.0.1:${port}/health`)
    return { status: resposta.status, corpo: await resposta.json() }
  } finally {
    servidor.close()
  }
}

test('o /health responde ok, sem procedência fora da imagem', async () => {
  const antes = { VERSAO: process.env.VERSAO, COMMIT: process.env.COMMIT }
  delete process.env.VERSAO
  delete process.env.COMMIT
  try {
    const { status, corpo } = await health()
    assert.equal(status, 200)
    assert.deepEqual(corpo, { status: 'ok', versao: null, commit: null })
  } finally {
    Object.assign(
      process.env,
      Object.fromEntries(Object.entries(antes).filter(([, v]) => v !== undefined)),
    )
  }
})

test('o /health declara a versão e o commit', async () => {
  process.env.VERSAO = 'v1.2.3'
  process.env.COMMIT = 'abc1234'
  try {
    assert.deepEqual((await health()).corpo, { status: 'ok', versao: 'v1.2.3', commit: 'abc1234' })
  } finally {
    delete process.env.VERSAO
    delete process.env.COMMIT
  }
})

test('smoke: o servidor sobe de verdade e responde', async () => {
  const porta = 3900 + Math.floor(Math.random() * 90)
  const filho = spawn(process.execPath, ['src/servidor.ts'], {
    env: { ...process.env, PORT: String(porta) },
  })
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
