# Recorta la foto de cada imagen original (_fuente/imagenes/), sin el texto ni los adornos que traían.
# Uso: python3 _fuente/imagenes.py  → genera img/<caso>.jpg (800×800; la web los recorta en círculo).
import os
from PIL import Image, ImageOps, ImageEnhance
D = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(os.path.dirname(D), "img")
# caso: (centro x, centro y, radio) del recorte sobre la imagen original (las de ChatGPT miden 1672×941; la de la ONG, 1200×799)
CROPS = {"caso-energia": (1225, 350, 260), "caso-ia": (1140, 610, 270), "caso-farma": (1200, 560, 300),
         "caso-ong": (600, 440, 345), "caso-diabetes": (1250, 400, 300)}
os.makedirs(OUT, exist_ok=True)
for slug, (cx, cy, r) in CROPS.items():
    im = Image.open(os.path.join(D, "imagenes", slug + ".png")).convert("RGB").crop((cx-r, cy-r, cx+r, cy+r)).resize((800, 800), Image.LANCZOS)
    # En color (decisión de Gema, 17 nov 2026), con la saturación algo contenida para que las cinco convivan
    ImageEnhance.Color(im).enhance(0.88).save(os.path.join(OUT, slug + ".jpg"), quality=82, optimize=True, progressive=True)
print("ok")
