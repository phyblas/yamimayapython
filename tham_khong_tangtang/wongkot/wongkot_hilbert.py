# -*- coding: utf-8 -*-
import maya.cmds as mc
import os
file_thangsairung = os.path.join(os.path.expanduser('~'),'sithangsairung.png') # ไฟล์สีพื้น

# ฟังก์ชันสร้างเส้นโค้งฮิลแบร์ท
def hilbert(n):
    def h(i):
        if(i==0):
            return [-2]
        else:
            a = []
            for x in h(i-1):
                if(x==-2):
                    a.extend([-1,2,0,1,-2,0,-2,1,0,2,-1])
                elif(x==2):
                    a.extend([1,-2,0,-1,2,0,2,-1,0,-2,1])
                else:
                    a.extend([x])
            return a
    
    def t(xx):
        a = [(1,1)]
        b = 1
        for x in xx:
            if(x==0):
                a.append((a[-1][0]+(b==0)-(b==2),a[-1][1]+(b==1)-(b==3)))
                a.append((a[-1][0]+(b==0)-(b==2),a[-1][1]+(b==1)-(b==3)))
            elif(x==-1 or x==1):
                if(x==1):
                    b += 1
                else:
                    b -= 1
                b %= 4
        return a
    
    return t(h(n))

import numpy as np
import matplotlib.pyplot as plt
n = 3
xy = [(1,0)]+hilbert(n)+[(1,2**(n+1))]
xy = np.array([(1,0)]+hilbert(n)+[(1,2**(n+1))])
# สร้างไฟล์ภาพพื้นสีสายรุ้ง
plt.figure(figsize=[6,6],facecolor='k')
plt.axes([0,0,1,1],aspect=1,xlim=[-0.5,2**(n+1)+0.5],ylim=[-0.5,2**(n+1)+0.5])
c = plt.get_cmap('rainbow')(np.linspace(0,1,len(xy)-1))
for i in range(len(xy)-1):
    plt.plot(xy[i:i+2,0],xy[i:i+2,1],color=c[i],lw=35)
plt.axis('off')
plt.savefig(file_thangsairung,dpi=512/6.,facecolor='k')
plt.close()

# สีผิวหลังคา
phiu_dam = mc.shadingNode('blinn',asShader=1,n='phiu_dam')
mc.setAttr(phiu_dam+'.c',0.05,0.05,0.05,typ='double3')
mc.setAttr(phiu_dam+'.ambc',0.5,0.5,0.5,typ='double3')
mc.setAttr(phiu_dam+'.sc',0.9,0.9,0.9,typ='double3')
mc.setAttr(phiu_dam+'.sro',0.3)
phiu = [phiu_dam]

# สีผิวผนัง
phiu_phanang = mc.duplicate(phiu_dam,n='phiu_phanang')[0]
mc.setAttr(phiu_phanang+'.sc',0.6,0.6,0.6,typ='double3')
mc.setAttr(phiu_phanang+'.c',1,1,1,typ='double3')

# สีผิวพื้น
phiu_phuen = mc.duplicate(phiu_dam,n='phiu_phuen')[0]
lai_phuen = mc.shadingNode('file',at=1,n='lai_phuen')
mc.connectAttr(lai_phuen+'.oc',phiu_phuen+'.c')
mc.setAttr(lai_phuen+'.ftn',file_thangsairung,typ='string')

s = 2**(n+1)+1
phuen = mc.polyPlane(w=s,h=s,sx=s,sy=s,n='wongkot_hilbert')[0]
mc.hyperShade(a=phiu_phuen)
nf = mc.polyEvaluate(f=1)
mc.select([phuen+'.f[%d]'%i for i in set(range(s**2))-set([i+j*s for i,j in xy])])
mc.polyExtrudeFacet(ltz=1)
nf2 = mc.polyEvaluate(f=1)
mc.hyperShade(a=phiu_dam)
mc.polyExtrudeFacet(off=-0.1)
mc.polyExtrudeFacet(ltz=0.4,off=0.4)
mc.select(phuen+'.f[%d:%d]'%(nf,nf2-1))
mc.hyperShade(a=phiu_phanang)
mc.polyExtrudeFacet(off=0.15,kft=0)
mc.polyExtrudeFacet(off=0.15,ltz=-0.15)
mc.hyperShade(a=phiu_phuen)

mc.polyProjection(phuen+'.f[*]',pcx=0,pcy=0,pcz=0,rx=90,ry=0,rz=0,psu=s,psv=s) # ใส่ uv
mc.scale(2,2,2,phuen)
