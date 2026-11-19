#!/usr/bin/env python3
"""CLI mínimo para os buckets R2 (Cloudflare) do projeto, via API S3.

Credenciais (do ambiente ou do `.env` da raiz, lidas pelo `ambiente.py` desta pasta):
  R2_ACCOUNT_ID, R2_ACCESS_KEY_ID, R2_SECRET_ACCESS_KEY
Os buckets, por apelido (nenhum nome de bucket fica no código):
  R2_BUCKET_CONTEUDO, R2_BUCKET_CURSO, R2_BUCKET_CAMPANHAS, ou qualquer R2_BUCKET_<APELIDO>
A URL pública de cada bucket (r2.dev ou domínio próprio), quando ele é público:
  R2_PUBLIC_BASE_<APELIDO>, como R2_PUBLIC_BASE_CONTEUDO

Uso:
  python r2.py smoke                                   # valida credenciais e os buckets configurados
  python r2.py ls conteudo [--prefix carousels/]       # lista objetos
  python r2.py put conteudo ./slide-01.png [chave]     # sobe arquivo (chave = nome do arquivo se omitida)
  python r2.py put conteudo ./images/ carousels/x/     # sobe pasta inteira sob um prefixo
  python r2.py get conteudo carousels/x/slide-01.png [destino]
  python r2.py rm conteudo carousels/x/slide-01.png
  python r2.py url conteudo carousels/x/slide-01.png   # URL pública; sem R2_PUBLIC_BASE_<APELIDO>, sai com 1
  python r2.py presign conteudo chave [--expires 3600]  # URL assinada temporária (bucket privado)
  python r2.py public conteudo [--enable|--disable]     # status/ativação do domínio público r2.dev (REST)

O comando "public" usa a API REST da Cloudflare, não a S3: precisa de CLOUDFLARE_API_TOKEN
(o "Token value" mostrado ao criar o token R2 com permissão Admin Read & Write).

Quem importa este módulo (a slides-export, por exemplo) usa:
  faltas(apelido, com_url=True)    -> lista das mensagens do que falta (vazia = pode subir)
  public_url(bucket, chave)        -> a URL, ou None com o aviso explícito no stderr (para testar sem sair)
  exigir_public_url(bucket, chave) -> a URL, ou sai com a mensagem completa
Sem a configuração, a saída é sempre a mensagem (a variável, para quê, onde se pega, como se põe), nunca traceback,
e nenhum valor de chave se imprime.
"""
from __future__ import annotations

import argparse
import json
import mimetypes
import os
import sys
import urllib.error
import urllib.request
import uuid
from urllib.parse import quote
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ambiente  # noqa: E402

for _fluxo in (sys.stdout, sys.stderr):
    try:
        _fluxo.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

# variável: (para que serve, onde se pega). O mesmo texto do `CHAVES` de `scripts/confere_ambiente.py` da raiz,
# repetido aqui para a skill funcionar também instalada como plugin noutro projeto.
CHAVES = {
    "R2_ACCOUNT_ID": ("a conta da Cloudflare que tem o R2",
                      "https://dash.cloudflare.com > R2 > Overview (o Account ID fica na lateral)"),
    "R2_ACCESS_KEY_ID": ("o par de acesso S3 do R2",
                         "https://dash.cloudflare.com > R2 > Manage API tokens > Create API token (o Access Key ID)"),
    "R2_SECRET_ACCESS_KEY": ("o segredo do par de acesso S3 do R2",
                             "o mesmo token do R2 (o Secret Access Key aparece uma vez só, ao criar)"),
    "CLOUDFLARE_API_TOKEN": ("só o comando `public` do r2.py (ligar o domínio público pela API REST)",
                             "o \"Token value\" mostrado ao criar o token do R2 com Admin Read & Write"),
}
CREDENCIAIS = ("R2_ACCOUNT_ID", "R2_ACCESS_KEY_ID", "R2_SECRET_ACCESS_KEY")
PREFIXO_BUCKET, PREFIXO_BASE = "R2_BUCKET_", "R2_PUBLIC_BASE_"

COMO_POR = ("Como pôr: copie o `.env.example` para `.env` na raiz do projeto (o `.env` nunca vai ao git) e preencha "
            "a linha da variável; ou ponha no bloco \"env\" do seu `.claude/settings.local.json`. Depois, reinicie a "
            "sessão do Claude Code. Para ver o quadro inteiro: python -X utf8 scripts/confere_ambiente.py --skill r2-storage")


def die(msg: str, code: int = 2) -> None:
    print(f"[ERRO] {msg}", file=sys.stderr)
    sys.exit(code)


def parar(linhas: list[str]) -> None:
    """Sai com 1 e a mensagem completa do que falta configurar."""
    print("[PARE] a skill r2-storage não roda sem a configuração abaixo. Falta:", file=sys.stderr)
    for linha in linhas:
        print(f"  - {linha}", file=sys.stderr)
    print(COMO_POR, file=sys.stderr)
    sys.exit(1)


def falta_chave(nome: str) -> str:
    uso, onde = CHAVES[nome]
    return f"variável {nome} ({uso}). Onde se pega: {onde}."


def falta_bucket(apelido: str) -> str:
    return (f"variável {PREFIXO_BUCKET}{apelido.upper()} (o nome do bucket de apelido `{apelido.lower()}`). Onde se "
            "pega: o nome do bucket que você criou em https://dash.cloudflare.com > R2 > Create bucket.")


def falta_base(apelido: str) -> str:
    return (f"variável {PREFIXO_BASE}{apelido.upper()} (a URL pública do bucket `{apelido}`, para montar os links). "
            "Onde se pega: https://dash.cloudflare.com > R2 > o bucket > Settings > Public access (o endereço r2.dev "
            f"ou o domínio próprio), ou pelo comando `r2.py public {apelido} --enable`, que imprime a linha pronta.")


def buckets() -> dict[str, str]:
    """{apelido: nome do bucket}, lido de toda variável R2_BUCKET_<APELIDO> do ambiente e do `.env`."""
    ambiente.carregar_env()
    out = {}
    for k in sorted(os.environ):
        if k.upper().startswith(PREFIXO_BUCKET) and len(k) > len(PREFIXO_BUCKET):
            v = ambiente.valor(k)
            if v:
                out[k[len(PREFIXO_BUCKET):].lower()] = v
    return out


def credenciais_faltando() -> list[str]:
    return [falta_chave(k) for k in CREDENCIAIS if not ambiente.valor(k)]


def faltas(apelido: str, com_url: bool = False) -> list[str]:
    """O que falta para subir ao bucket `apelido` (e montar a URL pública, com `com_url`): lista de mensagens."""
    linhas = credenciais_faltando()
    bs = buckets()
    if apelido.lower() not in bs and apelido not in bs.values():
        linhas.append(falta_bucket(apelido))
    if com_url and not public_base(apelido):
        linhas.append(falta_base(alias_of(apelido)))
    return linhas


def client():
    falta = credenciais_faltando()
    if falta:
        parar(falta)
    try:
        import boto3
        from botocore.config import Config
    except ImportError:
        die("falta o pacote Python boto3. Como instalar, da raiz do projeto: "
            "python -m pip install -r .claude/skills/r2-storage/requirements.txt", 1)
    return boto3.client(
        service_name="s3",
        endpoint_url=f"https://{ambiente.valor('R2_ACCOUNT_ID')}.r2.cloudflarestorage.com",
        aws_access_key_id=ambiente.valor("R2_ACCESS_KEY_ID"),
        aws_secret_access_key=ambiente.valor("R2_SECRET_ACCESS_KEY"),
        region_name="auto",
        config=Config(signature_version="s3v4", retries={"max_attempts": 3}),
    )


def bucket(name: str) -> str:
    """O nome do bucket pelo apelido (`conteudo`) ou pelo próprio nome, desde que configurado em R2_BUCKET_<APELIDO>."""
    bs = buckets()
    if name.lower() in bs:
        return bs[name.lower()]
    if name in bs.values():
        return name
    conhecidos = ", ".join(f"`{k}`" for k in bs) or "nenhum ainda"
    parar([falta_bucket(name) + f" Apelidos configurados: {conhecidos}."])


def alias_of(name: str) -> str:
    """O apelido de um bucket (o próprio apelido, ou o apelido cujo R2_BUCKET_ tem esse nome)."""
    bs = buckets()
    if name.lower() in bs:
        return name.lower()
    return next((k for k, v in bs.items() if v == name), name.lower())


def public_base(name: str) -> str:
    """A base pública do bucket (R2_PUBLIC_BASE_<APELIDO>), ou "" quando falta."""
    return ambiente.valor(f"{PREFIXO_BASE}{alias_of(name).upper()}")


_AVISADOS: set[str] = set()


def public_url(name: str, key: str) -> str | None:
    """A URL pública da chave, ou None. O None nunca é silencioso: avisa no stderr, uma vez por bucket, qual variável
    falta e onde se pega. Para quem precisa testar sem sair; quem precisa da URL usa exigir_public_url."""
    base = public_base(name)
    if base:
        return f"{base.rstrip('/')}/{quote(key, safe='/')}"
    apelido = alias_of(name)
    if apelido not in _AVISADOS:
        _AVISADOS.add(apelido)
        print(f"[AVISO] sem URL pública para o bucket `{apelido}`: falta a {falta_base(apelido)} {COMO_POR}",
              file=sys.stderr)
    return None


def exigir_public_url(name: str, key: str) -> str:
    """A URL pública da chave, ou sai com 1 e a mensagem completa."""
    base = public_base(name)
    if not base:
        parar([falta_base(alias_of(name)) + " Bucket privado? Use `presign`."])
    return f"{base.rstrip('/')}/{quote(key, safe='/')}"


def cmd_ls(s3, a):
    b = bucket(a.bucket)
    kw = {"Bucket": b}
    if a.prefix:
        kw["Prefix"] = a.prefix
    total = 0
    for page in s3.get_paginator("list_objects_v2").paginate(**kw):
        for o in page.get("Contents", []):
            total += 1
            print(f"{o['Size']:>10}  {o['LastModified']:%Y-%m-%d %H:%M}  {o['Key']}")
    print(f"-- {total} objeto(s) em {b}" + (f" (prefixo {a.prefix})" if a.prefix else ""))


def _put_one(s3, b: str, local: Path, key: str) -> None:
    ctype = mimetypes.guess_type(local.name)[0] or "application/octet-stream"
    s3.upload_file(str(local), b, key, ExtraArgs={"ContentType": ctype})
    print(f"[OK] {local} -> s3://{b}/{key} ({ctype})")
    url = public_url(b, key)  # sem a base pública, o aviso sai uma vez, no stderr
    if url:
        print(f"     {url}")


def cmd_put(s3, a):
    b = bucket(a.bucket)
    src = Path(a.local)
    if not src.exists():
        die(f"arquivo/pasta não existe: {src}")
    if src.is_dir():
        prefix = (a.key or src.resolve().name).strip("/")
        if not prefix:
            die("diga o prefixo no bucket para subir esta pasta: python r2.py put <bucket> <pasta> <prefixo>/", 1)
        files = sorted(p for p in src.rglob("*") if p.is_file())
        if not files:
            die(f"pasta vazia: {src}")
        for p in files:
            _put_one(s3, b, p, f"{prefix}/{p.relative_to(src).as_posix()}")
        print(f"-- {len(files)} arquivo(s) sob {prefix}/")
    else:
        _put_one(s3, b, src, a.key or src.name)


def cmd_get(s3, a):
    b = bucket(a.bucket)
    dest = Path(a.local) if a.local else Path(Path(a.key).name)
    dest.parent.mkdir(parents=True, exist_ok=True)
    s3.download_file(b, a.key, str(dest))
    print(f"[OK] s3://{b}/{a.key} -> {dest}")


def cmd_rm(s3, a):
    b = bucket(a.bucket)
    s3.delete_object(Bucket=b, Key=a.key)
    print(f"[OK] removido s3://{b}/{a.key}")


def cmd_url(s3, a):
    # a URL pública não pede o par de acesso, só o bucket e a base dele; o que faltar dos dois sai de uma vez
    bs = buckets()
    falta = [] if (a.bucket.lower() in bs or a.bucket in bs.values()) else [falta_bucket(a.bucket)]
    if not public_base(a.bucket):
        falta.append(falta_base(alias_of(a.bucket)) + " Bucket privado? Use `presign`.")
    if falta:
        parar(falta)
    print(exigir_public_url(bucket(a.bucket), a.key))


def cmd_presign(s3, a):
    print(s3.generate_presigned_url("get_object", Params={"Bucket": bucket(a.bucket), "Key": a.key},
                                    ExpiresIn=a.expires))


def cf_api(method: str, path: str, corpo: dict | None = None):
    token = ambiente.valor("CLOUDFLARE_API_TOKEN")
    falta = [] if ambiente.valor("R2_ACCOUNT_ID") else [falta_chave("R2_ACCOUNT_ID")]
    if not token:
        falta.append(falta_chave("CLOUDFLARE_API_TOKEN"))
    if falta:
        parar(falta)
    url = f"https://api.cloudflare.com/client/v4/accounts/{ambiente.valor('R2_ACCOUNT_ID')}{path}"
    dados = json.dumps(corpo).encode() if corpo is not None else None
    req = urllib.request.Request(url, data=dados, method=method,
                                 headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            status, texto = r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        status, texto = e.code, e.read().decode("utf-8", "replace")
    except urllib.error.URLError as e:
        die(f"Cloudflare API {method} {path}: sem resposta ({e.reason})", 1)
    try:
        data = json.loads(texto) if texto else {}
    except ValueError:
        data = {}
    if status >= 400 or not data.get("success", False):
        die(f"Cloudflare API {method} {path} -> {status}: {data.get('errors') or texto[:300]}", 1)
    return data.get("result", {})


def cmd_public(s3, a):
    b = bucket(a.bucket)
    path = f"/r2/buckets/{b}/domains/managed"
    if a.enable or a.disable:
        res = cf_api("PUT", path, {"enabled": bool(a.enable)})
        print(f"[OK] acesso público {'ligado' if a.enable else 'desligado'} em {b}")
    else:
        res = cf_api("GET", path)
    enabled = res.get("enabled")
    domain = res.get("domain")
    print(f"bucket={b} enabled={enabled} domain={domain}")
    if enabled and domain:
        print(f"-> {PREFIXO_BASE}{alias_of(b).upper()}=https://{domain}")


def cmd_smoke(s3, a):
    bs = buckets()
    if not bs:
        parar([falta_bucket("conteudo") + " Ou outro R2_BUCKET_<APELIDO>."])
    ok = True
    for alias, b in bs.items():
        try:
            s3.head_bucket(Bucket=b)
            vazio = not s3.list_objects_v2(Bucket=b, MaxKeys=1).get("Contents")
            print(f"[OK] {alias:<10} {b}: acessível" + (", vazio" if vazio else ""))
        except Exception as e:  # noqa: BLE001
            ok = False
            print(f"[FALHA] {alias:<10} {b}: {type(e).__name__}: {e}")
    if not ok:
        sys.exit(1)
    alias = "conteudo" if "conteudo" in bs else next(iter(bs))
    b = bs[alias]
    key = f"_smoke/{uuid.uuid4().hex}.txt"
    s3.put_object(Bucket=b, Key=key, Body=b"smoke test r2-storage", ContentType="text/plain")
    try:
        body = s3.get_object(Bucket=b, Key=key)["Body"].read()
    finally:
        s3.delete_object(Bucket=b, Key=key)
    if body != b"smoke test r2-storage":
        die(f"o objeto lido de volta em {b} não é o que subiu", 1)
    print(f"[OK] escrita/leitura/remoção em {b} (objeto temporário {key})")
    for alias in bs:
        base = public_base(alias)
        print(f"[{'OK' if base else '--'}] URL pública de {alias}: "
              + (base if base else f"não configurada ({PREFIXO_BASE}{alias.upper()}; opcional, só para bucket público)"))


def main(argv=None) -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("smoke").set_defaults(fn=cmd_smoke)
    s = sub.add_parser("ls")
    s.add_argument("bucket")
    s.add_argument("--prefix", default="")
    s.set_defaults(fn=cmd_ls)
    s = sub.add_parser("put")
    s.add_argument("bucket")
    s.add_argument("local")
    s.add_argument("key", nargs="?")
    s.set_defaults(fn=cmd_put)
    s = sub.add_parser("get")
    s.add_argument("bucket")
    s.add_argument("key")
    s.add_argument("local", nargs="?")
    s.set_defaults(fn=cmd_get)
    s = sub.add_parser("rm")
    s.add_argument("bucket")
    s.add_argument("key")
    s.set_defaults(fn=cmd_rm)
    s = sub.add_parser("url")
    s.add_argument("bucket")
    s.add_argument("key")
    s.set_defaults(fn=cmd_url, sem_s3=True)
    s = sub.add_parser("presign")
    s.add_argument("bucket")
    s.add_argument("key")
    s.add_argument("--expires", type=int, default=3600)
    s.set_defaults(fn=cmd_presign)
    s = sub.add_parser("public")
    s.add_argument("bucket")
    g = s.add_mutually_exclusive_group()
    g.add_argument("--enable", action="store_true")
    g.add_argument("--disable", action="store_true")
    s.set_defaults(fn=cmd_public, sem_s3=True)
    a = p.parse_args(argv)
    # url e public não falam com a API S3: não pedem o par de acesso, só o que cada um usa
    a.fn(None if getattr(a, "sem_s3", False) else client(), a)


if __name__ == "__main__":
    main()
