# Ilustraciones de los dos casos nuevos (23 nov 2026), mismo estilo que imagenes-anonimas.py
# Ejecutar desde la raíz del repositorio: python3 _fuente/imagenes-decisiones.py
from PIL import Image, ImageDraw
import random, math
SS=3; N=800*SS
CREAM=(244,239,227); INK=(22,22,22); COB=(34,52,196); VIO=(141,108,240); LIGHT=(214,221,255)
def canvas(): im=Image.new("RGB",(N,N),CREAM); return im, ImageDraw.Draw(im)
def save(im,name): im.resize((800,800),Image.LANCZOS).save(f"img/{name}.jpg",quality=88)
def P(x): return int(x*SS)

# 6 promesa: un bocadillo que promete algo abierto y, al otro lado, una caja cerrada en rejilla
im,d=canvas()
d.rounded_rectangle([P(80),P(170),P(380),P(380)],radius=P(26),outline=INK,width=P(5),fill=LIGHT)
d.polygon([(P(150),P(378)),(P(130),P(470)),(P(230),P(378))],fill=LIGHT,outline=INK)
d.line([P(150),P(380),P(130),P(470),P(230),P(380)],fill=INK,width=P(5),joint="curve")
d.ellipse([P(175),P(220),P(285),P(330)],outline=COB,width=P(8))
d.ellipse([P(207),P(252),P(253),P(298)],fill=COB)
for k in range(3):  # trazo discontinua de la promesa a la caja
    x=410+k*44; d.line([P(x),P(330+k*30),P(x+26),P(346+k*30)],fill=VIO,width=P(6))
d.rounded_rectangle([P(470),P(380),P(730),P(640)],radius=P(10),outline=INK,width=P(5),fill=(250,247,240))
for i in range(3):
    for j in range(3):
        x=490+i*80; y=400+j*80
        d.rounded_rectangle([P(x),P(y),P(x+62),P(y+62)],radius=P(6),fill=(VIO if (i,j)==(1,1) else (236,231,219)),outline=INK,width=P(3))
d.rectangle([P(470),P(380),P(730),P(392)],fill=INK)
save(im,"caso-promesa")

# 7 equipo de producto: una lupa que gira una interrogación sobre una rejilla de producto
im,d=canvas(); r=random.Random(7)
for i in range(4):
    for j in range(4):
        x=110+i*120; y=130+j*120
        d.rounded_rectangle([P(x),P(y),P(x+96),P(y+96)],radius=P(8),outline=INK,width=P(3),fill=(LIGHT if r.random()<.25 else CREAM))
cx,cy,R=470,430,150
d.ellipse([P(cx-R),P(cy-R),P(cx+R),P(cy+R)],fill=(250,247,240),outline=INK,width=P(7))
d.line([P(cx+R*0.72),P(cy+R*0.72),P(cx+R*1.55),P(cy+R*1.55)],fill=INK,width=P(22))
d.arc([P(cx-70),P(cy-95),P(cx+70),P(cy+30)],start=180,end=40,fill=COB,width=P(14))
d.line([P(cx+52),P(cy-12),P(cx),P(cy+30),P(cx),P(cy+50)],fill=COB,width=P(14),joint="curve")
d.ellipse([P(cx-12),P(cy+70),P(cx+12),P(cy+94)],fill=COB)
d.arc([P(cx-120),P(cy-120),P(cx+120),P(cy+120)],start=200,end=300,fill=VIO,width=P(6))
d.polygon([(P(cx+20),P(cy-132)),(P(cx-8),P(cy-108)),(P(cx-4),P(cy-140))],fill=VIO)
save(im,"caso-producto")
print("ok")
