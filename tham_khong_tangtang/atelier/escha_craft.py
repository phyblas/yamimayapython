# -*- coding: utf-8 -*-
import maya.cmds as mc
import math

r = 6 # รัศมีส่วนใน (ไม่รวมหนาม)
y = 1.5 # ความยาวหนาม กี่เท่าของรัศมี

phiu_nam = mc.shadingNode('blinn',asShader=1,n='phiu_nam') # ผิวหนามด้านล่าง
mc.setAttr(phiu_nam+'.c',0.49,0.36,0.12,typ='double3')
mc.setAttr(phiu_nam+'.sro',0.1)
phiu_nuea_nai = mc.duplicate(phiu_nam,n='phiu_nuea_nai')[0] # ผิวเนื้อไม้ด้านใน
mc.setAttr(phiu_nuea_nai+'.c',.78,0.63,0.38,typ='double3')
phiu_thian = mc.duplicate(phiu_nam,n='phiu_thian')[0] # ผิวเทียนสีแดง
mc.setAttr(phiu_thian+'.c',0.4,0.04,0,typ='double3')
phiu_sai_thian = mc.duplicate(phiu_nam,n='phiu_sai_thian')[0] # ผิวส่วนไส้เทียน
mc.setAttr(phiu_sai_thian+'.c',0.8,0.6,0.6,typ='double3')
nun = mc.shadingNode('bump3d',au=1)
lai = mc.shadingNode('cloud',at=1)
mc.connectAttr(nun+'.o',phiu_sai_thian+'.n')
mc.connectAttr(lai+'.oa',nun+'.bv')
for a,k in zip(['ripplesX','ripplesY','ripplesZ','amplitude'],[2,6,3,2]):
    mc.setAttr(lai+'.'+a,k)

# ใส่แอมเบียนต์
for mat in [phiu_nam,phiu_nuea_nai,phiu_thian,phiu_sai_thian]:
    mc.setAttr(mat+'.ambc',0.5,0.5,0.5,typ='double3')

# หนามด้านล่าง
craft_lang = mc.polySphere(r=10,sx=64,sy=32,n='craft_lang')[0]
mc.hyperShade(a=phiu_nam)
mc.scale(y,y,y,[craft_lang+'.vtx[%d]'%(i+j-(i/128)%2) for i in range(1,960,128) for j in range(0,64,2)])
mc.delete(craft_lang+'.f[960:1919]',craft_lang+'.f[1984:2047]')

# ส่วนด้านบน
craft_bon = mc.polySphere(r=10,sx=24,sy=4,n='craft_bon')[0]
mc.delete(craft_bon+'.f[24:47]',craft_bon+'.f[72:95]')
nf1 = mc.polyEvaluate(craft_bon,f=1) # จำนวนหน้าส่วนที่จะลบตอนหลัง
mc.select(craft_bon+'.e[24:47]')
# เนื้อไม้
mc.polyExtrudeEdge(sx=0.9,sz=0.9)
mc.polyExtrudeEdge(ty=-1)
mc.polyExtrudeEdge(sx=5./9,sz=5./9)
nf2 = mc.polyEvaluate(craft_bon,f=1)
# เทียนแดง
mc.polyExtrudeEdge(ty=10)
mc.polyExtrudeEdge(sx=0.8,sz=0.8)
mc.polyExtrudeEdge(ty=-1)
nf3 = mc.polyEvaluate(craft_bon,f=1)
# ไส้เทียน
mc.polyExtrudeEdge(sx=0.15,sz=0.15)
sl = mc.ls(sl=1)
kliao = mc.duplicate(craft_bon,n='kliao')[0]
mc.select(sl)
for i in range(15):
    mc.polyExtrudeEdge(ty=0.5,tx=0.04*i*math.cos(0.6*i),tz=0.04*i*math.sin(0.6*i))
mc.polyExtrudeEdge(sx=0,sz=0,ty=0.2)
mc.polyMergeVertex(d=0.01)
nf4 = mc.polyEvaluate(craft_bon,f=1)
mc.delete(craft_bon,ch=1)

# สร้างเบลนด์เชป
mc.select([s.replace(craft_bon,kliao) for s in sl])
for i in range(15):
    mc.polyExtrudeEdge(ty=0.55)
mc.polyExtrudeEdge(sx=0,sz=0,ty=0.2)
mc.polyMergeVertex(d=0.01)
bs = mc.blendShape(kliao,craft_bon)[0]

# สร้าง uv ให้แต่ละส่วนแยกกัน โดยจัดทำ uv ที่โหนดวัตถุเบลนด์เชป แล้วค่อยคัดลอกมาที่วัตถุหลัก
at = 'pcx pcy pcz rx ry rz phs pvs'.split()
ppj1 = mc.polyProjection(kliao+'.f[%d:%d]'%(nf1,nf2-1),t='spherical')[0]    
ppj2 = mc.polyProjection(kliao+'.f[%d:%d]'%(nf2,nf3-1),t='spherical')[0]
for a,k1,k2 in zip(at,[0,5,0,90,0,0,130,130],[0,-2,0,-90,0,0,160,160]):
    mc.setAttr(ppj1+'.'+a,k1)
    mc.setAttr(ppj2+'.'+a,k2)
mc.polyAutoProjection(kliao+'.f[%d:%d]'%(nf3,nf4-1),ps=0.4)
mc.polyTransfer(craft_bon,uv=1,ao=kliao,ch=0)
mc.delete(kliao)

# ใส่สีให้แต่ละหน้าต่างๆกัน
mc.select(craft_bon+'.f[%d:%d]'%(nf1,nf2-1))
mc.hyperShade(a=phiu_nuea_nai)
mc.select(craft_bon+'.f[%d:%d]'%(nf2,nf3-1))
mc.hyperShade(a=phiu_thian)
mc.select(craft_bon+'.f[%d:%d]'%(nf3,nf4-1))
mc.hyperShade(a=phiu_sai_thian)

# ลบหน้าส่วนล่างที่ไม่ได้ใช้
mc.delete(craft_bon+'.f[0:%d]'%(nf1-1))
mc.select([craft_bon+'.e[%d]'%i for i in range(121,166,4)])
mc.move(0,0.5,r=1)

# ปรับ uv ของส่วนล่าง
mc.select(craft_lang+'.map[*]')
mc.polyEditUV(sv=2,pv=0)

# รวมส่วนบนและล่างเข้าด้วยกัน
craft = mc.polyUnite(craft_bon,craft_lang,n='craft')[0]
mc.scale(r/10.,r/10.,r/10.,craft)

g = [] # กลุ่มจุดที่จะไม่ให้ขยับไปกับกระดูก
tamsut = 0 # หาจุดต่ำสุด
for i in range(mc.polyEvaluate(craft,v=1)):
    s = craft+'.vtx[%d]'%i
    t = mc.xform(s,q=1,t=1)
    if(t[0]**2+t[2]**2>9 or t[1]<8.1):
        g.append(s)
    if(t[1]<tamsut):
        tamsut = t[1]

# เชื่อมเข้ากับกระดูก
mc.select(cl=1)
kho1 = mc.joint(p=[0,0,0])
kho = [mc.joint(p=[0,8*r/10,0]),mc.joint(p=[0,12.225*r/10,0]),mc.joint(p=[0,16.45*r/10,0])]
sk = mc.skinCluster(kho,craft)[0]
mc.skinPercent(sk,g,tv=[(kho1,1.)])
mc.move(0,-tamsut*r/10.,0,kho1)