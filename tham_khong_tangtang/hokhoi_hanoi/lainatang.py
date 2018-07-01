import numpy as np
import matplotlib.pyplot as plt
from skimage import io

def hakmum(x):
    return np.minimum(1,2-x*2)

def rabaichut(a,xy,s,r,d=1,f=None):
    x,y = xy
    aa = a[max(0,y-r):y+r,max(0,x-r):x+r]
    rr = np.stack(np.meshgrid(range(a.shape[1]),range(a.shape[0])),2)
    rr = rr-xy
    rr = rr[max(0,y-r):y+r,max(0,x-r):x+r]
    rr = np.sqrt((rr**2).sum(2))
    if(f):
        dd = f(rr/r)
    else:
        dd = rr/r<1
    dd = np.maximum(0,dd*d)
    if(a.ndim==3):
        dd = dd[:,:,None]
    aa[:] = aa*(1-dd)+s*(dd)

def laklaisen(a,xy,s,r,d=1,f=None):
    dd = 0
    for xy_ in xy:
        xy1,xy2 = xy_
        x1,y1 = xy1
        x2,y2 = xy2
        yao = max(np.abs(np.array(xy1)-np.array(xy2)))
        for i in np.arange(yao):
            i = float(i)
            x = x1+int((x2-x1)*i/yao)
            y = y1+int((y2-y1)*i/yao)
            z = np.zeros_like(a)
            rabaichut(z,[x,y],1,r,1,f)
            dd = np.maximum(z,dd)
    dd *= d
    if(a.ndim==3):
        dd = dd[:,:,None]
    a[:] = a*(1-dd)+s*dd

n = 512
s = np.zeros([n,n])
chutsen = [
    [[30,236],[482,236]],
    [[30,276],[482,276]],
    [[30,236],[30,276]],
    [[482,236],[482,276]],
    [[256,0],[256,196]],
    [[256,316],[256,512]],
    [[30,256],[0,256]],
    [[482,256],[512,256]],
    
    [[30,196],[482,196]],
    [[30,196],[30,166]],
    [[482,196],[482,166]],
    [[30,166],[166,30]],
    [[346,30],[482,166]],
    [[166,30],[216,30]],
    [[346,30],[296,30]],
    [[216,30],[216,156]],
    [[296,30],[296,156]],
    [[216,156],[100,156]],
    [[296,156],[412,156]],
    [[100,156],[176,80]],
    [[412,156],[336,80]],
    
    [[30,316],[482,316]],
    [[30,512-196],[30,512-166]],
    [[482,512-196],[482,512-166]],
    [[30,512-166],[166,512-30]],
    [[346,512-30],[482,512-166]],
    [[166,512-30],[216,512-30]],
    [[346,512-30],[296,512-30]],
    [[216,512-30],[216,512-156]],
    [[296,512-30],[296,512-156]],
    [[216,512-156],[100,512-156]],
    [[296,512-156],[412,512-156]],
    [[100,512-156],[176,512-80]],
    [[412,512-156],[336,512-80]],
]
'''
laklaisen(s,chutsen,1,12,1,hakmum)
u,v = np.meshgrid(np.arange(n),np.arange(n))
#s[np.sqrt((u-256)**2+(v-256)**2)>256] = 1
w = np.maximum((np.sin((u+v)/2)**2),(np.sin((u-v)/2)**2))
v = np.tile([73,82,78],[n,n,1])*(np.random.uniform(0.5,1,[n,n])*w)[:,:,None]
z = np.tile([117,43,43],[n,n,1])
z[s==0] = v[s==0]
s[s==0] = ((w-0.5)/5)[s==0]
io.imsave('lai_bannatang.png',z)
io.imsave('nun_bannatang.png',s)'''

mum = np.linspace(0,np.pi*2,16,0)
x = 256*(1+np.cos(mum)[:,None]*np.array([0.25,1]))
y = 256*(1+np.sin(mum)[:,None]*np.array([0.25,1]))
chutsen = np.stack([x,y],2).astype(int)
s = np.ones([n,n])
laklaisen(s,chutsen,0,3,1,hakmum)
io.imsave('nun_khopnatang.png',s)