#!/usr/bin/env python3
"""Diz o que já funciona e o que falta configurar, skill por skill, sem mostrar valor de chave.

Uso, da raiz do repositório:
  python -X utf8 scripts/confere_ambiente.py                     # o quadro de todas as skills
  python -X utf8 scripts/confere_ambiente.py --skill research    # só uma; sai com 1 se faltar o obrigatório
  python -X utf8 scripts/confere_ambiente.py --skill slides-export --upload   # inclui o que a subida ao bucket pede

O primeiro passo de cada skill com chave roda a segunda forma. Código de saída:
  0  a skill pode rodar (o opcional que faltar só desliga uma parte, e o quadro diz qual);
  1  falta algo obrigatório: a skill para e repassa a mensagem;
  2  uso errado (skill desconhecida).

As chaves vêm do ambiente ou do `.env` da raiz (ver `.env.example` e o README). Este script só
diz se a variável existe; nunca imprime o valor, nem parte dele.
"""
from __future__ import annotations

import argparse
import filecmp
import importlib.util
import shutil
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "scripts"))
import ambiente  # noqa: E402

COMO_POR = ("Como pôr: copie o `.env.example` para `.env` na raiz do repositório (o `.env` nunca vai ao git) "
            "e preencha a linha da variável no seu editor, não pela conversa com o Claude (ou ponha no bloco \"env\" "
            "do seu `.claude/settings.local.json`). Depois, reinicie a sessão do Claude Code.")

# variável: (para que serve, onde se pega)
CHAVES = {
    "PERPLEXITY_API_KEY": ("a busca da Perplexity (Sonar), na research",
                           "https://www.perplexity.ai/account/api/keys (conta da Perplexity, aba API; a API é paga à parte do plano do app)"),
    "GEMINI_API_KEY": ("o Gemini com busca (research) e o Nano Banana (image-gen), pelo AI Studio",
                       "https://aistudio.google.com/apikey (Google AI Studio > Get API key)"),
    "VERTEX_API_KEY": ("o Gemini pelo Vertex AI (pós-pago), opcional no lugar do AI Studio",
                       "https://console.cloud.google.com/vertex-ai (Vertex AI > chave de API do modo expresso)"),
    "TYPESAFE_API_KEY": ("o Jev (TypeSafe), opcional: a conferência de texto na imagem e as sondas",
                         "https://docs.typesafe.ai (o painel da TypeSafe, chaves de API)"),
    "R2_ACCOUNT_ID": ("a conta da Cloudflare que tem o R2",
                      "https://dash.cloudflare.com > R2 > Overview (o Account ID fica na lateral)"),
    "R2_ACCESS_KEY_ID": ("o par de acesso S3 do R2",
                         "https://dash.cloudflare.com > R2 > Manage API tokens > Create API token (o Access Key ID)"),
    "R2_SECRET_ACCESS_KEY": ("o segredo do par de acesso S3 do R2",
                             "o mesmo token do R2 (o Secret Access Key aparece uma vez só, ao criar)"),
    "R2_BUCKET_CONTEUDO": ("o nome do bucket de conteúdo (o apelido `conteudo` das skills)",
                           "o nome do bucket que você criou em R2 > Create bucket"),
    "R2_PUBLIC_BASE_CONTEUDO": ("a URL pública do bucket de conteúdo, para montar os links das imagens",
                                "R2 > o bucket > Settings > Public access (o endereço r2.dev ou o domínio próprio)"),
    "CLOUDFLARE_API_TOKEN": ("só o comando `public` do r2.py (ligar o domínio público pela API REST)",
                             "o \"Token value\" mostrado ao criar o token do R2 com Admin Read & Write"),
}

# ferramenta de linha de comando: (para que serve, como se instala)
FERRAMENTAS = {
    "gh": ("ler e comentar issues e PRs (review); criar o repositório, a milestone e as specs (project-kit)", "https://cli.github.com, depois `gh auth login`"),
    "codex": ("o Codex como segunda revisão de código e buscador extra (opcional)", "https://developers.openai.com/codex/cli, depois `codex login`"),
    "shot-scraper": ("a foto das telas (slides-export)", "python -m pip install shot-scraper; depois, shot-scraper install"),
    "ffmpeg": ("o vídeo das telas e os quadros (slides-export, visual-form, object-anatomy)", "https://ffmpeg.org/download.html (no Windows: winget install Gyan.FFmpeg)"),
    "node": ("o teste do iso.js (object-anatomy, opcional)", "https://nodejs.org"),
}

# pacote Python: o arquivo de requisitos que o instala
PACOTES = {
    "openai": ".claude/skills/research/requirements.txt",
    "google.genai": ".claude/skills/research/requirements.txt",
    "boto3": ".claude/skills/r2-storage/requirements.txt",
    "PIL": ".claude/skills/image-gen/requirements.txt",
    "numpy": ".claude/skills/image-gen/requirements.txt",
    "playwright": ".claude/skills/visual-form/requirements.txt",
}

R2 = ["R2_ACCOUNT_ID", "R2_ACCESS_KEY_ID", "R2_SECRET_ACCESS_KEY", "R2_BUCKET_CONTEUDO"]
R2_UPLOAD = R2 + ["R2_PUBLIC_BASE_CONTEUDO"]  # a subida registra os links: precisa da URL pública

# skill: obrigatório (chaves, ferramentas, pacotes), opcional (idem), e o que só a subida ao bucket pede
SKILLS = {
    "idea-capture": {},
    "review": {"ferr_opc": ["gh", "codex"], "chaves_opc": ["TYPESAFE_API_KEY"]},
    "story-angle": {"nota": "sem chave própria, mas a apuração vai toda pela research: sem as chaves dela, a story-angle para na primeira busca (confira com --skill research)"},
    # a GEMINI_API_KEY é a rota padrão (e a única do modo profundo da research); a Vertex é pós-pago, só com estimativa
    "research": {"chaves": ["PERPLEXITY_API_KEY", "GEMINI_API_KEY"], "pacotes": ["openai", "google.genai"],
                 "chaves_opc": ["VERTEX_API_KEY", "TYPESAFE_API_KEY"], "ferr_opc": ["codex"]},
    "image-gen": {"chaves": ["GEMINI_API_KEY"], "pacotes": ["google.genai", "PIL", "numpy"],
                  "chaves_opc": ["VERTEX_API_KEY", "TYPESAFE_API_KEY"], "ferr_opc": ["codex"]},
    "r2-storage": {"chaves": R2, "pacotes": ["boto3"], "chaves_opc": ["R2_PUBLIC_BASE_CONTEUDO", "CLOUDFLARE_API_TOKEN"]},
    "slides-export": {"ferr": ["shot-scraper", "ffmpeg"], "pacotes": ["playwright", "PIL"],
                      "upload": R2_UPLOAD, "pacotes_upload": ["boto3"]},
    "visual-form": {"ferr": ["ffmpeg"], "pacotes": ["playwright", "PIL", "numpy"]},
    "object-anatomy": {"ferr": ["ffmpeg"], "pacotes": ["playwright", "PIL", "numpy"], "ferr_opc": ["node"]},
    "piece-creation": {"nota": "orquestra as outras: cada etapa confere a sua skill"},
    "piece-script": {},
    "base-enrichment": {},
    "project-kit": {"ferr": ["gh"], "nota": "montar e conferir pedem só o git e o Python; o gh, com `gh auth login`, cria o repositório, a milestone e as specs"},
}

COPIAS_DO_CARREGADOR = ["research", "image-gen", "r2-storage", "slides-export"]


_LOGIN_CODEX: bool | None = None


def codex_com_login() -> bool:
    """`codex login status` sai com 0 quando há login; consulta uma vez só por execução."""
    global _LOGIN_CODEX
    if _LOGIN_CODEX is None:
        try:
            r = subprocess.run([shutil.which("codex") or "codex", "login", "status"], capture_output=True, timeout=20)
            _LOGIN_CODEX = r.returncode == 0
        except (OSError, subprocess.TimeoutExpired):
            _LOGIN_CODEX = False
    return _LOGIN_CODEX


def tem_pacote(nome: str) -> bool:
    try:
        return importlib.util.find_spec(nome) is not None
    except (ImportError, ValueError):
        return False


def faltas(skill: str, upload: bool) -> tuple[list[str], list[str]]:
    """(o que falta e é obrigatório, o que falta e é opcional), como linhas de texto."""
    r = SKILLS[skill]
    obrig, opc = [], []
    chaves = list(r.get("chaves", [])) + (list(r.get("upload", [])) if upload else [])
    for c in chaves:
        if not ambiente.valor(c):
            uso, onde = CHAVES[c]
            obrig.append(f"variável {c} ({uso}). Onde se pega: {onde}.")
    for grupo in r.get("uma_de", []):
        if not any(ambiente.valor(c) for c in grupo):
            obrig.append("uma destas variáveis (basta uma): " + "; ".join(
                f"{c} ({CHAVES[c][0]}; onde se pega: {CHAVES[c][1]})" for c in grupo) + ".")
        elif not ambiente.valor(grupo[0]):
            opc.append(f"variável {grupo[0]} ({CHAVES[grupo[0]][0]}): sem ela, a skill roda só pela {', '.join(c for c in grupo[1:] if ambiente.valor(c))}"
                       " (passe --provider vertex onde o script pedir).")
    for f in r.get("ferr", []):
        if not shutil.which(f):
            uso, como = FERRAMENTAS[f]
            obrig.append(f"programa `{f}` ({uso}). Como instalar: {como}.")
    pacotes = list(r.get("pacotes", [])) + (list(r.get("pacotes_upload", [])) if upload else [])
    for p in pacotes:
        if not tem_pacote(p):
            obrig.append(f"pacote Python `{p}`. Como instalar: python -m pip install -r {PACOTES[p]}.")
    for c in r.get("chaves_opc", []):
        if not ambiente.valor(c):
            uso, onde = CHAVES[c]
            opc.append(f"variável {c} ({uso}). Onde se pega: {onde}.")
    for f in r.get("ferr_opc", []):
        if not shutil.which(f):
            uso, como = FERRAMENTAS[f]
            opc.append(f"programa `{f}` ({uso}). Como instalar: {como}.")
        elif f == "codex" and not codex_com_login():
            opc.append("o Codex está instalado, mas sem login: rode `codex login` (a review segue sem ele e diz isso).")
    if not upload and r.get("upload"):
        falta_up = [c for c in r["upload"] if not ambiente.valor(c)]
        if falta_up:
            opc.append("para subir ao bucket (`--upload`) e conferir o que já foi publicado: "
                       + ", ".join(falta_up) + " (rode com --upload para o detalhe).")
    return obrig, opc


def copias_iguais() -> list[str]:
    base = RAIZ / "scripts/ambiente.py"
    erradas = []
    copias = [RAIZ / f".claude/skills/{s}/scripts/ambiente.py" for s in COPIAS_DO_CARREGADOR] + [RAIZ / "scripts/jev/ambiente.py"]
    for c in copias:
        if not c.exists():
            erradas.append(c.relative_to(RAIZ).as_posix() + " (falta)")
        elif not filecmp.cmp(base, c, shallow=False):
            erradas.append(c.relative_to(RAIZ).as_posix())
    return erradas


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--skill", help="confere só esta skill e sai com 1 se faltar o obrigatório")
    ap.add_argument("--upload", action="store_true", help="inclui o que a subida ao bucket pede (slides-export)")
    a = ap.parse_args(argv)

    arq = ambiente.carregar_env(RAIZ)
    if a.skill:
        if a.skill not in SKILLS:
            print(f"[ERRO] skill desconhecida: {a.skill}. Conhecidas: {', '.join(SKILLS)}.")
            return 2
        obrig, opc = faltas(a.skill, a.upload)
        if obrig:
            print(f"[PARE] a skill {a.skill} não roda ainda. Falta configurar:")
            for linha in obrig:
                print(f"  - {linha}")
            print(COMO_POR)
            print("Depois de configurar, rode de novo: python -X utf8 scripts/confere_ambiente.py --skill " + a.skill
                  + (" --upload" if a.upload else ""))
            return 1
        print(f"[OK] a skill {a.skill} pode rodar.")
        for linha in opc:
            print(f"  (opcional, desligado) {linha}")
        if SKILLS[a.skill].get("nota"):
            print(f"  nota: {SKILLS[a.skill]['nota']}")
        return 0

    print("O ambiente, skill por skill" + (f" (lendo também o {arq.name} da raiz)" if arq else " (sem .env na raiz)") + ":\n")
    for s in SKILLS:
        obrig, opc = faltas(s, False)
        estado = "falta configurar" if obrig else ("pronta, com partes desligadas" if opc else "pronta")
        print(f"{s:16} {estado}")
        for linha in obrig:
            print(f"    falta: {linha}")
        for linha in opc:
            print(f"    opcional: {linha}")
        if SKILLS[s].get("nota"):
            print(f"    nota: {SKILLS[s]['nota']}")
    erradas = copias_iguais()
    if erradas:
        print("\n[AVISO] cópias do carregador de chaves diferentes de scripts/ambiente.py: " + ", ".join(erradas))
    print("\n" + COMO_POR)
    return 0


if __name__ == "__main__":
    sys.exit(main())
