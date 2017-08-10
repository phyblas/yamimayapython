# -*- coding: utf-8 -*-
import maya.cmds as mc

nx = 18 # จำนวนช่อง
nz = 18
w = 2.5 # ความกว้าง
h = 2.4 # ความสูง

phiu_phuen = mc.shadingNode('blinn',asShader=1,n='phiu_phuen')
mc.setAttr(phiu_phuen+'.ambc',0.5,0.5,0.5,typ='double3')
mc.setAttr(phiu_phuen+'.c',0.45,0.52,0.48,typ='double3')
lainun1 = mc.shadingNode('fractal',at=1)
mc.setAttr(lainun1+'.ratio',0.5)
mc.setAttr(lainun1+'.frequencyRatio',100)
ple1 = mc.shadingNode('place2dTexture',au=1)
mc.defaultNavigation(ce=1,s=ple1,d=lainun1)
lainun2 = mc.shadingNode('file',at=1)
mc.setAttr(lainun2+'.ftn','nunphuen4.png',typ='string')
ple2 = mc.shadingNode('place2dTexture',au=1)
mc.defaultNavigation(ce=1,s=ple2,d=lainun2)
lainun = mc.shadingNode('multiplyDivide',au=1,n='lai_phuen')
mc.connectAttr(lainun1+'.oc',lainun+'.input1')
mc.connectAttr(lainun2+'.oc',lainun+'.input2')
nun = mc.shadingNode('bump2d',au=1)
mc.connectAttr(lainun+'.ox',nun+'.bv')
mc.connectAttr(nun+'.o',phiu_phuen+'.n')

phiu_phanang = mc.duplicate(phiu_phuen,n='phiu_phanang')[0]
mc.setAttr(phiu_phanang+'.c',0.93,0.36,0.36,typ='double3')

phiu_than = mc.duplicate(phiu_phanang,n='phiu_than')[0]
mc.setAttr(phiu_than+'.c',0.995,1,0.921,typ='double3')
lainun1 = mc.shadingNode('file',au=1)
mc.setAttr(lainun1+'.ftn','nunthanphanang4.png',typ='string')
ple1 = mc.shadingNode('place2dTexture',au=1)
mc.defaultNavigation(ce=1,s=ple1,d=lainun1)
lainun2 = mc.shadingNode('fractal',au=1)
mc.setAttr(lainun2+'.ratio',0.5)
ple2 = mc.shadingNode('place2dTexture',au=1)
mc.defaultNavigation(ce=1,s=ple2,d=lainun1)
lainun = mc.shadingNode('multiplyDivide',au=1)
mc.connectAttr(lainun1+'.oc',lainun+'.input1')
mc.connectAttr(lainun2+'.oc',lainun+'.input2')
nun = mc.shadingNode('bump2d',au=1)
mc.connectAttr(lainun+'.ox',nun+'.bv')
mc.connectAttr(nun+'.o',phiu_than+'.n')

phiu_bonphanang = mc.duplicate(phiu_phanang,n='phiu_bonphanang')[0]
lai = mc.shadingNode('fractal',au=1)
mc.setAttr(lai+'.colorOffset',0.23,0.62,0.13,typ='double3')
mc.setAttr(lai+'.colorGain',0.15,0.15,0.15,typ='double3')
mc.connectAttr(lai+'.oc',phiu_bonphanang+'.c')
ple = mc.shadingNode('place2dTexture',au=1)
mc.defaultNavigation(ce=1,s=ple,d=lai)
lainun = mc.shadingNode('file',au=1,n='lai_bonphanang')
mc.setAttr(lainun+'.ftn','nunbonphanang4.png',typ='string')
ple = mc.shadingNode('place2dTexture',au=1)
mc.defaultNavigation(ce=1,s=ple,d=lainun)
nun = mc.shadingNode('bump2d',au=1,n='nun')
mc.connectAttr(lainun+'.oa',nun+'.bv')
mc.connectAttr(nun+'.o',phiu_bonphanang+'.n')

phiu_langkha = mc.duplicate(phiu_phanang,n='phiu_langkha')[0]
mc.setAttr(phiu_langkha+'.c',0.8,0.51,0.12,typ='double3')
lainun = mc.shadingNode('file',au=1)
mc.setAttr(lainun+'.ftn','nunlangkha4.png',typ='string')
nun = mc.shadingNode('bump2d',au=1)
mc.connectAttr(lainun+'.oa',nun+'.bv')
mc.connectAttr(nun+'.o',phiu_langkha+'.n')

phiu_tailangkha = mc.duplicate(phiu_phanang,n='phiu_tailangkha')[0]
mc.setAttr(phiu_tailangkha+'.c',0.1,0.066,0.0155,typ='double3')
lainun = mc.shadingNode('file',au=1)
mc.setAttr(lainun+'.ftn','nuntailangkha4.png',typ='string')
nun = mc.shadingNode('bump2d',au=1)
mc.connectAttr(lainun+'.oa',nun+'.bv')
mc.connectAttr(nun+'.o',phiu_tailangkha+'.n')



# ส่วนรอยต่อระหว่างผนัง
for i in range(nx+1):
    for j in range(nz+1):
        if(i==0 and j==0):
            sao = [mc.polyCube(w=0.04,h=h,d=0.04)[0]]
        else:
            sao += mc.duplicate(sao[0])
            if(i>0):
                mc.delete(sao[-1]+'.f[5]')
            if(i<nx):
                mc.delete(sao[-1]+'.f[4]')
            if(j>0):
                mc.delete(sao[-1]+'.f[2]')
            if(j<nz):
                mc.delete(sao[-1]+'.f[0]')
        mc.move(i*w,h/2.,j*w,sao[-1])
mc.delete(sao[0]+'.f[0]',sao[0]+'.f[4]')

# ส่วนผนัง
phanang = []
for i in range(nx+1):
    for j in range(nz):
        if(i==0 and j==0):
            phanang += [mc.polyCube(w=w-0.04,h=h,d=0.04,n='p0')[0]]
            mc.rotate(90,y=1)
        else:
            phanang += mc.duplicate(phanang[0])
        mc.move(i*w,h/2.,(j+0.5)*w,phanang[-1])
for i in range(nx):
    for j in range(nz+1):
        if(i==0 and j==0):
            phanang += [mc.polyCube(w=w-0.04,h=h,d=0.04,n='p0')[0]]
        else:
            phanang += mc.duplicate(phanang[(nx+1)*nz])
        mc.move((i+0.5)*w,h/2.,j*w,phanang[-1])

# ลบส่วนที่เปิดให้เป็นทาง
#lop = [9,10,11,13,14,17,18,20,21,22,23,25,26,27,28,29,30,34,36,37,39,40,42,43,44,45,47,49,52,53,56,57,58,61,63,66,67,71,72,74,76,78,90,91,93,94,96,97,106,107,108,112,114,115,116,125,126,128,132,136,141,142,146,147,151,152,153,155,156,157,158,162,163,165,166,168,171,173,175,177,178,179]
lop = [17,19,20,21,22,28,29,30,33,35,36,39,45,46,47,50,51,52,53,54,55,56,58,61,62,65,66,69,75,77,79,80,84,86,87,89,90,94,98,100,101,104,106,107,108,113,115,116,117,120,121,122,123,125,126,127,130,132,134,136,138,139,140,141,144,148,149,151,155,156,159,160,167,168,171,179,181,182,185,188,191,192,195,196,197,198,202,205,207,212,213,214,217,218,221,226,229,230,231,234,241,242,243,244,245,247,248,251,253,254,261,262,266,268,269,270,274,275,278,279,283,285,286,287,288,289,290,295,297,300,301,302,303,305,306,307,308,310,314,315,319,322,324,342,343,345,347,348,349,350,351,352,355,356,357,358,359,362,366,367,368,369,370,374,382,383,385,386,387,389,391,393,394,397,400,402,404,406,409,410,413,416,419,420,421,422,423,424,427,428,430,431,432,434,438,439,440,442,444,447,449,453,459,460,462,463,467,468,472,473,477,478,479,482,484,485,487,489,492,495,496,497,498,499,501,502,503,504,505,507,508,509,511,514,517,518,520,523,524,526,527,528,529,533,534,535,536,538,539,541,542,544,546,549,552,554,555,557,559,560,562,563,564,568,571,573,574,576,577,579,582,583,586,587,590,592,593,594,595,596,597,601,603,604,605,609,611,612,614,615,616,619,620,621,623,630,631,633,635,637,638,639,644,647,650,651,652,653,654,657,658,661,662,667,668,669,671,672,673,675,676,677,678,679,680,682,683]
chalop = []
for i in range((nx+1)*nz+(nz+1)*nx):
    if(i in lop):
        mc.polyNormal(phanang[i])
        chalop.append(phanang[i]+'.f[0:3]')
    else:
        chalop.append(phanang[i]+'.f[4:5]')
mc.delete(chalop)
wongkot = mc.polyUnite(sao,mc.ls(phanang),ch=0,n='wongkot')[0]
mc.polyMergeVertex(d=0.001,ch=0)

# กำจัดรอยต่อที่ไม่ได้ใช้โดยรวมโพลิกอน
for i in range(nx+1):
    for j in range(nz+1):
        yu = []
        xx = [0,0]
        zz = [0,0]
        for k in range(mc.polyEvaluate(wongkot,f=1)):
            s = wongkot+'.f[%d]'%k
            bb = mc.xform(s,q=1,bb=1,ws=1)
            if(i*w-0.04<bb[0] and bb[3]<i*w+0.04 and j*w-0.04<bb[2] and bb[5]<j*w+0.04):
                yu.append(s)
                if(bb[5]-bb[2]<0.001):
                    if(bb[5]<j*w):
                        xx[0] = s
                    else:
                        xx[1] = s
                if(bb[3]-bb[0]<0.001):
                    if(bb[3]<i*w):
                        zz[0] = s
                    else:
                        zz[1] = s
        if(len(yu)==3):
            if(zz[0]):
                mc.scale(0,zz[0],z=1,p=[i*w,0,j*w])
            elif(zz[1]):
                mc.scale(0,zz[1],z=1,p=[i*w,0,j*w])
            elif(xx[0]):
                mc.scale(0,xx[0],x=1,p=[i*w,0,j*w])
            elif(xx[1]):
                mc.scale(0,xx[1],x=1,p=[i*w,0,j*w])
        if(len(yu)==4):
            if(zz[0]):
                if(zz[1]):
                    mc.scale(0,zz,z=1,p=[i*w,0,j*w])
                elif(xx[0]):
                    mc.scale(0,xx[0],x=1,p=[i*w-0.02,0,j*w-0.02])
                    mc.scale(0,zz[0],z=1,p=[i*w-0.02,0,j*w-0.02])
                else:
                    mc.scale(0,xx[1],x=1,p=[i*w-0.02,0,j*w+0.02])
                    mc.scale(0,zz[0],z=1,p=[i*w-0.02,0,j*w+0.02])
            elif(zz[1]):
                0
                if(xx[0]):
                    mc.scale(0,xx[0],x=1,p=[i*w+0.02,0,j*w-0.02])
                    mc.scale(0,zz[1],z=1,p=[i*w+0.02,0,j*w-0.02])
                else:
                    mc.scale(0,xx[1],x=1,p=[i*w+0.02,0,j*w+0.02])
                    mc.scale(0,zz[1],z=1,p=[i*w+0.02,0,j*w+0.02])
            elif(xx[0]):
                mc.scale(0,xx,x=1,p=[i*w,0,j*w])
        elif(len(yu)==5):
            if(zz[0] and zz[1]):
                if(xx[0]):
                    mc.scale(0,zz,z=1,p=[i*w,0,j*w-0.02])
                else:
                    mc.scale(0,zz,z=1,p=[i*w,0,j*w+0.02])
            else:
                if(zz[0]):
                    mc.scale(0,xx,x=1,p=[i*w-0.02,0,j*w])
                else:
                    mc.scale(0,xx,x=1,p=[i*w+0.02,0,j*w])
        
mc.polyMergeVertex(d=0.001,ch=0)

# สร้างหลังคา
ao = []
for i in range(mc.polyEvaluate(wongkot,f=1)):
    s = wongkot+'.f[%d]'%i
    bb = mc.xform(s,q=1,bb=1,ws=1)
    if(bb[1]>h-0.1):
        ao.append(s)
mc.select(ao)
nf1 = mc.polyEvaluate(wongkot,f=1)
mc.polyExtrudeFacet(ltz=0.04)
nf2 = mc.polyEvaluate(wongkot,f=1)
mc.polyExtrudeFacet(ltz=0.01)
mc.polyExtrudeFacet(ltz=0.02,off=0.005)
mc.polyExtrudeFacet(ltz=0.01,off=0.01)
mc.select(wongkot+'.f[%d:%d]'%(nf1,nf2-1))
mc.polyExtrudeFacet(thickness=0.3)
mc.move(-0.3,y=1,r=1)

# ใส่ผิวให้หลังคา
s1,s2,s3 = [[],[],[]],[[],[],[]],[]
for i in range(mc.polyEvaluate(wongkot,f=1)):
    s = wongkot+'.f[%d]'%i
    bb = mc.xform(s,q=1,bb=1,ws=1)
    if(bb[1]>1):
        if(bb[4]>h+0.0401):
            s3.append(s)
        if(bb[4]>h+0.0399):
            if(bb[5]-bb[2]>bb[3]-bb[0]):
                s1[0].append(s)
            else:
                s2[0].append(s)
        elif(bb[4]<h-0.001):
            if(bb[5]-bb[2]>bb[3]-bb[0]):
                s1[2].append(s)
            else:
                s2[2].append(s)
        else:
            if(bb[5]-bb[2]>bb[3]-bb[0]):
                s1[1].append(s)
            else:
                s2[1].append(s)

mc.select(*s1+s2)
mc.hyperShade(a=phiu_langkha)
mc.select(s1[1],s2[1])
mc.hyperShade(a=phiu_tailangkha)
mc.polyProjection(s1[0],pcx=w/50.,pcy=h+0.04-0.15*8/7,pcz=w/50.,rx=0,ry=90,rz=0,psu=w/25.,psv=0.3*8/7)
mc.polyProjection(s2[0],pcx=w/50.,pcy=h+0.04-0.15*8/7,pcz=0,rx=0,ry=0,rz=0,psu=w/25.,psv=0.3*8/7)
mc.polyProjection(s1[1],pcx=w/50.,pcy=h-0.15,pcz=w/50.,rx=0,ry=90,rz=0,psu=w/25.,psv=0.3/4)
mc.polyProjection(s2[1],pcx=w/50.,pcy=h-0.15,pcz=w/50.,rx=0,ry=0,rz=0,psu=w/25.,psv=0.3/4)
mc.polyProjection(s1[2],pcx=w/50.,pcy=h-0.3+0.02*8,pcz=w/50.,rx=0,ry=90,rz=0,psu=w/25.,psv=0.04*8)
mc.polyProjection(s2[2],pcx=w/50.,pcy=h-0.3+0.02*8,pcz=w/50.,rx=0,ry=0,rz=0,psu=w/25.,psv=0.04*8)
mc.polyProjection(s3,pcy=h+0.08,rx=45,ry=0,rz=90,psu=0.04*512./111,psv=1000000)
mc.polySoftEdge(s3,a=90)

# ค้นหาว่าหน้าไหนเป็นผิวด้านใต้
tai = []
for i in range(nf1):
    s = wongkot+'.f[%d]'%i
    bb = mc.xform(s,q=1,bb=1,ws=1)
    if(bb[4]<0.1):
        tai.append(s)
mc.select(wongkot+'.f[*]')
mc.select(tai,*s1+s2,tgl=1)

# ทำผนังโดยแยกเป็นสามส่วน
nf3 = mc.polyEvaluate(wongkot,f=1)
mc.polyExtrudeFacet(sy=(h-1.)/h)
mc.move(-0.2,y=1,r=1)
nf4 = mc.polyEvaluate(wongkot,f=1)
mc.hyperShade(a=phiu_phanang)
mc.polyProjection(rx=0,pcx=0,pcy=1,pcz=90,ry=0,rz=0,psu=2,psv=h-1)
bon = [[],[]]
lang = [[],[]]
for i in range(nf3,nf4):
    s = wongkot+'.f[%d]'%i
    bb = mc.xform(s,q=1,bb=1,ws=1)
    if(bb[4]<0.4):
        if(bb[5]-bb[2]<0.001):
            lang[0].append(s)
        else:
            lang[1].append(s)
    else:
        if(bb[5]-bb[2]<0.001):
            bon[0].append(s)
        else:
            bon[1].append(s)
            
# ใส่ผิวส่วนด้านบน
mc.select(bon[0],bon[1])
mc.hyperShade(a=phiu_bonphanang)
mc.polyProjection(bon[0],pcx=0.35,pcy=h-0.35,pcz=0.35,rx=0,ry=0,rz=0,psu=0.7,psv=0.7)
mc.polyProjection(bon[1],pcx=0.35,pcy=h-0.35,pcz=0.35,rx=0,ry=90,rz=0,psu=0.7,psv=0.7)
for s in bon[0]:
    bb = mc.xform(s,q=1,bb=1,ws=1)
    if(bb[3]-bb[0]<0.041):
        mc.polyProjection(s,pcx=bb[0]-0.02,pcy=h-0.35,pcz=0.35,rx=0,ry=0,rz=0,psu=0.7,psv=0.7)
for s in bon[1]:
    bb = mc.xform(s,q=1,bb=1,ws=1)
    if(bb[5]-bb[2]<0.041):
        mc.polyProjection(s,pcx=0.35,pcy=h-0.35,pcz=bb[2]-0.02,rx=0,ry=0,rz=0,psu=0.7,psv=0.7)

# ยื่นส่วนด้านล่างออกมาแล้วใส่ผิว
mc.select(lang[0],lang[1])
mc.hyperShade(a=phiu_than)
mc.polyExtrudeFacet(thickness=0.02)
mc.polyProjection(lang[0],pcx=0.15,pcy=0.15,pcz=0.15,rx=0,ry=0,rz=0,psu=0.3,psv=0.3)
mc.polyProjection(lang[1],pcx=0.15,pcy=0.15,pcz=0.15,rx=0,ry=90,rz=0,psu=0.3,psv=0.3)
for s in lang[0]:
    bb = mc.xform(s,q=1,bb=1,ws=1)
    if(bb[3]-bb[0]<0.081):
        mc.polyProjection(s,pcx=bb[0]+0.04,pcy=0.15,pcz=0.15,rx=0,ry=0,rz=0,psu=0.3,psv=0.3)
for s in lang[1]:
    bb = mc.xform(s,q=1,bb=1,ws=1)
    if(bb[5]-bb[2]<0.081):
        mc.polyProjection(s,pcx=0.15,pcy=0.15,pcz=bb[2]+0.04,rx=0,ry=90,rz=0,psu=0.3,psv=0.3)

for i in range(nf4,mc.polyEvaluate(wongkot,f=1)):
    s = wongkot+'.f[%d]'%i
    bb = mc.xform(s,q=1,bb=1,ws=1)
    if(bb[4]<0.1):
        tai.append(s)
mc.delete(tai) # ลบผิวด้านใต้ทิ้งไป
mc.move(-nx/2.*w,0,-nz/2.*w,wongkot)

phuen = mc.polyPlane(w=nx*w*3,h=nz*w*3,sx=1,sy=1,n='phuen')[0]
mc.hyperShade(a=phiu_phuen)
mc.polyProjection(phuen+'.f[*]',pcx=w/4.,pcy=0,pcz=w/4.,rx=90,ry=0,rz=0,psu=w/2.,psv=w/2.)