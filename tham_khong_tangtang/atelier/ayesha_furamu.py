# -*- coding: utf-8 -*-
import maya.cmds as mc

# วัสดุผิว ตัวถังสีน้ำตาลกับส่วนหัวสีดำ
phiu_thang = mc.shadingNode('blinn',asShader=1,n='phiu_thang')
mc.setAttr(phiu_thang+'.c',0.33,0.158,0.051,typ='double3')
mc.setAttr(phiu_thang+'.ambc',0.5,0.5,0.5,typ='double3')
phiu_hua = mc.duplicate(phiu_thang,n='phiu_hua')[0]
mc.setAttr(phiu_hua+'.c',0.05,0.05,0.05,typ='double3')

# ส่วนตัวถังหลัก
furamu = mc.polySphere(r=6,sx=48,sy=24,n='furamu')[0]
mc.hyperShade(a=phiu_thang)
ppj = mc.polyProjection(furamu+'.f[*]',t='spherical')[0]
for a,k in zip(['pcy','rx','phs','pvs'],[6,90,160,160]):
    mc.setAttr(ppj+'.'+a,k)

# คัดส่วนที่เป็นด้านบนและล่างออกมาเพื่อทำการดึงยืด
bon,lang = [],[]
for i in range(mc.polyEvaluate(furamu,v=1)):
    s = furamu+'.vtx[%d]'%i
    t = mc.xform(s,q=1,t=1)
    if(t[1]>0.01):
        bon.append(s)
    elif(t[1]<-0.01):
        lang.append(s)
mc.move(0,0.5,0,bon,r=1)
mc.move(0,-0.5,0,lang,r=1)
mc.move(6.5,furamu,y=1) # ย้ายขึ้นให้อยู่ติดพื้น

# ดึงส่วนตรงกลางออก ทำสีดำ
mc.select(furamu+'.f[480:575]')
mc.hyperShade(a=phiu_hua)
nf1 = mc.polyEvaluate(furamu,f=1)
mc.polyExtrudeFacet(ltz=0.3,sy=0.8)
nf2 = mc.polyEvaluate(furamu,f=1)
mc.select(furamu+'.f[%d:%d]'%(nf1,nf2-1))
mc.hyperShade(a=phiu_hua)
ppj = mc.polyProjection(furamu+'.f[480:575]',furamu+'.f[%d:%d]'%(nf1,nf2-1),t='cylindrical')[0]
for a,k in zip(['phs','isu','isv','icx','icy'],[360,0.5,0.5,0.25,0.25]):
    mc.setAttr(ppj+'.'+a,k)

# ลบส่วนบนออกเพื่อใส่ฝา
lop = []
for i in range(mc.polyEvaluate(furamu,f=1)):
    s = furamu+'.f[%d]'%i
    b = mc.xform(s,q=1,bb=1)
    if(b[1]>5.5):
        lop.append(s)
mc.delete(lop)

# สร้างส่วนฝา
nf = mc.polyEvaluate(furamu,f=1)
bon = [] # คัดขอบที่อยู่ด้านบนสุดออกมาเพื่อยืดเป็นฝา
for i in range(mc.polyEvaluate(furamu,e=1)):
    s = furamu+'.e[%d]'%i
    b = mc.xform(s,q=1,bb=1)
    if(b[1]>5.5):
        bon.append(s)
mc.select(bon)
mc.polyExtrudeEdge(ty=1.5)
mc.polyExtrudeEdge(ty=0.2,sx=0.9,sz=0.9)
mc.polyExtrudeEdge(sx=0.9,sz=0.9)
mc.polyExtrudeEdge(ty=0.7)
mc.polyExtrudeEdge(ty=0.2,sx=0.9,sz=0.9)
mc.polyExtrudeEdge(sx=0.9,sz=0.9)
nf1 = mc.polyEvaluate(furamu,f=1)
mc.polyExtrudeEdge(ty=0.7)
nf2 = mc.polyEvaluate(furamu,f=1)
mc.polyExtrudeEdge(ty=0.5,sx=0.8,sz=0.8)
mc.polyExtrudeEdge(sx=0,sz=0)
b = mc.xform(furamu+'.f[%d:%d]'%(nf1,nf2-1),q=1,bb=1,ws=1)
nf3 = mc.polyEvaluate(furamu,f=1)
mc.select(furamu+'.f[%d:%d]'%(nf,nf3-1))
mc.hyperShade(a=phiu_hua)
ppj = mc.polyProjection(furamu+'.f[%d:%d]'%(nf,nf3-1),t='spherical')[0]
for a,k in zip(['pcx','pcy','pcz','rx','phs','pvs','isu','isv','icx','icy'],[0,12,0,-90,180,180,0.5,0.5,0.75,0.25]):
    mc.setAttr(ppj+'.'+a,k)
mc.polyMergeVertex(furamu,d=0.001)

# ส่วนด้ามจับที่ฝา
fa = mc.polyCube(w=1,h=b[4]-b[1],d=0.5,n='fa')[0]
mc.hyperShade(a=phiu_hua)
mc.move(0,(b[4]+b[1])/2,b[2])
mc.select(fa+'.f[2]')
mc.polyExtrudeFacet(tz=-0.2,ty=-0.1,sx=1.5)
mc.polyExtrudeFacet(tz=-4.1,ty=-0.6,rx=-45,lsy=0.6)
mc.polyExtrudeFacet(tz=-0.1,ty=-0.15)
mc.polyExtrudeFacet(tz=-1.8,ty=-4.5,lsy=0.5,sx=0.8)
mc.polyExtrudeFacet(ltz=0.2,lsx=0.7,lsy=0.7,sz=0.7)
mc.delete(fa+'.f[0]')
mc.polyAutoProjection(fa+'.f[*]',ps=0.4)[0]
mc.select(fa+'.map[*]')
mc.polyEditUV(su=0.5,sv=0.5,pu=0,pv=1)

# ส่วนห่วง
huang = mc.polyTorus(r=2.4,sr=0.25,sx=36,sy=9,n='huang')[0]
mc.hyperShade(a=phiu_hua)
mc.move(0,15.8,3.9)
mc.rotate(54,p=[0,15.8,1.3])
mc.polySoftEdge(a=180)
mc.select(huang+'.map[*]')
mc.polyEditUV(su=0.5,sv=0.5,pu=1,pv=1)