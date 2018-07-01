# -*- coding: utf-8 -*-
import maya.cmds as mc

# สีผิวส่วนดำ
phiu_dam = mc.shadingNode('blinn',asShader=1,n='phiu_dam')
mc.setAttr(phiu_dam+'.c',0,0,0,typ='double3')
mc.setAttr(phiu_dam+'.ambc',0.5,0.5,0.5,typ='double3')
mc.setAttr(phiu_dam+'.sc',0.9,0.9,0.9,typ='double3')
mc.setAttr(phiu_dam+'.sro',0.3)
phiu = [phiu_dam]

# สีผิวหน้าต่างๆ
for i in range(1,7):
    phiu.append(mc.duplicate(phiu_dam,n='phiu_na%d'%i)[0])
    lai_na = mc.shadingNode('file',at=1,n='lai_na%d'%i)
    mc.connectAttr(lai_na+'.oc',phiu[i]+'.c')
    mc.setAttr(lai_na+'.ftn','/Users/patn/Dropbox/lukbit/na%d.jpg'%i,typ='string')

k = 5.6 # ขนาดของลูกบิด
lukbit = [mc.polyCube(w=k/3,h=k,d=k,sx=1,sy=3,sz=3)[0]] # ส่วนตรงกลาง
mc.polyExtrudeFacet(lukbit[0]+'.f[0:11]',ltz=0.05,off=0.05,kft=0)
lukbit.append(mc.duplicate(lukbit[0])[0]) # ส่วนซ้าย
mc.move(-k/3,lukbit[1])
mc.polyExtrudeFacet(lukbit[1]+'.f[21:29]',ltz=0.05,off=0.05,kft=0)
lukbit.append(mc.duplicate(lukbit[0])[0]) # ส่วนขวา
mc.move(k/3,lukbit[2])
mc.polyExtrudeFacet(lukbit[2]+'.f[12:20]',ltz=0.05,off=0.05,kft=0)
lukbit[0],lukbit[1] = lukbit[1],lukbit[0]
nv = [mc.polyEvaluate(n,v=1) for n in lukbit] # เก็บจำนวนหน้าแต่ละส่วนไว้
nv = [0,nv[0],nv[0]+nv[1],sum(nv)]
lukbit = mc.polyUnite(lukbit,ch=0)[0] # รวมั้ง 3 ส่วนเข้าด้วยกัน
mc.hyperShade(a=phiu_dam) # ใส่สีดำ

# คัดกรองหาหน้าที่เป็นหน้าสีของลูกบิด
na = [[] for i in range(7)]
for i in range(mc.polyEvaluate(lukbit,f=1)):
    s = lukbit+'.f[%d]'%i
    bb = mc.xform(s,q=1,bb=1,ws=1)
    for j in range(3):
        if(bb[j]>k/2+0.049):
            na[j].append(s)
            break
        if(bb[j+3]<-k/2-0.049):
            na[j+3].append(s)
            break
    else:
        na[6].append(s)

for i in range(6):
    mc.select(na[i])
    mc.hyperShade(a=phiu[i+1]) # ใส่สีตามหน้า
    mc.polyProjection(pcx=0,pcy=0,pcz=0,rx=(i%3==1)*90,ry=(i%3==0)*90,rz=0,psu=k,psv=k) # ใส่ uv
mc.polyAutoProjection(na[6],ps=0.1)

# ใส่กระดูก
kho = []
for i in range(3):
    mc.select(cl=1)
    kho.append(mc.joint(p=[k/3*(i-1),0,0]))
sk = mc.skinCluster(kho,lukbit)[0]
for i in range(3):
    mc.skinPercent(sk,lukbit+'.vtx[%d:%d]'%(nv[i],nv[i+1]-1),tv=(kho[i],1))
