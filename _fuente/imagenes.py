# Recorta la foto de cada imagen original (_fuente/imagenes/) y le aplica el tratamiento de marca:
# monocromo cálido (tinta → papel) para que el único color de la web sean los acentos azul cielo y lavanda.
# Uso: python3 _fuente/imagenes.py  → genera img/<caso>.jpg (800×800; la web los recorta en círculo).
import os
from PIL import Image, ImageOps, ImageEnhance
D = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(os.path.dirname(D), "img")
# caso: (centro x, centro y, radio) del recorte sobre la imagen original de 1672×941
CROPS = {"caso-energia": (1225, 350, 260), "caso-ia": (1140, 610, 270), "caso-farma": (1200, 560, 300),
         "caso-ong": (1200, 395, 305), "caso-diabetes": (1250, 400, 300)}
os.makedirs(OUT, exist_ok=True)
for slug, (cx, cy, r) in CROPS.items():
    im = Image.open(os.path.join(D, "imagenes", slug + ".png")).convert("RGB").crop((cx-r, cy-r, cx+r, cy+r)).resize((800, 800), Image.LANCZOS)
    g = ImageEnhance.Contrast(ImageOps.autocontrast(ImageOps.grayscale(im), cutoff=1)).enhance(1.08)
    ImageOps.colorize(g, black=(24, 23, 22), white=(246, 244, 238), mid=(138, 134, 126)).save(os.path.join(OUT, slug + ".jpg"), quality=82, optimize=True, progressive=True)
print("ok")
