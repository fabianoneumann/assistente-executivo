"""Teste da linha de comando do saltos.py, sem vídeo nem ffmpeg: o --help mostra o uso e sai com 0, sem tentar abrir
um arquivo chamado "--help"; sem argumento, sai com 2; com arquivos, devolve a lista. A medida (`medir`) não muda e
segue coberta pelo caso 21 do teste_tela_em_video.py da slides-export.

    python -X utf8 .claude/skills/object-anatomy/scripts/teste_saltos.py
"""
import contextlib
import io
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import saltos  # noqa: E402

falhas = []


def caso(nome, ok):
    print(("ok    " if ok else "FALHA ") + nome)
    if not ok:
        falhas.append(nome)


def sai_com(argv):
    err, out = io.StringIO(), io.StringIO()
    try:
        with contextlib.redirect_stderr(err), contextlib.redirect_stdout(out):
            saltos.argumentos(argv)
    except SystemExit as e:
        return e.code, out.getvalue() + err.getvalue()
    return None, out.getvalue() + err.getvalue()


codigo, texto = sai_com(["--help"])
caso("--help sai com 0 e mostra o uso", codigo == 0 and "mp4" in texto)
codigo, texto = sai_com(["-h"])
caso("-h sai com 0", codigo == 0)
codigo, _ = sai_com([])
caso("sem arquivo sai com 2", codigo == 2)
caso("com arquivos devolve a lista", saltos.argumentos(["a.mp4", "b.mp4"]) == ["a.mp4", "b.mp4"])
caso("o -- deixa passar um nome com hífen", saltos.argumentos(["--", "-x.mp4"]) == ["-x.mp4"])
# pelo processo, como a pessoa roda: o --help não pode virar a tentativa de abrir o arquivo "--help"
r = subprocess.run([sys.executable, "-X", "utf8", str(AQUI / "saltos.py"), "--help"], capture_output=True, text=True,
                   encoding="utf-8")
caso("pelo processo, --help sai com 0, mostra o uso e não tem traceback",
     r.returncode == 0 and "usage:" in r.stdout and "mp4" in r.stdout and "Traceback" not in r.stderr)
import inspect  # noqa: E402
assinatura = inspect.signature(saltos.medir)
obrigatorios = [n for n, p in assinatura.parameters.items() if p.default is inspect.Parameter.empty]
caso("a interface que a slides-export usa continua: medir(mp4, ffmpeg, ffprobe), só o mp4 obrigatório",
     list(assinatura.parameters)[:3] == ["mp4", "ffmpeg", "ffprobe"] and obrigatorios == ["mp4"])

if falhas:
    print(f"\n{len(falhas)} caso(s) falharam")
    sys.exit(1)
print("\ntodos os casos ok")
