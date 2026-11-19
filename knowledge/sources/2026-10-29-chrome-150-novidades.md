---
titulo: "New in Chrome 150"
tipo: artigo
autor: "Rachel Andrew (Technical Writer, Chrome for Developers)"
url: "https://developer.chrome.com/blog/new-in-chrome-150"
publicado_em: 2026-06-30
capturado_em: 2026-10-29
licenca: "CC BY 4.0 para o texto e Apache 2.0 para os exemplos de código (rodapé da página: 'Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License')"
areas: [content-design]
tags: [css, chrome, text-fit, background-clip, focusgroup, browser-release, html-pieces]
---

Ficha de estudo em palavras próprias; o texto integral (licença CC BY 4.0) não vem neste repositório e se lê na url do frontmatter. Post curto do blog do Chrome para Desenvolvedores, publicado em 30/06/2026 (rodapé: "Last updated 2026-06-30 UTC"). Interessa aqui pelo `text-fit`, cuja referência completa está em [[2026-10-29-mdn-text-fit]]. Lido em 2026-10-29, na pesquisa sobre o layout das peças de tela fixa em HTML.

## O que traz

Os três destaques da versão 150 do Chrome; o resto fica nas notas de versão e no ChromeStatus.

- **`text-fit`:** muda o tamanho da fonte para o texto encher a largura da caixa que o contém, sem conta de `font-size` nem JavaScript; o post vende como tipografia responsiva que mantém o alinhamento em telas de tamanhos diferentes. Traz um exemplo no CodePen do web.dev.
- **`focusgroup`:** atributo HTML que dá navegação por setas, uma parada garantida no Tab e a memória do último item focado a widgets compostos (barra de ferramentas, por exemplo), no lugar dos scripts de `tabindex` móvel.
- **`background-clip: border-area`:** recorta o fundo do elemento na área pintada pela borda (considera largura e estilo da borda, ignora a transparência da cor), o que dá borda em degradê sem `border-image`.

## Para o nosso uso

Só o primeiro item toca as peças em HTML. O post não fala de Firefox nem de Safari; o suporte está na ficha do MDN.

---
