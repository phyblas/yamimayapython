import maya.cmds as mc
import numpy as np
mc.nurbsToPolygonsPref(f=3)

phiu_baiphai = mc.shadingNode('blinn',asShader=1,n='phiu_nairuea')
mc.setAttr(phiu_baiphai+'.ambc',0.5,0.5,0.5,typ='double3')
lai = mc.shadingNode('file',at=1)
mc.connectAttr(lai+'.oc',phiu_baiphai+'.c')
mc.setAttr(lai+'.ftn','/Users/patn/Dropbox/ruea/laibaiphai.png',typ='string')

theta,z = np.meshgrid(
    np.linspace(18,378,10,0),
    np.hstack([np.linspace(0,60,6,0),np.linspace(60,120,10)]))
r = np.hstack([np.linspace(-1,1,6)**2+1,np.ones(10)])[:,None]
x1 = np.cos(np.radians(theta))*r
y1 = np.sin(np.radians(theta))*r
x2 = np.where((theta+45)%180>90,x1*3,np.where(x1>0,9,-9))
y2 = np.where((theta+45)%180>90,np.where(y1>0,0.5,-0.5),y1/4)
w2 = np.zeros(10)+np.hstack([np.zeros(6),np.linspace(0,1,10)])[:,None]
w2 = np.where(np.abs(theta-180)==90,0,w2)**0.5
w1 = 1-w2
x = x1*w1+x2*w2
y = y1*w1+y2*w2
y[-1] = np.where(y[-1]>0.001,0.1,np.where(y[-1]<-0.001,-0.1,0))
p = np.stack([x,y,z],2)
wong = []
for i in range(z.shape[1]):
    wong.append(mc.curve(p=p[:,i],d=1))
baiphai = mc.loft(wong,d=1,c=1,r=1,po=1,ch=0)[0]
mc.hyperShade(a=phiu_baiphai)
mc.polyNormal(ch=0)
mc.delete(wong)
g = [[],[]]
for i in range(mc.polyEvaluate(e=1)):
    s = baiphai+'.e[%d]'%i
    bb = mc.xform(s,q=1,bb=1)
    if(bb[5]<0.1):
        g[0].append(s)
    if(bb[2]>120-0.1):
        g[1].append(s)
mc.select(g[0])
mc.polyExtrudeEdge(ch=0)
mc.scale(0,0,1)
mc.scale(0,1,1,g[1])
mc.polyMergeVertex(d=0.001,ch=0,n='baiphai')
mc.polyProjection(baiphai+'.f[*]',pcx=0,pcy=0,pcz=60,rx=90,ry=180,rz=0,psu=120,psv=120,ch=0)
mc.rotate(-90,baiphai)