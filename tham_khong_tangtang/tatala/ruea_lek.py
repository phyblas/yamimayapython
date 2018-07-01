# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import ListedColormap as licama
from mpl_toolkits.mplot3d import axes3d
from scipy.interpolate import interp1d,SmoothBivariateSpline as smubaisp

kuv = 4096 # ความละเอียด
nu = 85 # จำนวนจุดในแนวตามยาว
nv = 11 # และแนวตั้ง
rs = 10 # ความละเอียดของจุดที่ใช้คำนวณ
nnu = (nu-1)*rs+1 # จำนวนจุดที่ใช้คำนวณ = ความละเอียด x จำนวนจุดในแต่ละแนว
nnv = (nv-1)*rs+1
meu = np.linspace(0.,1,nnu)
mev = np.linspace(0.,1,nnv)
u,v = np.meshgrid(meu,mev)
# x คือแนวตามยาวของเรือ
x = np.where(u>0.5,-120+270*(1-0.5*(u-0.95)**2/0.425**2),0)
x = np.where(u<0.5,120-270*(1-0.5*(u-0.05)**2/0.425**2),x)
x += np.where(u>0.5,(np.abs(u-0.5)/0.5)**0.5,np.where(u==0.5,0,-(np.abs(u-0.5)/0.5)**0.5))*(1-v**2)*25*(1-(((u-0.5)/0.5)**2))
# y คือแนวตามความสูง
y = 140-(140-v**2*40)*(1-(((u-0.5)/0.5)**2))**0.5*(np.sin((np.abs(u-0.5))*np.pi/0.5)*2*(u-0.5)**2+1)
y = np.where(y<0,0,y)
# z คือแนวตามความกว้าง
z1 = 80*(1-((u-0.5)/0.5)**2)*v**2
z2 = np.where(v<0.5,10*(1-((u-0.5)/0.5)**2)*(v/0.5)**2,(10+70*(v-0.5)/0.5)*(1-((u-0.5)/0.5)**2))
z3 = 80*(1-((u-0.5)/0.5)**2)*v
w1 = np.where(np.abs(u-0.5)>0.25,np.abs((np.abs(u-0.5)-0.25)/0.25)**0.5,0)
w3 = np.where(np.abs(u-0.5)<0.25,((0.25-np.abs(u-0.5))/0.25)**2,0)
w2 = 1-w1-w3
z = 1+(z1*w1+z2*w2+z3*w3)*0.5
# วาดกราฟภาคตัดทั้ง ๓ ด้าน
fig = plt.figure()
plt.subplot(311,aspect=1,xlim=[-170,170],ylim=[0,150])
plt.plot(x[::rs,::rs],y[::rs,::rs],'#d01d3a')
plt.plot(x[::rs,::rs].T,y[::rs,::rs].T,'b')
plt.subplot(312,aspect=1,xlim=[-50,50],ylim=[0,150])
plt.plot(z[::rs,::rs],y[::rs,::rs],'#d01d3a')
plt.plot(z[::rs,::rs].T,y[::rs,::rs].T,'b')
plt.plot(-z[::rs,::rs].T,y[::rs,::rs].T,'b')
plt.subplot(313,aspect=1,xlim=[-170,170],ylim=[-50,50])
plt.plot(x[::rs,::rs],z[::rs,::rs],'#d01d3a')
plt.plot(x[::rs,::rs].T,z[::rs,::rs].T,'b')
plt.plot(x[::rs,::rs].T,-z[::rs,::rs].T,'b')
plt.savefig('phangruea_lek.png',dpi=200)
plt.close()

# วาดกราฟสามมิติ
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d',xlim=[-400,400],ylim=[-400,400],zlim=[-400,400])
ax.plot_wireframe(z[::rs,::rs],x[::rs,::rs],y[::rs,::rs],color='b')
ax.plot_wireframe(-z[::rs,::rs],x[::rs,::rs],y[::rs,::rs],color='#d01d3a')
plt.savefig('khrongruea_lek.png',dpi=200)
plt.close()

# แปลงพิกัดเป็นค่าตำแหน่งบนเท็กซ์เจอร์
diffx = np.diff(x,axis=0)
diffy = np.diff(y,axis=0)
diffz = np.diff(z,axis=0)
# เท็กซ์เจอร์ส่วนด้านข้างเรือ
uvx = np.vstack([-diffx[::-1],np.zeros([1,nnu])]).cumsum(0)[::-1]
uvy = np.vstack([-((diffy**2+diffz**2)**0.5)[::-1],np.zeros([1,nnu])]).cumsum(0)[::-1]
uvy += y[-1]
uvx += x[-1]
uvxmin = uvx.min()
yao = uvx.max()-uvxmin
uvx = 0.005+(uvx-uvxmin)/yao*0.99
uvy = (uvy-uvy.min())/yao*0.99+0.01
# เท็กซ์เจอร์ส่วนแถบแดงกลางเรือ
uvx2 = 0.005+u[:2]*0.99
uvy2 = v[:2]*0.2+0.6

# วาดเท็กซ์เจอร์ของภายนอกเรือ
plt.figure(figsize=[kuv/100.,kuv/100.])
ax = plt.axes([0,0,1,1],aspect=1,xlim=[0,1],ylim=[0,1])
ax.yaxis.set_major_locator(mpl.ticker.NullLocator())
ax.xaxis.set_major_locator(mpl.ticker.NullLocator())
plt.setp([ax.spines[xx] for xx in ax.spines],lw=0)

# ฟังก์ชันสำหรับการประมาณค่าในช่วงเพื่อแปลงหน่วยระหว่างตำแหน่งบนเรือกับตำแหน่งบน uv
fuvx = smubaisp(x.ravel(),y.ravel(),uvx.ravel()).ev
fuvy = smubaisp(x.ravel(),y.ravel(),uvy.ravel()).ev

# สีครีมผิวเรือ
plt.fill_between(uvx[0],uvy[0],0.6,color='#fffbf2',zorder=0.)
# สีแถบแดงใต้เรือ
plt.fill_between(uvx2[0],uvy2[0],uvy2[1],color='#d01d3a',edgecolor='#d01d3a',lw=2)

# ลายรูปคน
xsss = [-146,-117,-94,-26,0,26,94,117,146]
ysss = [40.]+[22.]*7+[40.]
ksss = [0.7,1.08,1]+[0.9]*3+[1,1.08,0.7]
for xs,ys,ks in zip(xsss,ysss,ksss):
    # ขาด้านล่าง
    xt = np.linspace(xs-1.6*ks,xs+1.6*ks,13)
    yt = -np.sqrt(np.abs(xt-xs)/1./ks)*1.*ks+ys
    plt.plot(fuvx(xt,yt),fuvy(xt,yt),'#d01d3a',zorder=0.1)
    
    # ลำตัวสีแดง
    xt = np.array([xs-1*ks,xs,xs+1*ks])
    yt = np.array([ys+2.5*ks,ys,ys+2.5*ks])
    yt2 = np.array([ys+2.5*ks,ys+3.5*ks,ys+2.5*ks])
    plt.fill_between(fuvx(xt,yt),fuvy(xt,yt),fuvy(xt,yt2),color='#d01d3a')
    
    # กิ่งอันล่าง
    xt = np.linspace(xs-5*ks,xs+5*ks,11)
    yt = np.abs(np.sqrt(np.abs(xt-xs)/5/ks)*4.5-2.5)*ks+ys+2.5*ks
    yt2 = np.abs(np.sqrt(np.abs(xt-xs)/5/ks)*4.5-2)*ks+ys+2*ks
    plt.fill_between(fuvx(xt,yt),fuvy(xt,yt),fuvy(xt,yt2),color='k')
    
    # หัวกลมๆ
    theta = np.linspace(0,180,7)
    xw = np.cos(np.radians(theta))+xs
    yw = np.sin(np.radians(theta))+ys+5.5*ks
    yw2 = -np.sin(np.radians(theta))+ys+5.5*ks
    plt.fill_between(fuvx(xw,yw),fuvy(xw,yw),fuvy(xw,yw2),color='k')
    
    # กิ่งอันกลาง
    xt = np.linspace(xs-2.5*ks,xs+2.5*ks,11)
    yt = np.sqrt(np.abs(xt-xs)/2.5/ks)*2.5*ks+ys+6*ks
    yt2 = np.sqrt(np.abs(xt-xs)/2.5/ks)*3*ks+ys+5.5*ks
    plt.fill_between(fuvx(xt,yt),fuvy(xt,yt),fuvy(xt,yt2),color='k')
    
    # กิ่งอันบน
    xt = [xs-1*ks,xs+1*ks]
    yt = [ys+7.5*ks,ys+7.5*ks]
    plt.plot(fuvx(xt,yt),fuvy(xt,yt),'k')
    xt = [xs,xs]
    yt = [ys+7.5*ks,ys+12.5*ks]
    plt.plot(fuvx(xt,yt),fuvy(xt,yt),'k')
    
    # ม้วนล่าง
    theta = np.linspace(0,360*3,18*3)
    xw = np.sin(np.radians(theta))*theta/(360*3)*ks+xs-5*ks
    yw = np.cos(np.radians(theta))*theta/(360*3)*ks+ys+3.5*ks
    plt.plot(fuvx(xw,yw),fuvy(xw,yw),'k',lw=0.5)
    xw = -np.sin(np.radians(theta))*theta/(360*3)*ks+xs+5*ks
    plt.plot(fuvx(xw,yw),fuvy(xw,yw),'k',lw=0.5)
    
    # ม้วนกลาง
    xw = np.sin(np.radians(theta))*theta/(360*3)*ks+xs-2.5*ks
    yw = np.cos(np.radians(theta))*theta/(360*3)*ks+ys+7.5*ks
    plt.plot(fuvx(xw,yw),fuvy(xw,yw),'k',lw=0.5)
    xw = -np.sin(np.radians(theta))*theta/(360*3)*ks+xs+2.5*ks
    plt.plot(fuvx(xw,yw),fuvy(xw,yw),'k',lw=0.5)
    
    # ม้วนบน
    for i in range(1,4):
        xw = np.sin(np.radians(theta[:19]))*i/3*ks+xs
        yw = np.cos(np.radians(theta[:19]))*i/3*ks+ys+13.5*ks
        plt.plot(fuvx(xw,yw),fuvy(xw,yw),'k',lw=0.5)

#แถบลายข้าวหลามตัดแนวตั้ง
llang = 18.
lbon = 38.
xsxs = []
ysys = []
x_tang = (np.array([-15,-14,14,15])+np.arange(-60,61,120)[:,None]).ravel()
for d in x_tang:
    xsxs.append(np.ones(39)*d)
    ysys.append(np.linspace(llang,lbon,39))

# เส้นหยึกหยักสามเส้นใหญ่ระหว่างแถบแนวตั้ง
for i in range(2):
    for j in range(3):
        xs = np.linspace(x_tang[1+i*4],x_tang[2+i*4],7)
        ys = np.where(np.arange(7)%2==0,llang+3.2+j*(lbon-llang)/4.4,llang+3.2+(j+0.5)*(lbon-llang)/4.4)
        uvxt = fuvx(xs,ys)
        uvyt = fuvy(xs,ys)
        uvyt2 = fuvy(xs,ys+(lbon-llang)/6.)
        plt.fill_between(uvxt,uvyt,uvyt2,color='#d01d3a',zorder=0.1)
        plt.plot(uvxt,uvyt,'k',zorder=0.1,lw=5)
        plt.plot(uvxt,uvyt2,'k',zorder=0.1,lw=5)

# วาดพวกแถบลายข้าวหลามตัดทั้งหมด
for xs,ys,ks in zip(xsxs,ysys,[[1,0]]*16):
    ns = len(xs)
    xt = np.where(np.arange(ns)%2==0,xs-0.5*ks[0],xs)
    yt = np.where(np.arange(ns)%2==0,ys-0.5*ks[1],ys)
    uvxt = fuvx(xt,yt)
    uvyt = fuvy(xt,yt)
    plt.tripcolor(uvxt,uvyt,np.arange(3)+np.arange(ns-2)[:,None],np.arange(ns-2)%2,cmap=licama(['#000000','#fffbf2']))
    plt.tripcolor(1-uvxt,uvyt,np.arange(3)+np.arange(ns-2)[:,None],np.arange(ns-2)%2,cmap=licama(['#000000','#fffbf2']))
    xt = np.where(np.arange(ns)%2==0,xs+0.5*ks[0],xs)
    yt = np.where(np.arange(ns)%2==0,ys+0.5*ks[1],ys)
    uvxt = fuvx(xt,yt)
    uvyt = fuvy(xt,yt)
    plt.tripcolor(uvxt,uvyt,np.arange(3)+np.arange(ns-2)[:,None],np.arange(ns-2)%2,cmap=licama(['#000000','#fffbf2']))
    plt.tripcolor(1-uvxt,uvyt,np.arange(3)+np.arange(ns-2)[:,None],np.arange(ns-2)%2,cmap=licama(['#000000','#fffbf2']))



# แถบลายขอบหัวท้ายเรือ
yt = uvy[0]
xt = np.where(np.arange(nnu)%2,uvx[0],uvx[0]+(0.5-uvx[0])*0.003)
plt.tripcolor(xt,yt,np.arange(3)+np.arange(nnu-2)[:,None],np.arange(1,nnu-1)%2,cmap=licama(['#000000','#fffbf2']))
xt = np.where(np.arange(nnu)%2==0,uvx[0]+(0.5-uvx[0])*0.003,uvx[0]+(0.5-uvx[0])*0.006)
plt.tripcolor(xt,yt,np.arange(3)+np.arange(nnu-2)[:,None],np.arange(1,nnu-1)%2,cmap=licama(['#000000','#fffbf2']))
xt = np.where(np.arange(nnu)%2,uvx[0]+(0.5-uvx[0])*0.006,uvx[0]+(0.5-uvx[0])*0.009)
plt.tripcolor(xt,yt,np.arange(3)+np.arange(nnu-2)[:,None],np.arange(1,nnu-1)%2,cmap=licama(['#000000','#fffbf2']))
xt = np.where(np.arange(nnu)%2==0,uvx[0]+(0.5-uvx[0])*0.009,uvx[0]+(0.5-uvx[0])*0.012)
plt.tripcolor(xt,yt,np.arange(3)+np.arange(nnu-2)[:,None],np.arange(1,nnu-1)%2,cmap=licama(['#000000','#fffbf2']))
xt = np.where(np.arange(nnu)%2,uvx[0]+(0.5-uvx[0])*0.012,uvx[0]+(0.5-uvx[0])*0.015)
plt.tripcolor(xt,yt,np.arange(3)+np.arange(nnu-2)[:,None],np.arange(nnu-2)%2,cmap=licama(['#000000','#fffbf2']))
xt = np.where(np.arange(nnu)%2==0,uvx[0]+(0.5-uvx[0])*0.015,uvx[0]+(0.5-uvx[0])*0.018)
plt.tripcolor(xt,yt,np.arange(3)+np.arange(nnu-2)[:,None],np.arange(1,nnu-1)%2,cmap=licama(['#000000','#fffbf2']))
xt = np.where(np.arange(nnu)%2,uvx[0]+(0.5-uvx[0])*0.018,uvx[0]+(0.5-uvx[0])*0.02)
plt.tripcolor(xt,yt,np.arange(3)+np.arange(nnu-2)[:,None],np.zeros(nnu-2),cmap=licama(['#d01d3a']))
xt = np.where(np.arange(nnu)%2,uvx[0]+(0.5-uvx[0])*0.02,uvx[0]+(0.5-uvx[0])*0.023)
plt.tripcolor(xt,yt,np.arange(3)+np.arange(nnu-2)[:,None],np.arange(nnu-2)%2,cmap=licama(['#000000','#fffbf2']))
xt = np.where(np.arange(nnu)%2==0,uvx[0]+(0.5-uvx[0])*0.023,uvx[0]+(0.5-uvx[0])*0.026)
plt.tripcolor(xt,yt,np.arange(3)+np.arange(nnu-2)[:,None],np.arange(1,nnu-1)%2,cmap=licama(['#000000','#fffbf2']))
xt = np.where(np.arange(nnu)%2,uvx[0]+(0.5-uvx[0])*0.026,uvx[0]+(0.5-uvx[0])*0.028)
plt.tripcolor(xt,yt,np.arange(3)+np.arange(nnu-2)[:,None],np.zeros(nnu-2),cmap=licama(['#d01d3a']))
xt = np.where(np.arange(nnu)%2,uvx[0]+(0.5-uvx[0])*0.028,uvx[0]+(0.5-uvx[0])*0.030)
plt.tripcolor(xt,yt,np.arange(3)+np.arange(nnu-2)[:,None],np.arange(1,nnu-1)%2,cmap=licama(['#000000','#fffbf2']))
xt = np.where(np.arange(nnu)%2==0,uvx[0]+(0.5-uvx[0])*0.030,uvx[0]+(0.5-uvx[0])*0.032)
plt.tripcolor(xt,yt,np.arange(3)+np.arange(nnu-2)[:,None],np.arange(1,nnu-1)%2,cmap=licama(['#000000','#fffbf2']))

# แถบลายขอบบน
g = np.hstack([[0],((np.diff(uvx[-1])**2+np.diff(uvy[-1])**2)**0.5).cumsum()])
g = g/g.max()
gx = interp1d(g,uvx[-1])
gy = interp1d(g,uvy[-1])
ns = 1201
sg = np.linspace(0,1,ns)
guvx = gx(sg)
guvy = gy(sg)

xt = np.where(np.arange(ns)%2,guvx,guvx-(0.5-guvx)*0.003)
yt = np.where(np.arange(ns)%2,guvy,guvy-0.0025)
plt.tripcolor(xt,yt,np.arange(3)+np.arange(ns-2)[:,None],np.arange(ns-2)%2,cmap=licama(['#000000','#fffbf2']))
xt = np.where(np.arange(ns)%2==0,guvx-(0.5-guvx)*0.003,guvx-(0.5-guvx)*0.006)
yt = np.where(np.arange(ns)%2==0,guvy-0.0025,guvy-0.005)
plt.tripcolor(xt,yt,np.arange(3)+np.arange(ns-2)[:,None],np.arange(1,ns-1)%2,cmap=licama(['#000000','#fffbf2']))
xt = np.where(np.arange(ns)%2,guvx-(0.5-guvx)*0.006,guvx-(0.5-guvx)*0.0075)
yt = np.where(np.arange(ns)%2,guvy-0.005,guvy-0.00625)
plt.tripcolor(xt,yt,np.arange(3)+np.arange(ns-2)[:,None],np.zeros(ns-2),cmap=licama(['#d01d3a']))
xt = np.where(np.arange(ns)%2,guvx-(0.5-guvx)*0.0075,guvx-(0.5-guvx)*0.0105)
yt = np.where(np.arange(ns)%2,guvy-0.00625,guvy-0.00875)
plt.tripcolor(xt,yt,np.arange(3)+np.arange(ns-2)[:,None],np.arange(ns-2)%2,cmap=licama(['#000000','#fffbf2']))
xt = np.where(np.arange(ns)%2==0,guvx-(0.5-guvx)*0.0105,guvx-(0.5-guvx)*0.0135)
yt = np.where(np.arange(ns)%2==0,guvy-0.00875,guvy-0.01125)
plt.tripcolor(xt,yt,np.arange(3)+np.arange(ns-2)[:,None],np.arange(1,ns-1)%2,cmap=licama(['#000000','#fffbf2']))
xt = np.where(np.arange(ns)%2,guvx-(0.5-guvx)*0.0135,guvx-(0.5-guvx)*0.015)
yt = np.where(np.arange(ns)%2,guvy-0.01125,guvy-0.0125)
plt.tripcolor(xt,yt,np.arange(3)+np.arange(ns-2)[:,None],np.zeros(ns-2),cmap=licama(['#d01d3a']))
xt = np.where(np.arange(ns)%2,guvx-(0.5-guvx)*0.015,guvx-(0.5-guvx)*0.0165)
yt = np.where(np.arange(ns)%2,guvy-0.0125,guvy-0.0140)
plt.tripcolor(xt,yt,np.arange(3)+np.arange(ns-2)[:,None],np.arange(1,ns-1)%2,cmap=licama(['#000000','#fffbf2']))
xt = np.where(np.arange(ns)%2==0,guvx-(0.5-guvx)*0.0165,guvx-(0.5-guvx)*0.018)
yt = np.where(np.arange(ns)%2==0,guvy-0.0140,guvy-0.0155)
plt.tripcolor(xt,yt,np.arange(3)+np.arange(ns-2)[:,None],np.arange(1,ns-1)%2,cmap=licama(['#000000','#fffbf2']))

# พื้นแดงท้องเรือ
ns = 501
xs = np.linspace(-160,160,ns)
ys = np.ones(ns)*19
uvxs = fuvx(xs,ys)
uvys = fuvy(xs,ys)
plt.fill_between(uvxs,uvys,0.01,color='#d01d3a')
xt = uvxs.copy()
# แถบลายด้านล่าง
yt = np.where(np.arange(ns)%2==0,uvys,uvys+0.002)
plt.tripcolor(xt,yt,np.arange(3)+np.arange(ns-2)[:,None],np.arange(ns-2)%2,cmap=licama(['#000000','#fffbf2']))
yt = np.where(np.arange(ns)%2,uvys+0.002,uvys+0.004)
plt.tripcolor(xt,yt,np.arange(3)+np.arange(ns-2)[:,None],np.arange(ns-2)%2,cmap=licama(['#000000','#fffbf2']))
yt = np.where(np.arange(ns)%2==0,uvys+0.004,uvys+0.006)
plt.tripcolor(xt,yt,np.arange(3)+np.arange(ns-2)[:,None],np.arange(ns-2)%2,cmap=licama(['#000000','#fffbf2']))
yt = np.where(np.arange(ns)%2,uvys+0.006,uvys+0.008)
plt.tripcolor(xt,yt,np.arange(3)+np.arange(ns-2)[:,None],np.arange(ns-2)%2,cmap=licama(['#000000','#fffbf2']))

# ขาตั้งแถบลายวงกลม
xt = np.linspace(140-2.2,140+2.2,13)
yt = -np.sqrt(np.abs(xt-140)*7)+25
plt.plot(fuvx(xt,yt),fuvy(xt,yt),'#d01d3a',zorder=0.1)
plt.plot(1-fuvx(xt,yt),fuvy(xt,yt),'#d01d3a',zorder=0.1)

# แถบลายวงกลม
xc = 140
yc = 32
theta = np.linspace(0,360,73)
xw1 = np.cos(np.radians(theta))*7-xc
yw1 = np.sin(np.radians(theta))*7+yc
plt.plot(fuvx(xw1,yw1),fuvy(xw1,yw1),'k',lw=2)
plt.plot(1-fuvx(xw1,yw1),fuvy(xw1,yw1),'k',lw=2)
xw2 = np.cos(np.radians(theta))*7*(1-0.3*np.abs(np.sin(np.radians(theta*6)))**0.5)-xc
yw2 = np.sin(np.radians(theta))*7*(1-0.3*np.abs(np.sin(np.radians(theta*6)))**0.5)+yc
xw3 = np.cos(np.radians(theta))*4.5-xc
yw3 = np.sin(np.radians(theta))*4.5+yc
xw = np.hstack([xw2,xw3])
yw = np.hstack([yw2,yw3])
uvxw = fuvx(xw,yw)
uvyw = fuvy(xw,yw)
plt.tripcolor(uvxw,uvyw,np.vstack([np.array([0,1,73])+np.arange(72)[:,None],np.array([1,73,74])+np.arange(72)[:,None]]),np.zeros(72*2),cmap=licama(['#000000']))
plt.tripcolor(1-uvxw,uvyw,np.vstack([np.array([0,1,73])+np.arange(72)[:,None],np.array([1,73,74])+np.arange(72)[:,None]]),np.zeros(72*2),cmap=licama(['#000000']))
plt.plot(fuvx(xw3,yw3),fuvy(xw3,yw3),'#d01d3a',lw=2)
plt.plot(1-fuvx(xw3,yw3),fuvy(xw3,yw3),'#d01d3a',lw=2)
xw4 = np.cos(np.radians(theta))*4.5*(1-0.5*np.abs(np.cos(np.radians(theta*3)))**0.5)-xc
yw4 = np.sin(np.radians(theta))*4.5*(1-0.5*np.abs(np.cos(np.radians(theta*3)))**0.5)+yc
xw5 = np.cos(np.radians(theta))*2-xc
yw5 = np.sin(np.radians(theta))*2+yc
xw = np.hstack([xw4,xw5])
yw = np.hstack([yw4,yw5])
uvxw = fuvx(xw,yw)
uvyw = fuvy(xw,yw)
plt.tripcolor(uvxw,uvyw,np.vstack([np.array([0,1,73])+np.arange(72)[:,None],np.array([1,73,74])+np.arange(72)[:,None]]),np.zeros(72*2),cmap=licama(['#000000']))
plt.tripcolor(1-uvxw,uvyw,np.vstack([np.array([0,1,73])+np.arange(72)[:,None],np.array([1,73,74])+np.arange(72)[:,None]]),np.zeros(72*2),cmap=licama(['#000000']))

plt.plot(fuvx(xw5,yw5),fuvy(xw5,yw5),'#d01d3a',lw=2)
plt.plot(1-fuvx(xw5,yw5),fuvy(xw5,yw5),'#d01d3a',lw=2)
xw6 = np.cos(np.radians(theta[::8]))-xc
yw6 = np.sin(np.radians(theta[::8]))+yc
xw6 = np.hstack([xw6,[-xc]])
yw6 = np.hstack([yw6,[yc]])
plt.tripcolor(fuvx(xw6,yw6),fuvy(xw6,yw6),np.stack([np.arange(9),np.arange(1,10),np.ones(9)*10],1),np.zeros(9),cmap=licama(['#000000']))
plt.tripcolor(1-fuvx(xw6,yw6),fuvy(xw6,yw6),np.stack([np.arange(9),np.arange(1,10),np.ones(9)*10],1),np.zeros(9),cmap=licama(['#000000']))

plt.savefig('nokruea_lek.png',dpi=100)
plt.close()



# พื้นเรือ
fz_xy = smubaisp(x.ravel(),y.ravel(),z.ravel(),kx=2,ky=2).ev
xp1 = np.linspace(-140,140,21)
yp1 = np.ones(21)*10
zp1 = fz_xy(xp1,yp1)-2.5

# แผนกั้นตามแนวความกว้างที่ท้องเรือ
np3 = 11
xp3 = np.array([[np.linspace(-101.5+i*50,-98.5+i*50,2)]*np3 for i in range(5)])
yp3 = np.zeros([5,np3,2])+10+(np.linspace(0,1,np3)[:,None]**2)*5
zp3 = fz_xy(xp3,yp3)-3

# สร้าง obj
x = x[::rs,::rs]
y = y[::rs,::rs]
z = z[::rs,::rs]
uvx = uvx[::rs,::rs]
uvy = uvy[::rs,::rs]

sv1 = 'v %.4f %.4f %.4f\n'%(x[0,0],y[0,0],z[0,0])
sv2 = 'v %.4f %.4f %.4f\n'%(x[0,0],y[0,0],-z[0,0])
svt = 'vt %.4f %.4f\n'%(uvx[0,0],uvy[0,0])
for i in range(1,nu-1):
    for j in range(nv):
        sv1 += 'v %.4f %.4f %.4f\n'%(x[j,i],y[j,i],z[j,i])
        sv2 += 'v %.4f %.4f %.4f\n'%(x[j,i],y[j,i],-z[j,i])
        svt += 'vt %.4f %.4f\n'%(uvx[j,i],uvy[j,i])

sv1 += 'v %.4f %.4f %.4f\n'%(x[0,-1],y[0,-1],z[0,-1])
sv2 += 'v %.4f %.4f %.4f\n'%(x[0,-1],y[0,-1],-z[0,-1])
svt += 'vt %.4f %.4f\n'%(uvx[0,-1],uvy[0,-1])

for i in range(nu):
    for j in range(2):
        svt += 'vt %.4f %.4f\n'%(uvx2[j,i],uvy2[j,i])

nvtx1 = (nu-2)*nv+2

sv3 = ''
for i in range(21):
    sv3 += 'v %.4f %.4f %.4f\n'%(xp1[i],yp1[i],zp1[i])
    sv3 += 'v %.4f %.4f %.4f\n'%(xp1[i],yp1[i],-zp1[i])

for k in range(5):
    for j in range(np3):
        for i in range(2):
            sv3 += 'v %.4f %.4f %.4f\n'%(xp3[k,j,i],yp3[k,j,i],zp3[k,j,i])
            sv3 += 'v %.4f %.4f %.4f\n'%(xp3[k,j,i],yp3[k,j,i],-zp3[k,j,i])

sv = sv1+sv2+sv3



sf1 = ''
sf2 = ''
sf3 = ''
for j in range(nv-1):
    sf1 += 'f %d/%d %d/%d %d/%d\n'%(1,1,j+2,j+2,j+3,j+3)
    sf2 += 'f %d/%d %d/%d %d/%d\n'%(1+nvtx1,1,j+3+nvtx1,j+3,j+2+nvtx1,j+2)
sf3 += 'f %d/%d %d/%d %d/%d %d/%d\n'%(
    1,nvtx1+1,1+nvtx1,nvtx1+2,
    2+nvtx1,nvtx1+4,2,nvtx1+3)

for i in range(1,nu-2):
    for j in range(nv-1):
        sf1 += 'f %d/%d %d/%d %d/%d %d/%d\n'%(
            (i-1)*nv+j+2,(i-1)*nv+j+2,i*nv+j+2,i*nv+j+2,
            i*nv+j+3,i*nv+j+3,(i-1)*nv+j+3,(i-1)*nv+j+3)
        sf2 += 'f %d/%d %d/%d %d/%d %d/%d\n'%(
            (i-1)*nv+j+2+nvtx1,(i-1)*nv+j+2,(i-1)*nv+j+3+nvtx1,(i-1)*nv+j+3,
            i*nv+j+3+nvtx1,i*nv+j+3,i*nv+j+2+nvtx1,i*nv+j+2)
    sf3 += 'f %d/%d %d/%d %d/%d %d/%d\n'%(
        (i-1)*nv+2,nvtx1+i*2+1,(i-1)*nv+2+nvtx1,nvtx1+i*2+2,
        i*nv+2+nvtx1,nvtx1+(i+1)*2+2,i*nv+2,nvtx1+(i+1)*2+1)

for j in range(nv-1):
    sf1 += 'f %d/%d %d/%d %d/%d\n'%(
        (nu-3)*nv+j+2,(nu-3)*nv+j+2,nvtx1,nvtx1,
        (nu-3)*nv+j+3,(nu-3)*nv+j+3)
    sf2 += 'f %d/%d %d/%d %d/%d\n'%(
        (nu-3)*nv+j+2+nvtx1,(nu-3)*nv+j+2,(nu-3)*nv+j+3+nvtx1,(nu-3)*nv+j+3,
        nvtx1*2,nvtx1)
sf3 += 'f %d/%d %d/%d %d/%d %d/%d\n'%(
    nvtx1-nv,nvtx1+2*nu-3,nvtx1*2-nv,nvtx1+2*nu-2,
    nvtx1*2,nvtx1+2*nu,nvtx1,nvtx1+2*nu-1)

sf4 = ''
for i in range(20):
    sf4 += 'f %d %d %d %d\n'%(nvtx1*2+1+i*2,nvtx1*2+3+i*2,nvtx1*2+4+i*2,nvtx1*2+2+i*2)

for k in range(5):    
    for j in range(np3-1):
        sf4 += 'f %d %d %d %d\n'%(nvtx1*2+42+k*np3*4+1+4*j,nvtx1*2+42+k*np3*4+1+4*(j+1),nvtx1*2+42+k*np3*4+2+4*(j+1),nvtx1*2+42+k*np3*4+2+4*j)
        sf4 += 'f %d %d %d %d\n'%(nvtx1*2+42+k*np3*4+1+4*j+2,nvtx1*2+42+k*np3*4+2+4*j+2,nvtx1*2+42+k*np3*4+2+4*(j+1)+2,nvtx1*2+42+k*np3*4+1+4*(j+1)+2)
    sf4 += 'f %d %d %d %d\n'%(nvtx1*2+42+k*np3*4+2+4*(j+1)+2,nvtx1*2+42+k*np3*4+2+4*(j+1),nvtx1*2+42+k*np3*4+1+4*(j+1),nvtx1*2+42+k*np3*4+1+4*(j+1)+2)

sf = '\ns 1\n'
sf += 'g tuaruea\n'
sf += 'usemtl phiu_nokruea\n'
sf += sf1+sf2+sf3
sf += '\ng phuenruea\n'
sf += sf4

with open('tatala_lek.obj','w') as f:
    f.write('mtllib tatala_lek.mtl\n\n'+sv+'\n'+svt+'\n'+sf)
with open('tatala_lek.mtl','w') as f:
    f.write('newmtl phiu_nokruea\nmap_Kd nokruea_lek.png')