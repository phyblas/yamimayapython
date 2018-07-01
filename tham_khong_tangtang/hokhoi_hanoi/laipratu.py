import numpy as np
from skimage import io

def norm(x):
    return (x-x.min())/(x.max()-x.min())

n = 1024
u,v = np.meshgrid(np.arange(n),np.arange(n))
z = np.tile([0,0,0.],[n,n,1])
z[:,325:1024-325] = [117,43,43]
z[:,511:513] = 0
s = np.ones([n,n])
for _ in 'aa':
    s = s[:,::-1]
    for i in range(5):
        for j in range(6,-1,-1):
            s[15+i*202-j:120+i*202+j,340-j:377+j] = j/6.
            s[15+i*202-j:120+i*202+j,392-j:428+j] = j/6.
            s[15+i*202-j:120+i*202+j,443-j:480+j] = j/6.
            s[135+i*202-j:202+i*202+j,340-j:402+j] = j/6.
            s[135+i*202-j:202+i*202+j,418-j:480+j] = j/6.
            
            s[:,511-j:512] = j/12.+0.5
        for j in range(12,-1,-1):
            s[462:562,500-j:501] = (j+1.)/13
w = np.maximum((np.sin((u+v)/2)**2),(np.sin((u-v)/2)**2))
v = np.tile([73,82,78],[n,n,1])*(np.random.uniform(0.5,1,[n,n])*w)[:,:,None]
v = v.astype(np.uint8)
r = np.random.normal(0,1,[n,n])
r = r.cumsum(0)
r += np.linspace(0,1,n,0)[::-1][:,None]*r[-1]
r -= r.mean(0)
r = norm(r)*0.2+0.8
z *= r[:,:,None]
z = z.astype(np.uint8)
z[s==0] = v[s==0]
s[s==0] = ((w-0.5)/5)[s==0]
s[:,511:513] = 0
io.imsave('lai_banpratu.png',z)
io.imsave('nun_banpratu.png',s)