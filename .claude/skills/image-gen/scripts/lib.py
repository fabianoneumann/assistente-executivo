"""Utilitários compartilhados da skill `image-gen`.

Mesmo padrão da skill `research`: leitura de chave e emissão do contrato JSON no stdout. Nenhuma lógica de imagem
vive aqui; ela fica em `nano_banana.py`.

A leitura de chave passa pelo `ambiente.py` desta pasta (cópia idêntica do `scripts/ambiente.py` da raiz do projeto):
o que já está no ambiente vence, e o que falta se lê do `.env` da raiz. Sem a chave, o script para com a mensagem
completa (a variável, para que serve, onde se pega e como se põe), sem traceback e sem imprimir valor nenhum.
"""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ambiente  # noqa: E402

# Windows usa cp1252 por padrão no stdout; forçamos UTF-8 para o JSON com acentos sair íntegro.
for _fluxo in (sys.stdout, sys.stderr):
    try:
        _fluxo.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

# variável: (para que serve, onde se pega). O mesmo texto do `CHAVES` de `scripts/confere_ambiente.py` da raiz,
# repetido aqui para a skill funcionar também instalada como plugin noutro projeto.
CHAVES = {
    "GEMINI_API_KEY": ("o Gemini com busca (research) e o Nano Banana (image-gen), pelo AI Studio",
                       "https://aistudio.google.com/apikey (Google AI Studio > Get API key)"),
    "VERTEX_API_KEY": ("o Gemini pelo Vertex AI (pós-pago), opcional no lugar do AI Studio",
                       "https://console.cloud.google.com/vertex-ai (Vertex AI > chave de API do modo expresso)"),
}

COMO_POR = ("Como pôr: copie o `.env.example` para `.env` na raiz do projeto (o `.env` nunca vai ao git) e preencha "
            "a linha da variável; ou ponha no bloco \"env\" do seu `.claude/settings.local.json`. Depois, reinicie a "
            "sessão do Claude Code. Para ver o quadro inteiro: python -X utf8 scripts/confere_ambiente.py --skill image-gen")


def mensagem_falta(name: str) -> str:
    uso, onde = CHAVES.get(name, ("uma chave da skill image-gen", "o painel do fornecedor"))
    return f"[PARE] a skill image-gen não roda sem a variável {name} ({uso}).\nOnde se pega: {onde}.\n{COMO_POR}"


def get_key(name: str) -> str:
    """Lê uma chave pelo `ambiente.py`; sem ela (ou ainda no marcador do `.env.example`), sai com a mensagem."""
    val = ambiente.valor(name)
    if not val:
        sys.exit(mensagem_falta(name))
    return val


def importar(modulo: str, requisitos: str = ".claude/skills/image-gen/requirements.txt"):
    """Importa um pacote; sem ele instalado, sai com a instrução de instalação, sem traceback."""
    import importlib
    try:
        return importlib.import_module(modulo)
    except ImportError:
        sys.exit(f"[PARE] falta o pacote Python `{modulo}` da skill image-gen. Como instalar, da raiz do projeto: "
                 f"python -m pip install -r {requisitos}")


def raiz_do_projeto() -> Path:
    """A raiz do projeto: a que contém esta skill (`.claude/skills/image-gen/scripts/`), ou, instalada como plugin, a
    pasta do projeto aberto (CLAUDE_PROJECT_DIR) ou a pasta de trabalho."""
    aqui = Path(__file__).resolve()
    if len(aqui.parents) > 4 and aqui.parents[2].name == "skills" and aqui.parents[3].name == ".claude":
        return aqui.parents[4]
    return Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path.cwd()).resolve()


def emit(result: dict) -> None:
    """Imprime o resultado no contrato JSON (stdout, UTF-8)."""
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
