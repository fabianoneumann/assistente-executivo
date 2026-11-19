"""Converte XML JATS (PMC / Europe PMC) em markdown simples para a seção "Texto integral".

Uso: python -I -X utf8 jats2md.py entrada.xml saida.md [nivel_base]
- títulos de seção como cabeçalhos markdown a partir de nivel_base (padrão 3: ###)
- parágrafos numa linha só; listas com "- "; tabelas como tabela markdown (rowspan e colspan viram células vazias)
- MathML linearizado (frações como (a)/(b), índices com _ e ^)
- sub/sup do texto como _x e ^x; itálico e negrito sem marcação
- figuras só pela legenda; referências uma por linha
- a seção "Associated Data" (acréscimo do PMC, repete o material suplementar) fica de fora
"""
import re
import sys
import xml.etree.ElementTree as ET

MML = "{http://www.w3.org/1998/Math/MathML}"
XLINK = "{http://www.w3.org/1999/xlink}"
BLOCKS = ("table-wrap", "fig", "list", "disp-formula", "disp-quote")


def local(tag):
    return tag.split("}", 1)[1] if "}" in tag else tag


def ws(s):
    return re.sub(r"\s+", " ", s or "").strip()


def math_text(el):
    t = local(el.tag)
    kids = list(el)
    if t in ("mi", "mn", "mo", "mtext", "ms"):
        return (el.text or "").strip()
    if t == "mfrac" and len(kids) == 2:
        return f"({math_text(kids[0])})/({math_text(kids[1])})"
    if t == "msub" and len(kids) == 2:
        return f"{math_text(kids[0])}_{math_text(kids[1])}"
    if t == "msup" and len(kids) == 2:
        return f"{math_text(kids[0])}^{math_text(kids[1])}"
    if t == "msubsup" and len(kids) == 3:
        return f"{math_text(kids[0])}_{math_text(kids[1])}^{math_text(kids[2])}"
    if t == "msqrt":
        return "√(" + " ".join(math_text(k) for k in kids) + ")"
    if t in ("munder", "mover", "munderover"):
        p = [math_text(k) for k in kids]
        if t == "munder":
            return f"{p[0]}_{{{p[1]}}}"
        if t == "mover":
            return f"{p[0]}^{{{p[1]}}}"
        return f"{p[0]}_{{{p[1]}}}^{{{p[2]}}}"
    if t == "mfenced":
        return "(" + ", ".join(math_text(k) for k in kids) + ")"
    return " ".join(x for x in (math_text(k) for k in kids) if x)


def inline(el):
    out = [el.text or ""]
    for k in el:
        t = local(k.tag)
        if t == "math" or k.tag.startswith(MML):
            out.append(" " + math_text(k) + " ")
        elif t == "inline-formula":
            m = [c for c in k.iter() if local(c.tag) == "math"]
            out.append(" " + (math_text(m[0]) if m else inline(k)) + " ")
        elif t == "xref" and k.get("ref-type") == "fn":
            out.append("^" + inline(k))
        elif t == "sub":
            out.append("_" + inline(k))
        elif t == "sup":
            out.append("^" + inline(k))
        elif t == "ext-link" and k.get("ext-link-type") == "google-scholar":
            pass
        elif t in ("ext-link", "uri"):
            txt = inline(k)
            href = k.get(XLINK + "href")
            out.append(txt if not href or href in txt else f"{txt} ({href})")
        elif t in ("fn",) + BLOCKS:
            pass
        else:
            out.append(inline(k))
        out.append(k.tail or "")
    return "".join(out)


def tidy(s):
    s = ws(s)
    s = re.sub(r"\s+([,.;:)\]])", r"\1", s)
    s = re.sub(r"([(\[])\s+", r"\1", s)
    return s


class Conv:
    def __init__(self, base):
        self.base = base
        self.lines = []

    def para(self, s):
        s = tidy(s)
        if s:
            self.lines += [s, ""]

    def heading(self, level, s):
        s = ws(s)
        if s:
            self.lines += ["#" * min(level, 6) + " " + s, ""]

    def table(self, tw):
        label = tw.find("label")
        cap = tw.find("caption")
        head = " ".join(x for x in [ws(inline(label)) if label is not None else "", ws(" ".join(inline(c) for c in cap)) if cap is not None else ""] if x)
        if head:
            self.para("**" + head + "**")
        for tb in tw.iter():
            if local(tb.tag) != "table":
                continue
            rows = []
            pending = {}
            for tr in tb.iter():
                if local(tr.tag) != "tr":
                    continue
                cells = []
                col = 0
                tds = [td for td in tr if local(td.tag) in ("td", "th")]
                i = 0
                while i < len(tds) or col in pending:
                    if col in pending:
                        rem = pending[col]
                        cells.append("")
                        if rem > 1:
                            pending[col] = rem - 1
                        else:
                            del pending[col]
                        col += 1
                        continue
                    td = tds[i]
                    i += 1
                    txt = tidy(inline(td)).replace("|", "\\|")
                    cs = int(td.get("colspan", "1"))
                    rs = int(td.get("rowspan", "1"))
                    for j in range(cs):
                        cells.append(txt if j == 0 else "")
                        if rs > 1:
                            pending[col] = rs - 1
                        col += 1
                rows.append(cells)
            if not rows:
                continue
            n = max(len(r) for r in rows)
            rows = [r + [""] * (n - len(r)) for r in rows]
            self.lines.append("| " + " | ".join(rows[0]) + " |")
            self.lines.append("|" + "---|" * n)
            for r in rows[1:]:
                self.lines.append("| " + " | ".join(r) + " |")
            self.lines.append("")
        foot = tw.find("table-wrap-foot")
        if foot is not None:
            for p in foot.iter():
                if local(p.tag) == "p":
                    self.para(inline(p))

    def refs(self, k):
        for ref in k.iter():
            if local(ref.tag) != "ref":
                continue
            lab = ref.find("label")
            cs = [x for x in ref.iter() if local(x.tag) == "named-content" and x.get("content-type") == "citation-string"]
            if cs:
                txt = tidy(inline(cs[0]))
            else:
                cit = [x for x in ref if local(x.tag) in ("mixed-citation", "element-citation", "citation")]
                txt = tidy(" ".join(inline(x) for x in cit)) if cit else tidy(inline(ref))
            self.lines.append("- " + (f"{ws(lab.text)} " if lab is not None and lab.text else "") + txt)
        self.lines.append("")

    def fig(self, f):
        label = f.find("label")
        cap = f.find("caption")
        parts = [ws(inline(label))] if label is not None else []
        if cap is not None:
            parts += [ws(inline(c)) for c in cap]
        self.para("**[Figura]** " + " ".join(p for p in parts if p))

    def block(self, el, level):
        t = local(el.tag)
        if t == "ref-list":
            title = el.find("title")
            if title is not None:
                self.heading(level, inline(title))
            self.refs(el)
            return
        if t == "sec":
            title = el.find("title")
            if title is not None and ws(inline(title)) == "Associated Data":
                return
            if title is not None:
                self.heading(level, inline(title))
            for k in el:
                if local(k.tag) not in ("title", "label"):
                    self.block(k, level + 1)
        elif t == "p":
            self.para(inline(el))
            for k in el:
                if local(k.tag) in BLOCKS:
                    self.block(k, level)
        elif t == "list":
            for li in el:
                if local(li.tag) == "list-item":
                    self.lines.append("- " + " ".join(tidy(inline(p)) for p in li if local(p.tag) == "p"))
            self.lines.append("")
        elif t == "table-wrap":
            self.table(el)
        elif t == "fig":
            self.fig(el)
        elif t == "disp-formula":
            label = el.find("label")
            m = [c for c in el.iter() if local(c.tag) == "math"]
            s = math_text(m[0]) if m else ws(inline(el))
            self.para(s + (f"   ({ws(label.text)})" if label is not None else ""))
        elif t == "disp-quote":
            for p in el:
                if local(p.tag) == "p":
                    self.para("> " + tidy(inline(p)))
        elif t == "supplementary-material":
            label = el.find("label")
            cap = el.find("caption")
            txt = " ".join(x for x in [ws(inline(label)) if label is not None else "", ws(" ".join(inline(c) for c in cap)) if cap is not None else ""] if x)
            self.para("**[Material suplementar]** " + txt)
        elif t == "fn-group":
            for fn in el.iter():
                if local(fn.tag) == "fn":
                    lab = fn.find("label")
                    txt = " ".join(tidy(inline(p)) for p in fn if local(p.tag) == "p")
                    self.para((ws(lab.text) + " " if lab is not None and lab.text else "") + txt)
        elif t in ("title", "label", "object-id"):
            pass
        else:
            for k in el:
                self.block(k, level)


def main():
    src, dst = sys.argv[1], sys.argv[2]
    base = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    root = ET.parse(src).getroot()
    c = Conv(base)
    meta = root.find("front/article-meta")
    corpo = root.find("body")
    if meta is None or corpo is None:  # registro só com resumo ou metadados: não há texto integral para converter
        sys.exit(f"{src}: sem front/article-meta ou sem body; o XML não traz o texto integral")
    titulo = meta.find("title-group/article-title")
    c.para("**" + (ws(inline(titulo)) if titulo is not None else "(sem título no XML)") + "**")
    names = []
    for cg in meta.iter():
        if local(cg.tag) != "contrib-group" or cg.get("content-type") not in (None, "author"):
            continue
        for ct in cg:
            if local(ct.tag) == "contrib" and ct.get("contrib-type", "author") == "author":
                n = ct.find("name")
                if n is not None:
                    names.append(ws(" ".join(x.text or "" for x in [n.find("given-names"), n.find("surname")] if x is not None)))
    c.para(", ".join(names))
    for ab in meta.findall("abstract"):
        c.heading(base, "Abstract")
        for k in ab:
            c.block(k, base + 1)
    for k in corpo:
        c.block(k, base)
    back = root.find("back")
    if back is not None:
        for k in back:
            if local(k.tag) == "ref-list" and k.find("title") is None:
                c.heading(base, "References")
            if local(k.tag) == "fn-group" and k.find("title") is None:
                c.heading(base, "Notes")
            c.block(k, base)
    text = "\n".join(c.lines).rstrip() + "\n"
    with open(dst, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(dst, len(text))


if __name__ == "__main__":
    main()
