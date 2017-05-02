# -*- coding: utf-8 -*-
import maya.cmds as mc
import math

r = 10 # รัศมี
ts = 1 # ความสูงของเทียนต่อรัศมี

phiu_nam_khiao = mc.shadingNode('blinn',asShader=1,n='phiu_nam_khiao') # ผิวหนามเขียวด้านล่าง
mc.setAttr(phiu_nam_khiao+'.c',0,0.5,0,typ='double3')
mc.setAttr(phiu_nam_khiao+'.sro',0.1)
phiu_nuea_nai = mc.duplicate(phiu_nam_khiao,n='phiu_nuea_nai')[0] # ผิวเนื้อไม้ด้านใน
mc.setAttr(phiu_nuea_nai+'.c',0.9,0.8,0.4,typ='double3')
phiu_thian_daeng = mc.duplicate(phiu_nam_khiao,n='phiu_thian_daeng')[0] # ผิวเทียนสีแดง
mc.setAttr(phiu_thian_daeng+'.c',0.5,0.05,0,typ='double3')
phiu_sai_thian = mc.duplicate(phiu_nam_khiao,n='phiu_sai_thian')[0] # ผิวส่วนไส้เทียน
mc.setAttr(phiu_sai_thian+'.c',0.9,0.7,0.7,typ='double3')

# หนามด้านล่าง
craft_lang = mc.polySphere(r=r,sx=64,sy=32,n='craft_lang')[0]
mc.hyperShade(a=phiu_nam_khiao)
mc.scale(1.5,1.5,1.5,[craft_lang+'.vtx[%d]'%(i+j-(i/128)%2) for i in range(1,960,128) for j in range(0,64,2)])
mc.delete(craft_lang+'.f[960:1919]',craft_lang+'.f[1984:2047]')

# ส่วนด้านบน
craft_bon = mc.polySphere(r=10,sx=24,sy=4,n='craft_bon')[0]
mc.delete(craft_bon+'.f[24:47]',craft_bon+'.f[72:95]')
nf1 = mc.polyEvaluate(craft_bon,f=1)
mc.select(craft_bon+'.e[24:47]')
# เนื้อไม้
mc.polyExtrudeEdge(sx=0.9,sz=0.9)
mc.polyExtrudeEdge(ty=-r*0.1)
mc.polyExtrudeEdge(sx=5./9,sz=5./9)
nf2 = mc.polyEvaluate(craft_bon,f=1)
# เทียนแดง
mc.polyExtrudeEdge(ty=r*ts)
mc.polyExtrudeEdge(sx=0.8,sz=0.8)
mc.polyExtrudeEdge(ty=-r*0.1)
nf3 = mc.polyEvaluate(craft_bon,f=1)
# ไส้เทียน
mc.polyExtrudeEdge(sx=0.15,sz=0.15)
for i in range(15):
    mc.polyExtrudeEdge(ty=r*0.05,tx=r*0.004*i*math.cos(0.6*i),tz=r*0.004*i*math.sin(0.6*i))
mc.polyExtrudeEdge(sx=0,sz=0,ty=0.02*r)
mc.polyMergeVertex(d=0.001*r)
nf4 = mc.polyEvaluate(craft_bon,f=1)
mc.select(craft_bon+'.f[%d:%d]'%(nf1,nf2-1))
mc.hyperShade(a=phiu_nuea_nai)
mc.select(craft_bon+'.f[%d:%d]'%(nf2,nf3-1))
mc.hyperShade(a=phiu_thian_daeng)
mc.select(craft_bon+'.f[%d:%d]'%(nf3,nf4-1))
mc.hyperShade(a=phiu_sai_thian)
mc.delete(craft_bon+'.f[0:%d]'%(nf1-1))
mc.select([craft_bon+'.e[%d]'%i for i in range(121,166,4)])
mc.move(0,0.05*r,r=1)
mc.delete(craft_lang,craft_bon,ch=1)
mc.group(craft_lang,craft_bon,n='craft')