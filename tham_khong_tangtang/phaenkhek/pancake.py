# -*- coding: utf-8 -*-
import maya.cmds as mc
import math,os,random
random.seed(0)



path = '' # โฟลเดอร์ที่เก็บไฟล์เท็กซ์เจอร์
laisenkwai = mc.shadingNode('file',at=1)
mc.setAttr(laisenkwai+'.ftn',os.path.join(path,'langtao.png'),typ='string') # กระดองเต่า
lainatao = mc.shadingNode('file',at=1)
mc.setAttr(lainatao+'.ftn',os.path.join(path,'natao.png'),typ='string') # หัวเต่า

wao = mc.shadingNode('bump3d',au=1) # ตะปุ่มตะป่ำบนผิวแพนเค้ก
lai = mc.shadingNode('solidFractal',at=1)
lis_at = ['threshold','amplitude','ratio','frequencyRatio','ripplesX','ripplesY','ripplesZ','depthMin']
lis_v = [0.5,0.5,1,2,10,10,10,8]
#lis_v = [0.01,0.02,1,2,1,1,1,8]
for at,v in zip(lis_at,lis_v):
    mc.setAttr(lai+'.'+at,v)
#mc.setAttr(wao+'.bd',0.1)
mc.connectAttr(lai+'.oa',wao+'.bv')

# ผิวหลังเต่า
phiu_bon = mc.shadingNode('blinn',asShader=1,n='phiu_bon') # ผิวเนื้อส่วนหลังตัวล่าง
mc.setAttr(phiu_bon+'.ambc',0.5,0.5,0.5,typ='double3')
mc.setAttr(phiu_bon+'.sc',0.3,0.3,0.3,typ='double3')
mc.setAttr(phiu_bon+'.sro',0.5)
phiu_bon2 = mc.duplicate(phiu_bon,n='phiu_bon2')[0] # ผิวเนื้อส่วนหลังตัวบน
mc.connectAttr(wao+'.o',phiu_bon+'.n')
mc.connectAttr(wao+'.o',phiu_bon2+'.n')
lai_bon = mc.shadingNode('brownian',at=1)

mc.setAttr(laisenkwai+'.colorGain',1.5,1.5,1.5,typ='double3')
mc.setAttr(lainatao+'.colorGain',1.5,1.5,1.5,typ='double3')
mc.setAttr(lai_bon+'.colorGain',0.649,0.408,0.148,typ='double3')
mc.setAttr(lai_bon+'.colorOffset',0.54,0.24,0.094,typ='double3')
ple = mc.shadingNode('place3dTexture',au=1)
mc.defaultNavigation(ce=1,s=ple,d=lai_bon)

# ผิวส่วนเนื้อตรงกลาง
phiu_klang = mc.duplicate(phiu_bon,n='phiu_klang')[0] # ผิวเนื้อตรงกลางตัวล่าง
phiu_klang2 = mc.duplicate(phiu_klang,n='phiu_klang2')[0] # ผิวเนื้อตรงกลางตัวบน
phiu_thuktat = mc.duplicate(phiu_klang2,n='phiu_thuktat')[0] # ผิวที่ถูกตัด
mc.connectAttr(wao+'.o',phiu_klang+'.n')
mc.connectAttr(wao+'.o',phiu_klang2+'.n')
mc.connectAttr(wao+'.o',phiu_thuktat+'.n')
lai_klang = mc.shadingNode('brownian',at=1)
mc.setAttr(lai_klang+'.colorGain',0.45,0.41,0.14,typ='double3')
mc.setAttr(lai_klang+'.colorOffset',1,0.895,0.53,typ='double3')
ple = mc.shadingNode('place3dTexture',au=1)
mc.defaultNavigation(ce=1,s=ple,d=lai_klang)

# บวกลายหลังบนหลังเต่า
buaklop = [mc.shadingNode('plusMinusAverage',au=1,n='buaklop')]
mc.connectAttr(lai_bon+'.oc',buaklop[0]+'.input3D[0]')
mc.connectAttr(laisenkwai+'.oc',buaklop[0]+'.input3D[1]')
mc.connectAttr(buaklop[0]+'.output3D',phiu_bon+'.c')
mc.connectAttr(buaklop[0]+'.output3D',phiu_bon2+'.c')

# บวกลายใบหน้าเต่า
buaklop += [mc.shadingNode('plusMinusAverage',au=1,n='buaklop')]
mc.connectAttr(lai_klang+'.oc',buaklop[1]+'.input3D[0]')
mc.connectAttr(lainatao+'.oc',buaklop[1]+'.input3D[1]')
mc.connectAttr(buaklop[1]+'.output3D',phiu_klang+'.c')
mc.connectAttr(buaklop[1]+'.output3D',phiu_klang2+'.c')
mc.connectAttr(lai_klang+'.oc',phiu_thuktat+'.c')

for i in [0,1]:
    mc.setAttr(buaklop[i]+'.operation',2)

# ผิวเนย
phiu_noei = mc.duplicate(phiu_bon,n='phiu_noei')[0]
mc.setAttr(phiu_noei+'.c',1,0.85,0.47,typ='double3')
wao_noei = mc.shadingNode('bump3d',au=1)
lai_noei = mc.shadingNode('brownian',at=1)
mc.connectAttr(lai_noei+'.oa',wao_noei+'.bv')
ple = mc.shadingNode('place3dTexture',au=1)
mc.defaultNavigation(ce=1,s=ple,d=lai_noei)
mc.connectAttr(wao_noei+'.o',phiu_noei+'.n')

# ผิวจาน
phiu_chan = mc.duplicate(phiu_bon,n='phiu_chan')[0]
mc.setAttr(phiu_bon+'.sc',0.8,0.8,0.8,typ='double3')
lai_chan = mc.shadingNode('marble',at=1)
mc.setAttr('.fillerColor',1,0.98,0.98,typ='double3')
mc.setAttr('.veinColor',1,0.523,0.523,typ='double3')
mc.connectAttr(lai_chan+'.oc',phiu_chan+'.c')
ple = mc.shadingNode('place3dTexture',au=1)
mc.defaultNavigation(ce=1,s=ple,d=lai_chan)

# ผิวส้อม
phiu_som = mc.duplicate(phiu_bon,n='phiu_som')[0]
mc.setAttr(phiu_som+'.c',0.4,0.4,0.4,typ='double3')
mc.setAttr(phiu_som+'.sc',1,1,1,typ='double3')



# สร้างส่วนตัวเต่า
for t in [0,1]:
    lamtua = mc.polySphere(r=8,sx=36,sy=9)[0] # โครงหลักเริ่มจากทรงกลม
    
    for i in range(mc.polyEvaluate(v=1)):
        s = lamtua+'.vtx[%d]'%i
        tt = mc.xform(s,t=1,q=1)
        rr = math.sqrt(tt[0]**2+tt[2]**2)
        if(abs(tt[1])>6): # ยุบส่วนบนล่างให้แบนลง
            mc.scale(1,(1.8+(abs(tt[1])-6.1)**0.5*0.2)/abs(tt[1]),1,s)
        else:
            mc.scale((8-(8-rr)/4)/rr,1./2.5,(8-(8-rr)/4)/rr,s)
            mum = math.degrees(math.atan2(tt[2],tt[0]))
    
    bon = [] # หน้าส่วนบน
    lang = [] # หน้าส่วนล่าง
    klang = [] # หน้าส่วนกลาง
    for i in range(mc.polyEvaluate(f=1)):
        s = lamtua+'.f[%d]'%i
        bb = mc.xform(s,bb=1,q=1)
        if(bb[1]<1 and bb[4]>-1):
            klang.append(s)
        elif(bb[4]>0):
            bon.append(s)
        else:
            lang.append(s)
    
    # ใส่ uv ให้แต่ละส่วนแยกกัน
    mc.polyProjection(bon,pcx=0,pcy=0,pcz=0,rx=-90,ry=0,rz=0,psu=16,psv=16) # ส่วนบน
    mc.polyEditUV(su=0.5,pu=0)
    mc.polyProjection(lang,pcx=0,pcy=0,pcz=0,rx=-90,ry=0,rz=0,psu=16,psv=16) # ส่วนล่าง
    mc.polyEditUV(su=0.5,pu=1)
    ppj = mc.polyProjection(klang,t='cylindrical')[0] # ส่วนกลาง
    for at,v in zip(['pcx','pcy','pcz','phs','ph','rx','ry','rz'],[0,10,0,360,30,0,0,0]):
        mc.setAttr(ppj+'.'+at,v)
        
    # ทำให้รูปร่างไม่เรียบโดยสุ่มปรับเลื่อนจุด
    for i in range(mc.polyEvaluate(v=1)):
        s = lamtua+'.vtx[%d]'%i
        tt = mc.xform(s,t=1,q=1)
        rr = math.sqrt(tt[0]**2+tt[2]**2)
        if(rr>0.001):
            sxz = random.uniform(0.96,1.04)
            mc.scale(sxz,random.uniform(0.96,1.),sxz,s)
    mc.polySoftEdge(lamtua,a=180)
    
    
    
    # ส่วนหัว
    hua = mc.polySphere(r=1.5,sx=18,sy=12)[0]
    lop = []
    for i in range(mc.polyEvaluate(f=1)):
        s = hua+'.f[%d]'%i
        bb = mc.xform(s,bb=1,q=1)
        if(bb[1]<-0.5):
            lop.append(s)
    mc.delete(lop)
    
    ppj = mc.polyProjection(hua+'.f[*]',t='spherical')[0]
    for at,v in zip(['pcx','pcy','pcz','phs','pvs','rx','ry','rz'],[0,-1,0,140,140,-90,90,0]):
        mc.setAttr(ppj+'.'+at,v)
    mc.polyEditUV(su=1./3,sv=1./3,pu=0.5,pv=0.5)
    
    mc.select(hua)
    for i in range(mc.polyEvaluate(hua,v=1)):
        s = hua+'.vtx[%d]'%i
        tt = mc.xform(s,t=1,q=1)
        rr = math.sqrt(tt[0]**2+tt[2]**2)
        mc.scale(random.uniform(0.9,1.),random.uniform(0.9,1.),random.uniform(0.9,1.),s)
    
    mc.rotate(-90,z=1)
    mc.scale(1,2,1.5)
    mc.move(8)
    mc.polySoftEdge(hua,a=180)
    
    
    
    # ส่วนขา
    for i in [0,1,3,4]:
        if(i==0):
            kha = [mc.polySphere(r=1.2,sx=18,sy=12,ax=[1,0,0])[0]]
            lop = []
            for i in range(mc.polyEvaluate(f=1)):
                s = kha[0]+'.f[%d]'%i
                bb = mc.xform(s,bb=1,q=1)
                if(bb[0]<-0.5):
                    lop.append(s)
            mc.delete(lop)
            ppj = mc.polyProjection(kha[0]+'.f[*]',t='spherical')[0]
            lis_at = ['pcx','pcy','pcz','phs','pvs','rx','ry','rz']
            lis_v = [-0.8,0,0,140,140,0,90,0]
            for at,v in zip(lis_at,lis_v):
                mc.setAttr(ppj+'.'+at,v)
            
            mc.polySoftEdge(kha[0],a=180)
            mc.select(kha[0])
            for i in range(mc.polyEvaluate(v=1)):
                s = kha[0]+'.vtx[%d]'%i
                tt = mc.xform(s,t=1,q=1)
                mc.move(-tt[0]*0.8,s,y=1,r=1)
                mc.scale(1,1,1+abs(tt[0])*0.1,s)
            mc.select(kha[0])
            mc.move(8)
            mc.scale(2,1,1.2)
            mc.rotate(60,y=1,r=1,p=[0,0,0])
        else:
            kha.append(mc.duplicate(kha[0])[0])
            for j in range(mc.polyEvaluate(kha[-1],v=1)):
                s = kha[-1]+'.vtx[%d]'%j
                tt = mc.xform(s,t=1,q=1)
                rr = math.sqrt(tt[0]**2+tt[2]**2)
                mc.scale(random.uniform(0.88,1.),random.uniform(0.88,1.),random.uniform(0.88,1.),s)
            mc.polySoftEdge(kha[-1],a=180)
            mc.select(kha[-1])
            mc.rotate(60*i,y=1,r=1,p=[0,0,0])
        
    mc.polyEditUV(kha[0]+'.map[*]',su=1./3,sv=1./3,pu=0,pv=1)
    mc.polyEditUV(kha[1]+'.map[*]',su=1./3,sv=1./3,pu=0,pv=0.5)
    mc.polyEditUV(kha[2]+'.map[*]',su=1./3,sv=1./3,pu=1,pv=1)
    mc.polyEditUV(kha[3]+'.map[*]',su=1./3,sv=1./3,pu=1,pv=0.5)
            
            
    
    # ส่วนหาง
    hang = mc.polySphere(r=1.4,sx=18,sy=12)[0]
    lop = []
    for i in range(mc.polyEvaluate(f=1)):
        s = hang+'.f[%d]'%i
        bb = mc.xform(s,bb=1,q=1)
        if(bb[1]<-0.5):
            lop.append(s)
    mc.delete(lop)
    
    ppj = mc.polyProjection(hang+'.f[*]',t='spherical')[0]
    for at,v in zip(['pcx','pcy','pcz','phs','pvs','rx'],[0,-14/15,0,140,140,-90]):
        mc.setAttr(ppj+'.'+at,v)
    mc.polyEditUV(su=1./3,sv=1./3,pu=0.5,pv=1)
    
    mc.select(hang)
    for i in range(mc.polyEvaluate(hang,v=1)):
        s = hang+'.vtx[%d]'%i
        tt = mc.xform(s,t=1,q=1)
        rr = math.sqrt(tt[0]**2+tt[2]**2)
        mc.scale(random.uniform(0.88,1.),random.uniform(0.88,1.),random.uniform(0.88,1.),s)
    
    mc.rotate(90,z=1)
    mc.scale(1,2,1.2)
    mc.move(-8)
    mc.polySoftEdge(hang,a=180)
    
    mc.select(lamtua)
    mc.hyperShade(a=[phiu_bon,phiu_bon2][t])
    mc.select(klang,hua,kha,hang)
    mc.hyperShade(a=[phiu_klang,phiu_klang2][t])
    tao = mc.polyUnite(lamtua,hua,kha,hang,n='tao1',ch=0)[0]
    
    # สำหรับเต่าตัวล่าง สร้างเบลนด์เชป
    if(t==0):
        thukkot = mc.duplicate(tao,n='thukkot')[0]
        mc.select(thukkot)
        lat = mc.lattice(dv=[5,3,5],oc=1,ldv=[4,4,4])[1]
        mc.move(-8,lat+'.pt[2][2][2]',y=1,r=1)
        mc.move(1,lat+'.pt[1:3][0:1][0]',lat+'.pt[1:3][0:1][4]',y=1,r=1)
        mc.move(0.5,lat+'.pt[0][0:1][2]',lat+'.pt[4][0:1][2]',y=1,r=1)
        mc.move(-3,lat+'.pt[1:3][0][1:3]',y=1,r=1)
        mc.move(15.,lat+'.pt[2][0][2]',y=1,r=1)
        
        mc.select(thukkot,tao)
        bs = mc.blendShape(n='tao_bs')[0]
        mc.delete(thukkot)
        mc.addAttr(bs,ln='namae',nn=u'名前',dt='string')
        mc.setAttr(bs+'.namae',u'%s๑押される๑1'%thukkot,typ='string')

        tao1 = tao
    # สำหรับเต่าตัวบน สร้างรอยตัด
    else:
        tat = mc.polyCylinder(r=2.5,h=4.5,sx=18,sy=4)[0] # ทรงกระบอกที่ใช้เป็นเค้าโครงรอยตัด
        mc.hyperShade(a=phiu_thuktat)
        ppj = mc.polyProjection(tat+'.f[*]',t='cylindrical')[0]
        for at,v in zip(['pcx','pcy','pcz','phs','ph','rx','ry','rz'],[0,0,0,180,4.5,0,-90,0]):
            mc.setAttr(ppj+'.'+at,v)
        mc.delete(tat,ch=1)
        mc.select(tat)
        for i in range(mc.polyEvaluate(v=1)):
            s = tat+'.vtx[%d]'%i
            tt = mc.xform(s,t=1,q=1)
            if(tt[0]>0):
                mc.scale(2,1,2,s)
            else:
                sxz = random.uniform(0.9,1)
                mc.scale(sxz,1,sxz,s)
                
        mc.move(8.2)
        kat2 = mc.duplicate(tat)[0]
        mc.polyNormal(kat2)
        chinhua = mc.duplicate(tao)[0]
        
        tao2 = mc.polyCBoolOp(tao,tat,op=2,n='tao2')[0] # ส่วนที่เหลือ
        chinhua2 = mc.polyCBoolOp(chinhua,kat2,op=2,n='chinhua2')[0] # ส่วนหัวที่ถูกตัด
        mc.rotate(180,-90,0)
        mc.move(0,18.5,0.5) # ย้ายไปไว้ปลายส้อม
        mc.move(-8.2,chinhua2+'.f[*]',x=1,r=1)
        mc.select(tao2)
    mc.move(2.2+3.6*t,y=1,r=1)



# เนยที่กองอยู่ด้านบน
noei = mc.polySphere(r=1.5,sx=18,sy=10,n='noei')[0]
for i in range(mc.polyEvaluate(v=1)):
    s = noei+'.vtx[%d]'%i
    tt = mc.xform(s,t=1,q=1)
    rr = (tt[0]**2+tt[2]**2)**0.5
    if(tt[1]<-0.01):
        mc.move(0,0,0,s)
    elif(rr>0.01):
        sxz = random.uniform(0.5,1)
        mc.scale(sxz*rr/1.5,random.uniform(0.9,1),sxz*rr/1.5,s)
mc.polyMergeVertex(noei,d=0.001)
mc.delete(noei,ch=1)

# สร้างเบลนด์เชปสำหรับกองสูงและแผ่กว้าง
sung,kwang = mc.duplicate(noei,n='kong_sung')+mc.duplicate(noei,n='phae_kwang')
mc.scale(1,5,1,sung+'.vtx[*]',p=[0,0,0])
mc.scale(5,1,5,kwang+'.vtx[*]',p=[0,0,0])
mc.select(sung,kwang,noei)
bs = mc.blendShape(n='noei_bs')[0]
mc.delete(sung,kwang)
mc.addAttr(bs,ln='namae',nn=u'名前',dt='string')
mc.setAttr(bs+'.namae',u'%s๑バター積み上げ๑2๐%s๑バター拡大๑1'%(sung,kwang),typ='string')

mc.select(noei)
mc.move(0,7.5,0)
mc.hyperShade(a=phiu_noei)



# จาน
chan = mc.polyCylinder(r=9,h=0.4,sx=36,n='chan')[0]
mc.move(0,0.2,0)
mc.select(chan+'.f[0:35]') # ส่วนด้านข้าง
mc.polyExtrudeFacet(ltz=2,ty=1)
mc.polyExtrudeFacet(ltz=1.5,ty=0.5)
mc.polyExtrudeFacet(ltz=0.5,ty=0.1)
mc.polySoftEdge(a=180)
mc.select(chan)
mc.hyperShade(a=phiu_chan)
mc.polyAutoProjection(chan+'.f[*]',ps=0.4)
mc.delete(chan,ch=1)



# ส้อม
som = mc.polyCube(w=1.2,h=1,d=0.1,sx=7,n='som')[0]
mc.select(som+'.f[21:27]') # ส่วนล่าง
mc.polyExtrudeFacet(ltz=2,sx=0.9)
mc.polyExtrudeFacet(ltz=3,sx=0.9)
mc.polyExtrudeFacet(ltz=0.3,sx=0.75)
mc.polyExtrudeFacet(ltz=0.2,sx=0.5)
mc.polyExtrudeFacet(ltz=0.1,sx=0.2)

mc.select(som+'.f[7:13]') # ส่วนบน
mc.polyExtrudeFacet(ltz=2,sx=0.8,rx=-5)
mc.polyExtrudeFacet(ltz=1.5,sx=0.8,rx=-5)
mc.polyExtrudeFacet(ltz=1,sx=0.8,rx=-5)
mc.polyExtrudeFacet(ltz=0.5,sx=1.1,rx=-5)
mc.polyExtrudeFacet(ltz=0.5,sx=2.4,rx=-5)
mc.polyExtrudeFacet(ltz=0.5,sx=1.4)
mc.polyExtrudeFacet(ltz=1,sx=1.2,rx=10)
mc.polyExtrudeFacet(ltz=1,sx=1.,rx=10)
# ปลายส้อมที่เริ่มแยกซี่
for i in [7,9,11,13]:
    mc.select(som+'.f[%d]'%i)
    bb = mc.xform(q=1,bb=1)
    xx = (bb[3]+bb[0])/2
    mc.scale(1.5,x=1,p=[xx,0,0])
    mc.polyExtrudeFacet(ltz=1,sx=0.8,rx=8)
    mc.polyExtrudeFacet(ltz=1,sx=0.8,rx=6)
    mc.polyExtrudeFacet(ltz=1,sx=0.5,rx=4)
    mc.polyExtrudeFacet(ltz=1,sx=0.3,rx=2)
mc.select(som)
# รวบจุดยอดที่ไม่จำเป็นเพื่อลดโพลิกอน
vv = ['1:6','9:14','17:22','25:30']
for j in range(33,221,16):
    vv += ['%d:%d'%(j,j+1),'%d:%d'%(j+3,j+12)]
mc.scale(0,[som+'.vtx[%s]'%v for v in vv],x=1)
mc.polyMergeVertex(d=0.0001)
mc.scale(0,[som+'.e[%s]'%e for e in [9,14,19,21,31,33,43,45,55,57]],y=1,p=[0,-2.5,0])
mc.polyMergeVertex(d=0.0001)
mc.polyAutoProjection(som,ps=0.4)
mc.select(som)
mc.move(-mc.xform(bb=1,q=1)[1],som+'.f[*]',y=1,r=1)
mc.hyperShade(a=phiu_som)
mc.delete(som,ch=1)



# ใส่กระดูก สำหรับ mmd
kho = []
for s in [chan,tao1,tao2,noei,som,chinhua2]:
    mc.select(cl=1)
    kho += [mc.joint(p=mc.xform(s,q=1,t=1))]
    mc.skinCluster(kho[-1],s)
mc.parent(kho[5],kho[4])

mc.select(kho[4])
mc.move(0,0,17.784,r=1)
mc.rotate(-49.729)
mc.group(chan,tao1,tao2,noei,som,chinhua2,n='taopancake')