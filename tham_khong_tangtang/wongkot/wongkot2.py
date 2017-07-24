# -*- coding: utf-8 -*-
import maya.cmds as mc

nx = 18 # จำนวนช่อง
nz = 18
w = 2 # ความกว้าง

phiu_phuen = mc.shadingNode('blinn',asShader=1,n='phiu_phuen')
mc.setAttr(phiu_phuen+'.ambc',0.5,0.5,0.5,typ='double3')
lai1 = mc.shadingNode('fractal',at=1)
mc.setAttr(lai1+'.ratio',0.5)
ple1 = mc.shadingNode('place2dTexture',au=1)
mc.defaultNavigation(ce=1,s=ple1,d=lai1)
lai2 = mc.shadingNode('file',at=1)
mc.setAttr(lai2+'.ftn','nunphuen2.jpg',typ='string')
ple2 = mc.shadingNode('place2dTexture',au=1)
mc.defaultNavigation(ce=1,s=ple2,d=lai2)
lai = mc.shadingNode('multiplyDivide',au=1,n='lai_phuen')
mc.connectAttr(lai1+'.oc',lai+'.input1')
mc.connectAttr(lai2+'.oc',lai+'.input2')
nun = mc.shadingNode('bump2d',au=1,n='nun')
mc.connectAttr(lai+'.ox',nun+'.bv')
mc.connectAttr(nun+'.o',phiu_phuen+'.n')

phiu_phanang = mc.duplicate(phiu_phuen,n='phiu_phanang')[0]
lailai = mc.shadingNode('file',at=1,n='lai_phanang')
mc.connectAttr(lailai+'.oc',phiu_phanang+'.c')
mc.setAttr(lailai+'.ftn','laiphanang2.png',typ='string')
ple = mc.shadingNode('place2dTexture',au=1)
mc.defaultNavigation(ce=1,s=ple,d=lailai)
lai1 = mc.shadingNode('fractal',at=1)
mc.setAttr(lai1+'.ratio',0.5)
ple1 = mc.shadingNode('place2dTexture',au=1)
mc.defaultNavigation(ce=1,s=ple1,d=lai1)
lai2 = mc.shadingNode('file',at=1)
mc.setAttr(lai2+'.ftn','nunphanang2.jpg',typ='string')
ple2 = mc.shadingNode('place2dTexture',au=1)
mc.defaultNavigation(ce=1,s=ple2,d=lai2)
lai = mc.shadingNode('multiplyDivide',au=1,n='lai_phuen')
mc.connectAttr(lai1+'.oc',lai+'.input1')
mc.connectAttr(lai2+'.oc',lai+'.input2')
nun = mc.shadingNode('bump2d',au=1,n='nun')
mc.connectAttr(lai+'.ox',nun+'.bv')
mc.connectAttr(nun+'.o',phiu_phanang+'.n')

phanang = []
for i in range(nx+1):
    for j in range(nz):
        if(i==0 and j==0):
            phanang += [mc.polyPlane(w=w,h=2,sx=1,sy=1,ax=[1,0,0],n='p0')[0]]
            mc.polyProjection(phanang[-1]+'.f[*]',rx=0,ry=90,rz=0,psu=w/2.,psv=w/2.)
        else:
            phanang += mc.duplicate(phanang[0])
        mc.move(i*w,1,(j+0.5)*w,phanang[-1])
for i in range(nx):
    for j in range(nz+1):
        if(i==0 and j==0):
            phanang += [mc.polyPlane(w=w,h=2,sx=1,sy=1,ax=[0,0,1],n='phanang1')[0]]
            mc.polyProjection(phanang[-1]+'.f[*]',rx=0,ry=0,rz=0,psu=w/2.,psv=w/2.)
        else:
            phanang += mc.duplicate(phanang[(nx+1)*nz])
        mc.move((i+0.5)*w,1,j*w,phanang[-1])

# ลบส่วนที่เปิดให้เป็นทาง
mc.delete([phanang[i] for i in 17,19,20,21,22,28,29,30,33,35,36,39,45,46,47,50,51,52,53,54,55,56,58,61,62,65,66,69,75,77,79,80,84,86,87,89,90,94,98,100,101,104,106,107,108,113,115,116,117,120,121,122,123,125,126,127,130,132,134,136,138,139,140,141,144,148,149,151,155,156,159,160,167,168,171,179,181,182,185,188,191,192,195,196,197,198,202,205,207,212,213,214,217,218,221,226,229,230,231,234,241,242,243,244,245,247,248,251,253,254,261,262,266,268,269,270,274,275,278,279,283,285,286,287,288,289,290,295,297,300,301,302,303,305,306,307,308,310,314,315,319,322,324,342,343,345,347,348,349,350,351,352,355,356,357,358,359,362,366,367,368,369,370,374,382,383,385,386,387,389,391,393,394,397,400,402,404,406,409,410,413,416,419,420,421,422,423,424,427,428,430,431,432,434,438,439,440,442,444,447,449,453,459,460,462,463,467,468,472,473,477,478,479,482,484,485,487,489,492,495,496,497,498,499,501,502,503,504,505,507,508,509,511,514,517,518,520,523,524,526,527,528,529,533,534,535,536,538,539,541,542,544,546,549,552,554,555,557,559,560,562,563,564,568,571,573,574,576,577,579,582,583,586,587,590,592,593,594,595,596,597,601,603,604,605,609,611,612,614,615,616,619,620,621,623,630,631,633,635,637,638,639,644,647,650,651,652,653,654,657,658,661,662,667,668,669,671,672,673,675,676,677,678,679,680,682,683])
phanang = mc.polyUnite(mc.ls(phanang),ch=0,n='phanang')
mc.move(-nx/2.*w,0,-nz/2.*w)
mc.select(phanang)
mc.hyperShade(a=phiu_phanang)
mc.polyMergeVertex(phanang,d=0.01)
yup = mc.duplicate(phanang,n='yup')[0]
mc.scale(0,yup+'.vtx[*]',y=1,p=[0,0,0])
mc.blendShape(yup,phanang)
mc.delete(yup)

phuen = mc.polyPlane(w=nx*w,h=nz*w,n='phuen')[0]
mc.hyperShade(a=phiu_phuen)
mc.polyProjection(phuen+'.f[*]',pcx=w/4.,pcy=0,pcz=w/4.,rx=90,ry=0,rz=0,psu=w/2.,psv=w/2.)
yok = mc.duplicate(phuen,n='yok')[0]
mc.move(2,yok+'.vtx[*]',y=1)
mc.blendShape(yok,phuen)
mc.delete(yok)