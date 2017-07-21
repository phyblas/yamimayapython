# -*- coding: utf-8 -*-
import maya.cmds as mc
import math,random
random.seed(0)
mc.nurbsToPolygonsPref(f=3)



# ผิว
phiu_phanang = mc.shadingNode('blinn',asShader=1,n='phiu_phanang') # ผิวผนัง
mc.setAttr(phiu_phanang+'.ambc',0.5,0.5,0.5,typ='double3')
mc.setAttr(phiu_phanang+'.sro',0.3)
mc.setAttr(phiu_phanang+'.sc',0.6,0.6,0.6,typ='double3')
mc.setAttr(phiu_phanang+'.c',1,0.986,0.834,typ='double3')

phiu_kropnatang = mc.duplicate(phiu_phanang,n='phiu_kropnatang')[0] # ผิวกรอบหน้าต่าง
mc.setAttr(phiu_kropnatang+'.c',0.29,0.2,0.058,typ='double3')
mc.setAttr(phiu_kropnatang+'.sc',0.9,0.9,0.9,typ='double3')

phiu_yangkropnatang = mc.duplicate(phiu_phanang,n='phiu_yangkropnatang')[0] # ผิวยางกรอบหน้าต่าง
mc.setAttr(phiu_yangkropnatang+'.c',0.7,0.7,0.7,typ='double3')
mc.setAttr(phiu_yangkropnatang+'.sc',0.1,0.1,0.1,typ='double3')

phiu_phaman = mc.duplicate(phiu_phanang,n='phiu_phaman')[0] # ผิวผ้าม่าน
mc.setAttr(phiu_phaman+'.c',0.7,0.92,0.7,typ='double3')
mc.setAttr(phiu_phaman+'.sc',0.1,0.1,0.1,typ='double3')


phiu_thisiap = mc.duplicate(phiu_phanang,n='phiu_thisiap')[0] # ผิวที่เสียบบัตรแอร์
mc.setAttr(phiu_thisiap+'.c',0.59,0.58,0.44,typ='double3')

phiu_chothisiap = mc.duplicate(phiu_phanang,n='phiu_chothisiap')[0] # ผิวจอที่เสียบบัตรแอร์
mc.setAttr(phiu_chothisiap+'.c',0.16,0.21,0.08,typ='double3')

phiu_pratu = mc.duplicate(phiu_phanang,n='phiu_pratu')[0] # ผิวประตู
mc.setAttr(phiu_pratu+'.c',0.81,0.67,0.38,typ='double3')

phiu_lotfai = mc.duplicate(phiu_phanang,n='phiu_lotfai')[0] # ผิวหลอดไฟ
mc.setAttr(phiu_lotfai+'.c',0.8,0.8,0.7,typ='double3')
mc.setAttr(phiu_lotfai+'.sc',0.9,0.9,0.9,typ='double3')

phiu_khoplotfai = mc.duplicate(phiu_phanang,n='phiu_khoplotfai')[0] # ผิวขอบหลอดไฟ
mc.setAttr(phiu_khoplotfai+'.c',0.7,0.7,0.6,typ='double3')

phiu_lotfaikhao = mc.duplicate(phiu_phanang,n='phiu_lotfaikhao')[0] # ผิวตัวหลอดไฟ
mc.setAttr(phiu_lotfaikhao+'.c',0.8,0.8,0.8,typ='double3')
mc.setAttr(phiu_lotfaikhao+'.sc',0,0,0,typ='double3')

phiu_ruto = mc.duplicate(phiu_phanang,n='phiu_ruto')[0] # ผิวรูที่โต๊ะ
mc.setAttr(phiu_ruto+'.c',0.7,0.7,0.7,typ='double3')

phiu_kaoi = mc.duplicate(phiu_phanang,n='phiu_kaoi')[0] # ผิวเก้าอี้
mc.setAttr(phiu_kaoi+'.c',0.16,0.5,0.44,typ='double3')

phiu_saotiang = mc.duplicate(phiu_phanang,n='phiu_saotiang')[0] # ผิวเสาเตียง
mc.setAttr(phiu_saotiang+'.c',1,0.86,0.57,typ='double3')

phiu_kha = mc.duplicate(phiu_phanang,n='phiu_kha')[0] # ผิวขาเสาเตียง
mc.setAttr(phiu_kha+'.c',0.1,0.1,0.1,typ='double3')

phiu_thinon1 = mc.duplicate(phiu_phanang,n='phiu_thinon1')[0] # ผิวที่นอนและหมอน 1
mc.setAttr(phiu_thinon1+'.c',1,0.71,0.79,typ='double3')
mc.setAttr(phiu_thinon1+'.sc',0.1,0.1,0.1,typ='double3')

phiu_thinon2 = mc.duplicate(phiu_thinon1,n='phiu_thinon2')[0] # ผิวที่นอนและหมอน 2
mc.setAttr(phiu_thinon2+'.c',0.84,0.77,1,typ='double3')

phiu_linchak = mc.duplicate(phiu_saotiang,n='phiu_linchak')[0] # ผิวลิ้นชัก
mc.setAttr(phiu_linchak+'.c',1,0.9,0.7,typ='double3')

phiu_ea = mc.duplicate(phiu_saotiang,n='phiu_ea')[0] # ผิวแอร์
mc.setAttr(phiu_linchak+'.c',1,0.88,0.69,typ='double3')

phiu_saikhao = mc.duplicate(phiu_saotiang,n='phiu_saikhao')[0] # ผิวสายขาว
mc.setAttr(phiu_saikhao+'.c',0.8,0.8,0.8,typ='double3')

phiu_tho = mc.duplicate(phiu_saotiang,n='phiu_tho')[0] # ผิวท่อ
mc.setAttr(phiu_tho+'.c',0.4,0.4,0.4,typ='double3')
mc.setAttr(phiu_tho+'.sc',0.1,0.1,0.1,typ='double3')

phiu_loha = mc.duplicate(phiu_phanang,n='phiu_loha')[0] # ผิวโลหะ
mc.setAttr(phiu_loha+'.c',0.5,0.5,0.5,typ='double3')
mc.setAttr(phiu_loha+'.sc',1,1,1,typ='double3')

phiu_thichap = mc.duplicate(phiu_loha,n='phiu_thichap')[0] # ผิวที่จับ
mc.setAttr(phiu_thichap+'.c',0.35,0.35,0.35,typ='double3')

phiu_yuetea = mc.duplicate(phiu_loha,n='phiu_yuetea')[0] # ผิวที่จับ
mc.setAttr(phiu_yuetea+'.c',0.09,0.19,0.17,typ='double3')

phiu_muet = mc.shadingNode('lambert',asShader=1,n='phiu_muet') # ผิวมืด
mc.setAttr(phiu_muet+'.c',0,0,0,typ='double3')

phiu_phuen = mc.duplicate(phiu_phanang,n='phiu_phuen')[0] # ผิวพื้น
lai_phuen = mc.shadingNode('granite',at=1)
mc.connectAttr(lai_phuen+'.oc',phiu_phuen+'.c')
for at,v in zip(['color1','color2','color3','fillerColor'],[(0.08,0.097,0.0915),(0.17,0.21,0.24),(0.88,1.0,0.999),(0.59,0.59,0.59)]):
    mc.setAttr(lai_phuen+'.'+at,*v,typ='double3')
for at,v in zip(['cellSize','density','mixRatio','spottyness','randomness','threshold'],[10,0.8,0.5,0.1,1,0.8]):
    mc.setAttr(lai_phuen+'.'+at,v)
ple = mc.shadingNode('place3dTexture',au=1)
mc.defaultNavigation(ce=1,s=ple,d=lai_phuen)

phiu_khopphuen = mc.duplicate(phiu_phuen,n='phiu_khopphuen')[0] # ผิวแถวขอบพื้น
lai_khopphuen = mc.duplicate(lai_phuen)[0]
mc.connectAttr(lai_khopphuen+'.oc',phiu_khopphuen+'.c')
for at,v in zip(['color1','color2','color3','fillerColor'],[(0.047,0.057,0.054),(0.14,0.17,0.19),(0.947,1,1),(0.36, 0.36, 0.36)]):
    mc.setAttr(lai_khopphuen+'.'+at,*v,typ='double3')
mc.setAttr(lai_khopphuen+'.cellSize',5)
ple = mc.shadingNode('place3dTexture',au=1)
mc.defaultNavigation(ce=1,s=ple,d=lai_khopphuen)

phiu_to = mc.duplicate(phiu_phanang,n='phiu_to')[0] # ผิวโต๊ะไม้
lai_to = mc.shadingNode('wood',at=1)
mc.connectAttr(lai_to+'.oc',phiu_to+'.c')
for at,v in zip(['fillerColor','veinColor','grainColor'],[(0.82,0.67,0.41),(0.81,0.44,0.23),(0.59,0.26,0)]):
    mc.setAttr(lai_to+'.'+at,*v,typ='double3')
for at,v in zip(['veinSpread','layerSize','amplitudeY'],[1,1,0.4]):
    mc.setAttr(lai_to+'.'+at,v)
ple = mc.shadingNode('place3dTexture',au=1)
mc.defaultNavigation(ce=1,s=ple,d=lai_to)
for at,v in zip(['rx','sx','sy','sz'],[125,5,5,5]):
    mc.setAttr(ple+'.'+at,v)

phiu_chanbon = mc.duplicate(phiu_to,n='phiu_chanbon')[0] # ผิวชั้นไม้
phiu_tiang = mc.duplicate(phiu_to,n='phiu_tiang')[0]
phiu_bandai = mc.duplicate(phiu_to,n='phiu_bandai')[0]
phiu_tusueapha = mc.duplicate(phiu_to,n='phiu_tusueapha')[0]
phiu_chanwang = mc.duplicate(phiu_to,n='phiu_chanwang')[0]
for phiu in [phiu_chanbon,phiu_tiang,phiu_bandai,phiu_tusueapha,phiu_chanwang]:
    lai_chan = mc.duplicate(lai_to,n='lai_chan')[0]
    mc.connectAttr(lai_chan+'.oc',phiu+'.c')
    ple_chan = mc.duplicate(ple)[0]
    mc.defaultNavigation(ce=1,s=ple_chan,d=lai_chan)
    mc.setAttr(ple_chan+'.rx',90)
    mc.setAttr(ple_chan+'.ry',45)
    for at,v in zip(['fillerColor','veinColor'],[(0.81,0.61,0.25),(0.68,0.13,0)]):
        mc.setAttr(lai_chan+'.'+at,*v,typ='double3')
    mc.setAttr(lai_chan+'.veinSpread',4)

phiu_paithisiap = mc.duplicate(phiu_phanang,n='phiu_paithisiap')[0] # ผิวป้ายที่เสียบบัตรแอร์
#mc.setAttr(phiu_paithisiap+'.c',0.5,0.22,0.08,typ='double3')
lai_pai = mc.shadingNode('file',at=1)
mc.connectAttr(lai_pai+'.oc',phiu_paithisiap+'.c')
mc.setAttr(lai_pai+'.ftn','jiong.png',typ='string')

phiu_krachok = mc.duplicate(phiu_kropnatang,n='phiu_krachok')[0] # ผิวกระจก
mc.setAttr(phiu_krachok+'.c',0,0,0,typ='double3')
mc.setAttr(phiu_krachok+'.sc',1,1,1,typ='double3')
mc.setAttr(phiu_krachok+'.it',0.9,0.9,0.9,typ='double3')



# พื้นและผนัง
phuen = mc.polyCube(w=430,h=286,d=340,sy=4,sz=3)[0]
mc.move(430/2.,286/2.,340/2.)
mc.polyNormal()
mc.scale(87*3./340,[phuen+'.f[%d]'%i for i in [15,18,21,24,27,30,33,36]],z=1)
mc.move(15,[phuen+'.e[%s]'%s for s in [1,10,'42:44','59:61']],y=1)
mc.move(81,[phuen+'.e[%s]'%s for s in [2,9,'45:47','62:64']],y=1)
mc.move(286-64,[phuen+'.e[%s]'%s for s in [3,8,'48:50','65:67']],y=1)
mc.move(20,[phuen+'.e[%d]'%i for i in [72,74]],z=1)
mc.move(170,[phuen+'.e[%d]'%i for i in [73,75]],z=1)

sao = mc.polyCube(w=44,h=286,d=19,sy=4)[0]
mc.move(44/2.,286/2.,19/2.)
mc.move(15,[sao+'.e[%d]'%s for s in [1,8,30,33]],y=1)
mc.move(286-64,[sao+'.e[%d]'%s for s in [3,6,32,35]],y=1)
sao = [sao,mc.duplicate(sao)[0]]
mc.move(44/2.,286/2.,340-19/2.)
sao.append(mc.polyCube(w=10,h=64,d=340)[0])
mc.move(430-10/2.,286-64/2.,340/2.)
sao.append(mc.polyCube(w=44,h=11,d=340)[0])
mc.move(44/2.,286-64+11/2.,340/2.)
phuen = mc.polyCBoolOp(phuen,sao,op=1,ch=0,n='phuen')[0]
mc.hyperShade(a=phiu_phanang)

mc.polyExtrudeFacet([phuen+'.f[%s]'%i for i in [0,'2:3','6:8','12:14','19:20',45,51,'54:55']])
mc.move(0.5,[phuen+'.f[%s]'%i for i in [8,14,20,45,55]],x=1,r=1)
mc.move(-0.5,[phuen+'.f[%s]'%i for i in [2,6,12]],x=1,r=1)
mc.move(-0.5,[phuen+'.f[%s]'%i for i in [0,51]],z=1,r=1)
mc.move(0.5,[phuen+'.f[%s]'%i for i in [19,54]],z=1,r=1)
mc.polyExtrudeFacet([phuen+'.f[%s]'%i for i in [3,7,13]],off=10)
mc.delete([phuen+'.f[%s]'%i for i in [6,11,17,60]]) # เจาะประตู
mc.select(phuen+'.f[25]') # เจาะหน้าต่าง
mc.polyExtrudeFacet(ltz=-4,off=0.5)
mc.delete()
mc.polyExtrudeEdge(phuen+'.e[117]',tx=20)
g = []
for i in range(mc.polyEvaluate(phuen,f=1)):
    s = phuen+'.f[%d]'%i
    bb = mc.xform(s,q=1,bb=1,ws=1)
    if(bb[1]<1 and i not in [3,6,11]):
       g.append(s) 
mc.select(g)
mc.hyperShade(a=phiu_khopphuen)
mc.polyAutoProjection(ps=0.2)
mc.select([phuen+'.f[%s]'%i for i in [3,6,11]])
mc.hyperShade(a=phiu_phuen)
mc.polyProjection(rx=90,ry=180,rz=0,psu=40,psv=40)



# หน้าต่าง
krop = []
krop.append(mc.polyCube(w=6,h=1,d=152,sx=3)[0])
mc.move(-3,0.5)
krop.append(mc.polyCube(w=6,h=8,d=152,sx=3)[0])
mc.move(-3,89+4)
for i in [0,1]:
    mc.polyExtrudeFacet(krop[i]+'.f[4:5]',ltz=2)
    mc.select(krop[i]+'.f[5]')
    mc.polyExtrudeFacet(ltz=2)
    mc.polyExtrudeFacet(sx=0.5,sz=(152-2.)/152)
    mc.move(-0.3,r=1)
    mc.polyExtrudeFacet(ltz=-1)
    mc.select(krop[i]+'.f[4]')
    mc.polyExtrudeFacet(sx=0.8,sz=(152-2.)/152)
    mc.move(0.1,r=1)
    mc.polyExtrudeFacet(ltz=-1)
    mc.select(krop[i]+'.f[3]')
    mc.polyExtrudeFacet(sx=0.9,sz=(152-2.)/152)
    mc.move(0.05,r=1)
    mc.polyExtrudeFacet(ltz=-0.9)
    mc.select(krop[i]+'.f[13]')
    mc.polyExtrudeFacet(ltz=1)
    mc.select(krop[i]+'.f[50]')
    mc.polyExtrudeFacet(sx=0.9,sz=(152-2.)/152)
    mc.move(0.05,r=1)
    mc.polyExtrudeFacet(ltz=-0.9)

krop.append(mc.polyCube(w=6,h=3,d=152,sx=3)[0])
mc.move(-3,141-0.5)
for i in [1,2]:
    mc.select(krop[i]+'.f[11]')
    mc.polyExtrudeFacet(sx=0.5,sz=(152-2.)/152)
    mc.move(-0.3,r=1)
    mc.polyExtrudeFacet(ltz=-1)
    mc.select(krop[i]+'.f[10]')
    mc.polyExtrudeFacet(sx=0.8,sz=(152-2.)/152)
    mc.move(0.1,r=1)
    mc.polyExtrudeFacet(ltz=-1)
    mc.select(krop[i]+'.f[9]')
    mc.polyExtrudeFacet(sx=0.9,sz=(152-2.)/152)
    mc.move(0.05,r=1)
    
mc.select(krop[1]+'.f[48]')
mc.polyExtrudeFacet(sx=0.9,sz=(152-2.)/152)
mc.move(0.05,r=1)
mc.polyExtrudeFacet(ltz=-0.9)

mc.select(krop[2]+'.f[13]')
mc.polyExtrudeFacet(ltz=1)
mc.select(krop[2]+'.f[34]')
mc.polyExtrudeFacet(sx=0.9,sz=(152-2.)/152)
mc.move(0.05,r=1)
mc.polyExtrudeFacet(ltz=-0.9)

krop.append(mc.polyCube(w=6,h=142,d=3,sx=3)[0])
mc.move(-3,142/2.,74.5)
mc.select(krop[-1]+'.f[8]')
mc.polyExtrudeFacet(sx=0.5,sy=(142-2.)/142)
mc.move(-0.3,r=1)
mc.polyExtrudeFacet(ltz=-1)
mc.select(krop[-1]+'.f[7]')
mc.polyExtrudeFacet(sx=0.8,sy=(142-2.)/142)
mc.move(0.1,r=1)
mc.polyExtrudeFacet(ltz=-1)
mc.select(krop[-1]+'.f[6]')
mc.polyExtrudeFacet(sx=0.9,sy=(142-2.)/142)
mc.move(0.05,r=1)
mc.polyExtrudeFacet(ltz=-0.9)

krop.append(mc.duplicate(krop[-1])[0])
mc.scale(-1,krop[-1],p=[0,0,0],z=1)
krop = mc.polyUnite(krop,ch=0)[0]
mc.hyperShade(a=phiu_kropnatang)

natang = []
for h,y in zip([86,40],[4,100]):
    natang.append(mc.polyCube(w=2,h=h,d=76)[0])
    mc.hyperShade(a=phiu_kropnatang)
    mc.move(-1.9,y+h/2.,-76/2.+2)
    mc.select(natang[-1]+'.f[4:5]')
    mc.polyExtrudeFacet(sz=(76+1.)/76,off=5)
    mc.move(0.5,z=1,r=1)
    mc.hyperShade(a=phiu_yangkropnatang)
    mc.polyExtrudeFacet(off=0.3,ltz=-0.5)
    mc.polyExtrudeFacet(off=-0.3)
    mc.polyExtrudeFacet(ltz=-0.5)
    mc.polyMergeVertex(d=0.001)
    mc.delete(natang[-1]+'.f[4:5]')
    mc.select(natang[-1]+'.f[2]')
    mc.polyExtrudeFacet(sy=(h-2.)/h,sx=1.5/2)
    mc.polyExtrudeFacet(ltz=-1)
    
    krachok = mc.polyCube(w=1,h=h-10,d=67)[0]
    mc.hyperShade(a=phiu_krachok)
    mc.move(-1.9,y+h/2.,-76/2.+2+0.5)
    natang[-1] = mc.polyUnite(natang[-1],krachok,ch=0)[0]

    natang.append(mc.polyCube(w=2,h=h+2,d=76)[0])
    mc.hyperShade(a=phiu_kropnatang)
    mc.move(-3.9,y+h/2.-1,76/2.-2)
    mc.select(natang[-1]+'.f[4:5]')
    mc.polyExtrudeFacet(sz=(76+1.)/76,sy=h/(h+2.),off=5)
    mc.move(0,1,-0.5,r=1)
    mc.hyperShade(a=phiu_yangkropnatang)
    mc.polyExtrudeFacet(off=0.3,ltz=-0.5)
    mc.polyExtrudeFacet(off=-0.3)
    mc.polyExtrudeFacet(ltz=-0.5)
    mc.polyMergeVertex(d=0.001)
    mc.delete(natang[-1]+'.f[4:5]')
    mc.select(natang[-1]+'.f[0]')
    mc.polyExtrudeFacet(sy=(h-2.)/h,sx=1.5/2)
    mc.polyExtrudeFacet(ltz=-1)
    
    krachok = mc.polyCube(w=1,h=h-10,d=67)[0]
    mc.hyperShade(a=phiu_krachok)
    mc.move(-3.9,y+h/2.,76/2.-2-0.5)
    natang[-1] = mc.polyUnite(natang[-1],krachok,ch=0)[0]


# ราวม่าน
raoman = mc.polyCube(w=2,h=2,d=160)[0]
mc.hyperShade(a=phiu_saikhao)
mc.move(5,140,3)
mc.select('.f[3]')
mc.polyExtrudeFacet(sx=0.4,sz=156./160)
mc.polyExtrudeFacet(ltz=-1)
krop = mc.polyUnite(krop,raoman)[0]

# ผ้าม่าน
phaman = mc.polyPlane(w=157.75,h=150,sx=420,sy=1,ax=[1,0,0],n='phaman')[0]
mc.hyperShade(a=phiu_phaman)
for i in range(mc.polyEvaluate(v=1)):
    mc.select(phaman+'.vtx[%d]'%i)
    mc.move(random.uniform(2,2.2),random.uniform(-0.15,0.15),157.75/2,r=1)
kang = mc.duplicate(phaman,n='kangman')[0]
mc.select(cl=1)
kho = []
for i in range(421):
   kho.append(mc.joint(p=[2.1,0,i*0.375]))
mc.skinCluster(kho,phaman)

for i in range(0,421):
    mc.rotate(0,25*math.cos((0.5+i)*math.pi/15),kho[i])
mc.delete(phaman,ch=1)
mc.delete(kho)
mc.blendShape(kang,phaman)
mc.delete(kang)
mc.move(0,146.5,19,phaman)
    


nv1 = mc.polyEvaluate(krop,v=1)
nv2 = mc.polyEvaluate(natang[0],v=1)
natang = mc.polyUnite(krop,natang,ch=0,n='natang')[0]

# เชื่อมกับข้อเพื่อให้เปิดปิดหน้าต่างได้
mc.select(cl=1)
kho = [mc.joint(p=[0,0,0],n='kraduk_natang')]
kho.append(mc.joint(p=[-1.9,47,-76/2.+2+0.5]))
kho.append(mc.joint(p=[-1.9,47,-20+2+0.5]))
mc.select(kho[0])
kho.append(mc.joint(p=[-3.9,47,76/2.-2-0.5]))
kho.append(mc.joint(p=[-3.9,47,20-2-0.5]))
mc.select(kho[0])
kho.append(mc.joint(p=[-1.9,120,-76/2.+2+0.5]))
kho.append(mc.joint(p=[-1.9,120,-20+2+0.5]))
mc.select(kho[0])
kho.append(mc.joint(p=[-3.9,120,76/2.-2-0.5]))
kho.append(mc.joint(p=[-3.9,120,20-2-0.5]))
sk = mc.skinCluster(kho,natang)[0]
mc.skinPercent(sk,natang+'.vtx[0:%d]'%(nv1-1),tv=[(kho[0],1)])
mc.skinPercent(sk,natang+'.vtx[%d:%d]'%(nv1,nv1+nv2-1),tv=[(kho[1],1)])
mc.skinPercent(sk,natang+'.vtx[%d:%d]'%(nv1+nv2,nv1+nv2*2-1),tv=[(kho[3],1)])
mc.skinPercent(sk,natang+'.vtx[%d:%d]'%(nv1+nv2*2,nv1+nv2*3-1),tv=[(kho[5],1)])
mc.skinPercent(sk,natang+'.vtx[%d:%d]'%(nv1+nv2*3,nv1+nv2*4-1),tv=[(kho[7],1)])
mc.move(-4,81,95,kho[0])
kraduk_natang = kho



# รูปลั๊กไฟ
ruplak = mc.polyCube(w=12,h=7,d=0.4)[0]
mc.hyperShade(a=phiu_saikhao)
mc.move(0,0,0.2)
mc.select(ruplak+'.f[0]')
mc.polyExtrudeFacet(off=0.2,ltz=0.1)
mc.polyExtrudeFacet(off=0.7,ltz=0.1)
mc.polyExtrudeFacet(sx=7.1/10.2,sy=3.1/5.2)
mc.polyExtrudeFacet(ltz=-0.5)
mc.polyExtrudeFacet(sx=7/7.1,sy=3/3.1)
mc.polyExtrudeFacet(ltz=0.6)

ru = [mc.polyCube(w=0.2,h=1,d=0.5)[0]]
mc.move(-2.7,0.5,0.35)
mc.polyExtrudeFacet('.f[0]',sx=3,sy=1.1)
mc.polyExtrudeFacet('.f[0]',ltz=0.101,off=-0.1)
mc.polyBevel('.e[25]',o=0.1)
ru.append(mc.polyCube(w=0.2,h=0.8,d=0.5)[0])
mc.move(-1.3,0.5,0.35)
mc.polyExtrudeFacet('.f[0]',sx=3,sy=1.1/0.8)
mc.polyExtrudeFacet('.f[0]',ltz=0.101,off=-0.1)
mc.polyBevel('.e[23]',o=0.1)
ru.append(mc.polyCube(w=0.6,h=0.4,d=0.5)[0])
mc.move(-2,-0.8,0.35)
mc.polyExtrudeFacet('.f[1]',ltz=0.1,sx=0.3/0.4)
mc.polyExtrudeFacet('.f[1]',ltz=0.1,sx=0.1/0.3)
mc.polyExtrudeFacet('.f[0]','.f[6]','.f[10]',off=-0.05,ty=-0.05)
mc.scale(0,'.e[33]','.e[38]','.e[43]',p=[-3,0,0])
mc.scale(0,'.e[30]','.e[35]','.e[40]',p=[-1.,0,0])
mc.polyExtrudeFacet('.f[0]','.f[6]','.f[10]',off=-0.1,ltz=0.101)
mc.scale(0.6,'.e[42:43]')
ru.extend(mc.duplicate(ru))
mc.move(4,ru[-3:],r=1)
ru = mc.polyUnite(ru,ch=0)[0]
mc.hyperShade(a=phiu_saikhao)
ruplak = mc.polyCBoolOp(ruplak,ru,op=2,ch=0,n='ruplak')[0]
mc.select(ruplak+'.f[15:31]')
mc.hyperShade(a=phiu_ea)
mc.select([ruplak+'.f[%d]'%i for i in [36,51,66,72,79,95,110,138,131,125]])
mc.hyperShade(a=phiu_muet)
mc.move(99,108,ruplak)

ruplak2 = mc.duplicate(ruplak)[0]
mc.scale(1,1,-1,ruplak2)
mc.move(0,0,340,ruplak2,r=1)



# สวิตช์ไฟ
switchfai = mc.polyCube(w=12,h=7,d=0.4,sx=2,n='switchfai')[0]
mc.hyperShade(a=phiu_ea)
mc.move(0,0,0.2)
mc.select(switchfai+'.f[0:1]')
mc.polyExtrudeFacet(off=0.2,ltz=0.1)
mc.polyExtrudeFacet(off=0.7,ltz=0.1)
mc.polyExtrudeFacet(kft=0,off=0.6,lsx=3.7/5.1)
mc.hyperShade(a=phiu_saikhao)
mc.polyExtrudeFacet(ltz=0.1)
mc.polyExtrudeFacet(off=0.3)
mc.polyExtrudeFacet(ltz=0.2,rx=-5)
mc.polyBevel([switchfai+'.e[%d]'%i for i in [10,12,16,18,19,23,26,28]],o=0.2)
mc.polySoftEdge(switchfai,a=89)
mc.rotate(-90,switchfai,y=1,p=[0,0,0])
mc.move(430,104,115,switchfai,r=1)



# หลอดไฟ
lotfai = [mc.polyCube(w=120,h=1,d=13)[0]]
mc.hyperShade(a=phiu_lotfai)
mc.move(0,-0.5)
mc.select('.f[3]')
mc.polyExtrudeFacet(ltz=3,sz=7/13.)

lotfai.append(mc.polyCylinder(r=2,h=1.5,ax=[1,0,0],sx=12)[0])
mc.hyperShade(a=phiu_lotfai)
mc.move(60-1.25,-6)
mc.rotate(15)
mc.select('.f[2:6]')
mc.scale(1,0,p=[0,-4,0],ws=1)
lotfai.append(mc.duplicate(lotfai[1])[0])
mc.scale(-1,lotfai[2],p=[0,0,0])

lotfai.append(mc.polyCylinder(r=1.25,h=105,sx=24,ax=[1,0,0])[0])
mc.hyperShade(a=phiu_lotfaikhao)
mc.move(0,-6)
mc.select('.f[24:25]')
mc.hyperShade(a=phiu_khoplotfai)
mc.polyExtrudeFacet(ltz=5)
mc.polyExtrudeFacet(off=0.2)
mc.hyperShade(a=phiu_lotfai)
mc.polyExtrudeFacet(ltz=0.5)
mc.delete()

lotfai = mc.polyUnite(lotfai,ch=0,n='lotfai1')
mc.move(-100+215,286,170,lotfai,r=1)
mc.polySoftEdge(lotfai,a=89)
lotfai += mc.duplicate(lotfai)
mc.move(200,r=1)



# ที่เสียบบัตรแอร์
thisiap = mc.polyCube(w=11.3,h=15.5,d=3.5,sy=2,n='thisiap')[0]
mc.hyperShade(a=phiu_thisiap)
mc.select(thisiap+'.f[0:1]')
mc.polyExtrudeFacet(off=0.2)
mc.polyExtrudeFacet(ltz=0.1)
mc.polyExtrudeFacet(off=-0.2)
mc.polyExtrudeFacet(ltz=0.9)
mc.polyExtrudeFacet(off=0.9,ltz=1.5)
mc.select(thisiap+'.f[1]')
mc.polyExtrudeFacet(off=0.6,ltz=1)
mc.polyExtrudeFacet(sx=6.8/8.3,sy=1.8/5.65)
mc.polyExtrudeFacet(off=0.1,ltz=-0.1)
mc.hyperShade(a=phiu_chothisiap)
mc.select(thisiap+'.f[0]')
mc.polyExtrudeFacet(off=0.2)
mc.hyperShade(a=phiu_paithisiap)
mc.polyProjection(t='planar',md='z')
mc.select(thisiap+'.f[6:7]')
mc.polyExtrudeFacet(sy=5.9/15.5,sz=1.5/3.5)
mc.move(0.2,-1.5,r=1)
mc.hyperShade(a=phiu_kha)
mc.polyExtrudeFacet(ltz=0.3)
mc.polyExtrudeFacet(sy=5.4/5.9,sz=0.15/3.5)
mc.move(0.2,r=1)
mc.polyExtrudeFacet(ltz=-10)
mc.rotate(-90,thisiap,y=1)
mc.move(430-3.5/2,120,106,thisiap)



# ประตู
pratu = mc.polyCube(w=3.5,h=185,d=82)[0]
mc.hyperShade(a=phiu_pratu)
mc.move(430+3.5/2,185/2.,170)
khoppratu = mc.polyCube(w=16.5,h=222,d=87)[0]
mc.move(430-2+16.5/2,222/2.,170)
lop = mc.polyCube(w=16.5,h=221,d=83)[0]
mc.move(430-2+16.5/2,221/2.,170)
khoppratu = mc.polyCBoolOp(khoppratu,lop,op=2,ch=0)[0]
mc.select(khoppratu+'.f[7:9]')
mc.polyExtrudeFacet(sx=12.5/16.5)
mc.polyExtrudeFacet()
mc.scale(1,184.5/221,81./83,p=[0,0,170])
lop = [mc.duplicate(pratu)[0],mc.duplicate(pratu)[0]]
mc.move(35.5,lop[1]+'.f[1]',y=1,r=1)
mc.move(185+2,lop[1]+'.f[3]',y=1)
mc.move(10,lop[1]+'.f[4]',x=1,r=1)
khoppratu = mc.polyCBoolOp(khoppratu,lop,op=2,ch=0)[0]
mc.polyExtrudeFacet(khoppratu+'.f[32:35]',sy=25.5/33.5,sz=74./82)
bonpratu = mc.polyCube(w=12.5,h=25.5,d=4)[0]
mc.move(436.25,203.75,170)
mc.delete(bonpratu+'.f[1]',bonpratu+'.f[3]')

sisi = [mc.polyCube(w=3,h=0.5,d=35)[0]]
mc.rotate(-60,z=1,p=[1.5,-0.25,0])
mc.move(430,191+0.25,150.5)
for i in range(1,8):
    sisi.append(mc.duplicate(sisi[-1])[0])
    mc.move(3.2,sisi[-1],y=1,r=1)
sisi.extend(mc.duplicate(sisi))
mc.scale(-1,sisi[8:16],z=1,p=[0,0,170])
mc.scale(1,184./185,81.5/82,pratu)

# กลอนประตู
klon = mc.polyCube(w=3.3,h=7,d=0.1)[0]
mc.move(430+3.3/2,185/2.,170-41+0.05)
mc.select(klon+'.f[5]')
mc.polyExtrudeFacet(ltz=0.1,sy=0.5)
mc.polyExtrudeFacet(ltz=0.5)
mc.polyExtrudeFacet(ltz=0.5,tz=-0.25)

lop = mc.polyCube(w=1.5,h=2.5,d=4)[0]
mc.move(430+3.3/2,185/2.,170-41+0.05)
klon = mc.polyCBoolOp(klon,lop,op=2,ch=0)[0]
mc.hyperShade(a=phiu_loha)

# จุดหมุนประตู
chutmun = mc.polyCylinder(r=0.4,h=0.4,sx=18)[0]
mc.hyperShade(a=phiu_thichap)
mc.move(0,0.2)
mc.select(chutmun+'.f[19]')
nf = [mc.polyEvaluate(f=1)]
for i in range(5):
    mc.polyExtrudeFacet(off=-0.1)
    mc.polyExtrudeFacet(ty=1.6)
    mc.polyExtrudeFacet(off=0.1)
    nf.append(mc.polyEvaluate(f=1))
    mc.polyExtrudeFacet(ty=0.4)
    nf.append(mc.polyEvaluate(f=1))
mc.select([chutmun+'.f[%d:%d]'%(nf[0+2*i],nf[1+2*i]-1) for i in range(5)])
mc.hyperShade(a=phiu_loha)
mc.select([chutmun+'.f[%d:%d]'%(nf[0+2*i],nf[1+2*i]-1) for i in [1,3]])
mc.polyChipOff(kft=1,dup=0)
mc.select([chutmun+'.f[%d]'%i for i in [38,125,182,269,326]])
mc.polyExtrudeFacet()
mc.scale(0,x=1,p=[0.5,0,0])
mc.polyExtrudeFacet(chutmun+'.f[182]',ltz=5)
mc.polyExtrudeFacet([chutmun+'.f[%d]'%i for i in [400,402]],ltz=4.4)
mc.polyExtrudeFacet(chutmun+'.f[125]',ltz=5)
mc.polyExtrudeFacet(chutmun+'.f[412]',ltz=2.4)
mc.polyExtrudeFacet(chutmun+'.f[414]',ltz=6.4)
c = mc.polySeparate(chutmun,ch=0)
mc.move(430-2,10,211,c,r=1)
c.extend(mc.duplicate(c))
mc.move(165,c[5:],y=1)



# ลูกบิด
lukbit = [mc.polyCylinder(r=3.25,h=1,ax=[-1,0,0],sx=24)[0]]
mc.hyperShade(a=phiu_loha)
mc.select(lukbit[0]+'.f[25]')
mc.scale(1,3.5/6.5,3.5/6.5)
mc.polyExtrudeFacet(ltz=1,off=0.4)
mc.polyExtrudeFacet(off=0.1)
mc.polyExtrudeFacet(ltz=1.5)
for i in range(10):
    mc.polyExtrudeFacet(ltz=0.35,off=(i-4.5)/10)
mc.polyExtrudeFacet(ltz=-0.75/2,off=0.7*(1-3**0.5/2))
mc.polyExtrudeFacet(ltz=-0.75*(3**0.5/2-0.5),off=0.7*(3**0.5/2-0.5))
mc.polyExtrudeFacet(ltz=-0.75*(1-3**0.5/2),off=0.7/2)
mc.polyExtrudeFacet(ltz=-1)
mc.polyExtrudeFacet(off=0.05)
mc.polyExtrudeFacet(ltz=2)
mc.polyExtrudeFacet(off=0.1)
mc.polyExtrudeFacet(ltz=-0.1,off=0.1)
mc.move(430-0.5,185/2.,135.5,lukbit)



# รวมส่วนของประตู
khoppratu = mc.polyUnite(khoppratu,bonpratu,sisi,ch=0)[0]
mc.hyperShade(a=phiu_pratu)
pratu = mc.polyUnite(pratu,lukbit,c[0],c[1],c[3],c[5],c[6],c[8],ch=0)[0]
nv1 = mc.polyEvaluate(pratu,v=1)
pratu = mc.polyUnite(pratu,khoppratu,klon,c[2],c[4],c[7],c[9],ch=0,n='pratu')[0]
nv2 = mc.polyEvaluate(pratu,v=1)

# เชื่อมกับข้อเพื่อให้เปิดปิดประตูได้
mc.select(cl=1)
kraduk_pratu = [mc.joint(p=[430-2,0,170],n='kraduk_pratu'),mc.joint(p=[430-2,185/2.,211]),mc.joint(p=[430-2,185/2.,129])]
sk = mc.skinCluster(kraduk_pratu,pratu)[0]
mc.skinPercent(sk,pratu+'.vtx[0:%d]'%(nv2-1),tv=[(kraduk_pratu[0],1)])
mc.skinPercent(sk,pratu+'.vtx[0:%d]'%(nv1-1),tv=[(kraduk_pratu[1],1)])



# โต๊ะ
to = [mc.polyCube(w=180,h=3,d=70)[0]]
mc.move(0,71+3/2.,70/2.)
mc.polyBevel('.e[0:1]',o=1.5,sg=3)
to.append(mc.polyCube(w=2.6,h=71,d=60)[0])
mc.move(-180/2.+0.8+2.6/2.,71/2.,3+60/2.)
to.append(mc.polyCube(w=2.6,h=71,d=60)[0])
mc.move(180/2.-0.8-2.6/2.,71/2.,3+60/2.)
to.append(mc.polyCube(w=180-0.8*2-2.6*2,h=37,d=2)[0])
mc.move(0,71-37/2.,3+1)
mc.delete([to[-1]+'.f[%d]'%i for i in [1,4,5]])
to = mc.polyUnite(to,ch=0)
mc.hyperShade(a=phiu_to)

ru = mc.polyCylinder(r=3.5,h=3,sx=12,sz=1)[0]
mc.move(41.5-180/2.,74-3/2.,11.5)
ru = [ru,mc.duplicate(ru)[0]]
mc.move(180/2.-41.5,74-3/2.,11.5)
to = mc.polyCBoolOp(to,ru,op=2,ch=0)[0]
mc.delete(to+'.f[18:41]')

ru = mc.polyPipe(r=3.5,h=6.8,t=0.1,sa=24,sh=3)[0]
mc.hyperShade(a=phiu_ruto)
g = []
for i in range(mc.polyEvaluate(f=1)):
    s = ru+'.f[%d]'%i
    bb = mc.xform(s,q=1,bb=1,ws=1)
    if(bb[4]<1 and bb[1]>-1):
        g.append(s)
mc.select(g)
mc.scale(0.2/6.8*6,y=1)
mc.move(1.7-0.3,y=1,r=1)
mc.polyExtrudeFacet(ltz=0.3)
mc.scale(1.05,1,1.05)
mc.select(ru+'.e[120:143]')
mc.scale(1.07,0.2,1.07,p=[0,1.7,0])
mc.move(41.5-180/2.,74-3/2.+0.15,11.5,ru)
ru = [ru,mc.duplicate(ru)[0]]
mc.scale(-1,ru[1],x=1,p=[0,0,0])
to = mc.polyUnite(to,ru,ch=0,n='to1')[0]
mc.polyMergeVertex(to,d=0.001)
mc.polySoftEdge(to,a=89)
mc.polyAutoProjection(to,ps=0.1)
mc.move(47+200/2.,0,0,to)

to2 = mc.duplicate(to)[0]
mc.scale(1,1,-1,to2)
mc.move(340,to2,z=1)



# ชั้นหนังสือ
chansai = mc.polyCube(w=30,h=105,d=30)[0]
mc.move(-180/2+30/2.,71+3+105/2.,30/2.)
mc.select(chansai+'.f[0]')
mc.polyExtrudeFacet(off=2)
mc.polyExtrudeFacet(ltz=-28)
kan1 = mc.polyCube(w=26,h=2,d=27)[0]
mc.move(-180/2+30/2.,71+3+105/3.,27/2.+2)
mc.delete(kan1+'.f[2]',kan1+'.f[4:5]')
kan2 = mc.duplicate(kan1)
mc.move(105/3.,y=1,r=1)
chansai = mc.polyUnite(chansai,kan1,kan2,n='chansai',ch=0)[0]
chankhwa = mc.duplicate(chansai,n='chankhwa')[0]
mc.move(180-30,x=1,r=1)
chanbon = mc.polyCube(w=120,h=50,d=30)[0]
mc.move(0,71+3+55+50/2.,30/2.)
mc.select(chanbon+'.f[0]')
mc.polyExtrudeFacet(off=2)
mc.polyExtrudeFacet(ltz=-28)
kan1 = mc.polyCube(w=2,h=46,d=27.5)[0]
mc.move(0,71+3+105-2-46/2.,2+27.5/2)
kan2 = mc.polyCube(w=57.,h=2,d=27)[0]
mc.move(-1-57/2.,71+3+105-2-15,2+27/2.)
kan3 = mc.duplicate(kan2)[0]
mc.move(57+2,r=1)
kan4 = mc.polyCube(w=120,h=8,d=2)[0]
mc.move(0,71+3+55-8/2.,30-1.2)
mc.delete(kan1+'.f[1:3]',kan2+'.f[2]',kan2+'.f[4:5]',kan3+'.f[2]',kan3+'.f[4:5]',kan4+'.f[1]',kan4+'.f[4:5]')
chanbon = mc.polyUnite(chanbon,kan1,kan2,kan3,kan4,chansai,chankhwa,ch=0)[0]
mc.hyperShade(a=phiu_chanbon)
mc.polyAutoProjection(chanbon,ps=0.2,ch=0)



# หลอดไฟโต๊ะ
lotfaito = [mc.polyCube(w=60,h=5.5,d=4)[0]]
mc.hyperShade(a=phiu_lotfai)
mc.move(0,0,-2)
lotfaito.append(mc.polyCylinder(r=1.25,h=1,ax=[1,0,0],sx=12)[0])
mc.hyperShade(a=phiu_lotfai)
mc.move(30-1.5,0,-4-1.25)
mc.rotate(15)
mc.select('.f[5:9]')
mc.scale(1,1,0,p=[0,0,-4],ws=1)
lotfaito.append(mc.duplicate(lotfaito[1])[0])
mc.scale(-1,lotfaito[2],p=[0,0,0])

lotfaito.append(mc.polyCylinder(r=1.25,h=48,sx=24,ax=[1,0,0])[0])
mc.hyperShade(a=phiu_lotfaikhao)
mc.move(0,0,-4-1.25)
mc.select('.f[24:25]')
mc.hyperShade(a=phiu_lotfai)
mc.polyExtrudeFacet(off=-0.2)
mc.polyExtrudeFacet(ltz=3)
mc.polyExtrudeFacet(off=0.2,ltz=0.2)
mc.polyExtrudeFacet(ltz=0.7)
mc.polyExtrudeFacet(off=0.1,ltz=0.1)
mc.delete()
lotfaito = mc.polyUnite(lotfaito)[0]
mc.move(0,71+3+55-4,30-2.2)
mc.polySoftEdge(a=89)
chanbon = mc.polyUnite(chanbon,lotfaito,ch=0,n='chanbon1')[0]
mc.move(47+200/2.)

chanbon2 = mc.duplicate(chanbon)[0]
mc.scale(1,1,-1,chanbon2)
mc.move(340,chanbon2,z=1)



# ตู้ลิ้นชัก
tulinchak = mc.polyCube(w=38,h=64,d=56,sy=2)[0]
mc.hyperShade(a=phiu_linchak)
mc.move(0,3+64/2.,56/2.)
mc.move(65,[tulinchak+'.e[%s]'%i for i in [1,4,'18:19']],y=1)
mc.select(tulinchak+'.f[1]')
mc.polyExtrudeFacet(ltz=2)
mc.select([tulinchak+'.f[%s]'%i for i in [2,12]])
mc.polyExtrudeFacet(off=-0.2)
mc.polyExtrudeFacet(ty=2)
mc.select(tulinchak+'.f[0]',tulinchak+'.f[10]')
mc.polyExtrudeFacet(off=1.5)
mc.select(tulinchak+'.f[0]')
mc.polyExtrudeFacet(tz=-54.5)
mc.polyBevel([tulinchak+'.e[%s]'%i for i in [22,25,33,35,42,'45:50']],o=0.5)
mc.select(tulinchak+'.f[19]')
mc.polyExtrudeFacet(ltz=-2)

g = []
for i in range(mc.polyEvaluate(tulinchak,f=1)):
    s = tulinchak+'.f[%d]'%i
    bb = mc.xform(s,q=1,bb=1,ws=1)
    if(bb[1]>67-0.001):
        g.append(s)
mc.select(g)
mc.hyperShade(a=phiu_saotiang)

# ลิ้นชัก
wang = []
linchak = []
for a,b,c in [(6.3,61.75,-0.5),(14.8,51,2),(39.,23.75,13)]:
    # ส่วนที่วาง
    wang.append(mc.polyCube(w=1.8,h=0.2,d=54,sx=2)[0])
    mc.hyperShade(a=phiu_loha)
    mc.move(-38/2.+1.5+1.8/2,b+0.4-a/2,1.5+54/2.)
    mc.polyExtrudeFacet(wang[-1]+'.f[2]',ltz=0.5)
    mc.delete([wang[-1]+'.f[%s]'%i for i in ['4:5',9,'12:13']])
    wang.append(mc.duplicate(wang[-1])[0])
    mc.scale(-1,wang[-1],x=1,p=[0,0,0])
    
    # ตัวลิ้นชัก
    linchak.append(mc.polyCube(w=33,h=a-1,d=54.7)[0])
    mc.hyperShade(a=phiu_linchak)
    mc.move(0,b,54.7/2+1.5)
    mc.select(linchak[-1]+'.f[0]')
    mc.polyExtrudeFacet(off=-0.5,sx=38./34)
    mc.polyExtrudeFacet(ltz=1.8)
    mc.polyExtrudeFacet(sx=10./38,sy=3./a)
    mc.move(c,y=1,r=1)
    mc.polyExtrudeFacet(ltz=-1.3)
    mc.select(linchak[-1]+'.f[20]')
    mc.polyExtrudeFacet(off=0.1,sx=9.8/10.6,tx=0.4)
    mc.polyExtrudeFacet(ltz=-1.5)
    mc.select(linchak[-1]+'.f[1]')
    mc.polyExtrudeFacet(off=0.5)
    mc.polyExtrudeFacet(ltz=-4.8)
    mc.polyBevel([linchak[-1]+'.e[%d]'%i for i in [36,41]],o=0.8,sg=3)
    mc.polyBevel([linchak[-1]+'.e[%d]'%i for i in [24,27]],o=0.5)

# ล้อตู้
lo = mc.polyCylinder(r=0.5,h=0.8,sx=24,ax=[1,0,0])[0]
mc.hyperShade(a=phiu_kha)
mc.move(1.25,y=1)
mc.select(lo+'.f[24:25]')
mc.polyExtrudeFacet(ltz=0.4)
mc.polyExtrudeFacet(off=-0.75)
mc.polyExtrudeFacet(ltz=0.4)
mc.select(lo+'.f[5:16]')
mc.polyExtrudeFacet(ltz=0.85)
mc.polyExtrudeFacet(sx=2.25)
mc.polyExtrudeFacet(ltz=0.1)
mc.select(lo+'.f[5:10]')
mc.scale(0,y=1,p=[0,3,0])
mc.move(-14,0,51,lo,r=1)
lo = [lo,mc.duplicate(lo)[0]]
mc.scale(-1,lo[-1],z=1,p=[0,0,28])
lo.append(mc.duplicate(lo[0])[0])
mc.scale(-1,lo[2],p=[0,0,28])
lo.append(mc.duplicate(lo[1])[0])
mc.scale(-1,lo[3],x=1,p=[0,0,28])

# รวมส่วนต่างๆที่ประกอบเป็นตู้ลิ้นชัก
nf_l = mc.polyEvaluate(linchak[0],v=1)
tulinchak = mc.polyUnite(tulinchak,lo,wang,linchak,ch=0,n='tulinchak1')[0]
nf = mc.polyEvaluate(v=1)
tulinchak = [tulinchak,mc.duplicate(tulinchak)[0]]

# เชื่อมกับข้อเพื่อให้เปิดเปิดลิ้นชักได้
kraduk_tulinchak = []
for tlc in tulinchak:
    mc.select(cl=1)
    kho = [mc.joint(p=[0,0,0],n='kraduk_tulinchak1')]
    mc.select(kho[0])
    kho.append(mc.joint(p=[0,62.75,56.7]))
    kho.append(mc.joint(p=[0,62.75,56.7+5]))
    mc.select(kho[0])
    kho.append(mc.joint(p=[0,54.5,56.7]))
    kho.append(mc.joint(p=[0,54.5,56.7+5]))
    mc.select(kho[0])
    kho.append(mc.joint(p=[0,38.25,56.7]))
    kho.append(mc.joint(p=[0,38.25,56.7+5]))
    sk = mc.skinCluster(kho,tlc)[0]
    mc.skinPercent(sk,tlc+'.vtx[0:%d]'%(nf-3*nf_l-1),tv=[(kho[0],1)])
    mc.skinPercent(sk,tlc+'.vtx[%d:%d]'%(nf-3*nf_l,nf-2*nf_l-1),tv=[(kho[1],1)])
    mc.skinPercent(sk,tlc+'.vtx[%d:%d]'%(nf-2*nf_l,nf-nf_l-1),tv=[(kho[3],1)])
    mc.skinPercent(sk,tlc+'.vtx[%d:%d]'%(nf-nf_l,nf-1),tv=[(kho[5],1)])
    
    kraduk_tulinchak.append(kho)
    mc.move(208,0,20,kho[0])

mc.rotate(180,kho[0],y=1)
mc.move(86,0,320,kho[0])



# เก้าอี้
kha = mc.polyPlane(w=0.5,h=3,sx=1,sy=7)[0]
mc.move(-22-0.75,0,-54/2.+3/2.)
mc.polySoftEdge(a=89)
mc.scale(10/5.,1,1.2,kha+'.f[1:5]')
mc.scale(14./10,1,1.2,kha+'.f[2:4]')
mc.scale(15/14.,1,1.2,kha+'.f[3]')
mc.select(kha+'.f[0:6]')
mc.polyExtrudeFacet(ty=37,tz=8)
for i in range(6):
    mc.polyExtrudeFacet()
    mc.rotate(15,p=[0,37,-14.5+0.5*i])
    mc.move(0.5,z=1,r=1)
mc.polyExtrudeFacet(tz=23)
for i in range(6):
    mc.polyExtrudeFacet()
    mc.move(0.5,z=1,r=1)
    mc.rotate(15,p=[0,37,12+0.5*i])
mc.polyExtrudeFacet(ty=-37,tz=8)
kha = [kha,mc.duplicate(kha)[0]]
mc.scale(-1,kha[1],p=[0,0,0])
kha.append(mc.polyCylinder(r=0.75,h=45,ax=[1,0,0],sx=12)[0])
mc.move(0,37,17.5)
mc.delete('.f[12:13]')
kha.append(mc.duplicate(kha[2])[0])
mc.scale(-1,kha[3],z=1,p=[0,0,0])
mc.select(kha)
mc.hyperShade(a=phiu_kha)

knot = [mc.polyCylinder(r=0.4,h=0.4,sx=6)[0]]
mc.hyperShade(a=phiu_loha)
mc.move(0,0.3)
mc.delete('.f[6]')
knot.append(mc.polyCylinder(r=0.6,h=0.1,sx=12)[0])
mc.hyperShade(a=phiu_loha)
mc.move(0,0.05)
mc.polySoftEdge(a=89)
knot = mc.polyUnite(knot,ch=0)
mc.rotate(0,0,-90)
mc.move(23.5,40,12)
knot.append(mc.duplicate(knot[0])[0])
mc.scale(1,-1,1,knot[-1],r=1,p=[0,0,0])
knot.append(mc.duplicate(knot[0])[0])
mc.scale(1,1,-1,knot[-1],r=1,p=[0,0,0])
knot.append(mc.duplicate(knot[0])[0])
mc.scale(1,-1,-1,knot[-1],r=1,p=[0,0,0])

chut = [(-22,83,28),(-22,72,26),(-22,52,21),(-22,44,18),(-22,42,15),(-22,42,-20),(-19,42,-24),(-14,42,-25)]
for i in reversed(range(len(chut))):
    chut.append((-chut[i][0],chut[i][1],chut[i][2]))
sen1 = mc.curve(p=chut)
sen2 = mc.duplicate(sen1)[0]
mc.move(0,-4,0,r=1)
kaoi = mc.loft(sen2,sen1,po=1,ch=0)[0]
mc.hyperShade(a=phiu_kaoi)
mc.delete(sen1,sen2)
nf = mc.polyEvaluate(f=1)
mc.polyExtrudeFacet(ltz=0.2)
mc.select(kaoi+'.f[%d:%d]'%(nf/3*2,nf-1))
mc.scale(0.6,1,0.9)
mc.move(0,-1,3,r=1)
mc.scale(0,1,0.9)
mc.move(0,-0.5,3,r=1)
mc.delete()
mc.polyMergeVertex(kaoi,d=0.001)
mc.move(1,kaoi+'.f[78]',kaoi+'.f[88]',z=1,r=1)
mc.polySoftEdge(kaoi,a=89)
kaoi = mc.polyUnite(kaoi,kha,knot,ch=0,n='kaoi1')[0]
mc.move(147,0,100)

kaoi2 = mc.duplicate(kaoi)[0]
mc.scale(1,1,-1,kaoi2)
mc.move(340-100,kaoi2,z=1)



# โครงใต้เตียง
khrong = mc.polyPlane(w=196,h=91,sx=4,sy=1,ax=[0,-1,0])[0]
mc.hyperShade(a=phiu_saotiang)
mc.move(0,186-4.6)
mc.select('.f[*]')
mc.polyExtrudeFacet(off=2,kft=0)
mc.polyExtrudeFacet(ltz=-4.6)
mc.select(khrong+'.f[5]',khrong+'.f[21]',khrong+'.f[27]')
mc.scale(0.5,x=1,r=1,p=[-45,0,0])
mc.move(0.5,x=1,r=1)
mc.scale(0.5,khrong+'.f[25]',khrong+'.f[31]',x=1,r=1)
mc.select(khrong+'.f[19]',khrong+'.f[29]',khrong+'.f[35]')
mc.scale(0.5,x=1,r=1,p=[45,0,0])
mc.move(-0.5,x=1,r=1)
mc.delete(khrong+'.f[0:3]')

# เสาเตียง
saotiang = mc.polyCube(w=6.5,h=212,d=6.5,sz=4)[0]
mc.hyperShade(a=phiu_saotiang)
mc.move(187/2.+6.5/2,4+212/2.,82/2.+6.5/2,saotiang)
mc.move(4.5,saotiang+'.f[14]',x=1,r=1)
mc.move(0.5-6.5/4,saotiang+'.e[33]',z=1,r=1)
mc.move(0.5,0,6.5/4,saotiang+'.e[34]',r=1)
mc.move(-1,saotiang+'.e[11]',r=1)
mc.move(-1+math.sin(math.pi/6),0,6.5/4-1+math.cos(math.pi/6),saotiang+'.e[32]',r=1)
mc.move(-1+math.sin(math.pi/3),0,6.5/2-1+math.cos(math.pi/3),saotiang+'.e[31]',r=1)
mc.move(0,0,3*6.5/4-1,saotiang+'.e[30]',r=1)

# หัวเสาด้านบนและล่าง
huasaobon = mc.duplicate(saotiang)[0]
mc.hyperShade(a=phiu_kha)
mc.scale(1./212,y=1)
mc.move(0.5+212+4,y=1)
huasaolang = mc.duplicate(huasaobon)[0]
mc.move(3.5,y=1)
mc.hyperShade(a=phiu_kha)

# ทำส่วนนูนเว้าบนตัวเสา
mc.select(saotiang+'.e[0:1]')
mc.polySplitRing(stp=2,div=7)
mc.select([saotiang+'.f[%d]'%i for i in range(18,26,2)])
mc.polyExtrudeFacet(ltz=-0.2)
mc.select(saotiang+'.e[19]',saotiang+'.e[23]')
mc.polySplitRing(stp=2,div=7)
mc.select([saotiang+'.f[%d]'%i for i in [10,42,44,46]])
mc.polyExtrudeFacet(ltz=-0.2)
mc.select(saotiang+'.e[16]',saotiang+'.e[24]')
mc.polySplitRing(stp=2,div=8)
mc.select([saotiang+'.f[%d]'%i for i in range(65,72,2)])
mc.polyExtrudeFacet(ltz=-0.2)

lop = [] # ลบส่วนบนล่างออก
for i in range(mc.polyEvaluate(saotiang,f=1)):
    s = saotiang+'.f[%d]'%i
    bb = mc.xform(s,q=1,bb=1)
    if(bb[1]>1 or bb[4]<-1):
        lop.append(s)
mc.delete(lop)

# รวมส่วนหัวเข้ากับเสา
saotiang = mc.polyUnite(huasaobon,huasaolang,saotiang,ch=0)[0]
saotiang = [saotiang,mc.duplicate(saotiang)[0]]
mc.scale(-1,saotiang[1],x=1,p=[0,0,0])
saotiang.append(mc.duplicate(saotiang[0])[0])
mc.scale(-1,saotiang[-1],z=1,p=[0,0,0])
saotiang.append(mc.duplicate(saotiang[0])[0])
mc.scale(-1,-1,saotiang[-1],xz=1,p=[0,0,0])



# ขาเสา
khasao = [mc.polyCube(w=5,h=0.5,d=3,sx=2)[0]]
mc.move(0,0.25,0)
mc.scale(0.8,'.f[8:9]',z=1)
khasao.append(mc.polyCylinder(r=1,h=0.5,sx=18,sz=1)[0])
mc.move(0,0.75,0)
mc.delete('.f[18:35]')
khasao.append(mc.polyCylinder(r=0.3,h=2,sx=18,sz=1)[0])
mc.move(0,2,0)
mc.delete('.f[18:35]')
khasao.append(mc.polyCylinder(r=0.3,h=0.3,sx=18,sz=1)[0])
mc.move(-1.8,0.5+0.15)
mc.delete('.f[18:35]')
khasao.append(mc.polyCylinder(r=0.3,h=0.3,sx=18,sz=1)[0])
mc.move(1.8,0.5+0.15)
mc.delete('.f[18:35]')
mc.select(khasao[:2])
mc.hyperShade(a=phiu_kha)
mc.select(khasao[2:])
mc.hyperShade(a=phiu_loha)
khasao = mc.polyUnite(khasao,ch=0)
mc.rotate(-45,khasao,y=1)
mc.move(187/2.+4,0,82/2.+4,khasao)
khasao.append(mc.duplicate(khasao)[0])
mc.rotate(45,khasao[1],y=1)
mc.move(-82/2.-4,khasao[1],z=1)
khasao.append(mc.duplicate(khasao[0])[0])
mc.move(-187/2.-4,-82/2.-4,khasao[2],xz=1)
khasao.append(mc.duplicate(khasao[0])[0])
mc.rotate(45,khasao[3],y=1)
mc.move(-187/2.-4,khasao[3],x=1)



# เตียง
tiang = []
tiang.append(mc.polyCube(w=187,h=35,d=2)[0])
mc.move(0,181+35/2.,82/2.+6.5-1)
mc.delete('.f[4:5]')
tiang.append(mc.polyCube(w=187,h=14,d=2)[0])
mc.move(0,181+14/2.,-82/2.-6.5+1)
tiang.append(mc.polyCube(w=2,h=14,d=82)[0])
mc.move(187/2.+6.5-1,181+14/2.,0)
mc.delete('.f[0]','.f[2]')
tiang.append(mc.polyCube(w=2,h=35,d=82)[0])
mc.move(-187/2.-6.5+1,181+35/2.,0)
mc.delete('.f[0]','.f[2]')
tiang.append(mc.polyCube(w=196,h=2,d=91)[0]) # แผ่นใต้
mc.move(0,181+5+1)
mc.select(tiang)
mc.hyperShade(a=phiu_tiang)
tiang = mc.polyUnite(tiang)[0]
mc.polyAutoProjection(tiang,ps=0.2)

# รวมเสาเตียงเข้ากับเตียง
tiang = mc.polyUnite(tiang,saotiang,khrong,khasao,n='tiang1',ch=0)[0]
mc.move(47+200/2.,0,95/2.+1,tiang)

tiang2 = mc.duplicate(tiang)[0]
mc.scale(1,1,-1,tiang2)
mc.move(340-95/2.-1,tiang2,z=1)



# ที่นอน
thinon = []
for a in [phiu_thinon1,phiu_thinon2]:
    thinon.append(mc.polyCube(w=190,h=5,d=90,sx=19,sz=7,n='thinon1')[0])
    mc.hyperShade(a=a)
    mc.polyBevel([thinon[-1]+'.e[%d]'%i for i in [304,323,464,483]],o=6)
    for i in range(mc.polyEvaluate(v=1)):
        s = thinon[-1]+'.vtx[%d]'%i
        t = mc.xform(s,q=1,t=1)
        mc.move(random.uniform(-0.5,0.5),0,random.uniform(-0.5,0.5),s,r=1)
        if(t[1]>0):
            mc.move(random.random(),s,y=1,r=1)
mc.move(145,186+2+5/2.,95/2.+1,thinon[0])
mc.move(145,186+2+5/2.,340-95/2.-1,thinon[1])

# หมอน
mon = []
for a in [phiu_thinon1,phiu_thinon2]:
    mon.append(mc.polyCube(w=65,h=15,d=40,sx=13,sy=1,sz=8,n='mon1')[0])
    mc.hyperShade(a=a)
    ymin = 0
    for i in range(mc.polyEvaluate(v=1)):
        s = mon[-1]+'.vtx[%d]'%i
        t = mc.xform(s,q=1,t=1)
        mc.scale((((32.5**2-t[0]**2)*(20**2-t[2]**2))**0.5/32.5/20+0.1/7.5)*random.uniform(0.9,1.1),s,y=1,p=[0,0,0])
        mc.move(random.uniform(-0.5,0.5),0,random.uniform(-0.5,0.5),s,r=1)
        if(t[1]<ymin):
            ymin = t[1]
    mc.rotate(90,y=1)
mc.move(78,186+2+5-ymin,95/2.+1,mon[0])
mc.move(78,186+2+5-ymin,340-95/2.-1,mon[1])



# บันไดขึ้นเตียง
bandai = mc.polyCube(w=2,h=167,d=88)[0]
mc.move(-24,167/2.,88./2)
mc.polyBevel(bandai+'.e[1]',o=40)
mc.move(50,bandai+'.e[26]',y=1)
mc.polyBevel(bandai+'.e[13:14]',o=8,sg=3)
mc.move(2,bandai+'.e[6]',z=1,r=1)
mc.delete(bandai+'.f[2]')
bandai = [bandai,mc.duplicate(bandai)[0]]
mc.scale(-1,bandai[-1],x=1,p=[0,0,0])
bandai = mc.polyUnite(bandai,ch=0)[0]
mc.polyBridgeEdge([bandai+'.e[%d]'%i for i in [1,2,5,6,38,39,42,43]],dv=0,ch=0)

for i in range(0,5):
    if(i==0):
        khan = [mc.polyPlane(w=46,h=0.2,sx=1,sy=1,ax=[0,0,1])[0]]
        mc.select(khan[0]+'.e[3]')
        mc.polyExtrudeEdge(ty=0.2,tz=0.2)
        mc.polyExtrudeEdge(ty=0.3)
        mc.polyExtrudeEdge(ty=0.2,tz=-0.2)
        mc.polyExtrudeEdge(ty=0.2)
        mc.polyExtrudeEdge(ty=0.2,tz=0.2)
        mc.polyExtrudeEdge(ty=0.3)
        for _ in range(4):
            mc.polyExtrudeEdge(ty=0.2,tz=-0.2)
            mc.polyExtrudeEdge(tz=-0.3)
            mc.polyExtrudeEdge(ty=-0.2,tz=-0.2)
            mc.polyExtrudeEdge(tz=-0.2)
        mc.select(khan[0]+'.e[0]')
        mc.polyExtrudeEdge(ty=-0.2,tz=0.2)
        mc.polyExtrudeEdge(ty=-0.3)
        mc.polyExtrudeEdge(ty=-0.2,tz=-0.2)
        mc.polyExtrudeEdge(ty=-0.2)
        mc.polyExtrudeEdge(ty=-0.2,tz=0.2)
        mc.polyExtrudeEdge(ty=-0.3)
        mc.polyExtrudeEdge(ty=-0.2,tz=-0.2)
        mc.polyExtrudeEdge(tz=-0.2)
        mc.polyExtrudeEdge(ty=0.2,tz=-0.2)
    else:
        khan.append(mc.duplicate(khan[0])[0])
    mc.move(0,32.5+i*33,37.5+(4-i)*12,khan[-1])
    
for k in khan:
    mc.select(k+'.e[69]',k+'.e[96]')
    mc.polyExtrudeEdge()
    mc.scale(0,z=1,p=[0,0,1])

kan = [mc.polyPlane(w=2,h=30,sx=1,sy=1,ax=[0,0,1])[0]]
mc.move(0,1+30/2.,72.5)
for i in range(4):
    kan.append(mc.duplicate(kan[-1])[0])
    mc.move(0,33,-12,kan[-1],r=1)
for i in range(5):
    mc.select(kan[i]+'.e[1:2]')
    mc.polyExtrudeEdge()
    mc.scale(0,z=1,p=[0,0,2])
mc.polyBridgeEdge([kan[0]+'.e[%d]'%i for i in [4,7]],dv=0)
mc.select(kan[0]+'.f[3]')
mc.move(0,3,r=1)
mc.polyExtrudeFacet(ty=-4)
mc.polyExtrudeFacet(kan[0]+'.f[7]',ltz=5)
mc.polyExtrudeFacet([kan[0]+'.f[%d]'%i for i in [4,6,9,11]],ltz=22)
mc.delete()
mc.scale(23,kan[0]+'.f[7]')
mc.scale(0,1,0,kan[0]+'.f[3]',p=[0,0,2])
mc.move(0,0,5,[kan[0]+'.vtx[%d]'%i for i in [16,19,22,24]],r=1)
mc.polyMergeVertex(kan[0],d=0.001)

bandai = mc.polyUnite(bandai,khan,kan,ch=0,n='bandai1')[0]
mc.hyperShade(a=phiu_bandai)
mc.move(47+200+50/2.,0,1)
mc.polySoftEdge(bandai,a=89)
mc.polyAutoProjection(bandai,ps=0.2)

bandai2 = mc.duplicate(bandai)[0]
mc.scale(1,1,-1,bandai2)
mc.move(340-1,bandai2,z=1)



# ตู้เสื้อผ้า
tusueapha = mc.polyCube(w=132,h=180,d=58)[0]
mc.move(0,180/2.,58/2.)
mc.select(tusueapha+'.f[0]')
mc.polyExtrudeFacet(off=2)
mc.polyExtrudeFacet(ltz=-56)
mc.move(10,tusueapha+'.f[10]',y=1,r=1)

channaitu = [mc.polyCube(w=87,h=2,d=55)[0]]
mc.move(2+87/2.-132/2.,12+28+1,2+55/2.)
mc.delete(channaitu[0]+'.f[2]',channaitu[0]+'.f[4:5]')
channaitu.append(mc.duplicate(channaitu)[0])
mc.move(2+87/2.-132/2.,12+28+2+21+1,2+55/2.,channaitu[-1])
channaitu.append(mc.duplicate(channaitu[0])[0])
mc.move(2+87/2.-132/2.,180-2-31-1,2+55/2.,channaitu[-1])
channaitu.append(mc.polyCube(w=2,h=166,d=56)[0])
mc.move(132/2.-42,12+166/2.,2+56/2.)
mc.delete(channaitu[-1]+'.f[1:3]')
channaitu.append(mc.polyCube(w=39,h=4,d=56)[0])
mc.move(132/2.-2-39/2.,180-85,2+56/2.)
mc.delete(channaitu[-1]+'.f[2]',channaitu[-1]+'.f[4:5]')
channaitu.append(mc.polyCube(w=39,h=2,d=55)[0])
mc.move(132/2.-2-39/2.,12+28+1,2+55/2.)
mc.delete(channaitu[-1]+'.f[2]',channaitu[-1]+'.f[4:5]')
channaitu.append(mc.duplicate(channaitu[-1])[0])
mc.move(30,channaitu[-1],y=1,r=1)

tusueapha = mc.polyUnite(tusueapha,channaitu,ch=0)[0]

pratutu = [mc.polyCube(w=45-0.4,h=170-0.4,d=2)[0]]
mc.move(-132/2.+45/2.,170/2.+10,58+1)
pratutu.append(mc.duplicate(pratutu[0])[0])
mc.move(45,pratutu[1],x=1,r=1)
pratutu.append(mc.polyCube(w=42-0.4,h=85-0.4,d=2)[0])
mc.move(132/2.-42/2.,180-85/2.,58+1)
pratutu.append(mc.polyCube(w=42-0.4,h=85-0.4,d=2)[0])
mc.move(132/2.-42/2.,10+85/2.,58+1)
mc.select(tusueapha,pratutu)
mc.hyperShade(a=phiu_tusueapha)



wong = []
for i in range(19):
    wong.append(mc.circle(r=0.2+((i-9.)/9)**2*0.3)[0])
    mc.scale(0.8)
    mc.move(0,-2-((i-9.)/9)**2*3.)
    mc.rotate(-i*10,p=[0,0,0])
thichap = mc.loft(wong,po=1,ch=0)
mc.delete(wong)
mc.hyperShade(a=phiu_thichap)
mc.move(4-21,170/2.+10,58+2)
thichap.append(mc.duplicate(thichap)[0])
mc.move(-4-21,thichap[0],x=1)
thichap.append(mc.duplicate(thichap[0])[0])
mc.move(28,170/2.+10+10,58+2,thichap[-1])
thichap.append(mc.duplicate(thichap[0])[0])
mc.move(28,170/2.+10-10,58+2,thichap[-1])


'''
# จุดหมุนประตูตู้เสื้อผ้า (ทำได้ไม่สมบูรณ์จึงตัดทิ้ง)
chutmun = mc.polyCube(w=0.8,h=1.5,d=6,ch=0)
mc.move(-64+0.2+0.4,172,58-0.2-3)
mc.move(0.2,'.e[5]',r=1)
mc.polyExtrudeFacet('.f[0]',ltz=0.2)
mc.scale(0.6,'.f[0]',x=1,p=[-62.8,0,0])
mc.polyExtrudeFacet('.f[0]',ltz=0.8)
mc.scale(0.2,'.f[0]',x=1)
mc.move(0.3,'.e[19]',r=1)
chutmun.append(mc.polyCylinder(r=0.1,h=1.4,sx=12)[0])
mc.move(-63.8,172,58.5)
mc.polyExtrudeFacet('.f[10]',tx=0.35,tz=0.2,sy=15./14)
mc.delete('.f[10]')
chutmun = mc.polyUnite(chutmun,ch=0)
chutmun.append(mc.polyCube(w=2,h=6,d=0.2,sy=3)[0])
mc.move(-64+2.5,172,58+0.1)
mc.scale(1.5,'.f[1]','.f[5]',y=1)
mc.polyExtrudeFacet('.f[12]',ltz=0.5)
mc.polyExtrudeFacet('.f[12]',ltz=0.5,sy=0.8)
mc.polyExtrudeFacet('.f[12]',ltz=0.4,sy=0.63)
mc.delete('.f[0:2]','.f[15]','.f[19]','.f[23]')
mc.polyExtrudeFacet('.f[2]','.f[13]','.f[16]','.f[19]',off=0.1)
mc.polyExtrudeFacet('.f[2]','.f[13]','.f[16]','.f[19]',ltz=-1)
mc.polyBevel('.e[65]','.e[67]',o=0.05)
mc.scale(10,10,1,'.f[41]',p=[-60.6,170.6,0])
mc.scale(10,10,1,'.f[40]',p=[-60.6,173.4,0])
mc.move(-63.8,172.75,58.5,'.rotatePivot')
'''

for i in range(0,4):
    pratutu[i] = mc.polyUnite(pratutu[i],thichap[i],ch=0)[0]

nv = [mc.polyEvaluate(tusueapha,v=1)]
nv += [mc.polyEvaluate(pratutu[i],v=1) for i in range(4)]
tusueapha = mc.polyUnite(tusueapha,pratutu,ch=0,n='tusueapha1')[0]
mc.polyAutoProjection(mc.sets(phiu_tusueapha+'SG',q=1),ps=0.2)

tusueapha = [tusueapha,mc.duplicate(tusueapha)[0]]
mc.scale(1,1,-1,tusueapha[1])

# เชื่อมกับข้อเพื่อให้เปิดปิดประตูได้
kraduk_tusueapha = []
for i,tsp in zip([1,-1],tusueapha):
    mc.select(cl=1)
    kho = [mc.joint(p=[0,0,0],n='kraduk_tusueapha1')]
    kho.append(mc.joint(p=[-65.8,170/2.+10,58*i]))
    kho.append(mc.joint(p=[-65.8+20,170/2.+10,58*i]))
    mc.select(kho[0])
    kho.append(mc.joint(p=[23.8,170/2.+10,58*i]))
    kho.append(mc.joint(p=[23.8-20,170/2.+10,58*i]))
    mc.select(kho[0])
    kho.append(mc.joint(p=[65.8,170/2.+20,58*i]))
    kho.append(mc.joint(p=[65.8-20,170/2.+20,58*i]))
    mc.select(kho[0])
    kho.append(mc.joint(p=[65.8,170/2.,58*i]))
    kho.append(mc.joint(p=[65.8-20,170/2.,58*i]))
    sk = mc.skinCluster(kho,tsp)[0]
    mc.skinPercent(sk,tsp+'.vtx[0:%d]'%(sum(nv)-1),tv=[(kho[0],1)])
    mc.skinPercent(sk,tsp+'.vtx[%d:%d]'%(nv[0],sum(nv[0:2])-1),tv=[(kho[1],1)])
    mc.skinPercent(sk,tsp+'.vtx[%d:%d]'%(sum(nv[0:2]),sum(nv[0:3])-1),tv=[(kho[3],1)])
    mc.skinPercent(sk,tsp+'.vtx[%d:%d]'%(sum(nv[0:3]),sum(nv[0:4])-1),tv=[(kho[5],1)])
    mc.skinPercent(sk,tsp+'.vtx[%d:%d]'%(sum(nv[0:4]),sum(nv)-1),tv=[(kho[7],1)])
    kraduk_tusueapha.append(kho)

mc.move(47+200+50+132/2.,0,1,kraduk_tusueapha[0][0])
mc.move(47+200+50+132/2.,0,340-1,kraduk_tusueapha[1][0])



# ชั้นวางของ
chanwang = mc.polyCube(w=72,h=153,d=52,sx=5,sy=9,n='chanwang')[0]
mc.hyperShade(a=phiu_chanwang)
mc.move(0,153/2.,52/2.)
mc.move(9,[chanwang+'.e[%d]'%i for i in [11,13]],y=1,r=1)
mc.move(11,[chanwang+'.e[%d]'%i for i in [21,23]],y=1,r=1)
mc.move(13,[chanwang+'.e[%d]'%i for i in [31,33]],y=1,r=1)
mc.move(15,[chanwang+'.e[%d]'%i for i in [41,43]],y=1,r=1)
mc.move(-8,[chanwang+'.e[%d]'%i for i in [6,8]],y=1,r=1)
mc.move(-6,[chanwang+'.e[%d]'%i for i in [16,18]],y=1,r=1)
mc.move(-4,[chanwang+'.e[%d]'%i for i in [26,28]],y=1,r=1)
mc.move(-2,[chanwang+'.e[%d]'%i for i in [36,38]],y=1,r=1)
mc.scale(34/21.6,[chanwang+'.e[%s]'%i for i in [107,110,119,122,131,134,143,146]])
mc.scale(1/7.2,[chanwang+'.f[%s]'%i for i in [7,17,27,37]])
mc.scale(0,[chanwang+'.f[%s]'%i for i in ['50:89','101:108','110:117']],y=1,p=[0,153,0])
mc.polyMergeVertex(d=0.001)
mc.scale(0,[chanwang+'.f[%s]'%i for i in ['45:48','50:53','55:58']],x=1,p=[-72/2.,0,0])
mc.polyMergeVertex(d=0.001)
mc.polyExtrudeFacet([chanwang+'.f[%d]'%i for i in [6,8,16,18,26,28,36,38]],ltz=-50)
mc.select(chanwang)
mc.rotate(90,y=1,p=[0,0,0])
mc.move(232,z=1)
mc.polyAutoProjection(chanwang,ps=0.2)



# เครื่องปรับอากาศ
ea = mc.polyCube(w=72,d=16,h=26,sz=5)[0]
mc.hyperShade(a='phiu_ea')
for i,[a,b] in enumerate(zip([36,37,38,39,13],[40,41,42,43,12]),1):
    mc.scale((100.-i**2)/100.,ea+'.e[%d]'%a,ea+'.e[%d]'%b,y=1,p=[0,2,0])

mc.polyBevel(ea+'.f[0]',o=0.5)
mc.polySplitRing(ea+'.e[40]',ea+'.e[45]',stp=2,div=2)
mc.scale(1,2,1,ea+'.f[54]',ea+'.f[57]',p=[0,0.5,0])
mc.select(ea+'.f[21]',ea+'.f[26]')
mc.polyExtrudeFacet(sx=71/72.,sy=0.95,ltz=0.2,off=0.5)

mc.select(ea+'.f[27]')
mc.polyExtrudeFacet(off=0.2,sx=67/72.)
mc.hyperShade(a=phiu_muet)
mc.polyExtrudeFacet(ltz=-10)

mc.select(ea+'.f[7:8]',ea+'.f[23]')
mc.polyChipOff()
bb = mc.xform(bb=1,q=1,ws=1)
mc.scale(62./71,0.9,0.7,p=[bb[0],bb[4],bb[2]])
mc.move(1,-0.1,2,r=1)
mc.polyExtrudeFacet(ltz=0.1)

mc.select(ea+'.f[7:8]',ea+'.f[23]')
mc.polyExtrudeFacet(off=0.5)
mc.scale(64./71,1,1,p=[mc.xform(bb=1,q=1,ws=1)[0],0,0])
mc.hyperShade(a=phiu_muet)
mc.polyExtrudeFacet()
bb = mc.xform(bb=1,q=1,ws=1)
mc.scale(1,0,0,p=[0,bb[4],bb[2]])
mc.polyMergeVertex(d=0.001)

mc.select([ea+'.e[%s]'%i for i in ['18:25','48:49',34,36,'56:57',39,42,'8:15','46:47',67,69]])
mc.polyBevel(o=0.5)
mc.select(ea+'.f[31]')
mc.polyExtrudeFacet(off=0.5)
mc.hyperShade(a=phiu_muet)
mc.scale(1,0.1,1,p=[0,mc.xform(bb=1,q=1)[1],0])
mc.polyExtrudeFacet(ltz=-3)

sisi = []
for i in range(1,25):
    sisi.append(mc.polyCube(w=71,h=0.32,d=0.2)[0])
    mc.hyperShade(a='phiu_ea')
    mc.scale(0.97,sisi[-1]+'.f[0]')
    mc.move(0,-5.6667+0.5*i,7.7+0.4)

ea = mc.polyUnite(ea,sisi,ch=0)[0]
mc.move(44+16/2.+0.2,235+26/2.,170,ea)
mc.rotate(0,90,ea)
mc.polySoftEdge(ea,a=89)

yuetea = mc.polyCube(w=0.2,h=59,d=3)[0]
mc.move(-0.2,yuetea+'.e[7]',y=1,r=1)
mc.select(yuetea+'.f[1]')
mc.move(-0.2,y=1,r=1)
mc.polyExtrudeFacet(ltz=0.2*2**0.5)
mc.polyExtrudeFacet()
mc.scale(0,x=1,p=[6,0,0])
mc.scale(2**0.5,2**0.5,yuetea+'.f[9]',p=[-0.1,29.9,0])
mc.polySoftEdge(yuetea,a=89)

# เจาะรู
ru = [mc.polyCylinder(r=0.6,h=1,sx=8,ax=[1,0,0])[0]]
mc.rotate(22.5)
mc.move(0.5,'.f[1]','.f[3]',y=1,r=1)
mc.move(0,-27.5)
for i in range(19):
    ru.append(mc.duplicate(ru[-1])[0])
    mc.move(3,ru[-1],y=1,r=1)

mc.rotate(90,z=1,r=1)
mc.move(2,r=1)
ru.append(mc.duplicate(ru[-1])[0])
mc.move(3,ru[-1],r=1)
yuetea = mc.polyCBoolOp(yuetea,ru,op=2,ch=0,n='yuetea1')[0]
mc.hyperShade(a=phiu_yuetea)

mc.move(44+0.1,286-59/2.,170-26,yuetea)
yuetea = [yuetea,mc.duplicate(yuetea)[0]]
mc.scale(-1,yuetea[1],z=1,p=[0,0,170])

# สายเชื่อมแอร์เข้ากับผนัง
wong = [mc.circle(r=1.5)[0]]
mc.move(54.5,239,206)
for i in range(18*3):
    wong.append(mc.duplicate(wong[-1])[0])
    if(i%2):
        mc.scale(0.95,0.95,0.95,wong[-1])
    else:
        mc.scale(1/0.95,1/0.95,1/0.95,wong[-1])
    mc.rotate(10/3.,x=1,r=1,p=[54.5,209,206])
for i in range(15*2):
    if(i%2==0):
        mc.scale(0.95,0.95,0.95,wong[-1])
    else:
        mc.scale(1/0.95,1/0.95,1/0.95,wong[-1])
    wong.append(mc.duplicate(wong[-1])[0])
    mc.rotate(10/2.,y=1,r=1,p=[34.5,179,206])
for i in range(6*2):
    if(i%2==0):
        mc.scale(0.95,0.95,0.95,wong[-1])
    else:
        mc.scale(1/0.95,1/0.95,1/0.95,wong[-1])
    wong.append(mc.duplicate(wong[-1])[0])
    mc.rotate(-10/2.,y=1,r=1,p=[0,179,186])
saiea = mc.loft(wong,po=1,ch=0)[0]
mc.hyperShade(a=phiu_saikhao)
mc.polySoftEdge(a=46)
mc.delete(wong)

# กล่องที่เชื่อมกับแอร์
klong = mc.polyCube(w=10,h=30,d=20)[0]
mc.hyperShade(a=phiu_linchak)
mc.move(5,269,99)
mc.select('.f[0]')
mc.polyExtrudeFacet(sy=1/3./0.9,sx=0.5/0.8)
nf1 = mc.polyEvaluate(klong,f=1)
mc.polyExtrudeFacet(ltz=0.9,sy=0.9,sx=0.8)
mc.polyExtrudeFacet(sy=0.4,sx=0.4)
mc.polyExtrudeFacet(ltz=0.1)
nf2 = mc.polyEvaluate(klong,f=1)
mc.polyExtrudeFacet(sy=1.25,sx=1.25)
mc.polyExtrudeFacet(ltz=2)
mc.select(klong+'.f[%d:%d]'%(nf1,nf2-1))
mc.hyperShade(a=phiu_saikhao)
mc.polyExtrudeFacet(klong+'.f[4]',off=2)
mc.polyExtrudeFacet(klong+'.f[4]',klong+'.f[30:33]',off=0.1,ltz=0.1,kft=0)
mc.select(klong+'.f[4]')
mc.polyExtrudeFacet(sy=0.12,sz=0.3)
mc.move(4,r=1,z=1)
nf1 = mc.polyEvaluate(klong,f=1)
mc.polyExtrudeFacet(ltz=1)
mc.polyExtrudeFacet(sy=0.5,sz=0.4,tz=2)
mc.polyExtrudeFacet(ltz=-0.9)
nf2 = mc.polyEvaluate(klong,f=1)
mc.select(klong+'.f[%d:%d]'%(nf1,nf2-1),klong+'.f[4]')
mc.hyperShade(a=phiu_kha)
# น็อตทั้ง ๔ ที่มุม
knot = [mc.polyCylinder(r=0.5,h=0.1,sx=12,ax=[1,0,0])[0]]
mc.hyperShade(a=phiu_loha)
mc.move(10.15,282,108)
mc.polyExtrudeFacet('.f[13]',off=0.2,ltz=0.1)
mc.delete('.f[12]')
mc.polySoftEdge(a=89)
knot.append(mc.duplicate(knot)[0])
mc.scale(1,1,-1,knot[-1],p=[5,269,99])
knot.append(mc.duplicate(knot[0])[0])
mc.scale(1,-1,1,knot[-1],p=[5,269,99])
knot.append(mc.duplicate(knot[0])[0])
mc.scale(1,-1,-1,knot[-1],p=[5,269,99])
klong = mc.polyUnite(klong,knot,ch=0)



# สายที่เชื่อมแอร์เข้ากับกล่อง
wong = [mc.circle(r=0.5,nr=[-1,0,0])[0]]
mc.move(47.2,236.5,136)
wong.append(mc.duplicate(wong[-1])[0])
mc.move(-4,-0.5,wong[-1],r=1)
wong.append(mc.duplicate(wong[-1])[0])
mc.move(-6,-1.5,-0.5,wong[-1],r=1)
wong.append(mc.duplicate(wong[-1])[0])
mc.move(-6,-0.5,-1,wong[-1],r=1)
for i in range(9):
    wong.append(mc.duplicate(wong[-1])[0])
    mc.rotate(0,0,-10,wong[-1],p=[18,265,0],r=1)
    mc.move(0.1,3,-1.5,r=1)
for i in range(18):
    wong.append(mc.duplicate(wong[-1])[0])
    mc.rotate(-10,wong[-1],p=[0,270,115.8],r=1)
    mc.move(0.13,0,-0.2,r=1)

saiea = [saiea,mc.loft(wong,po=1,ch=0)[0]]
mc.hyperShade(a=phiu_saikhao)
mc.delete(wong)



# ท่อที่ลากยาวด้านบน
thobon = mc.polyCube(w=1.9,h=1.9,d=70)[0]
mc.hyperShade(a=phiu_tho)
mc.move(1,282,54)
mc.move(1.9,'.e[9]',z=1,r=1)
mc.polyExtrudeFacet('.f[2]',tx=44)
mc.polyExtrudeFacet('.f[2]',tz=-19)
mc.polyExtrudeFacet('.f[2]',tx=376)
mc.move(-3.8,'.e[32]',x=1,r=1)
mc.polyExtrudeFacet('.f[2]')
mc.scale(0,'.f[2]',z=1,p=[0,0,98.05])
mc.polyExtrudeFacet('.f[2]',ltz=1.9)
mc.polyExtrudeFacet('.f[22]',ltz=3.05)
mc.polyExtrudeFacet('.f[24]',ltz=59.1)
mc.move(-1.9,'.e[67]',y=1,r=1)
mc.polyExtrudeFacet('.f[24]')
mc.scale(0,'.f[24]',x=1,p=[430,0,0])
ea = mc.polyUnite(ea,saiea,klong,yuetea,thobon,ch=0,n='ea')[0]
hong = mc.polyUnite(phuen,ea,ch=0,n='hong')[0]
mc.setAttr(mc.listRelatives(hong,s=1)[0]+'.doubleSided',0) # ทำให้ผนังและเพดานมองทะลุได้จากด้านนอก



# ใส่กระดูกให้ทั้งหมดและตั้งชื่อ สำหรับ mmd
g = [hong,phaman,ruplak,ruplak2,switchfai,lotfai[0],lotfai[1],thisiap,to,to2,
     chanbon,chanbon2,kaoi,kaoi2,tiang,tiang2,thinon[0],thinon[1],mon[0],mon[1],
     bandai,bandai2,chanwang]

kraduk = [kraduk_natang[0],kraduk_pratu[0],kraduk_tulinchak[0][0],kraduk_tulinchak[1][0],kraduk_tusueapha[0][0],kraduk_tusueapha[1][0]]
for n in g:
    p = mc.xform(n,q=1,t=1,ws=1)
    mc.select(cl=1)
    kraduk.append(mc.joint(p=p,n='kraduk_'+n))
    mc.skinCluster(kraduk[-1],n)
kraduk_nh = [u'窓',u'扉',u'引き出し1',u'引き出し2',u'箪笥1',u'箪笥2',
    u'部屋',u'カーテン',u'プラグ板1',u'プラグ板2',u'スイッチ',u'電灯1',u'電灯2',u'カード入り',u'机1',u'机2',
    u'本棚1',u'本棚2',u'椅子1',u'椅子2',u'寝床1',u'寝床2',u'マットレス1',u'マットレス2',u'枕1',u'枕2',
    u'磐梯1',u'磐梯2',u'大きな棚']

for nh,n in zip(kraduk_nh,kraduk):
    mc.addAttr(n,ln='namae',nn=u'名前',dt='string')
    mc.setAttr(n+'.namae',nh,typ='string')
    r = mc.listRelatives(n,f=1)
    if(r):
        for i,d in enumerate(r):
            mc.addAttr(d,ln='namae',nn=u'名前',dt='string')
            mc.setAttr(d+'.namae',u'%sの%s'%(nh,i+1),typ='string')
    
mc.move(-215,0,-170,kraduk,r=1)
mc.group(kraduk,n='kraduk_hongho')
mc.group([g[0]]+[natang,pratu,tulinchak[0],tulinchak[1],tusueapha[0],tusueapha[1]]+g[1:],n='hongho')