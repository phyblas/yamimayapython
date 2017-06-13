# -*- coding: utf-8 -*-
import maya.cmds as mc
import math,random
random.seed(0)

nai = 1
    

phiu_tuyen = mc.shadingNode('blinn',asShader=1,n='phiu_tuyen') # ผิวตัวตู้เย็น
mc.setAttr(phiu_tuyen+'.ambc',0.5,0.5,0.5,typ='double3')
mc.setAttr(phiu_tuyen+'.c',0.65,0.68,0.67,typ='double3')
phiu_khoptu = mc.duplicate(phiu_tuyen,n='phiu_khoptu')[0] # ผิวขอบตู้เย็น
mc.setAttr(phiu_khoptu+'.c',0.49,0.5,0.41,typ='double3')
phiu_maelek = mc.duplicate(phiu_tuyen,n='phiu_maelek')[0] # ผิวแม่เหล็ก
mc.setAttr(phiu_maelek+'.c',0.7,0.7,0.7,typ='double3')
phiu_kha = mc.duplicate(phiu_tuyen,n='phiu_kha')[0] # ผิวขา
mc.setAttr(phiu_kha+'.c',0.1,0.1,0.1,typ='double3')
mc.setAttr(phiu_tuyen+'.sc',0.8,0.8,0.8,typ='double3')



# ตัวตู้เย็น
tuatu = mc.polyCube(w=48,h=75,d=40,ch=0,n='tuatu')[0]
mc.hyperShade(a=phiu_tuyen)
mc.move(0,2+37.5,20)
mc.makeIdentity(a=1)
mc.select(tuatu+'.f[0]')
mc.polyExtrudeFacet(off=2)
mc.delete()
mc.polyAutoProjection(tuatu,ps=0.4,ch=0)
mc.polyEditUV(sv=0.5,pv=0)



# ส่วนแผงแม่เหล็กเชื่อมตู้
maelek = mc.polyCube(w=46,h=73,d=1,n='maelek')[0]
mc.hyperShade(a=phiu_maelek)
mc.move(0,3+36,0.5+40)
mc.select(maelek+'.f[2]')
mc.polyExtrudeFacet(off=1)
mc.polyExtrudeFacet(off=1,tz=0.4)
mc.polyExtrudeFacet(off=0.5,tz=0.6)
mc.delete(maelek+'.f[0]',maelek+'.f[2]')
mc.select(maelek+'.f[0:3]')
mc.polyExtrudeFacet(sz=0.6)
mc.polyExtrudeFacet(ltz=-0.3)
mc.polyExtrudeFacet(sz=1./3)
mc.polyExtrudeFacet(ltz=0.3)
mc.polySoftEdge(maelek,a=0,ch=0)
mc.polyAutoProjection(maelek,ps=0.4,ch=0)
mc.delete(maelek,ch=1)



# ประตูตู้เย็น
pratu = mc.polyCube(w=48,h=72,d=4,sx=10,ch=0,n='pratu')[0]
mc.hyperShade(a=phiu_tuyen)
mc.move(0,3+36,1+2+40)
mc.move(48/2-2,0,1+1.5+40,'.rotatePivot')
for i,d in zip(range(41,50),[0.5,1,4./9,1./9,0,1./9,4./9,1,0.5]):
    mc.move(d,'.e[%d]'%i,z=1,r=1)
mc.polyBevel([pratu+'.e[%d]'%i for i in [40,50,62,72]],o=0.5)

# ขอบบนประตู
bonpratu = mc.duplicate(pratu,n='bonpratu')[0]
mc.select(bonpratu)
mc.scale(49./48,2./72,4.5/4,bonpratu,p=[0,73+2,41])
mc.move(2,bonpratu,y=1,r=1)
mc.select(bonpratu+'.f[10]',bonpratu+'.f[40]')
mc.polyExtrudeFacet(off=0.5,ch=0)
mc.polyExtrudeFacet(ch=0)
mc.select(bonpratu+'.f[40]')
mc.scale(1,0,1,p=[0,75.1,0])
mc.scale(1,0,1,[bonpratu+'.f[%d]'%i for i in [49,50,53]],p=[0,76.2,0])
mc.polySoftEdge(bonpratu,a=180,ch=0)

# ขอบล่างประตู
langpratu = mc.duplicate(pratu,n='langpratu')[0]
mc.select(langpratu)
mc.scale(49./48,1./72,4.5/4,langpratu,p=[0,2+1,41])
mc.move(-1,langpratu,y=1,r=1)

khoppratu = mc.polyUnite([bonpratu,langpratu],ch=0,n='khoppratu')[0]
mc.hyperShade(a=phiu_khoptu)
mc.polyAutoProjection(khoppratu,ps=0.4,ch=0)
mc.polyEditUV(khoppratu+'.map[*]',sv=0.5,pv=0)

# ลบส่วนของประตูที่ไม่จำเป็น
mc.delete(pratu+'.f[10:18]',pratu+'.f[20:27]',pratu+'.f[29:37]',pratu+'.f[40:41]')
mc.delete(pratu,ch=1)
mc.polyAutoProjection(pratu+'.f[*]',ps=0.4)
mc.polyEditUV(pratu+'.map[*]',sv=0.5,pv=1)



# ส่วนแผงด้านบนที่เชื่อมประตูกับตัวตู้
thiyuet = mc.polyCube(w=5,h=1,d=11,sz=20,ch=0)[0]
mc.hyperShade(a=phiu_khoptu)
mc.move(48/2-2.5-0.5,2+75+0.5,40-1)
for i in range(mc.polyEvaluate(v=1)):
    mc.select(thiyuet+'.vtx[%d]'%i)
    t = mc.xform(q=1,t=1,ws=1)
    if(t[0]<20):
        if(t[2]>36.5):
            mc.move(23-5*math.cos((t[2]-39.5)/10*math.pi),x=1)
        else:
            mc.move(23-6*math.cos((t[2]-39.5)/12*math.pi),x=1)
mc.polyBevel(thiyuet+'.e[43]',thiyuet+'.e[85]',o=0.2,ch=0)
mc.polySoftEdge(thiyuet,a=180,ch=0)

# ตาปลา
tapla = mc.polyCylinder(r=0.5,h=1,sz=2,ch=0,n='tapla')[0]
mc.hyperShade(a=phiu_khoptu)
mc.move(48/2-2,2+75+0.5,1+1.5+40)
lop = []
yok = []
for i in range(mc.polyEvaluate(f=1)):
    s = tapla+'.f[%d]'%i
    bb = mc.xform(s,q=1,bb=1)
    if(bb[1]<0):
        lop.append(s)
    elif(bb[1]>0 and bb[0]>-0.4 and bb[2] >-0.4 and bb[3]<0.4 and bb[5]<0.4):
        yok.append(s)
mc.move(0.2,yok,y=1,r=1)
mc.delete(lop)

# ส่วนเชื่อมขาหน้าขวา
chueamkha = mc.polyCube(w=3,h=0.5,d=10,ch=0,n='chueamkha')[0]
mc.hyperShade(a=phiu_khoptu)
mc.move(22.5,0.25+1.5,40)
mc.polyBevel('.e[4:5]','.e[8:9]',o=0.9,ch=0)
mc.polySoftEdge(chueamkha+'.e[16:23]',a=180,ch=0)

thiyuet = mc.polyUnite(thiyuet,tapla,chueamkha,ch=0,n='thiyuet')[0]
mc.polyAutoProjection(thiyuet,ps=0.4,ch=0)
mc.polyEditUV(thiyuet+'.map[*]',sv=0.5,pv=1)



# ขาทั้งสี่
kha = mc.polyCylinder(r=1.5,h=1.5,sz=1,sx=12,ch=0,n='kha1')[:1]
mc.hyperShade(a=phiu_kha)
mc.move(24-1.5,0.75,43.5)
mc.select('.f[24:35]')
mc.polyExtrudeFacet(off=0.6,ch=0)
mc.polyExtrudeFacet(ltz=0.5,ch=0)
mc.polyAutoProjection(kha,ps=0.4,ch=0)
kha += mc.duplicate(kha[0])
mc.move(-24+1.5,37.5,kha[1],xz=1)
kha += mc.duplicate(kha[0])
mc.move(1.5,kha[2],z=1)
kha += mc.duplicate(kha[0])
mc.move(-24+1.5,1.5,kha[3],xz=1)
mc.scale(0.75,kha[0],y=1,p=[0,0,0])



if(nai):
    phiu_naitu = mc.duplicate(phiu_tuyen,n='phiu_naitu')[0] # ผิวด้านในตู้เย็น
    mc.setAttr(phiu_naitu+'.c',0.86,0.86,0.82,typ='double3')
    phiu_naipratu = mc.duplicate(phiu_naitu,n='phiu_naipratu')[0] # ผิวด้านในประตู
    phiu_takraeng = mc.duplicate(phiu_naitu,n='phiu_takraeng')[0] # ผิวตะแกรง
    mc.setAttr(phiu_takraeng+'.c',0.2,0.2,0.2,typ='double3')
    phiu_namkhaeng = mc.duplicate(phiu_naitu,n='phiu_namkhaeng')[0] # ผิวน้ำแข็ง
    mc.setAttr(phiu_namkhaeng+'.c',1,1,1,typ='double3')
    nun = mc.shadingNode('bump3d',au=1)
    lai = mc.shadingNode('cloud',at=1)
    mc.connectAttr(nun+'.o',phiu_namkhaeng+'.n')
    mc.connectAttr(lai+'.oa',nun+'.bv')
    phiu_chongkhaeng = mc.duplicate(phiu_naitu,n='phiu_chongkhaeng')[0] # ผิวช่องแข็ง
    mc.setAttr(phiu_chongkhaeng+'.c',0.8,0.8,0.8,typ='double3')
    mc.setAttr(phiu_chongkhaeng+'.it',0.5,0.5,0.5,typ='double3')
    
    
    
    # ตัวตู้ด้านใน
    naituatu = mc.polyCube(w=44,h=71,d=36,sy=3)[0]
    mc.move(0,2+2+35.5,22)
    mc.scale(1,2.8,1,naituatu+'.f[1]')
    mc.select(naituatu+'.f[0:2]')
    mc.polyExtrudeFacet(off=1)
    mc.polyExtrudeFacet(ltz=-35)
    mc.select(naituatu+'.f[22]',naituatu+'.f[28]')
    mc.scale(32./34,1,34./35,p=[0,0,40])
    mc.select(naituatu+'.f[0]')
    mc.scale(1,2,2,naituatu+'.f[0]',p=[0,5,5])
    mc.polyExtrudeFacet(tz=16)
    mc.select(naituatu+'.f[0]',naituatu+'.f[32]')
    mc.polyExtrudeFacet(ty=16)
    mc.move(-2,naituatu+'.f[34]',z=1,r=1)
    mc.select(naituatu+'.f[34]')
    mc.move(-21,naituatu+'.e[67]',x=1)
    mc.move(21,naituatu+'.e[68]',x=1)
    mc.polyExtrudeFacet(tz=1)
    mc.move(1.75,naituatu+'.f[42]',y=1,r=1)
    mc.polyExtrudeFacet(tz=1)
    mc.scale(16.75/17.75,y=1,p=[0,5,0])
    mc.delete(naituatu+'.f[3:13]')
    mc.delete([naituatu+'.f[%d]'%i for i in [19,20,22,26,27,28,29,30,32,33,36]])
    
    # ส่วนที่ยื่นในตู้
    yuen1 = mc.polyCube(w=1,h=2,d=1,sy=2)[0]
    mc.move(-21+0.5,36+5-0.2,28+5-1)
    mc.move(1.2,'.e[6]','.e[8]',z=1,r=1)
    mc.move(0.2,'.e[7]','.e[9]',z=1,r=1)
    mc.move(1,'.e[13]','.e[15]',z=1,r=1)
    mc.select('.f[4]','.f[6]')
    mc.polyExtrudeFacet()
    mc.scale(1.6,1,4,p=[-21,0,37])
    mc.scale(1,1,0,yuen1+'.f[4]',p=[0,0,5])
    mc.move(-0.8,yuen1+'.e[15]',yuen1+'.e[24]',y=1,r=1)
    mc.scale(0,yuen1+'.e[28]',y=1,p=[0,40.6,0])
    mc.delete(yuen1+'.f[8:9]',yuen1+'.f[12]')
    
    yuen2 = mc.polyCube(w=1.6,h=1,d=12)[0]
    mc.move(-21+0.8,37+5,6+5)
    mc.move(0.5,'.e[11]',r=1,y=1)
    mc.move(1,'.e[4]',r=1,z=1)
    mc.delete(yuen2+'.f[5]')
    
    yuen = mc.duplicate(yuen1,yuen2)
    mc.scale(-1,1,1,yuen,p=[0,0,0])
    
    yuen = [yuen1,yuen2]+yuen+mc.duplicate(yuen,yuen1,yuen2)
    mc.move(-6,yuen[4:],r=1,y=1)
    
    yuen += mc.duplicate(yuen2)
    mc.move(16,yuen[-1]+'.f[0]',z=1,r=1)
    mc.move(17,yuen[-1],y=1,r=1)
    yuen += mc.duplicate(yuen[-1])
    mc.scale(-1,yuen[-1],x=1,p=[0,0,0])
    
    yuen.append(mc.polyCube(w=1.6,h=1,d=10.8)[0])
    mc.move(-21+0.8,16.5+0.8+5,17+10.8/2+5)
    mc.move(0.5,'.e[11]',r=1,y=1)
    mc.move(1,'.e[4]',r=1,z=1)
    mc.delete(yuen[-1]+'.f[5]')
    yuen += mc.duplicate(yuen[-1])
    mc.scale(-1,yuen[-1],x=1,p=[0,0,0])
    
    yuen.append(mc.polyCube(w=36,h=2,d=0.5,sy=2)[0])
    mc.move(0,5+1,33)
    mc.move(-0.5,yuen[-1]+'.e[18:19]',y=1,r=1)
    mc.select(yuen[-1]+'.f[5]')
    mc.scale(2.5,z=1)
    mc.move(-0.25,z=1,r=1)
    mc.delete()
    mc.select(yuen[-1]+'.f[5:8]')
    mc.polyExtrudeFacet(ltz=1,tz=-2./9,sz=1.5)
    mc.polyExtrudeFacet(ltz=1,tz=-6./9,sz=1.5)
    mc.polyExtrudeFacet(ltz=1,tz=-10./9,sz=1.5)
    
    # รวมส่วนที่ยื่นเข้ากับตัวตู้
    naituatu = mc.polyUnite(naituatu,yuen,ch=0,n='naituatu')
    mc.hyperShade(a=phiu_naitu)
    mc.polySoftEdge(a=91,ch=0)
    mc.polyAutoProjection(ps=0.4,ch=0)
    
    
    
    # ที่เปิดช่องแข็ง
    chongkhaeng = mc.polyCube(w=36,h=12,d=0.2)[0]
    mc.move(0,5+69-6,33.5+0.1)
    mc.select(chongkhaeng+'.f[0]')
    mc.polyExtrudeFacet(off=1)
    mc.polyExtrudeFacet(sx=0.6,sy=0.7,tz=-0.1)
    mc.move(1,y=1,r=1)
    mc.polySoftEdge(chongkhaeng,a=91,ch=0)
    ru = []
    for i in range(-15,16,2):
        ru.append(mc.polyCube(w=0.7,h=3,d=1)[0])
        mc.polyBevel(o=0.2)
        mc.move(i*0.6,69,+33.5+0.1)
    chongkhaeng = mc.polyCBoolOp(chongkhaeng,ru,op=2,ch=0,n='chongkhaeng')[0]
    mc.hyperShade(a=phiu_chongkhaeng)
    mc.polyBevel(chongkhaeng+'.e[165]',chongkhaeng+'.e[169]',o=0.4)
    
    # น้ำแข็งในช่องแข็ง
    namkhaeng = mc.polyTorus(r=6,sr=4,ax=[0,0,1],ch=0,n='namkhaeng')[0]
    mc.hyperShade(a=phiu_namkhaeng)
    yup = mc.polyTorus(r=6,sr=0.1,ax=[0,0,1],ch=0,n='yup')[0]
    mc.move(0,5+69-6,5,namkhaeng,yup)
    lop = []
    for i in range(mc.polyEvaluate(f=1)):
        s = namkhaeng+'.f[%d]'%i
        bb = mc.xform(s,q=1,bb=1)
        if(bb[1]>-0.1 or bb[5]<0.1):
            lop.append(s)
            lop.append(s.replace(namkhaeng,yup))
    mc.delete(lop)
    
    g = [[],[],[],[]]
    for i in range(mc.polyEvaluate(v=1)):
        s = namkhaeng+'.vtx[%d]'%i
        t = mc.xform(s,q=1,t=1)
        if(t[0]>0.01):
            g[0].append(s)
            g[0].append(s.replace(namkhaeng,yup))
        elif(t[0]<-0.01):
            g[1].append(s)
            g[1].append(s.replace(namkhaeng,yup))
        if(t[1]>-0.01):
            g[2].append(s)
            g[2].append(s.replace(namkhaeng,yup))
        if(t[2]>0.01):
            g[3].append(s)
            g[3].append(s.replace(namkhaeng,yup))
            mc.move(3.3,s.replace(namkhaeng,yup),z=1,r=1)
    
    mc.move(10,g[0],x=1,r=1)
    mc.move(-10,g[1],x=1,r=1)
    mc.move(6,g[2],y=1,r=2)
    mc.move(24,g[3],z=1,r=1)
    
    mc.polyAutoProjection(namkhaeng,ps=0.4)
    for i in range(mc.polyEvaluate(v=1)):
        s = namkhaeng+'.vtx[%d]'%i
        t = mc.xform(s,q=1,t=1)
        mc.move(random.uniform(-0.5,0.5),s,x=1,r=1)
        if(t[1]<0.01):
            mc.move(random.uniform(-0.5,0.5),s,y=1,r=1)
        if(t[2]>0.01):
            mc.move(random.uniform(-0.5,0.5),s,z=1,r=1)
        
    mc.select(yup,namkhaeng)
    bs = mc.blendShape(n='namkhaeng_bs')[0]
    mc.delete(yup)
    mc.addAttr(bs,ln='namae',nn=u'名前',dt='string')
    mc.setAttr(bs+'.namae',yup+u'๑氷を消す๑2๐',typ='string')
    
    
    
    # ตะแกรงวางของในตู้
    takraeng1 = mc.polyTorus(r=2,sr=0.2,sx=8,sy=8)[0]
    mc.rotate(22.5,y=1)
    g = [[],[],[],[]]
    for i in range(mc.polyEvaluate(v=1)):
        s = takraeng1+'.vtx[%d]'%i
        t = mc.xform(s,q=1,t=1,ws=1)
        g[2*(t[0]<0)+(t[2]<0)].append(s)
    mc.move(42/2-2.2,0,12-2.2,g[0],r=1)
    mc.move(42/2-2.2,0,-16+2.2,g[1],r=1)
    mc.move(-42/2+2.2,0,12-2.2,g[2],r=1)
    mc.move(-42/2+2.2,0,-16+2.2,g[3],r=1)
    mc.move(0,5+18,16+5,takraeng1)
    takraeng2 = mc.duplicate(takraeng1)[0]
    mc.move(18,y=1,r=1)
    mc.move(16,g[1],g[3],z=1,r=1)
    
    # ซี่ของตะแกรง
    sitakraeng1 = []
    sitakraeng2 = []
    for i in range(-6,7):
        sitakraeng1.append(mc.polyCube(w=0.3,h=0.3,d=12-0.8)[0])
        mc.delete(sitakraeng1[-1]+'.f[0]',sitakraeng1[-1]+'.f[2]')
        mc.move(i*3,5+18,22+5)
        sitakraeng2.append(mc.polyCube(w=0.3,h=0.3,d=28-0.8)[0])
        mc.delete(sitakraeng2[-1]+'.f[0]',sitakraeng2[-1]+'.f[2]')
        mc.move(i*3,5+36,14+5)
    takraeng1 = mc.polyUnite(takraeng1,sitakraeng1,ch=0,n='takraeng1')
    takraeng2 = mc.polyUnite(takraeng2,sitakraeng2,ch=0,n='takraeng2')
    takraeng = mc.polyUnite(takraeng1,takraeng2,ch=0,n='takraeng')[0]
    mc.hyperShade(a=phiu_takraeng)
    mc.polySoftEdge(a=180,ch=0)
    mc.polyAutoProjection(ps=0.4,ch=0)
    
    
    
    # ชั้นวางด้านในประตู
    naipratu = mc.polyCube(w=41,h=68,d=1,sx=5,sy=7)[0]
    mc.move(0,3+36,0.5+41)
    mc.scale(1,1.95,1,naipratu+'.f[45:49]',p=[0,3+36+17.5,0])
    mc.scale(1,1.95,1,naipratu+'.f[55:59]',p=[0,3+36,0])
    mc.scale(1,1.95,1,naipratu+'.f[65:69]',p=[0,3+36-17.5,0])
    mc.scale(1.5,1,1,[naipratu+'.f[%d]'%(i+j) for i in range(42,73,5) for j in range(-1,2)])
    mc.scale(2.6,1,1,[naipratu+'.f[%d]'%i for i in range(42,73,5)])
    mc.polyExtrudeFacet([naipratu+'.f[%d]'%i for i in range(40,75) if i%10!=7])
    mc.move(-7,[naipratu+'.f[%d]'%(i+j) for i in range(42,73,5) for j in [-2,2]],naipratu+'.f[72]',z=1,r=1)
    mc.move(-5,[naipratu+'.f[%d]'%i for i in range(52,63,10)],z=1,r=1)
    mc.move(-1,naipratu+'.f[42]',z=1,r=1)
    mc.move(2,[naipratu+'.e[%d]'%i for i in [158,192,222]],y=1,r=1)
    mc.polyExtrudeFacet([naipratu+'.f[%d]'%i for i in [46,48,56,58,66,68,103,104,111,112,119,120]])
    mc.scale(0,[naipratu+'.f[%d]'%i for i in [48,58,68,104,112,120]],x=1,p=[18.45,0,0])
    mc.scale(0,[naipratu+'.f[%d]'%i for i in [46,56,66,103,111,119]],x=1,p=[-18.45,0,0])
    mc.polyBevel([naipratu+'.e[%d]'%i for i in [148,166,171,178,183,194,199,206,211,222,227,234,240,252,239,243,247,250,253]],o=1)
    
    mc.select(naipratu+'.f[159:160]')
    mc.polyExtrudeFacet()
    mc.scale(0.4,p=[0,8.5,0],y=1)
    mc.polyExtrudeFacet(ltz=1)
    mc.scale(0.7,p=[0,9.5,0],y=1)
    mc.scale(0.7,naipratu+'.f[159]',p=[-18.45,0,0],x=1)
    mc.scale(0.7,naipratu+'.f[160]',p=[18.45,0,0],x=1)
    mc.move(0.5,2,[naipratu+'.e[%d]'%i for i in [283,286,295,301,307,313,319]],xz=1,r=1)
    mc.move(-0.5,2,[naipratu+'.e[%d]'%i for i in [287,290,296,302,308,314,320]],xz=1,r=1)
    mc.move(0.5,naipratu+'.vtx[179]',naipratu+'.vtx[187]',y=1,r=1)
    mc.delete(naipratu+'.f[0:39]',naipratu+'.f[58:76]')
    
    # ที่กั้น
    thikan = [mc.polyCube(w=36.9,h=2,d=1)[0]]
    mc.move(0,13,34)
    mc.polyBevel('.e[2:3]',o=0.25)
    thikan.append(mc.duplicate(thikan[0])[0])
    mc.move(0,34,35,thikan[1])
    thikan.append(mc.duplicate(thikan[0])[0])
    mc.move(0,56,35,thikan[2])
    naipratu = mc.polyUnite(naipratu,thikan,ch=0,n='naipratu')
    
    #lop = mc.duplicate(naituatu)[0]
    #naipratu = mc.polyCBoolOp(naipratu,lop,op=2,ch=0,n='naipratu')[0]
    mc.hyperShade(a=phiu_naipratu)
    mc.polySoftEdge(a=89,ch=0)
    mc.polyAutoProjection(ps=0.4,ch=0)



    # ใส่กระดูกให้หมุนตู้เย็นได้
    mc.select(cl=1)
    kho = mc.joint(p=[24-1.5,2+75+0.5,1+2.5+40]),mc.joint(p=[-24+1.5,2+75+0.5,1+2.5+40])
    for p in [pratu,khoppratu,maelek,naipratu]:
        mc.skinCluster(kho[1],p)[0]
    mc.rotate(0,180,0,kho[0])
    
    mc.select(cl=1)
    kho1 = mc.joint(p=[0,5+18,16+5])
    mc.select(cl=1)
    kho2 = mc.joint(p=[0,5+36,16+5])
    sk = mc.skinCluster(kho1,kho2,takraeng)[0]
    n_vtx = mc.polyEvaluate(takraeng,v=1)
    mc.skinPercent(sk,takraeng+'.vtx[0:%d]'%(n_vtx/2-1),tv=(kho1,1))
    mc.skinPercent(sk,takraeng+'.vtx[%d:%d]'%(n_vtx/2,n_vtx),tv=(kho2,1))
    
    mc.select(cl=1)
    kho = mc.joint(p=[0,5+69,33.5+0.2]),mc.joint(p=[0,5+69-12,33.5+0.2])
    sk = mc.skinCluster(kho,chongkhaeng)[0]
    mc.skinPercent(sk,chongkhaeng+'.vtx[*]',tv=(kho[0],1))