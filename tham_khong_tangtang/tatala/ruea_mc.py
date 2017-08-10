# -*- coding: utf-8 -*-
import maya.cmds as mc

lek = 0

o = mc.ls(typ='transform')
if(lek==0):
    mc.file('tatala.obj',i=1)
else:
    mc.file('tatala_lek.obj',i=1)
phuenruea,tuaruea = [x for x in mc.ls(typ='transform') if x not in o]

phiu_nairuea = mc.shadingNode('blinn',asShader=1,n='phiu_nairuea')
mc.setAttr(phiu_nairuea+'.ambc',0.5,0.5,0.5,typ='double3')
lai = mc.shadingNode('file',at=1)
mc.connectAttr(lai+'.oc',phiu_nairuea+'.c')
mc.setAttr(lai+'.ftn','laimai.jpg',typ='string')

mc.select(tuaruea)
nf1 = mc.polyEvaluate(f=1)
mc.polyNormal()
mc.polyExtrudeFacet(ltz=2)
if(lek==0):
    mc.scale(57./59,z=1)
else:
    mc.scale(37./39,z=1)
nf2 = mc.polyEvaluate(tuaruea,f=1)
mc.select(tuaruea+'.f[*]')
mc.select(tuaruea+'.f[%d:%d]'%(nf1,nf1*2-1),tgl=1)
mc.hyperShade(a=phiu_nairuea)
mc.polyProjection(rx=90,ry=180,rz=0,psu=10,psv=130)
mc.select(phuenruea)
mc.hyperShade(a=phiu_nairuea)
mc.polyProjection(phuenruea+'.f[*]',rx=90,ry=180,rz=0,psu=30,psv=130)

if(lek==0):
    g = []
    for i in range(mc.polyEvaluate(phuenruea,f=1)):
        s = phuenruea+'.f[%d]'%i
        bb = mc.xform(s,q=1,bb=1)
        if(bb[1]>=33.9):
            g.append(s)
    mc.polyExtrudeFacet(g,off=0.2,ltz=1,kft=0)

g = []
for i in range(mc.polyEvaluate(phuenruea,f=1)):
    s = phuenruea+'.f[%d]'%i
    bb = mc.xform(s,q=1,bb=1)
    if(bb[3]-bb[0]<0.3):
        g.append(s)
mc.polyProjection(g,rx=90,ry=0,rz=90,psu=30,psv=130)

ruea = mc.polyUnite(tuaruea,phuenruea,ch=0,n='ruea')