# Ilustraciones neutras para la versión anónima de los casos (23 nov 2026): sin fotos que sugieran sector
from PIL import Image, ImageDraw
import random, math
SS=3; N=800*SS
CREAM=(244,239,227); INK=(22,22,22); COB=(34,52,196); VIO=(141,108,240); LIGHT=(214,221,255)
def canvas(): im=Image.new("RGB",(N,N),CREAM); return im, ImageDraw.Draw(im)
def save(im,name): im.resize((800,800),Image.LANCZOS).save(f"img/{name}.jpg",quality=88)
def P(x): return int(x*SS)
def phone(d,x,y,w,h):
    d.rounded_rectangle([P(x),P(y),P(x+w),P(y+h)],radius=P(36),outline=INK,width=P(5),fill=(250,247,240))
    d.rounded_rectangle([P(x+w/2-40),P(y+18),P(x+w/2+40),P(y+28)],radius=P(5),fill=INK)
# 1 relación: dos nodos unidos por muchos hilos
im,d=canvas(); r=random.Random(1)
a=(230,420); b=(570,380)
for k in range(26):
    off=r.uniform(-170,170); col=COB if k%3 else VIO
    pts=[]
    for t in [i/40 for i in range(41)]:
        x=a[0]+(b[0]-a[0])*t; y=a[1]+(b[1]-a[1])*t+math.sin(t*math.pi)*off
        pts.append((P(x),P(y)))
    d.line(pts,fill=col,width=P(2.2))
for (x,y),c in ((a,COB),(b,VIO)):
    d.ellipse([P(x-62),P(y-62),P(x+62),P(y+62)],fill=CREAM,outline=INK,width=P(5))
    d.ellipse([P(x-30),P(y-30),P(x+30),P(y+30)],fill=c)
save(im,"caso-relacion")
# 2 web: muchas piezas sueltas que pasan a tres bloques
im,d=canvas(); r=random.Random(2)
for i in range(32):
    x=80+(i%4)*62+r.uniform(-8,8); y=150+(i//4)*62+r.uniform(-8,8)
    d.rounded_rectangle([P(x),P(y),P(x+48),P(y+40)],radius=P(6),outline=INK,width=P(3),fill=(LIGHT if r.random()<.3 else CREAM))
d.line([P(360),P(400),P(470),P(400)],fill=COB,width=P(6)); d.line([P(450),P(380),P(472),P(400),P(450),P(420)],fill=COB,width=P(6),joint="curve")
for j,c in enumerate((COB,VIO,LIGHT)):
    d.rounded_rectangle([P(510),P(190+j*150),P(720),P(310+j*150)],radius=P(10),fill=c,outline=INK,width=P(4))
save(im,"caso-web")
# 3 IA: tablero con pósits por columnas
im,d=canvas(); r=random.Random(3)
d.rounded_rectangle([P(90),P(110),P(710),P(690)],radius=P(10),outline=INK,width=P(4),fill=(250,247,240))
for cx in range(5):
    x0=120+cx*118
    d.line([P(x0-8),P(140),P(x0-8),P(660)],fill=(200,195,185),width=P(2)) if cx else None
    for k in range(r.randint(3,5)):
        c=r.choice([COB,VIO,LIGHT,LIGHT,(236,231,219)]); x=x0+r.uniform(-4,10); y=150+k*100+r.uniform(-6,6)
        im2=Image.new("RGBA",(P(90),P(80)),(0,0,0,0)); dd=ImageDraw.Draw(im2); dd.rectangle([0,0,P(90),P(80)],fill=c+(255,))
        im2=im2.rotate(r.uniform(-6,6),expand=True,resample=Image.BICUBIC); im.paste(im2,(P(x),P(y)),im2)
save(im,"caso-ia")
# 4 app: teléfono con un recorrido que vuelve sobre sí mismo
im,d=canvas()
phone(d,250,90,300,620)
pts=[]
for i in range(200):
    t=i/199; x=400+math.sin(t*math.pi*3)*95; y=190+t*430
    pts.append((P(x),P(y)))
d.line(pts,fill=COB,width=P(6),joint="curve")
for t,c in ((0,VIO),(.33,COB),(.66,VIO),(1,COB)):
    x=400+math.sin(t*math.pi*3)*95; y=190+t*430
    d.ellipse([P(x-18),P(y-18),P(x+18),P(y+18)],fill=c,outline=INK,width=P(3))
save(im,"caso-app")
# 5 prototipo: teléfono con marcas de evaluación
im,d=canvas()
phone(d,230,90,300,620)
for k in range(5):
    y=180+k*95
    d.rounded_rectangle([P(270),P(y),P(490),P(y+56)],radius=P(8),fill=LIGHT if k%2 else (236,231,219))
for k,(x,y) in enumerate(((520,200),(540,390),(515,580))):
    d.ellipse([P(x-32),P(y-32),P(x+32),P(y+32)],fill=COB if k!=1 else VIO)
    d.line([P(x-13),P(y+1),P(x-3),P(y+12),P(x+15),P(y-11)],fill=CREAM,width=P(6),joint="curve")
save(im,"caso-prototipo")
print("ok")
