 # -*- coding: utf-8 -*-
import maya.cmds as mc

phiu_kin = mc.shadingNode('blinn',asShader=1,n='phiu_kin') # ผิวตัวเครื่อง
mc.setAttr(phiu_kin+'.c',0,0,0,typ='double3')
mc.setAttr(phiu_kin+'.ambc',0.35,0.35,0.35,typ='double3')
wao = mc.shadingNode('bump2d',au=1)
lai = mc.shadingNode('file',at=1)
mc.connectAttr(wao+'.o',phiu_kin+'.n')
mc.connectAttr(lai+'.oa',wao+'.bv')
mc.setAttr(wao+'.bd',0.04)
mc.setAttr(lai+'.ftn','ka.png',typ='string')
phiu_cho = mc.duplicate(phiu_kin,n='phiu_cho')[0] # ผิวจอ
mc.setAttr(phiu_cho+'.c',0.9,0.9,0.9,typ='double3')
phiu_pum = mc.duplicate(phiu_kin,n='phiu_pum')[0] # ผิวปุ่ม
phiu_ru = mc.duplicate(phiu_kin,n='phiu_ru')[0] # ผิวช่องเสียบสาย
mc.setAttr(phiu_ru+'.c',0.5,0.5,0.5,typ='double3')
mc.setAttr(phiu_ru+'.sc',1,1,1,typ='double3')

kin = mc.polyCube(w=11.6,h=0.2,d=16.8,n='kindei')[0]
mc.hyperShade(a=phiu_kin)
mc.select(kin+'.f[3]')
mc.polyExtrudeFacet(off=1./3**2,ltz=0.1)
mc.polyExtrudeFacet(off=((2./3)**2-(1./3)**2),ltz=0.1)
mc.polyExtrudeFacet(off=(1-(2./3)**2),ltz=0.1)
mc.polyBevel([kin+'.e[%d]'%i for i in [4,5,8,9,12,13,15,17,20,21,23,25,28,29,31,33]],o=0.4)
mc.select(kin+'.f[0]')
mc.polyExtrudeFacet(off=0.2,ltz=0.1)
mc.polyExtrudeFacet(sx=9.5/(11.6-0.4),sz=12.6/(16.8-0.4))
mc.move(0,0,-0.4,r=1)
mc.polyExtrudeFacet(off=0.1,ltz=-0.1)

mc.select([kin+'.e[%d]'%i for i in [106,110,114,118]])
cho = kin+'.f[0]'
b = mc.xform(cho,q=1,bb=1,ws=1)
mc.scale(0,1,0,kin+'.e[106]',p=[b[0],0,b[5]])
mc.scale(0,1,0,kin+'.e[110]',p=[b[3],0,b[5]])
mc.scale(0,1,0,kin+'.e[114]',p=[b[3],0,b[2]])
mc.scale(0,1,0,kin+'.e[118]',p=[b[0],0,b[2]])
mc.polyMergeVertex(d=0.001)

mc.scale(0.5,1,0.5,kin+'.e[90]',p=[b[0]-0.1,0,b[5]+0.1])
mc.scale(0.5,1,0.5,kin+'.e[94]',p=[b[3]+0.1,0,b[5]+0.1])
mc.scale(0.5,1,0.5,kin+'.e[98]',p=[b[3]+0.1,0,b[2]-0.1])
mc.scale(0.5,1,0.5,kin+'.e[102]',p=[b[0]-0.1,0,b[2]-0.1])



mc.select([kin+'.f[%d]'%i for i in [24,28,32]])
mc.polyExtrudeFacet(sx=0.4)
mc.polyExtrudeFacet()
mc.scale(1,1,0,p=[0,0,8.4])
mc.move(-0.02,kin+'.e[136]',z=1,r=1)
mc.move(-0.04,kin+'.e[141]',z=1,r=1)
mc.move(-0.06,kin+'.e[146]',z=1,r=1)

mc.select(kin+'.f[24]',kin+'.f[28]')
mc.polyExtrudeFacet(sx=0.8)
mc.scale(0,1,1,kin+'.e[151]',kin+'.e[156]',p=[-1.55,0,0])
mc.scale(0,1,1,kin+'.e[154]',kin+'.e[159]',p=[-0.85,0,0])
mc.polyExtrudeFacet()
mc.scale(1,1,0,p=[0,0,8])
mc.select(kin+'.f[28]')
mc.polyExtrudeFacet(sx=0.6,sy=0.2)
mc.polyExtrudeFacet(ltz=0.36)

mc.polySoftEdge(kin,a=180)



# ปุ่ม
pum = mc.polyCube(w=0.7,d=0.1,h=0.2,n='pum')[0]
mc.hyperShade(a=phiu_pum)
mc.move(1.2,-0.2,8.4)
mc.delete('.f[2]')

# ช่องเสียบสาย
ru = mc.polyCylinder(r=0.1,h=0.36,ax=[0,0,1],sx=8,n='ru')[0]
mc.hyperShade(a=phiu_ru)
mc.move(-1.2,-0.2,8.18)
mc.rotate(22.5,z=1)
mc.delete(ru+'.f[8:9]')
mc.move(-0.25,ru+'.f[1:3]',x=1,r=1)
mc.move(0.25,ru+'.f[5:7]',x=1,r=1)
mc.move(-0.03,ru+'.f[2]',ru+'.f[6]',y=1,r=1)
mc.polyExtrudeFacet(ru+'.f[*]',ltz=-0.02)
mc.polyNormal(ru)

# คัดกรองแยกโพลิกอนเป็นกลุ่มเพื่อทำการสร้าง uv แยกกัน
g = [[],[],[],[]]
for i in range(1,mc.polyEvaluate(kin,f=1)):
    s = kin+'.f[%d]'%i
    bb = mc.xform(s,q=1,bb=1,ws=1)
    if(bb[4]-bb[1]<0.0001 and bb[5]-bb[2]<0.0001):
        g[3].append(s)
    elif(bb[4]<0):
        b = (bb[0]+bb[3])/2
        if(bb[2]>7.8 and b>-1.9 and b<1.9):
            g[1].append(s)
        else:
            g[0].append(s)
    elif(bb[1]<0.11 and abs(bb[0])>5 and abs(bb[2])>7):
        g[1].append(s)
    else:
        g[2].append(s)

bb = mc.xform(g[0],q=1,bb=1,ws=1)
mc.polyProjection(g[0],pcx=0,pcy=0,pcz=0,rx=90,ry=180,rz=0,psu=bb[5]-bb[2],psv=bb[5]-bb[2])[0]
mc.polyEditUV(su=0.5,sv=0.5,pu=0,pv=1)

mc.polyAutoProjection(g[1],ps=0.4)
mc.polyEditUV(su=0.48,sv=0.48,pu=0.02,pv=0.02)

bb = mc.xform(g[2],q=1,bb=1,ws=1)
mc.polyProjection(g[2],pcx=0,pcy=0,pcz=0,rx=-90,ry=0,rz=0,psu=bb[5]-bb[2]+0.6,psv=bb[5]-bb[2]+0.6)[0]
mc.polyEditUV(su=0.5,sv=0.5,pu=1,pv=0)
bb = mc.xform(cho,q=1,bb=1,ws=1)
mc.polyProjection(cho,pcx=0,pcy=0,pcz=(bb[5]+bb[2])/2,rx=-90,ry=0,rz=0,psu=bb[5]-bb[2],psv=bb[5]-bb[2])[0]
mc.polyEditUV(su=0.5,sv=0.5,pu=1,pv=1)
mc.select(cho)
mc.hyperShade(a=phiu_cho)

mc.delete(g[3])
mc.delete(kin,ch=1)