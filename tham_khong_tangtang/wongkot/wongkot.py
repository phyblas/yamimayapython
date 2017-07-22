# -*- coding: utf-8 -*-
import maya.cmds as mc
import math,random

nx = 9 # จำนวนช่อง
nz = 9
w = 2 # ความกว้าง

phiu_phanang = mc.shadingNode('blinn',asShader=1,n='phiu_phanang')
lai_phanang = mc.shadingNode('brownian',at=1,n='lai_phanang')
mc.connectAttr(lai_phanang+'.oc',phiu_phanang+'.c')
mc.setAttr(lai_phanang+'.colorOffset',0.34,0.08,0.05,typ='double3')
mc.setAttr(lai_phanang+'.colorGain',0,0.44,0.13,typ='double3')
ple = mc.shadingNode('place3dTexture',au=1)
mc.defaultNavigation(ce=1,s=ple,d=lai_phanang)

phiu_phuen = mc.shadingNode('blinn',asShader=1,n='phiu_phuen')
lai_phuen = mc.shadingNode('checker',at=1,n='lai_phuen')
mc.connectAttr(lai_phuen+'.oc',phiu_phuen+'.c')
mc.setAttr(lai_phuen+'.color1',0.34,0.08,0.05,typ='double3')
mc.setAttr(lai_phuen+'.color2',0,0.44,0.13,typ='double3')
ple = mc.shadingNode('place2dTexture',au=1)
mc.defaultNavigation(ce=1,s=ple,d=lai_phuen)
mc.setAttr(ple+'.coverageU',4)
mc.setAttr(ple+'.coverageV',4)

for i in range(nx+1):
    for j in range(nz+1):
        if(i==0 and j==0):
            sao = [mc.polyCube(w=0.1,h=2,d=0.1)[0]]
            mc.select([sao[0]+'.f[%d]'%k for k in [0,2,4,5]])
            mc.polyExtrudeFacet(sy=1.8/2)
            mc.polyExtrudeFacet(sy=1.76/1.8,ltz=-0.02)
            mc.select(sao[0]+'.f[1]')
            mc.polyExtrudeFacet(off=-0.02)
            mc.polyExtrudeFacet(ltz=0.05)
            mc.polyExtrudeFacet(off=0.02,ltz=0.02)
        else:
            sao += mc.duplicate(sao[0])
        mc.move(i*w,1,j*w,sao[-1])
phanang = []
for i in range(nx+1):
    for j in range(nz):
        if(i==0 and j==0):
            phanang += [mc.polyCube(w=0.06,h=2,d=w-0.08)[0]]
            mc.polyExtrudeFacet(*['.f[%d]'%k for k in [0,2,4,5]],sy=1.8/2)
            mc.polyExtrudeFacet('.f[4:5]',sy=1.76/1.8,ltz=-0.02,kft=0)
            mc.delete(*['.f[%s]'%k for k in [0,'2:3','6:9',15,17,19,21]])
        else:
            phanang += mc.duplicate(phanang[0])
        mc.move(i*w,1,(j+0.5)*w,phanang[-1])
for i in range(nx):
    for j in range(nz+1):
        if(i==0 and j==0):
            phanang += [mc.polyCube(w=w-0.08,h=2,d=0.06)[0]]
            mc.polyExtrudeFacet(*['.f[%d]'%k for k in [0,2,4,5]],sy=1.8/2)
            mc.polyExtrudeFacet('.f[0]','.f[2]',sy=1.76/1.8,ltz=-0.02,kft=0)
            mc.delete(*['.f[%s]'%k for k in ['3:5','10:13',15,17,19,21]])
        else:
            phanang += mc.duplicate(phanang[(nx+1)*nz])
        mc.move((i+0.5)*w,1,j*w,phanang[-1])

# ลบส่วนที่เปิดให้เป็นทาง
mc.delete([phanang[i] for i in [9,10,11,13,14,17,18,20,21,22,23,25,26,27,28,29,30,34,36,37,39,40,42,43,44,45,47,49,52,53,56,57,58,61,63,66,67,71,72,74,76,78,90,91,93,94,96,97,106,107,108,112,114,115,116,125,126,128,132,136,141,142,146,147,151,152,153,155,156,157,158,162,163,165,166,168,171,173,175,177,178,179]])
mc.polyUnite(sao,mc.ls(phanang),ch=0,n='phanang')
mc.move(-nx/2.*w,0,-nz/2.*w)
mc.select(phanang)
mc.hyperShade(a=phiu_phanang)
mc.polyAutoProjection(ps=0.2,ch=0)

phuen = mc.polyPlane(w=nx*w,h=nz*w,sx=1,sy=1,n='phuen')[0]
mc.hyperShade(a=phiu_phuen)
mc.polyProjection(phuen+'.f[*]',pcx=w/32.,pcy=0,pcz=w/32.,rx=90,ry=0,rz=0,psu=w/16.,psv=w/16.)

