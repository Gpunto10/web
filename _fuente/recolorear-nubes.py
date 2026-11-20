import numpy as np, sys
from PIL import Image
im=np.asarray(Image.open('img/nubes-azules.jpg').convert('RGB')).astype(float)/255
r,g,b=im[...,0],im[...,1],im[...,2]
# "nube": blanco/violeta frente a cielo turquesa (el cielo tiene mucho verde)
lum=.299*r+.587*g+.114*b
cloud=np.clip((b-g)*1.6+ (lum-.55)*1.2 +.45,0,1)
sky=np.clip((g-r-.08)/.18,0,1)
tc=np.clip(.42+(lum-.35)/.5*.58,0,1)
t=tc*(1-sky)+(.3+(lum-.7)*.3)*sky
stops=[(0,'1A2899'),(.38,'2234C4'),(.62,'8D6CF0'),(.82,'D6DDFF'),(1,'F4EFE3')]
def h(x): return np.array([int(x[i:i+2],16) for i in (0,2,4)])/255
out=np.zeros_like(im)
for (a,ca),(bb,cb) in zip(stops,stops[1:]):
    m=(t>=a)&(t<=bb); k=((t-a)/(bb-a))[...,None]
    out[m]=(h(ca)*(1-k)+h(cb)*k)[m]
Image.fromarray((out*255).astype('uint8')).save('img/nubes-cobalto.jpg',quality=86)
o=Image.open('img/nubes-cobalto.jpg');o.thumbnail((600,600));o.save(sys.argv[1])
