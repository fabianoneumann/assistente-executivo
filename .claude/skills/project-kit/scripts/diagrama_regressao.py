"""A regressão visual dos diagramas do kit: cada exemplo, no claro e no escuro, contra a linha de base guardada.

A linha de base fica em `assets/diagramas/linha-de-base/<exemplo>-<tema>.png`: a figura inteira reduzida a 320 px de
largura, em tons de cinza (de 19 a 33 KB cada, cerca de 354 KB os 14), feita pelo próprio navegador, sem biblioteca de imagem. A redução
tira o ruído de antialiasing de uma máquina para outra e guarda o que importa numa regressão de diagrama: a caixa que
mudou de lugar, a seta que sumiu, o rótulo que pulou, a altura que cresceu. O que ela não vê (um pixel de cor, uma
letra trocada) as outras conferências pegam (o esquema e o `diagrama_conferir.py`).

A comparação, por exemplo e tema:
  - a base com outra largura que a de 320 px: `REG-BASE-INVALIDA` (gere de novo com `--atualizar`);
  - a altura da figura nova contra a da base: mais de 2% de diferença é regressão (`REG-ALTURA`);
  - até 2% de altura, a figura inteira: a faixa que só uma das duas tem conta toda como diferença; a fração de pixels cuja diferença de cinza passa de 32 (em 255): acima do limiar, regressão
    (`REG-PIXELS`); o limiar padrão é 0,01% (`--limiar 0.0001`), medido em 19/11: o mesmo exemplo renderizado de novo
    na mesma máquina dá 0% nos 14 (sete exemplos, dois temas), e o rótulo "sim" da prioridade movido 40 px para baixo e 40 para a esquerda (uns 57 px) dá 0,015%
    (cerca de 14 pixels na redução): o rótulo pequeno some quase todo a 320 px, por isso o limiar fica perto de zero;
  - sem a base: `REG-SEM-BASE` (rode com `--atualizar` depois de aprovar a figura).
A base vale para um ambiente só: o `linha-de-base/ambiente.json` grava o sistema e a versão do Chromium que a geraram, e
a comparação noutro ambiente sai com o AVISO `REG-AMBIENTE` (a diferença pode vir do ambiente). Noutra máquina, gere a
base dela numa pasta fora do git antes de comparar. `--atualizar` sobrescreve a base versionada: é aprovar a figura
nova, e só depois da conferência e da leitura.

Uso: python -X utf8 diagrama_regressao.py [dados.json ...] [--atualizar] [--limiar 0.0001] [--saida <pasta>]
  sem dados, todos os exemplos de `assets/diagramas/*.json` (só os dados de diagrama); grava, na <saida> (padrão: a
  pasta temporária, fora do repositório), o regressao.json e, para cada falha, a imagem
  da diferença (<exemplo>-<tema>-diferenca.png, em vermelho sobre a base); sai com 1 se houver regressão."""
import argparse, base64, json, shutil, subprocess, sys, tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import diagrama_render as render  # noqa: E402

BASE = render.MODELO / "linha-de-base"
LARGURA = 320
CORTE_CINZA = 32

JS = r"""
async ({nova, base, largura, corte, gravar}) => {
  const carrega = src => new Promise((ok, erro) => { const i = new Image(); i.onload = () => ok(i); i.onerror = erro; i.src = src; });
  const cinza = img => { const h = Math.round(img.height * largura / img.width), c = document.createElement('canvas');
    c.width = largura; c.height = h; const x = c.getContext('2d'); x.drawImage(img, 0, 0, largura, h);
    const d = x.getImageData(0, 0, largura, h);
    for (let k = 0; k < d.data.length; k += 4) { const g = Math.round(0.299 * d.data[k] + 0.587 * d.data[k + 1] + 0.114 * d.data[k + 2]);
      d.data[k] = d.data[k + 1] = d.data[k + 2] = g; }
    x.putImageData(d, 0, 0); return {c, d, h}; };
  const n = cinza(await carrega(nova));
  if (gravar) return {png: n.c.toDataURL('image/png'), altura: n.h};
  const bImg = await carrega(base), b = {c: document.createElement('canvas')};
  b.c.width = bImg.width; b.c.height = bImg.height; const bx = b.c.getContext('2d'); bx.drawImage(bImg, 0, 0);
  b.d = bx.getImageData(0, 0, bImg.width, bImg.height); b.h = bImg.height;
  const res = {altura_nova: n.h, altura_base: b.h};
  if (bImg.width !== largura) { res.motivo = 'base'; res.largura_base = bImg.width; return res; }
  if (Math.abs(n.h - b.h) / b.h > 0.02) { res.motivo = 'altura'; return res; }
  // a figura inteira: a faixa que só uma das duas tem conta toda como diferença (a altura que mudou até 2% não
  // escapa por comparar só a parte comum)
  const h = Math.max(n.h, b.h), hc = Math.min(n.h, b.h); let dif = 0;
  const out = new ImageData(largura, h);
  for (let y = 0; y < h; y++) for (let x = 0; x < largura; x++) {
    const k = (y * largura + x) * 4;
    const difere = y >= hc || Math.abs(n.d.data[k] - b.d.data[k]) > corte;
    const g = y < b.h ? b.d.data[k] : 255;
    if (difere) { dif++; out.data[k] = 220; out.data[k + 1] = 30; out.data[k + 2] = 30; }
    else { out.data[k] = out.data[k + 1] = out.data[k + 2] = g; }
    out.data[k + 3] = 255;
  }
  res.fracao = dif / (largura * h);
  if (dif) { const c = document.createElement('canvas'); c.width = largura; c.height = h; c.getContext('2d').putImageData(out, 0, 0); res.diferenca = c.toDataURL('image/png'); }
  return res;
}
"""


def data_url(p: Path) -> str:
    return "data:image/png;base64," + base64.b64encode(p.read_bytes()).decode()


def comparar(pg, nova: Path, base: Path | None, limiar: float, gravar: bool = False) -> dict:
    """Compara uma figura (PNG de 1280 px) com a base reduzida; com gravar, devolve a base nova em data URL."""
    r = pg.evaluate(JS, {"nova": data_url(nova), "base": data_url(base) if base else "", "largura": LARGURA,
                         "corte": CORTE_CINZA, "gravar": gravar})
    if gravar:
        return r
    if r.get("motivo") == "base":
        r.update(codigo="REG-BASE-INVALIDA", regressao=True)
    elif r.get("motivo") == "altura":
        r.update(codigo="REG-ALTURA", regressao=True)
    else:
        r.update(codigo="REG-PIXELS" if r["fracao"] > limiar else None, regressao=r["fracao"] > limiar)
    return r


AMBIENTE = BASE / "ambiente.json"


def ambiente(nav) -> dict:
    """O ambiente que gera a figura: o sistema e a versão do Chromium. A base só vale nele."""
    import platform
    return {"sistema": f"{platform.system()} {platform.release()}", "chromium": nav.version}


def ambiente_igual(nav) -> tuple[bool, dict, dict]:
    atual = ambiente(nav)
    try:
        gravado = json.loads(AMBIENTE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        gravado = {}
    return gravado == atual, atual, gravado


def exemplos() -> list[Path]:
    """Os exemplos da pasta do modelo: só os dados de diagrama (o regressao.json e outros JSON de trabalho ficam fora)."""
    def eh_diagrama(p: Path) -> bool:
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return False
        return isinstance(d, dict) and ("nos" in d or "participantes" in d)
    return sorted(p for p in render.MODELO.glob("*.json") if p.name != "regressao.json" and eh_diagrama(p))


def main():
    from playwright.sync_api import sync_playwright
    ap = argparse.ArgumentParser()
    ap.add_argument("dados", nargs="*")
    ap.add_argument("--atualizar", action="store_true", help="grava a base nova (aprovar a figura)")
    ap.add_argument("--limiar", type=float, default=0.0001)
    ap.add_argument("--saida", default=str(Path(tempfile.gettempdir()) / "diagrama-regressao"),
                    help="onde gravar o regressao.json e as diferenças (padrão: a pasta temporária, fora do repositório)")
    a = ap.parse_args()
    alvos = [Path(d).resolve() for d in a.dados] or exemplos()
    saida = Path(a.saida); saida.mkdir(parents=True, exist_ok=True)
    tmp = Path(tempfile.mkdtemp(prefix="regressao-"))
    try:
        r = subprocess.run([sys.executable, "-X", "utf8", str(Path(render.__file__)), *map(str, alvos), "--saida", str(tmp)],
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        if r.returncode:
            raise SystemExit("o render falhou: " + r.stderr.strip()[-600:])
        resultado, falhas = {}, 0
        BASE.mkdir(exist_ok=True)
        with sync_playwright() as p:
            nav = p.chromium.launch(args=["--disable-lcd-text"]); pg = nav.new_page()
            igual, atual, gravado = ambiente_igual(nav)
            if a.atualizar:
                AMBIENTE.write_text(json.dumps(atual, indent=1, ensure_ascii=False) + chr(10), encoding="utf-8")
            elif not igual:
                print(f"AVISO REG-AMBIENTE: a base foi gerada em {gravado or 'ambiente não registrado'}, e esta máquina é "
                      f"{atual}; a diferença de pixels pode vir do ambiente. Gere a base desta máquina numa pasta fora do "
                      "git para comparar, ou aprove a figura com --atualizar.")
            for d in alvos:
                for tema in ("claro", "escuro"):
                    nome = f"{d.stem}-{tema}"; nova = tmp / f"{nome}.png"; base = BASE / f"{nome}.png"
                    if a.atualizar:
                        g = comparar(pg, nova, None, a.limiar, gravar=True)
                        base.write_bytes(base64.b64decode(g["png"].split(",", 1)[1]))
                        resultado[nome] = {"base": "gravada", "altura": g["altura"]}; print(f"{nome}: base gravada"); continue
                    if not base.exists():
                        resultado[nome] = {"codigo": "REG-SEM-BASE", "regressao": True}; falhas += 1
                        print(f"{nome}: REG-SEM-BASE (rode com --atualizar depois de aprovar a figura)"); continue
                    c = comparar(pg, nova, base, a.limiar)
                    dif = c.pop("diferenca", None)
                    if c["regressao"]:
                        falhas += 1
                        if dif:
                            (saida / f"{nome}-diferenca.png").write_bytes(base64.b64decode(dif.split(",", 1)[1]))
                    resultado[nome] = c
                    medida = (f"altura {c['altura_nova']} contra {c['altura_base']}" if c.get("codigo") == "REG-ALTURA"
                              else f"{100 * c['fracao']:.2f}% dos pixels")
                    print(f"{nome}: " + (f"{c['codigo']} ({medida})" if c["regressao"] else f"igual ({medida})"))
            nav.close()
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    (saida / "regressao.json").write_text(json.dumps(resultado, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"total: {falhas} regressão(ões)")
    sys.exit(1 if falhas else 0)


if __name__ == "__main__":
    main()
