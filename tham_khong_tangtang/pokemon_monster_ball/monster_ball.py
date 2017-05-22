# -*- coding: utf-8 -*-

r = 5 # รัศมี

# สร้างสี
phiu_daeng = mc.shadingNode('blinn',asShader=1,n='phiu_daeng')
mc.setAttr(phiu_daeng+'.c',1,0,0,typ='double3')
mc.setAttr(phiu_daeng+'.it',0.5,0.5,0.5,typ='double3')
phiu_khao = mc.shadingNode('blinn',asShader=1,n='phiu_khao')
mc.setAttr(phiu_khao+'.c',1,1,1,typ='double3')
phiu_dam = mc.shadingNode('blinn',asShader=1,n='phiu_dam')
mc.setAttr(phiu_dam+'.c',0,0,0,typ='double3')

# ใส่แอมเบียนต์
for mat in [phiu_daeng,phiu_khao,phiu_dam]:
    mc.setAttr(mat+'.ambc',0.5,0.5,0.5,typ='double3')

# ส่วนทรงกลมหลัก
mball = mc.polySphere(r=r-0.1,sy=24,sx=48)[0]
mc.polyExtrudeFacet(sx=1+0.1/(r-0.1),sy=1+0.1/(r-0.1),sz=1+0.1/(r-0.1))
lop1 = mc.polyCylinder(h=1,r=1.5,sx=24,ax=[0,0,1])[0]
mc.move(0,0,r-0.1)
lop2 = mc.polyCylinder(h=0.6,r=5.5,sx=24)[0]
lop3 = mc.duplicate(lop1,lop2)
mball = mc.polyCBoolOp(mball,lop1,lop2,op=2,ch=0)[0]

# ส่วนสีดำด้านในตรงกลาง
naib = mc.polySphere(r=r-0.2,sy=24,sx=48)[0]
mc.hyperShade(a=phiu_dam)
mc.polyExtrudeFacet(sx=1+0.1/(r-0.2),sy=1+0.1/(r-0.2),sz=1+0.1/(r-0.2))
naib = mc.polyCBoolOp(naib,lop3,op=3,ch=0)[0]

# แยกส่วนด้านล่างกับด้านบน
lang,bon = mc.polySeparate(mball,ch=0)
mball = mc.listRelatives(p=1)[0]
mc.select(bon)
mc.hyperShade(a=phiu_daeng)
n_na_bon = mc.polyEvaluate(f=1)
mc.select(lang)
lang = mc.rename('lang')
mc.hyperShade(a=phiu_khao)

# ส่วนปุ่มสีขาว
pum = mc.polyCylinder(h=0.2,r=1,sx=24,ax=[0,0,1])[0]
mc.move(0,0,r-0.1)
mc.hyperShade(a=phiu_khao)
mc.select(pum+'.f[25]')
mc.polyExtrudeFacet(sx=0.75,sy=0.75)
mc.polyExtrudeFacet(ltz=0.2)

# รวมส่วนดำตรงกลางกับผิวด้านบน
bon = mc.polyUnite(bon,pum,naib,ch=0,n='bon')[0]
mc.parent(bon,mball)
n_vtx_bon = mc.polyEvaluate(bon,v=1)
pkmb = mc.polyUnite([bon,lang],ch=0,n='pkmb')[0]
n_vtx_pkmb = mc.polyEvaluate(pkmb,v=1)

mc.select(pkmb+'.f[0:%d]'%(n_na_bon-1))
mc.polyProjection(md='y') # กาง uv จากด้านบน

mc.select(cl=1)
# สร้างข้อต่อ
kho = [mc.joint(p=[0,0,0]),mc.joint(p=[0,-0.3,0.1-r]),mc.joint(p=[0,-0.3,r-0.1])]
sk = mc.skinCluster(kho,pkmb)[0] # เชื่อมโพลิกอนกับข้อ
mc.skinPercent(sk,pkmb+'.vtx[%d:%d]'%(n_vtx_bon,n_vtx_pkmb-1),tv=(kho[0],1))
mc.skinPercent(sk,pkmb+'.vtx[0:%d]'%(n_vtx_bon-1),tv=(kho[1],1))