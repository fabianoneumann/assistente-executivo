"""Teste do extrai_pdf.py, sem rede e sem material de terceiro: o PDF se gera aqui, com o PyMuPDF.

Cinco páginas, uma por caso: 1, texto corrido limpo (não marca); 2, vazia (sem_texto); 3, uma imagem que cobre
a página (imagem); 4, uma grade desenhada com texto nas células (tabela); 5, texto com caracteres de controle
partido por hífen no fim da linha (estranho; o caractere de substituição se testa direto na medida); 6 e 7,
o papel escaneado com OCR, com o texto só no alto (imagem) e pela página toda (nada); 8, a tabela sem grade,
lida pelos números (tabela). Confere também a marca de página e a numeração no .md, a página citada por uma
ficha falsa, o render só das marcadas, o código de saída e o motor pdftotext quando ele existe.

Rodar: <venv>/Scripts/python.exe -I -X utf8 teste_extrai_pdf.py (o python de uma venv com o PyMuPDF; sem ele, só os casos que não geram PDF)   (grava só num diretório temporário; TESTE_TMP=<pasta> o põe em outro disco)
"""
import json
import os
import shutil
import sys
import tempfile
from pathlib import Path

try:
    import pymupdf
except ImportError:  # sem o PyMuPDF, só os casos que não geram PDF rodam (a faixa e as fichas)
    pymupdf = None

sys.path.insert(0, str(Path(__file__).resolve().parent))
import extrai_pdf  # noqa: E402

LOREM = ("A extração por script lê a camada de texto de cada página e marca o que pede olho. "
         "Esta frase se repete para a página ter texto bastante, como um capítulo comum de manual. ")


def gerar(pdf: Path) -> None:
    doc = pymupdf.open()
    p = doc.new_page()  # 1: texto limpo
    p.insert_textbox(pymupdf.Rect(50, 50, 550, 800), LOREM * 6, fontsize=11)
    doc.new_page()  # 2: vazia
    p = doc.new_page()  # 3: imagem que cobre a página
    pix = pymupdf.Pixmap(pymupdf.csRGB, pymupdf.IRect(0, 0, 60, 80), 0)
    pix.clear_with(200)
    p.insert_image(p.rect, pixmap=pix)
    p.insert_text((60, 60), "Figura 1", fontsize=11)
    p = doc.new_page()  # 4: grade
    for i in range(7):
        p.draw_line((50, 100 + i * 30), (500, 100 + i * 30))
    for j in range(5):
        p.draw_line((50 + j * 112.5, 100), (50 + j * 112.5, 280))
    for i in range(6):
        for j in range(4):
            p.insert_text((55 + j * 112.5, 120 + i * 30), f"c{i}{j}", fontsize=10)
    p.insert_textbox(pymupdf.Rect(50, 320, 550, 800), LOREM * 3, fontsize=11)
    p = doc.new_page()  # 5: palavras partidas por hífen no fim da linha, como na coluna estreita
    for i in range(20):
        p.insert_text((50, 60 + i * 16), f"linha {i} com uma pala-", fontsize=11)
    for cheia in (False, True):  # 6 e 7: o papel escaneado com OCR (a imagem cobre a página, o texto por cima)
        p = doc.new_page()
        p.insert_image(p.rect, pixmap=pix)
        for i in range(46 if cheia else 8):
            p.insert_text((40, 40 + i * 17), "A camada de OCR por cima do papel escaneado, linha a linha, de margem a margem " + str(i), fontsize=11)
    p = doc.new_page()  # 8: tabela escaneada lida como texto, sem grade: muitos números e fragmentos
    for i in range(12):
        p.insert_text((50, 60 + i * 16), "  ".join(f"{i}{j} 0.{j}" for j in range(5)), fontsize=10)
    doc.save(str(pdf))
    doc.close()


def main() -> int:
    falhas = []

    def ok(cond, msg):
        print(("ok    " if cond else "FALHA ") + msg)
        if not cond:
            falhas.append(msg)

    # a faixa e as fichas limitam o intervalo ao total antes de expandir (o "1-1000000000" não estoura)
    ok(extrai_pdf.faixa("1-1000000000", 3) == [1, 2, 3], "0a. a faixa enorme se limita ao total")
    ok(extrai_pdf.faixa("0-2,7", 5) == [1, 2], "0b. a faixa fora de 1..total some")
    tmp = Path(tempfile.mkdtemp(prefix="teste_extrai_pdf_", dir=os.environ.get("TESTE_TMP") or None))
    try:
        fic = tmp / "ficha-grande.md"
        fic.write_text("PDF p. 1-1000000000\n", encoding="utf-8")
        ok(extrai_pdf.citadas_nas_fichas([str(fic)], "x.pdf", 4) == {1, 2, 3, 4}, "0c. o intervalo da ficha se limita ao total")
        if pymupdf is None:
            print("pulado 1 a 20: o PyMuPDF não está neste python (rode pelo python da venv)")
            return 1 if falhas else 0
        pdf = tmp / "obra-teste.pdf"
        gerar(pdf)
        ficha = tmp / "ficha.md"
        ficha.write_text("Proveniência: obra-teste, PDF p. 1.\n", encoding="utf-8")
        saida = tmp / "out"
        cod = extrai_pdf.main([str(pdf), "--saida", str(saida), "--numerar", "--fichas", str(ficha), "--dpi", "50"])
        dados = json.loads((saida / "obra-teste.pontos.json").read_text(encoding="utf-8"))
        pg = dados["paginas"]
        ok(cod == 1, "1. código 1 quando há página marcada")
        ok(pg["1"]["marcas"] == ["citada"], f"2. a página limpa só leva a marca de citada (veio {pg['1']['marcas']})")
        ok("sem_texto" in pg["2"]["marcas"], "3. a página vazia sai sem_texto")
        ok("imagem" in pg["3"]["marcas"], f"4. a página com imagem sai imagem (área {pg['3'].get('area_imagem')})")
        ok("tabela" in pg["4"]["marcas"], f"5. a grade sai tabela (tabelas {pg['4'].get('tabelas')}, traços {pg['4'].get('tracos')})")
        ok("estranho" in pg["5"]["marcas"], f"6. o texto partido por hífen sai estranho (hífens {pg['5'].get('hifen_fim')})")
        m = extrai_pdf.medidas_texto("texto com lixo " + "\ufffd\ufffd\ue000\x07 " * 3)
        ok(m["frac_ruins"] >= 0.02, f"6b. caractere de substituição, de uso privado e de controle contam como ruins ({m['frac_ruins']})")
        ok("imagem" in pg["6"]["marcas"] and pg["6"]["escaneada"], f"6c. escaneada com o texto só no alto: imagem (cobertura {pg['6'].get('cobertura_texto')})")
        ok(pg["7"]["marcas"] == [] and pg["7"]["escaneada"], f"6d. escaneada com o texto pela página toda: nada a conferir (veio {pg['7']['marcas']}, cobertura {pg['7'].get('cobertura_texto')})")
        ok("tabela" in pg["8"]["marcas"], f"6e. a tabela sem grade, pelos números, sai tabela (números {pg['8'].get('frac_numeros')})")
        md = (saida / "obra-teste.md").read_text(encoding="utf-8")
        ok("<!-- página 3 -->" in md and "<!-- página 5 -->" in md, "7. o .md marca cada página")
        ok("\nL1| " in md, "8. com --numerar, as linhas levam o número dentro da página")
        imgs = sorted(p.name for p in (saida / "paginas").glob("*.png"))
        ok(imgs == ["obra-teste-p0002.png", "obra-teste-p0003.png", "obra-teste-p0004.png", "obra-teste-p0005.png",
                    "obra-teste-p0006.png", "obra-teste-p0008.png"],
           f"9. só as páginas marcadas viram imagem, e a só citada não (vieram {imgs})")
        ok(dados["resumo"]["paginas_marcadas"] == 7 and dados["resumo"]["imagens_geradas"] == 6
           and dados["resumo"]["paginas_escaneadas"] == 2, "10. o resumo conta as marcadas e as imagens")
        # faixa e código 0
        saida2 = tmp / "out2"
        cod2 = extrai_pdf.main([str(pdf), "--saida", str(saida2), "--paginas", "1", "--sem-render"])
        ok(cod2 == 0, "11. só a página limpa, sem ficha: código 0")
        ok(not (saida2 / "paginas").exists(), "12. --sem-render não gera imagem")
        # entrada inexistente
        ok(extrai_pdf.main([str(tmp / "nao-existe.pdf"), "--saida", str(tmp / "x")]) == 2, "13. PDF que não existe: código 2")
        # o motor pdftotext, quando existe
        if shutil.which("pdftotext"):
            saida3 = tmp / "out3"
            extrai_pdf.main([str(pdf), "--saida", str(saida3), "--motor", "pdftotext"])
            d3 = json.loads((saida3 / "obra-teste.pontos.json").read_text(encoding="utf-8"))
            ok(d3["resumo"]["motor"] == "pdftotext" and "sem_texto" in d3["paginas"]["2"]["marcas"]
               and d3["resumo"]["aviso"], "14. o pdftotext lê o texto, marca a vazia e avisa o que não faz")
            # o PDF corrompido no pdftotext é erro (código 2), e não página vazia
            ruim = tmp / "ruim.pdf"
            ruim.write_bytes(b"%PDF-1.4\nisto nao e um pdf\n")
            ok(extrai_pdf.main([str(ruim), "--saida", str(tmp / "out-ruim"), "--motor", "pdftotext",
                                "--paginas", "1"]) == 2, "15. PDF corrompido no pdftotext: código 2")
        else:
            print("pulado 14 e 15. pdftotext ausente")
        # sem o PyMuPDF, o --motor auto para (código 2), e só segue com --aceitar-pdftotext, avisando no topo
        guardado = extrai_pdf.pymupdf
        try:
            extrai_pdf.pymupdf = None
            ok(extrai_pdf.main([str(pdf), "--saida", str(tmp / "out4")]) == 2, "16. auto sem o PyMuPDF: código 2")
            if shutil.which("pdftotext"):
                extrai_pdf.main([str(pdf), "--saida", str(tmp / "out5"), "--aceitar-pdftotext"])
                topo = (tmp / "out5" / "obra-teste.pontos.md").read_text(encoding="utf-8")
                ok("não vale como conferência" in topo, "17. com --aceitar-pdftotext, o .pontos.md avisa no topo")
        finally:
            extrai_pdf.pymupdf = guardado
        # a rodada nova na mesma pasta apaga as imagens antigas do mesmo PDF
        (saida / "paginas" / "obra-teste-p0099.png").write_bytes(b"velho")
        extrai_pdf.main([str(pdf), "--saida", str(saida), "--dpi", "40"])
        ok(not (saida / "paginas" / "obra-teste-p0099.png").exists(), "18. as imagens antigas do mesmo PDF saem")
        # outro PDF de mesmo nome, noutra pasta, não sobrescreve a saída do primeiro
        outra = tmp / "outra"
        outra.mkdir()
        shutil.copy(pdf, outra / "obra-teste.pdf")
        extrai_pdf.main([str(outra / "obra-teste.pdf"), "--saida", str(saida), "--sem-render"])
        nomes = sorted(p.name for p in saida.glob("obra-teste*.pontos.json"))
        ok(len(nomes) == 2, f"19. o mesmo nome noutra pasta ganha sufixo (vieram {nomes})")
        # a página girada: a cobertura do texto é a mesma da página sem rotação
        cob = {}
        for rot in (0, 90):
            g = tmp / f"girada{rot}.pdf"
            d = pymupdf.open()
            p = d.new_page()
            p.insert_textbox(pymupdf.Rect(50, 50, 550, 800), LOREM * 6, fontsize=11)
            p.set_rotation(rot)
            d.save(str(g))
            d.close()
            extrai_pdf.main([str(g), "--saida", str(tmp / f"out-g{rot}"), "--sem-render"])
            cob[rot] = json.loads((tmp / f"out-g{rot}" / f"girada{rot}.pontos.json").read_text(encoding="utf-8"))["paginas"]["1"]["cobertura_texto"]
        ok(cob[0] > 0.1 and abs(cob[0] - cob[90]) < 0.01, f"20. a página girada mantém a cobertura (0°: {cob[0]}, 90°: {cob[90]})")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("TODOS OK" if not falhas else f"{len(falhas)} FALHA(S)")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
