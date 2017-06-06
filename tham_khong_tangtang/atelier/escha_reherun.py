# -*- coding: utf-8 -*-
import maya.cmds as mc
import math,random

phiu_sai = mc.shadingNode('blinn',asShader=1,n='phiu_sai')
mc.setAttr(phiu_sai+'.ambc',0.5,0.5,0.5,typ='double3')
phiu_hua = mc.duplicate(phiu_sai,n='phiu_hua')[0]
phiu_namkhaeng = mc.duplicate(phiu_sai,n='phiu_namkhaeng')[0]
mc.setAttr(phiu_sai+'.c',0.8,0.6,0.6,typ='double3')
nun = mc.shadingNode('bump3d',au=1)
lai = mc.shadingNode('cloud',at=1)
mc.connectAttr(nun+'.o',phiu_sai+'.n')
mc.connectAttr(lai+'.oa',nun+'.bv')
mc.setAttr(phiu_hua+'.c',0.09,0.17,0.37,typ='double3')
mc.setAttr(phiu_namkhaeng+'.c',0.63,0.9,1.,typ='double3')
mc.setAttr(phiu_namkhaeng+'.it',0.2,0.2,0.2,typ='double3')
nun = mc.shadingNode('bump3d',au=1)
lai = mc.shadingNode('solidFractal',at=1)
mc.connectAttr(nun+'.o',phiu_namkhaeng+'.n')
mc.connectAttr(lai+'.oa',nun+'.bv')

namkhaeng = mc.polySphere(r=6,sx=48,sy=24,n='namkhaeng')[0]
mc.hyperShade(a=phiu_namkhaeng)
g = []
for i in range(mc.polyEvaluate(f=1)):
    f = namkhaeng+'.f[%d]'%i
    b = mc.xform(f,q=1,bb=1)
    if(b[1]>5.6):
        g.append(f)
mc.delete(g)
for i in range(mc.polyEvaluate(v=1)):
    mc.select(namkhaeng+'.vtx[%d]'%i)
    t = mc.xform(q=1,t=1)
    phi = math.atan2(t[2],t[0])
    fu = 1+0.1*math.sin(6*phi)*math.cos(t[1])
    mc.scale(fu+random.uniform(-0.05,0.05),1.05,fu+random.uniform(0,0.1))
    
hua = mc.polyCylinder(r=2.5,h=3,sx=24,sy=1,sz=1,n='hua')
mc.hyperShade(a=phiu_hua)
mc.move(0,7)
mc.delete(hua+'.f[24:47]')
sai = mc.polyCylinder(r=0.25,h=3,sx=12,sy=10,sz=1,n='sai')[0]
mc.hyperShade(a=phiu_sai)
mc.move(0,10)
mc.move(0.1,'.vtx[133]',y=1,r=1)
for i in range(mc.polyEvaluate(v=1)):
    mc.select(sai+'.vtx[%d]'%i)
    t = mc.xform(q=1,t=1)
    r = (t[1]+1.5)*0.15
    mc.move(r*math.sin(t[1]*3),0,r*math.cos(t[1]*3),r=1)

mc.polySoftEdge(sai,a=180)
mc.select(sai,hua,namkhaeng)
mc.move(6.3,y=1,r=1)