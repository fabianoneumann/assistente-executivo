"""Testa o r2.py sem rede e sem chave: os buckets que vêm do ambiente, as mensagens do que falta e o aviso da URL.

  python -X utf8 .claude/skills/r2-storage/scripts/teste_r2.py

Roda cada caso num subprocesso com um ambiente limpo (sem nenhuma variável R2_* nem CLOUDFLARE_*) e numa pasta
temporária sem `.env`, para o `.env` da raiz não entrar na conta. Sai com erro no primeiro caso que falhar.
"""
import os
import subprocess
import sys
import tempfile
from pathlib import Path

R2 = Path(__file__).resolve().with_name("r2.py")


def ambiente_limpo(**extra):
    env = {k: v for k, v in os.environ.items()
           if not k.startswith(("R2_", "CLOUDFLARE_")) and k != "CLAUDE_PROJECT_DIR"}
    env.update(extra)
    env["PYTHONUTF8"] = "1"
    return env


def roda(args, pasta, **extra):
    return subprocess.run([sys.executable, str(R2), *args], capture_output=True, text=True, encoding="utf-8",
                          cwd=pasta, env=ambiente_limpo(**extra))


def importa(codigo, pasta, **extra):
    prog = f"import sys; sys.path.insert(0, {str(R2.parent)!r}); import r2\n{codigo}"
    return subprocess.run([sys.executable, "-c", prog], capture_output=True, text=True, encoding="utf-8",
                          cwd=pasta, env=ambiente_limpo(**extra))


def caso(nome, cond, extra=""):
    print(("ok    " if cond else "FALHA ") + nome)
    if not cond:
        print("   ", extra)
    assert cond, nome


with tempfile.TemporaryDirectory() as tmp:
    (Path(tmp) / ".git").mkdir()  # a busca do `.env` para aqui, sem subir à pasta de quem roda
    for cmd in (["smoke"], ["ls", "conteudo"], ["put", "conteudo", "x.png"], ["get", "conteudo", "k"],
                ["rm", "conteudo", "k"], ["presign", "conteudo", "k"]):
        r = roda(cmd, tmp)
        caso(f"1. sem chave, `{cmd[0]}` sai com 1, a mensagem e sem traceback",
             r.returncode == 1 and "R2_ACCOUNT_ID" in r.stderr and "Onde se pega" in r.stderr
             and ".env.example" in r.stderr and "Traceback" not in r.stderr, r.stderr[-500:])
    r = roda(["url", "conteudo", "a/b.jpg"], tmp)
    caso("2. `url` sem bucket nem base: sai com 1 e diz as duas variáveis",
         r.returncode == 1 and "R2_BUCKET_CONTEUDO" in r.stderr and "R2_PUBLIC_BASE_CONTEUDO" in r.stderr
         and "Traceback" not in r.stderr, r.stderr[-500:])
    r = roda(["url", "conteudo", "a/b.jpg"], tmp, R2_BUCKET_CONTEUDO="meu-bucket")
    caso("3. `url` com o bucket e sem a base: sai com 1 e diz a base",
         r.returncode == 1 and "R2_PUBLIC_BASE_CONTEUDO" in r.stderr and "R2_BUCKET_CONTEUDO" not in r.stderr, r.stderr)
    r = roda(["url", "conteudo", "a/b.jpg"], tmp, R2_BUCKET_CONTEUDO="meu-bucket",
             R2_PUBLIC_BASE_CONTEUDO="https://cdn.exemplo.com/")
    caso("4. `url` configurada: a URL, código 0", r.returncode == 0 and r.stdout.strip() == "https://cdn.exemplo.com/a/b.jpg",
         (r.returncode, r.stdout, r.stderr))
    r = roda(["public", "conteudo"], tmp, R2_BUCKET_CONTEUDO="meu-bucket")
    caso("5. `public` sem o token: sai com 1 e diz CLOUDFLARE_API_TOKEN e R2_ACCOUNT_ID",
         r.returncode == 1 and "CLOUDFLARE_API_TOKEN" in r.stderr and "R2_ACCOUNT_ID" in r.stderr, r.stderr)
    r = importa("print(sorted(r2.buckets().items())); print(r2.bucket('meu-bucket-2')); print(r2.alias_of('meu-bucket-2'))",
                tmp, R2_BUCKET_CONTEUDO="meu-bucket", R2_BUCKET_ARQUIVO="meu-bucket-2", R2_BUCKET_VAZIO="COLE_AQUI")
    caso("6. os buckets vêm de todo R2_BUCKET_<APELIDO>, e o marcador do .env.example não conta",
         r.stdout.splitlines() == ["[('arquivo', 'meu-bucket-2'), ('conteudo', 'meu-bucket')]", "meu-bucket-2", "arquivo"],
         (r.stdout, r.stderr))
    r = importa("print(r2.public_url('conteudo', 'k')); print(r2.public_url('conteudo', 'k2'))", tmp,
                R2_BUCKET_CONTEUDO="meu-bucket")
    caso("7. public_url sem a base: None, com o aviso explícito uma vez só, no stderr",
         r.returncode == 0 and r.stdout.split() == ["None", "None"] and r.stderr.count("[AVISO]") == 1
         and "R2_PUBLIC_BASE_CONTEUDO" in r.stderr, (r.stdout, r.stderr))
    r = importa("print(r2.faltas('conteudo', com_url=True))", tmp)
    caso("8. faltas(): as três credenciais, o bucket e a base", r.returncode == 0 and all(
        v in r.stdout for v in ("R2_ACCOUNT_ID", "R2_ACCESS_KEY_ID", "R2_SECRET_ACCESS_KEY", "R2_BUCKET_CONTEUDO",
                                "R2_PUBLIC_BASE_CONTEUDO")), r.stdout)
    r = importa("r2.bucket('outro')", tmp, R2_BUCKET_CONTEUDO="meu-bucket")
    caso("9. bucket desconhecido: sai com 1, diz a variável e os apelidos que existem",
         r.returncode == 1 and "R2_BUCKET_OUTRO" in r.stderr and "`conteudo`" in r.stderr and "Traceback" not in r.stderr,
         r.stderr)
    r = importa("r2.exigir_public_url('conteudo', 'k')", tmp, R2_BUCKET_CONTEUDO="meu-bucket")
    caso("10. exigir_public_url sem a base: sai com 1 e a mensagem", r.returncode == 1 and "R2_PUBLIC_BASE_CONTEUDO" in r.stderr,
         r.stderr)
    (Path(tmp) / ".env").write_text("R2_BUCKET_CONTEUDO=do-env\nR2_PUBLIC_BASE_CONTEUDO=https://cdn.do-env.exemplo\n",
                                    encoding="utf-8")
    r = roda(["url", "conteudo", "k"], tmp)
    caso("11. o `.env` da pasta de trabalho vale", r.returncode == 0 and r.stdout.strip() == "https://cdn.do-env.exemplo/k",
         (r.stdout, r.stderr))
print("TODOS OK")
