# Genera vistas previas (prueba-a/b/c.html) a partir de index.html con una capa CSS extra.
# No afecta a la web publicada: son páginas aparte, sin enlace desde la home y con noindex.
import os, re, hashlib
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(R, "index.html"), encoding="utf-8").read()
V = {"a": "A · Crema y calma", "b": "B · Color por secciones", "c": "C · Robusta", "d": "D · Mezcla A + C"}
def h(p): return hashlib.md5(open(os.path.join(R, p), "rb").read()).hexdigest()[:8]
for k, name in V.items():
    css = f"prueba-{k}.css"
    html = re.sub(r'(<link rel="stylesheet" href="styles\.css\?v=[^"]*">)',
                  rf'\1<link rel="stylesheet" href="{css}?v={h(css)}"><meta name="robots" content="noindex">', src, count=1)
    links = " ".join(
        (f'<b>{x.upper()}</b>' if x == k else f'<a href="prueba-{x}.html">{x.upper()}</a>') for x in V) \
        + ' <a href="index.html">Actual</a>'
    bar = f'<div class="pv-bar"><span>Vista previa {name}</span><nav>{links}</nav></div>'
    html = html.replace("</body>", bar + "</body>")
    open(os.path.join(R, f"prueba-{k}.html"), "w", encoding="utf-8").write(html)
print("ok")
