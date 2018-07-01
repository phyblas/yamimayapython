# -*- coding: utf-8 -*-
import maya.cmds as mc

# เตรียมฟังก์ชันสำหรับใส่ผิวนูนเว้า
def sainun(m,f,n):
    lainun = mc.shadingNode('file',at=1,n=n)
    mc.setAttr(lainun+'.alphaIsLuminance',1)
    mc.setAttr(lainun+'.ftn',f,typ='string')
    nun = mc.shadingNode('bump2d',au=1,n='nun')
    #mc.setAttr(nun+'.bumpDepth',0.1)
    mc.connectAttr(lainun+'.oa',nun+'.bv')
    mc.connectAttr(nun+'.o',m+'.n')
    ple = mc.shadingNode('place2dTexture',au=1)
    mc.defaultNavigation(ce=1,s=ple,d=lainun)

# ผิวส่วนฐาน
phiu_than = mc.shadingNode('blinn',asShader=1,n='phiu_than')
mc.setAttr(phiu_than+'.ambc',0.5,0.5,0.5,typ='double3')
mc.setAttr(phiu_than+'.sro',0.3)
lai_than = mc.shadingNode('file',at=1,n='lai_than')
mc.connectAttr(lai_than+'.oc',phiu_than+'.c')
mc.setAttr(lai_than+'.ftn','/Users/patn/Dropbox/hokhoi_hanoi/lai_than.jpg',typ='string')
sainun(phiu_than,'/Users/patn/Dropbox/hokhoi_hanoi/nun_than.jpg','lai_than')

# ผิวส่วนฐานที่มีลานอิฐ
phiu_thanit = mc.duplicate(phiu_than,n='phiu_thanit')[0]
lai_thanit = mc.shadingNode('file',at=1,n='lai_thanit')
mc.connectAttr(lai_thanit+'.oc',phiu_thanit+'.c')
mc.setAttr(lai_thanit+'.ftn','/Users/patn/Dropbox/hokhoi_hanoi/lai_thanit.jpg',typ='string')
sainun(phiu_thanit,'/Users/patn/Dropbox/hokhoi_hanoi/nun_thanit.jpg','lai_nunthanit')

# ผิวเสาหลัก
phiu_sao = mc.duplicate(phiu_than,n='phiu_sao')[0]
mc.setAttr(phiu_sao+'.sc',0.2,0.2,0.2,typ='double3')
lai_sao = mc.shadingNode('file',at=1,n='lai_sao')
mc.connectAttr(lai_sao+'.oc',phiu_sao+'.c')
mc.setAttr(lai_sao+'.ftn','/Users/patn/Dropbox/hokhoi_hanoi/lai_mai.jpg',typ='string')

# ผิวรั้วหอคอย
phiu_rua = mc.duplicate(phiu_than,n='phiu_rua')[0]
mc.setAttr(phiu_rua+'.sc',0.2,0.2,0.2,typ='double3')
lai_rua = mc.shadingNode('file',at=1,n='lai_rua')
mc.connectAttr(lai_rua+'.oc',phiu_rua+'.c')
mc.setAttr(lai_rua+'.ftn','/Users/patn/Dropbox/hokhoi_hanoi/lai_mai.jpg',typ='string')
sainun(phiu_rua,'/Users/patn/Dropbox/hokhoi_hanoi/nun_ruamai.jpg','nun_mai')

# ผิวเสาที่มุม
phiu_saomum = mc.duplicate(phiu_than,n='phiu_saomum')[0]
mc.setAttr(phiu_saomum+'.sc',0.7,0.7,0.7,typ='double3')
lai_hingranite = mc.shadingNode('granite',at=1,n='lai_hingranite')
mc.connectAttr(lai_hingranite+'.oc',phiu_saomum+'.c')
mc.setAttr(lai_hingranite+'.fillerColor',0.65,0.41,0.42,typ='double3')
ple = mc.shadingNode('place3dTexture',au=1)
mc.defaultNavigation(ce=1,s=ple,d=lai_hingranite)

# ผิวส่วนขอบทุมของหอคอย
phiu_khopho = mc.duplicate(phiu_than,n='phiu_khopho')[0]
mc.setAttr(phiu_khopho+'.c',0.65,0.34,0.35,typ='double3')

# ผิวผนังหอคอย
phiu_phanang = mc.duplicate(phiu_than,n='phiu_phanang')[0]
lai_phanang = mc.shadingNode('file',at=1,n='lai_phanang')
mc.connectAttr(lai_phanang+'.oc',phiu_phanang+'.c')
mc.setAttr(lai_phanang+'.ftn','/Users/patn/Dropbox/hokhoi_hanoi/lai_phanangit.jpg',typ='string')
sainun(phiu_phanang,'/Users/patn/Dropbox/hokhoi_hanoi/nun_phanangit.jpg','nun_phanang')

# ผิวขอบประตู
phiu_khoppratu = mc.duplicate(phiu_than,n='phiu_khoppratu')[0]
mc.setAttr(phiu_khoppratu+'.sc',0.2,0.2,0.2,typ='double3')
mc.connectAttr(lai_hingranite+'.oc',phiu_khoppratu+'.c')

# ผิวบานประตู
phiu_banpratu = mc.duplicate(phiu_than,n='phiu_banpratu')[0]
mc.setAttr(phiu_banpratu+'.sc',0.2,0.2,0.2,typ='double3')
lai_banpratu = mc.shadingNode('file',at=1,n='lai_banpratu')
mc.setAttr(lai_banpratu+'.ftn','/Users/patn/Dropbox/hokhoi_hanoi/lai_banpratu.png',typ='string')
mc.connectAttr(lai_banpratu+'.oc',phiu_banpratu+'.c')
sainun(phiu_banpratu,'/Users/patn/Dropbox/hokhoi_hanoi/nun_banpratu.png','nun_banpratu')

# ผิวขอบหน้าต่าง
phiu_khopnatang = mc.duplicate(phiu_than,n='phiu_khopnatang')[0]
mc.setAttr(phiu_khopnatang+'.sc',0.7,0.7,0.7,typ='double3')
mc.connectAttr(lai_hingranite+'.oc',phiu_khopnatang+'.c')
sainun(phiu_khopnatang,'/Users/patn/Dropbox/hokhoi_hanoi/nun_khopnatang.png','nun_khopnatang')

# ผิวบานหน้าต่าง
phiu_bannatang = mc.duplicate(phiu_than,n='phiu_bannatang')[0]
mc.setAttr(phiu_bannatang+'.sc',0.2,0.2,0.2,typ='double3')
lai_bannatang = mc.shadingNode('file',at=1,n='lai_bannatang')
mc.setAttr(lai_bannatang+'.ftn','/Users/patn/Dropbox/hokhoi_hanoi/lai_bannatang.png',typ='string')
mc.connectAttr(lai_bannatang+'.oc',phiu_bannatang+'.c')
sainun(phiu_bannatang,'/Users/patn/Dropbox/hokhoi_hanoi/nun_bannatang.png','nun_bannatang')

# ผิวพื้นหอคอย
phiu_phuenho = mc.duplicate(phiu_than,n='phiu_phuenho')[0]
lai_phuenho = mc.shadingNode('file',at=1,n='lai_phuenho')
mc.connectAttr(lai_phuenho+'.oc',phiu_phuenho+'.c')
mc.setAttr(lai_phuenho+'.ftn','/Users/patn/Dropbox/hokhoi_hanoi/lai_phuenit.jpg',typ='string')
sainun(phiu_phuenho,'/Users/patn/Dropbox/hokhoi_hanoi/nun_phuenit.jpg','nun_phuenho')

# ผิวเสารั้วหอคอย
phiu_saorua = mc.duplicate(phiu_than,n='phiu_saorua')[0]
mc.setAttr(phiu_saorua+'.sc',0.6,0.6,0.6,typ='double3')
lai = mc.shadingNode('marble',at=1,n='lai_hinon')
mc.connectAttr(lai+'.oc',phiu_saorua+'.c')
for at,v in zip(['veinWidth','diffusion','contrast','amplitude','ripplesX','ripplesY','ripplesZ','amplitude','ratio'],[0.01,0.5,0,1,0.8,0.8,0.8,5,0.9]):
    mc.setAttr(lai+'.'+at,v)
mc.setAttr(lai+'.fillerColor',0.98,0.98,0.98,typ='double3')
mc.setAttr(lai+'.veinColor',0.19,0.21,0.26,typ='double3')
ple = mc.shadingNode('place3dTexture',au=1)
mc.defaultNavigation(ce=1,s=ple,d=lai)
for at,v in zip(['sx','sy','sz'],[4,4,4]):
    mc.setAttr(ple+'.'+at,v)

# ผิวม้านั่งด้านบนหอคอย
phiu_manang = mc.duplicate(phiu_saorua,n='phiu_bandai')[0]
mc.setAttr(phiu_manang+'.sc',0.6,0.6,0.6,typ='double3')
mc.connectAttr(lai+'.oc',phiu_manang+'.c')

# ผิวบันไดด้านบนหอคอย
phiu_bandai = mc.duplicate(phiu_than,n='phiu_manang')[0]
mc.setAttr(phiu_bandai+'.c',0.5,0.5,0.5,typ='double3')
mc.setAttr(phiu_bandai+'.sc',0.9,0.9,0.9,typ='double3')

# ผิวส่วนมืดมิดด้านในที่เสียบเสา
phiu_dammit = mc.duplicate(phiu_than,n='phiu_dammit')[0]
mc.setAttr(phiu_dammit+'.c',0.,0.,0.,typ='double3')
mc.setAttr(phiu_dammit+'.sc',0.,0.,0.,typ='double3')
mc.setAttr(phiu_dammit+'.ambc',0.,0.,0.,typ='double3')



thansung = 4 # ความสูงฐาน
sungchanla = 3 # หอคอยสูงชั้นละ
hokhoi = [] # ลิสต์เก็บส่วนประกอบต่างๆของหอคอย
for i in range(5):
    yusung = thansung+i*sungchanla # ความสูงของพื้นชั้น
    kwang = 15.-2.5*i # ความกว้างหอคอย
    dankwang = kwang/(1+2**0.5) # ความกว้างของด้าน
    tuachan = mc.polyPrism(ns=8,w=dankwang,l=sungchanla)[0] # ตัวชั้น
    mc.rotate(45/2.,y=1)
    mc.move(sungchanla/2.+yusung,y=1)
    mc.hyperShade(a=phiu_khopho)
    
    # ทำให้พื้นด้านบนตัวชั้นมีขึ้นมีลง
    mc.select(tuachan+'.f[9]')
    mc.polyExtrudeFacet(sx=(kwang-0.45)/kwang,sz=(kwang-0.45)/kwang)
    mc.polyExtrudeFacet(ltz=-0.05)
    if(i<4):
        mc.polyExtrudeFacet(sx=(kwang-2.2)/(kwang-0.45),sz=(kwang-2.2)/(kwang-0.45))
        mc.polyExtrudeFacet(ltz=0.11)
        mc.polyExtrudeFacet(sx=(kwang-2.5)/(kwang-2.2),sz=(kwang-2.5)/(kwang-2.2))
        mc.polyExtrudeFacet(ltz=-0.06)
    else:
        mc.polyExtrudeFacet(sx=(kwang-2.2)/(kwang-0.9),sz=(kwang-2.2)/(kwang-0.9))
        mc.polyExtrudeFacet(ltz=0.05)
    
    # ทำให้ผนังหยักเว้าลงไป
    mc.select(tuachan+'.f[0:7]')
    for j in range(8):
        mc.polyExtrudeFacet(sy=(3-0.04*(j+1+3))/(3-0.04*(j+(j!=0)*3)))
        mc.polyExtrudeFacet(ltz=-0.02)
    
    saolop = mc.polyCylinder(h=100,r=0.5,sx=16)[0] # เสาเสียบตรงกลางที่จะเจาะรูหอคอย
    mc.hyperShade(a=phiu_dammit)
    tuachan = mc.polyCBoolOp([tuachan,saolop],op=2,n='chanhokhoi%d'%(i+1))[0]
    
    l = [[],[],[],[],[],[],[],[]] # คัดเลือกแยกหน้าต่างๆของหอคอย
    phuenho = [] # ส่วนพื้น
    klangho = [] # ส่วนกลาง
    nai = [] # ส่วนด้านในที่โดนเสาเสียบ
    for j in range(mc.polyEvaluate(tuachan,f=1)):
        s = tuachan+'.f[%d]'%j
        bb = mc.xform(s,q=1,bb=1,ws=1)
        bx = bb[3]-bb[0]
        bz = bb[5]-bb[2]
        if(abs(bb[0])<1 and abs(bb[2])<1 and abs(bb[3])<1 and abs(bb[5])<1):
            nai.append(s)
            continue
        if(bb[1]<yusung+1.5 and bb[4]>yusung+1.5):
            klangho.append(s)
        if(bb[1]-(yusung+3-0.05)>-0.001 and bb[4]-(yusung+3-0.05)<0.001):
            phuenho.append(s)
        elif(bx-bz>0.001):
            if(bb[2]>0):
                l[0].append(s)
            else:
                l[4].append(s)
        elif(bx-bz<-0.001):
            if(bb[0]<0):
                l[2].append(s)
            else:
                l[6].append(s)
        elif(bb[0]*bb[3]>0):
            if(bb[3]*bb[5]>0):
                if(bb[0]<0):
                    l[3].append(s)
                else:
                    l[7].append(s)
            else:
                if(bb[0]<0):
                    l[1].append(s)
                else:
                    l[5].append(s)
    for j in range(8):
        mc.select(l[j])
        k = (j+i*3)%8
        mc.polyProjection(pcx=(6-dankwang/2.)*(k%2*2-1),pcy=yusung+1.5+(k//2-1.5)*3*0.95,pcz=0,rx=0,ry=0,rz=0,psu=12,psv=12*0.95)
        mc.rotate(45,tuachan,y=1,r=1)
    mc.select(phuenho)
    mc.hyperShade(a=phiu_phuenho)
    mc.polyProjection(pcx=0,pcy=0,pcz=0,rx=90,ry=0,rz=0,psu=1,psv=1)
    mc.select(klangho)
    mc.hyperShade(a=phiu_phanang)
    
    # เสาที่มุมหอคอย
    saomum = []
    for j in range(8):
        saomum.append(mc.polyCylinder(h=sungchanla-0.12,r=0.15,sx=8)[0])
        mc.hyperShade(a=phiu_saomum)
        ppj = mc.polyProjection(saomum[-1]+'.f[*]',t='cylindrical')[0]
        for at,v in zip(['pcx','pcy','pcz','phs','ph','rx','ry','rz'],[0,0,0,360,sungchanla-0.12,0,0,0]):
            mc.setAttr(ppj+'.'+at,v)
        mc.select(saomum[-1])
        mc.move(0,yusung+sungchanla/2.,(dankwang**2+kwang**2)**0.5/2-0.02*8)
        mc.rotate((45+j*90)/2.,y=1,r=1,p=[0,0,0])
        mc.delete(saomum[-1]+'.f[8:9]')
    suanprakop = [tuachan]+saomum
    
    # ขอบประตู
    pratu = mc.polyCube(w=0.1,h=0.2,d=0.16)[0]
    mc.hyperShade(a=phiu_khoppratu)
    mc.move(0,yusung+2.4+0.1,kwang/2.-0.08)
    mc.select(pratu+'.f[4]')
    mc.rotate(-15,z=1,r=1)
    for j in range(5):
        mc.polyExtrudeFacet(ltz=0.14,rz=-15)
    mc.polyExtrudeFacet(ltz=1.95)
    mc.select(pratu+'.f[5]')
    mc.rotate(15,z=1,r=1)
    for j in range(5):
        mc.polyExtrudeFacet(ltz=0.14,rz=15)
    mc.polyExtrudeFacet(ltz=1.95)
    # คัดลบส่วนด้านล่างและด้านในที่มองไม่เห็น
    lop = []
    for k in range(mc.polyEvaluate(pratu,f=1)):
        s = pratu+'.f[%d]'%k
        bb = mc.xform(s,q=1,bb=1)
        if(bb[5]<0 or bb[4]<-0.9):
            lop.append(s)
    mc.delete(lop)
    mc.polyBevel(pratu,o=0.01) # หักขอบสักหน่อย
    mc.polySoftEdge(pratu,a=44)
    mc.polyAutoProjection(pratu+'.f[*]',ps=0.1)
    
    # บานประตู
    banpratu = mc.polyPlane(w=0.84,h=2.31,sx=1,sy=1,ax=[0,0,1])[0]
    mc.hyperShade(a=phiu_banpratu)
    mc.polyProjection(banpratu+'.f[*]',rx=0,ry=0,rz=0,psu=2.31,psv=2.31)
    mc.move(0,yusung+1.24,kwang/2.-0.02,banpratu)
    pratu = mc.polyUnite(pratu,banpratu,ch=0)[0] # รวมประตูกับขอบ
    
    # หน้าต่าง
    natang = []
    for j in range(1,8):
        if(j==4 and i==4):
            continue # ชั้นบนสุดด้านหลังไม่ต้องเพราะใส่บันได
        natang.append(mc.polyCylinder(r=0.6,h=0.08,ax=[0,0,1],sx=16,sz=3)[0])
        mc.hyperShade(a=phiu_khopnatang)
        mc.move(0,yusung+1.5,kwang/2.-0.08)
        wongyai = [] # ขอบหน้าต่างด้านใน
        wonglek = [] # ส่วนบานหน้าต่าง
        lop = [] # ส่วนด้านในที่จะลบ
        for k in range(mc.polyEvaluate(f=1)):
            s = natang[-1]+'.f[%d]'%k
            bb = mc.xform(s,q=1,bb=1)
            if(bb[2]>0):
                r = (((bb[0]+bb[3])/2)**2+((bb[1]+bb[4])/2)**2)**0.5
                if(r<0.4):
                    wongyai.append(s)
                if(r<0.2):
                    wonglek.append(s)
            elif(bb[5]<0):
                lop.append(s)
        sc = 1+0.08/0.6*2**0.5
        mc.scale(sc,sc,1,lop)
        mc.polyProjection(natang[-1]+'.f[*]',pcy=yusung+1.5,rx=0,ry=0,rz=0,psu=1.2*sc,psv=1.2*sc)
        mc.scale(1/sc,1/sc,1,lop)
        mc.select(wonglek)
        mc.move(-0.07,r=1,z=1)
        mc.scale(2,2,1)
        mc.hyperShade(a=phiu_bannatang) # ผิวบานหน้าต่าง
        mc.polyProjection(wonglek,pcy=yusung+1.5,rx=0,ry=0,rz=0,psu=0.8,psv=0.8)
        mc.select(wongyai)
        mc.scale(1.2,1.2,1)
        mc.polySoftEdge(a=89)
        mc.delete(lop)
        mc.rotate(j*45,natang[-1],y=1,p=[0,0,0])
    
    # รั้วระเบียงหอคอย
    rua1 = mc.polyCube(w=dankwang-0.05,h=0.08,d=0.08)[0] # รั้วส่วนบน
    mc.hyperShade(a=phiu_rua)
    mc.polyProjection(rua1+'.f[0]',rua1+'.f[2]',rx=0,ry=0,rz=90,psu=0.2,psv=0.02)
    mc.polyProjection(rua1+'.f[1]',rua1+'.f[3]',rx=90,ry=90,rz=0,psu=0.2,psv=0.02)
    mc.move(0,yusung+sungchanla+1.2,kwang/2-0.1,rua1)
    mc.delete([rua1+'.f[4:5]'])
    
    rua2 = mc.polyCube(w=dankwang-0.05,h=0.6,d=0.08,sy=5)[0] # รั้วส่วนล่าง
    mc.hyperShade(a=phiu_rua)
    mc.move(0,yusung+sungchanla+0.5,kwang/2-0.1)
    mc.select(rua2+'.f[2]',rua2+'.f[8]')
    mc.scale(1,2.8,0.5)
    mc.polyProjection(rx=0,ry=0,rz=0,psu=0.6,psv=0.6)
    mc.polyProjection([rua2+'.f[%d]'%j for j in [0,4,6,10]],rx=0,ry=0,rz=90,psu=0.2,psv=0.02)
    mc.polyProjection([rua2+'.f[%d]'%j for j in range(1,14,2)],rx=90,ry=90,rz=0,psu=0.2,psv=0.02)
    mc.delete(rua2+'.f[12:21]')
    saolaerua = [rua1,rua2]
    for j in range(7):
        if(i==4 and j==3):
            # ชั้นบนสุดด้านหลังใส่บันไดแต่ไม่ใส่รั้ว
            bandai = [mc.polyCube(w=0.5,h=2.84,d=0.1)[0]]
            for k in range(-4,5):
                bandai.append(mc.polyCube(w=0.46,h=0.26,d=1)[0])
                mc.move(k*0.3,y=1)
            bandai = mc.polyCBoolOp(bandai,op=2,ch=0)[0]
            mc.move(0,yusung+sungchanla/2.,-kwang/2.+0.06)
            mc.hyperShade(a=phiu_bandai)
            saolaerua.append(bandai)
        else:
            # ใส่รั้ว
            rua = mc.duplicate(rua1,rua2)
            mc.rotate(45*(j+1),rua,y=1,p=[0,0,0])
            saolaerua.extend(rua)
    # เสาที่มุมรั้ว
    for j in range(8):
        saorua = mc.polyCube(w=0.18,h=1.3,d=0.18)[0]
        mc.hyperShade(a=phiu_saorua)
        mc.move(0,yusung+sungchanla+1.3/2,(dankwang**2+kwang**2)**0.5/2-0.14)
        mc.rotate((45+j*90)/2.,y=1,r=1,p=[0,0,0])
        mc.polyExtrudeFacet(saorua+'.f[1]',ltz=0.04,off=0.04)
        mc.delete(saorua+'.f[3]')
        mc.polyAutoProjection(saorua+'.f[*]',ps=0.1)
        saolaerua.append(saorua)
    
    suanprakop.extend([pratu]+natang+saolaerua)
    tuachan = mc.polyUnite(suanprakop,ch=0,n='ho1')[0] # รวมส่วนประกอบในแต่ละชั้นเข้าด้วยกัน
    mc.move(-yusung,tuachan+'.f[*]',y=1,r=1)
    mc.move(yusung,tuachan,y=1,r=1)
    hokhoi.append(tuachan)

# เก้าอี้ที่ชั้นบนสุด
manang = mc.polyTorus(r=1.25,sr=0.25*2**0.5,sx=32,sy=4,tw=45)[0]
mc.hyperShade(a=phiu_manang)
mc.rotate(360/64.,manang+'.f[*]',y=1)
mc.move(yusung+sungchanla+0.25,y=1)
mc.select([manang+'.f[%d]'%(6+i*8) for i in range(4)])
mc.move(-0.48,r=1,y=1)
mc.select([manang+'.f[%d:%d]'%(31+i*8+(i==0),37+i*8) for i in range(4)]+[manang+'.f[63]'])
mc.polyExtrudeFacet(lsx=0.7,lsy=0.9)
mc.polyExtrudeFacet(ltz=-0.1,lsx=0.6,lsy=0.8)
mc.polyAutoProjection(manang+'.f[*]',ps=0.1)
mc.parent(manang,hokhoi[-1])

# เสาเสียบตรงกลาง
saoklangsung = 15.86
saoklang = []
for i in range(3):
    saoklang.append(mc.polyCylinder(h=saoklangsung,r=0.4,sx=16)[0])
    mc.hyperShade(a=phiu_sao)
    ppj = mc.polyProjection(saoklang[-1]+'.f[*]',t='cylindrical')[0]
    for a,v in zip(['pcx','pcy','pcz','phs','ph','ra'],[0,0,0,360,2,35]):
        mc.setAttr('%s.%s'%(ppj,a),v)
    mc.move((i-1)*22,thansung+saoklangsung/2.,0,saoklang[-1])
    mc.polyExtrudeFacet(saoklang[-1]+'.f[17]',off=0.04,ltz=0.04)
    mc.delete(saoklang[-1]+'.f[16]')



# ฐานด้านล่าง
thanlang = mc.polyCube(w=77,h=0.2,d=33)[0]
mc.hyperShade(a=phiu_than)
lueak = [] # เลือกขอบส่วนมุม
for i in range(mc.polyEvaluate(e=1)):
    s = thanlang+'.e[%d]'%i
    bb = mc.xform(s,q=1,bb=1,ws=1)
    if(bb[0]*bb[3]>0 and bb[2]*bb[5]>0):
        lueak.append(s)
mc.select(lueak)
mc.polyBevel(o=5) # หักส่วนมุม
mc.select(thanlang+'.f[4]')
for i in range(9):
    mc.polyExtrudeFacet(off=0.3)
    mc.polyExtrudeFacet(ltz=0.2)
mc.polyExtrudeFacet(off=0.1)
mc.polyExtrudeFacet(off=0.02,ltz=-0.02)
mc.polyExtrudeFacet(off=0.2)
mc.polyExtrudeFacet(off=0.02,ltz=0.02)
mc.hyperShade(a=phiu_thanit)
w = 3
mc.polyProjection(thanlang+'.f[*]',pcx=0,pcy=0,pcz=0,rx=90,ry=0,rz=0,psu=w,psv=w)



# ฐานส่วนบน
thanbon = [mc.polyCube(w=20*3+2*2,h=2.0,d=20)[0]]
mc.move(0,2+1.,0)
for i in [-1,1]:
    for j in [-1,1]:
        thanbon.append(mc.polyCube(w=2,h=4,d=12)[0])
        mc.move(11*i,3,10*j)
thanbon = mc.polyCBoolOp(thanbon,op=2,ch=0)[0]
mc.hyperShade(a=phiu_than)

lueak = []
for i in range(mc.polyEvaluate(f=1)):
    s = thanbon+'.f[%d]'%i
    bb = mc.xform(s,q=1,bb=1,ws=1)
    if(bb[4]>2 and bb[1]<3):
        lueak.append(s)
    elif(bb[1]>2):
        phuenbon = s
    else:
        phuenlang = s
mc.select(lueak)
for i in range(5):
    mc.polyExtrudeFacet(sy=0.7)
    mc.polyExtrudeFacet(ltz=-0.04*(1+i/2.5))
mc.select(phuenbon)
mc.polyExtrudeFacet(off=0.1)
mc.polyExtrudeFacet(ltz=-0.05)
mc.hyperShade(a=phiu_thanit)
mc.delete(phuenlang)

# บันไดรอบฐานด้านบน
bandaibon = []
for i in [1,0,-1]:
    for j in [1,0,-1]:
        if(i==0|j==0):
            continue
        if(bandaibon==[]):
            bandaibon.append(mc.polyPrism(ns=6,w=4,l=0.2,sc=1)[0])
            mc.hyperShade(a=phiu_than)
            mc.select('.f[12:17]')
            for k in range(8):
                mc.polyExtrudeFacet(off=0.3)
                mc.polyExtrudeFacet(ltz=0.2)
            lop = []
            for k in range(mc.polyEvaluate(f=1)):
                s = bandaibon[-1]+'.f[%d]'%k
                bb = mc.xform(s,q=1,bb=1)
                if(bb[5]<0.01 or bb[4]<0.01):
                    lop.append(s)
            mc.delete(lop)
        else:
            bandaibon.append(mc.duplicate(bandaibon[0])[0])
        mc.select(bandaibon[-1])
        if(j!=0):
            mc.move(22*i,2+0.1,9.7*j)
        else:
            mc.move((22+9.7)*i,2+0.1,0)
        if(j==-1):
            mc.rotate(180,y=1)
        elif(j==0):
            mc.rotate(180-i*90,y=1)

bandaibon = mc.polyUnite(bandaibon,ch=0)[0]
mc.polyProjection([b+'.f[*]' for b in [thanbon,bandaibon]],pcx=0,pcy=0,pcz=0,rx=90,ry=0,rz=0,psu=w,psv=w)

# ใส่ uv ให้ด้านข้าง
for i in range(6):
    lueak = []
    for j in range(mc.polyEvaluate(bandaibon,f=1)):
        s = bandaibon+'.f[%d]'%j
        bb = mc.xform(s,q=1,bb=1,ws=1)
        if(bb[5]-bb[2]<0.001):
            lueak.append(s)
    mc.rotate(60,bandaibon,y=1,r=1)
    mc.polyProjection(lueak,pcx=0,pcy=0,pcz=0,rx=0,ry=90,rz=0,psu=w,psv=w)

# ฐานแปดเหลี่ยมรอบหอ
thanho = [mc.polyPrism(ns=8,w=15./(1+2**0.5)+0.1,l=0.1)[0]]
mc.hyperShade(a=phiu_than)
mc.rotate(45/2.,y=1)
mc.move(thansung-0.05+0.1/2,y=1)
nf0 = mc.polyEvaluate(thanho,f=1)
mc.select('.f[9]')
mc.polyExtrudeFacet(off=0.1)
nf1 = mc.polyEvaluate(thanho,f=1)
mc.polyExtrudeFacet(ltz=-0.05)
mc.hyperShade(a=phiu_thanit)
mc.polyProjection([thanho[0]+'.f[9]',thanho[0]+'.f[%d:%d]'%(nf0,nf1-1)],pcx=0,pcy=0,pcz=0,rx=90,ry=0,rz=0,psu=w,psv=w)
for i in [-1,1]:
    thanho.append(mc.duplicate(thanho[0])[0])
    mc.move(22*i,0,0,thanho[-1],r=1)

than = mc.polyUnite(thanlang,thanbon,thanho)[0] # รวมส่วนฐานทั้งหมดเข้าด้วยกัน

# ใส่ uv ให้ด้านข้าง
for i in range(8):
    lueak = []
    for j in range(mc.polyEvaluate(than,f=1)):
        s = than+'.f[%d]'%j
        bb = mc.xform(s,q=1,bb=1,ws=1)
        if(bb[5]-bb[2]<0.001):
            lueak.append(s)
    mc.rotate(45,than,y=1,r=1)
    mc.polyProjection(lueak,rx=0,ry=90,rz=0,psu=w,psv=w)

than = mc.polyUnite(than,bandaibon,saoklang,ch=0,n='than')[0] # รวมส่วนฐานและเสาและบันได
klum = mc.group(hokhoi,than)



# ใส่กระดูกและมอร์ฟ สำหรับ mmd
klum_hokhoi = [than]+hokhoi+[manang]
mc.parent(manang,klum)
mc.ungroup(klum)
nahokhoi = [0] # นับจำนวนหน้าของแต่ละส่วนก่อนรวม
tamnaeng = []
for hk in klum_hokhoi:
    nahokhoi.append(nahokhoi[-1]+mc.polyEvaluate(hk,v=1))
    tamnaeng.append(mc.xform(hk,q=1,t=1))
hokhoi = mc.polyUnite(klum_hokhoi,ch=0,n='hokhoi')[0]

# สร้างเบลนด์เชปให้ขยายขนาดได้
khayai = mc.duplicate(hokhoi,n='khayai')[0]
mc.scale(200,200,200,khayai+'.vtx[*]',p=[0,0,0])
mc.select(khayai,hokhoi)
bs = mc.blendShape(n='hokhoi_bs')[0]
mc.delete(khayai)
mc.addAttr(bs,ln='namae',nn=u'名前',dt='string')
mc.setAttr(bs+'.namae',u'%s๑巨大化๑1'%khayai,typ='string')

# ใส่กระดูก
chue_kraduk = [u'基礎',u'一階',u'二階',u'三階',u'四階',u'五階',u'椅子']
kho = []
for i,c in enumerate(chue_kraduk):
    mc.select(cl=1)
    kho.append(mc.joint(p=tamnaeng[i]))
    mc.addAttr(kho[-1],ln='namae',nn=u'名前',dt='string')
    mc.setAttr(kho[-1]+'.namae',c,typ='string')
sk = mc.skinCluster(kho,hokhoi)[0]
for i in range(len(kho)):
    mc.skinPercent(sk,hokhoi+'.vtx[%d:%d]'%(nahokhoi[i],nahokhoi[i+1]-1),tv=(kho[i],1))
mc.parent(kho[6],kho[5])