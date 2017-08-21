# -*- coding: utf-8 -*-
import maya.cmds as mc
import numpy as np
import math
import os

def svsf(r,h,chue):
    n = len(h)
    global sv,svt,sf,nv,nvt
    sv += 'v %.4f %.4f %.4f\n'%(0,0,0)
    for j in range(n):
        for theta in range(0,360,10):
            sv += 'v %.4f %.4f %.4f\n'%(math.sin(math.radians(theta))*r[j],h[j],math.cos(math.radians(theta))*r[j])
    sv += 'v %.4f %.4f %.4f\n'%(0,max(h),0)
    
    dv = ((np.diff([0]+h+[120])**2+np.diff([0]+r+[0])**2)**0.5).cumsum()
    dv = dv/dv.max()
    rmax = max(r)
    
    svt += 'vt %.4f %.4f\n'%(0.5,0)
    for j in range(n):
        for c in np.linspace(-0.5,0.5,37):
            svt += 'vt %.4f %.4f\n'%(0.5+c*r[j]/rmax,dv[j])
    svt += 'vt %.4f %.4f\n'%(0.5,1)
    
    sf += '\ns 1\ng %s\n'%chue
    for i in range(1,37):
        sf += 'f %d/%d %d/%d %d/%d\n'%(nv+1,nvt+1,nv+i%36+2,nvt+i+2,nv+i+1,nvt+i+1)
    for j in range(n-1):
        for i in range(1,37):
            sf += 'f %d/%d %d/%d %d/%d %d/%d\n'%(nv+j*36+i+1,nvt+j*37+i+1,nv+j*36+i%36+2,nvt+j*37+i+2,nv+(j+1)*36+i%36+2,nvt+(j+1)*37+i+2,nv+(j+1)*36+i+1,nvt+(j+1)*37+i+1)
    for i in range(1,37):
        sf += 'f %d/%d %d/%d %d/%d\n'%(nv+36*n+2,nvt+37*n+2,nv+36*(n-1)+i+1,nvt+37*(n-1)+i+1,nv+36*(n-1)+i%36+2,nvt+37*(n-1)+i+2)
    
    nv += 2+n*36
    nvt += 2+n*37

# สีผิวหินอ่อน
phiu_hinon = mc.shadingNode('blinn',asShader=1,n='phiu_hinon')
mc.setAttr(phiu_hinon+'.ambc',0.5,0.5,0.5,typ='double3')
mc.setAttr(phiu_hinon+'.sc',1,1,1,typ='double3')
mc.setAttr(phiu_hinon+'.sro',0.5)
lai = mc.shadingNode('marble',at=1)
mc.connectAttr(lai+'.oc',phiu_hinon+'.c')
for at,v in zip(['veinWidth','diffusion','contrast','amplitude','ripplesX','ripplesY','ripplesZ'],[0.01,0.5,0,1,0.8,0.8,0.8]):
    mc.setAttr(lai+'.'+at,v)
mc.setAttr(lai+'.fillerColor',1,0.89,0.715,typ='double3')
mc.setAttr(lai+'.veinColor',0.3,0.35,0.47,typ='double3')
ple = mc.shadingNode('place3dTexture',au=1)
mc.defaultNavigation(ce=1,s=ple,d=lai)
for at,v in zip(['tx','ty','sx','sy','sz'],[1.951,16.164,30,40,10]):
    mc.setAttr(ple+'.'+at,v)

phiu_kaoi = []
for i in range(6):
    phiu_kaoi.append(mc.duplicate(phiu_hinon)[0])
    mc.connectAttr(lai+'.oc',phiu_kaoi[i]+'.c')

sv = ''
svt = ''
sf = ''
nv = 0
nvt = 0

# โต๊ะ
r = [19,22.5,22.5,20,20]
h = [0,0.5,1.7,1.7,2]
for theta in range(18,91,18):
    theta = math.radians(theta)
    r.append(20-4*math.sin(theta))
    h.append(5-3*math.cos(theta))
for theta in range(18,91,18):
    theta = math.radians(theta)
    r.append(13+3*math.cos(theta))
    h.append(5+2*math.sin(theta))
r += [13,12.5,12.5]
h += [8,8,10]
for theta in range(0,91,30):
    theta = math.radians(theta)
    r.append(10.5+2*math.cos(theta))
    h.append(10+1*math.sin(theta))
r += [10.5,10,10,9.5,9.5]
h += [13,13,13.5,13.5,15]
for i in range(3):
    r += [10,10,9.5,9.5]
    h += [15.5+i*10,17.5+i*10,16+i*12,28+i*10]
for theta in range(0,91,9):
    theta = math.radians(theta)
    r.append(60-(60-10)*math.cos(theta))
    h.append(38+26*math.sin(theta))
r += [60]
h += [64.5]
for theta in range(0,181,30):
    theta = math.radians(theta)
    r.append(60+2.5*math.sin(theta))
    h.append(67-2.5*math.cos(theta))
r += [60]
h += [70]
svsf(r,h,'tohinon')



# เก้าอี้
r = [12,15.5,15.5,15,15]
h = [0,0.5,1.8,1.8,2]
for theta in range(18,91,18):
    theta = math.radians(theta)
    r.append(15-3*math.sin(theta))
    h.append(4-2*math.cos(theta))
for theta in np.arange(22.5,91,22.5):
    theta = math.radians(theta)
    r.append(10+2*math.cos(theta))
    h.append(4+math.sin(theta))
r += [10,9.5,9.5]
h += [5,5,7]
for theta in range(0,91,30):
    theta = math.radians(theta)
    r.append(8+math.cos(theta))
    h.append(7+2*math.sin(theta))
r += [8]
h += [9.5]
for theta in range(0,91,30):
    theta = math.radians(theta)
    r.append(6.5+math.cos(theta))
    h.append(9.5+3*math.sin(theta))
r += [6.5,6.3,6.3,6,6]
h += [13,13,13.5,13.5,16.5]
for i in range(3):
    r += [6.5,6.5,6,6]
    h += [17+i*7,19+i*7,19.5+i*7,23.5+i*7]
for theta in range(0,91,9):
    theta = math.radians(theta)
    r.append(17.5-(17.5-6.5)*math.cos(theta))
    h.append(37.5+2.5*math.sin(theta))
r += [17.5]
h += [40.5]
for theta in range(0,181,30):
    theta = math.radians(theta)
    r.append(17.5+1.5*math.sin(theta))
    h.append(42-1.5*math.cos(theta))
r += [17.5]
h += [44]
svsf(r,h,'kaoihinon')

# เขียนไฟล์ .obj เสร็จแล้วอ่าน แล้วก็ลบ
with open('tohinon.obj','w') as f:
    f.write(sv+'\n'+svt+'\n'+sf)
o = mc.ls(typ='transform')
mc.file('tohinon.obj',i=1)
os.remove('tohinon.obj')
sl = [x for x in mc.ls(typ='transform') if x not in o]
kaoi = []
for s in sl:
    mc.select(s)
    mc.polySoftEdge(a=50)
    if('kaoi' in s):
        # เพิ่มเก้าอี้เป็นหลายตัว
        for i in range(6):
            mc.select(s)
            mc.hyperShade(a=phiu_kaoi[i])
            if(i>0):
                s = mc.duplicate(s)[0]
            kaoi.append(s)
            mc.move(85*math.cos(math.radians(i*60)),0,85*math.sin(math.radians(i*60)))
    else:
        mc.hyperShade(a=phiu_hinon)
        to = s

mc.group(to,kaoi,n='to_kaoi_hinon')

# ใส่กระดูก สำหรับ mmd
mc.select(cl=1)
kho = [mc.joint(p=[0,0,0])]
mc.skinCluster(kho,to)
for s in kaoi:
    mc.select(cl=1)
    kho += [mc.joint(p=mc.xform(s,q=1,t=1))]
    mc.skinCluster(kho[-1],s)

mc.group(kho,n='kho_to_kaoi_hinon')