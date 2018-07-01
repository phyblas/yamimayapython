# -*- coding: utf-8 -*-
import maya.cmds as mc

r = 5 # รัศมี

# สร้างสี
phiu_lang = mc.shadingNode('blinn',asShader=1,n='phiu_lang')
mc.setAttr(phiu_lang+'.c',1,1,1,typ='double3')
phiu_klang = mc.shadingNode('blinn',asShader=1,n='phiu_klang')
mc.setAttr(phiu_klang+'.c',0,0,0,typ='double3')
phiu_pum = mc.shadingNode('blinn',asShader=1,n='phiu_pum')
mc.setAttr(phiu_pum+'.c',1,1,1,typ='double3')
phiu_bon = mc.shadingNode('blinn',asShader=1,n='phiu_bon')
mc.setAttr(phiu_bon+'.c',1,0,0,typ='double3')
mc.setAttr(phiu_bon+'.it',0.5,0.5,0.5,typ='double3') # ทำให้โปร่งใส

# ใส่แอมเบียนต์
for mat in [phiu_bon,phiu_lang,phiu_pum]:
    mc.setAttr(mat+'.ambc',0.5,0.5,0.5,typ='double3')

# ส่วนทรงกลมหลัก
pkmb = mc.polySphere(r=r-0.1,sy=24,sx=48)[0]
mc.polyExtrudeFacet(sx=1+0.1/(r-0.1),sy=1+0.1/(r-0.1),sz=1+0.1/(r-0.1))
klang1 = mc.polyCylinder(h=1,r=1.5,sx=24,ax=[0,0,1])[0]
mc.move(0,0,r-0.1)
klang2 = mc.polyCylinder(h=0.6,r=5.5,sx=24)[0]
klang = mc.duplicate(klang1,klang2)
pkmb = mc.polyCBoolOp(pkmb,klang1,klang2,op=2,ch=0)[0]

# ส่วนสีดำตรงกลาง
nai = mc.polySphere(r=r-0.2,sy=24,sx=48)[0]
mc.hyperShade(a=phiu_klang)
mc.polyExtrudeFacet(sx=1+0.1/(r-0.2),sy=1+0.1/(r-0.2),sz=1+0.1/(r-0.2))
klang = mc.polyCBoolOp(nai,klang,op=3,ch=0)[0]
n_na_klang = mc.polyEvaluate(klang,f=1)

# แยกส่วนด้านล่างกับด้านบน
lang,bon = mc.polySeparate(pkmb,ch=0)
mc.select(bon)
mc.hyperShade(a=phiu_bon)
mc.select(lang)
mc.hyperShade(a=phiu_lang)

# ลบส่วนด้านในของผิวด้านบน
l= []
d = 4*(r-0.099)**2
for i in range(mc.polyEvaluate(bon,f=1)):
    f = bon+'.f[%d]'%i
    b = mc.xform(f,q=1,bb=1)
    if((b[3]+b[0])**2+(b[4]+b[1])**2+(b[5]+b[2])**2<d and b[3]-b[0]<5):
        l.append(f)
mc.delete(l)
n_na_bon = mc.polyEvaluate(bon,f=1) # จำนวนหน้าส่วนฝาด้านบน

# ส่วนปุ่มสีขาว
pum = mc.polyCylinder(h=0.2,r=1,sx=24,sz=1,ax=[0,0,1])[0]
mc.move(0,0,r-0.1)
mc.hyperShade(a=phiu_pum)
mc.select(pum+'.f[48:71]')
mc.polyExtrudeFacet(sx=0.75,sy=0.75)
mc.polyExtrudeFacet(ltz=0.2)
mc.delete(pum+'.f[24:47]')
n_na_pum = mc.polyEvaluate(pum,v=1) # จำนวนหน้าของส่วนปุ่ม

# รวมส่วนดำตรงกลางกับผิวด้านบน
bon = mc.polyUnite(bon,pum,klang,ch=0)[0]

# หา z จุดหมุน
n_vtx_bon = mc.polyEvaluate(bon,v=1) # จำนวนจุดส่วนบนที่ต้องการให้เคลื่อนไหวทั้งหมด
p = ((r-0.1)**2-0.3**2)**0.5
d = 0.1
for i in range(n_vtx_bon):
    t = mc.xform(bon+'.vtx[%d]'%i,q=1,t=1)
    d0 = abs(t[2]+p)
    if(d0<d and t[1]<0):
        d = d0
chutmun = d-p

# รวมโพลิกอนทั้งหมดเข้าด้วยกัน
pkmb = mc.polyUnite([bon,lang],ch=0,n='pkmb')[0]
n_vtx_pkmb = mc.polyEvaluate(pkmb,v=1) # จำนวนจุดทั้งหมด
n_na_pkmb = mc.polyEvaluate(pkmb,f=1) # จำนวนหน้าทั้งหมด

# แก้ uv ให้ส่วนที่จำเป็น ส่วนบนและล่างกาง uv จากด้านบน
mc.polyProjection(pkmb+'.f[0:%d]'%(n_na_bon-1),
                  pkmb+'.f[%d:%d]'%(n_na_bon+n_na_pum+n_na_klang,n_na_pkmb-1),
                  pcx=0,pcy=0,pcz=0,rx=-90,ry=0,rz=0,psu=10,psv=10) 
# ส่วนปุ่มกาง uv แบบทรงกลม
ppj = mc.polyProjection(pkmb+'.f[%d:%d]'%(n_na_bon,n_na_bon+n_na_pum-1),t='spherical')[0]
mc.setAttr(ppj+'.pcx',0)
mc.setAttr(ppj+'.pcy',0)
mc.setAttr(ppj+'.pcz',r-0.8)
mc.setAttr(ppj+'.phs',120)
mc.setAttr(ppj+'.pvs',120)

# สร้างเบลนด์เชปให้ย่อและขยายขนาดได้
yosuan,khayai = mc.duplicate(pkmb,n='yosuan')+mc.duplicate(pkmb,n='khayai')
mc.scale(0,0,0,yosuan+'.vtx[*]',p=[0,-0.3,chutmun])
mc.scale(100,100,100,khayai+'.vtx[*]',p=[0,-0.3,chutmun])
mc.select(yosuan,khayai,pkmb)
bs = mc.blendShape(n='pkmb_bs')[0]
mc.delete(yosuan,khayai)
mc.addAttr(bs,ln='namae',nn=u'名前',dt='string')
mc.setAttr(bs+'.namae',u'%s๑縮小๑2๐%s๑巨大化๑1'%(yosuan,khayai),typ='string')

# สร้างข้อต่อ
mc.select(cl=1)
kho = [mc.joint(p=[0,0,0]),mc.joint(p=[0,-0.3,chutmun]),mc.joint(p=[0,-0.3,-chutmun])]
sk = mc.skinCluster(kho,pkmb)[0]
mc.skinPercent(sk,pkmb+'.vtx[%d:%d]'%(n_vtx_bon,n_vtx_pkmb-1),tv=(kho[0],1))
mc.skinPercent(sk,pkmb+'.vtx[0:%d]'%(n_vtx_bon-1),tv=(kho[1],1))