# -*- coding: utf-8 -*-
import numpy as np
from matplotlib.colors import LinearSegmentedColormap as Lisecama
from skimage import io

def norm(x):
    return (x-x.min())/(x.max()-x.min())

def frama(kn,al):
    cs = 1.
    kna = 2
    am = np.random.uniform(-cs,cs,[2,2])
    while(kna < kn):
        cs /= al
        am_lk = np.roll(am,-1,1)
        am_ll = np.roll(am,-1,0)
        am_lkl = np.roll(am_ll,-1,1)
        ac = (am+am_lk+am_ll+am_lkl)/4 + np.random.uniform(-cs,cs,[kna,kna])
        ac_ls = np.roll(ac,1,1)
        ac_lb = np.roll(ac,1,0)
        amm = np.empty([kna*2,kna*2])
        amm[0::2,0::2] = am
        amm[1::2,1::2] = ac
        amm[0::2,1::2] = (am+am_lk+ac+ac_lb)/4 + np.random.uniform(-cs,cs,[kna,kna])
        amm[1::2,0::2] = (am+am_ll+ac+ac_ls)/4 + np.random.uniform(-cs,cs,[kna,kna])
        am = amm
        kna *= 2
    return am

n = 1024
n1 = 1024*4
nn = 4
x,y = np.meshgrid(np.arange(1,n1+1),np.arange(1,n+1))
cc = []
for i in range(nn):
    c = np.random.normal(1,0.4,[n,n1]).cumsum(0)
    c += np.random.normal(0.1*(i-1.5),0.8,[n,n1]).cumsum(1)
    c -= 0.1*(i-1.5)*n
    c += np.sin(x*2*np.pi/(n/16.))*n/5.
    cc.append(c)
c = np.vstack(cc)
fra = frama(n1,1)
c += fra[:n*nn,:n1]*200
c -= c.mean()
c = np.arctan(c/100)
c = norm(c)
si = [[0.02,0.12,0.05],[0.8,0.6,0.3]]
cmap = Lisecama.from_list('',si)
z = cmap(c)
x,y = np.meshgrid(np.arange(1,n1+1),np.arange(1,n*nn+1))
rongit = np.maximum((np.cos(x*2*np.pi/(n/4.)+(np.sin(y*2*np.pi/(n/8.))>0)*n/2.))>0.995,
                    np.where(np.cos(y*2*np.pi/n)>0.999,0,(np.cos(y*2*np.pi/(n/16.)))>0.95))
rongit = rongit*np.random.uniform(0.5,1,[n1,n1])
rongit = (rongit[:,:,None]*np.array([1,1,1,1]))
z = np.where(rongit,rongit,z)
io.imsave('lai_phanangit.jpg',z)

z1 = np.minimum((-np.cos(x*2*np.pi/(n/4.)+(np.sin(y*2*np.pi/(n/8.))>0)*n/2.)),-0.99)
z2 = np.minimum((-np.cos(y*2*np.pi/(n/16.))),-0.9)
z1 = norm(z1)
z2 = norm(z2)
fr = fra[::-1,::-1][:n*nn,:n1]
fr = norm(fr)
z = np.minimum(z1,z2)*fr
io.imsave('nun_phanangit.jpg',z)

fra = norm(frama(512,1))
x,y = np.meshgrid(np.arange(1,512+1),np.arange(1,512+1))
z = cmap(fra)
rongit = np.maximum((np.cos(x*2*np.pi/256.+(np.sin(y*2*np.pi/256.)>0)*n/2.))>0.999,
                    np.cos(y*2*np.pi/128.)>0.998)
rongit = rongit*np.random.uniform(0.5,1,[512,512])
rongit = (rongit[:,:,None]*np.array([1,1,1,1]))
z = np.where(rongit,rongit,z)
io.imsave('lai_phuenit.jpg',z)

z1 = np.minimum((-np.cos(x*2*np.pi/256+(np.sin(y*2*np.pi/256.)>0)*n/2.)),-0.998)
z2 = np.minimum((-np.cos(y*2*np.pi/128.)),-0.995)
z1 = norm(z1)
z2 = norm(z2)
z = np.minimum(z1,z2)*fra[::-1,::-1]
io.imsave('nun_phuenit.jpg',z)

n = 1024
x,y = np.meshgrid(np.arange(1,n+1),np.arange(1,n+1))
fra = norm(frama(n,1))
cmap = Lisecama.from_list('',[[0.76,0.73,0.65],[1,0.96,0.83]])
z = cmap(fra)
io.imsave('lai_than.jpg',z)

rongit = np.maximum((np.cos(x*2*np.pi/256.+(np.sin(y*2*np.pi/256.)>0)*n/2.))>0.999,
                    np.cos(y*2*np.pi/128.)>0.998)
rongit = rongit*np.random.uniform(0.5,1,[n,n])
rongit = (rongit[:,:,None]*np.array([1,1,1,1]))
z = np.where(rongit,rongit,z[::-1,::-1])
io.imsave('lai_thanit.jpg',z)

fra = norm(frama(n,1))
z = fra
io.imsave('nun_than.jpg',z)

z1 = np.minimum((-np.cos(x*2*np.pi/256+(np.sin(y*2*np.pi/256.)>0)*n/2.)),-0.998)
z2 = np.minimum((-np.cos(y*2*np.pi/128.)),-0.995)
z1 = norm(z1)
z2 = norm(z2)
z = np.minimum(z1,z2)*fra[::-1,::-1]
io.imsave('nun_thanit.jpg',z)

def k(x,a,tau,b):
    x1,x2 = np.meshgrid(x,x)
    return a**2*np.exp(-np.sin((x1-x2)*np.pi/tau)**2/2) + a**2*np.exp(-np.sin((x1-x2)*np.pi/tau*b)**2/2)

n = 1024
x = np.linspace(0,n,n,0)
v1 = k(x,1,n,10)
z1 = np.random.multivariate_normal(np.zeros(n),v1)
v2 = k(x,1,n,4)
z2 = np.random.multivariate_normal(np.zeros(n),v2)
cmap = Lisecama.from_list('',[[0,0,0],[0.36,0.17,0.17]])
z = norm(z1+z2[:,None])
io.imsave('nun_ruamai.jpg',z)

n = 1024
u,v = np.meshgrid(np.arange(0.,n),np.arange(0.,n))
z = np.random.normal(0,1,[n,n])
z = z.cumsum(0)
z += np.linspace(0,1,1024,0)[::-1][:,None]*z[-1]
z -= z.mean(0)
z = norm(z)
si = [[0.28,0.18,0.14],[0.14,0.09,0.07]]
cmap = Lisecama.from_list('',si)
z = cmap(z)
io.imsave('lai_mai.jpg',z)

n = 1024
u,v = np.meshgrid(np.arange(0.,n),np.arange(0.,n))
z = np.random.normal(0,1,[n,n])
z = z.cumsum(0)
z += np.linspace(0,1,1024,0)[::-1][:,None]*z[-1]
z -= z.mean(0)
z = norm(z)
io.imsave('nun_mai.jpg',z)