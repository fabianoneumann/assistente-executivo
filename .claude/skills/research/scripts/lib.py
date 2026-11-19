"""Utilitários compartilhados dos scripts de pesquisa (skill `research`).

Baixo acoplamento de propósito: cada script por fornecedor importa daqui apenas
o contrato de saída e a leitura de chave. Nenhuma lógica específica de fornecedor
vive neste módulo; ela fica em `perplexity_search.py` / `gemini_search.py`.

A leitura de chave passa pelo `ambiente.py` desta pasta (cópia idêntica do
`scripts/ambiente.py` da raiz do projeto): o que já está no ambiente vence, e o
que falta se lê do `.env` da raiz. Sem a chave, o script para com a mensagem
completa (a variável, para que serve, onde se pega e como se põe), sem traceback
e sem imprimir valor nenhum.

O registro de fontes na base (`knowledge/sources/`) NÃO acontece aqui: ele é um
ritual conduzido pelo Claude (extrair conteúdo, discutir takeaways, sintetizar),
seguindo o schema de `knowledge/sources/README.md`.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ambiente  # noqa: E402

CONTRACT_VERSION = "1"

# Windows usa cp1252 por padrão no stdout; forçamos UTF-8 para o JSON com acentos
# e caracteres fora do cp1252 sair íntegro (evita mojibake / erro ao capturar).
for _fluxo in (sys.stdout, sys.stderr):
    try:
        _fluxo.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

# variável: (para que serve, onde se pega). O mesmo texto do dicionário `CHAVES`
# de `scripts/confere_ambiente.py`, repetido aqui para a skill funcionar também
# instalada como plugin noutro projeto, sem aquele script.
CHAVES = {
    "PERPLEXITY_API_KEY": ("a busca da Perplexity (Sonar), na research",
                           "https://www.perplexity.ai/account/api/keys (conta da Perplexity, aba API; "
                           "a API é paga à parte do plano do app)"),
    "GEMINI_API_KEY": ("o Gemini com busca (research) e o Nano Banana (image-gen), pelo AI Studio",
                       "https://aistudio.google.com/apikey (Google AI Studio > Get API key)"),
    "VERTEX_API_KEY": ("o Gemini pelo Vertex AI (pós-pago), opcional no lugar do AI Studio",
                       "https://console.cloud.google.com/vertex-ai (Vertex AI > chave de API do modo expresso)"),
}

COMO_POR = ("Como pôr: copie o `.env.example` para `.env` na raiz do projeto (o `.env` nunca vai ao git) "
            "e preencha a linha da variável; ou ponha no bloco \"env\" do seu `.claude/settings.local.json`. "
            "Depois, reinicie a sessão do Claude Code. Para ver o quadro inteiro: "
            "python -X utf8 scripts/confere_ambiente.py --skill research")


def mensagem_falta(name: str) -> str:
    """A mensagem de chave ausente, sem valor nenhum: a variável, para que serve, onde se pega, como se põe."""
    uso, onde = CHAVES.get(name, ("uma chave da skill research", "o painel do fornecedor"))
    return (f"[PARE] a skill research não roda sem a variável {name} ({uso}).\n"
            f"Onde se pega: {onde}.\n{COMO_POR}")


def get_key(name: str) -> str:
    """Lê uma chave de API pelo `ambiente.py`; sem ela (ou ainda no marcador do `.env.example`), sai com a mensagem."""
    val = ambiente.valor(name)
    if not val:
        sys.exit(mensagem_falta(name))
    return val


def importar_sdk(modulo: str):
    """Importa o SDK do fornecedor; sem ele instalado, sai com a instrução de instalação, sem traceback."""
    import importlib
    try:
        return importlib.import_module(modulo)
    except ImportError:
        sys.exit(f"[PARE] falta o pacote Python `{modulo}` da skill research. Como instalar, da raiz do projeto: "
                 "python -m pip install -r .claude/skills/research/requirements.txt")


def make_result(provider, mode, model, query,
                answer="", results=None, citations=None, error=None) -> dict:
    """Monta o contrato de saída uniforme entre fornecedores.

    ``answer`` (texto aterrado) fica separado de ``results`` (fontes cruas) de
    propósito: o Claude vê os dois, triangula entre fornecedores e reconcilia
    contradições na hora de sintetizar.
    """
    return {
        "contract_version": CONTRACT_VERSION,
        "provider": provider,
        "mode": mode,
        "model": model,
        "query": query,
        "answer": answer or "",
        "results": results or [],
        "citations": citations or [],
        "error": error,
    }


def emit(result: dict) -> None:
    """Imprime o resultado no contrato JSON (stdout, UTF-8)."""
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
