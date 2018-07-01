# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import ListedColormap as licama
ku = 1024
kv = 1024

plt.figure(figsize=[ku/100.,kv/100.])
ax = plt.axes([0,0,1,1],aspect=1,xlim=[0,ku],ylim=[0,kv],facecolor='#fffbf2')
ax.yaxis.set_major_locator(mpl.ticker.NullLocator())
ax.xaxis.set_major_locator(mpl.ticker.NullLocator())
plt.setp([ax.spines[x] for x in ax.spines],lw=0)

# เส้นแดงแนวนอนที่ด้าม
plt.axhspan(800,840,fc='#d01d3a',lw=3,edgecolor='k')
plt.axhspan(600,640,fc='#d01d3a',lw=3,edgecolor='k')
# เส้นแดงเฉียงที่ใบพาย
plt.fill_between([512-60,512+60],[220,420],[280,480],color='#d01d3a')
plt.plot([512-60,512+60],[220,420],'k',lw=3)
plt.plot([512-60,512+60],[280,480],'k',lw=3)

# สัญลักษณ์กลมๆกลางใบพาย
theta = np.linspace(0,360,73)
u = np.sin(np.radians(theta))*44+512
v = np.cos(np.radians(theta))*44+90
plt.plot(u,v,'k',lw=2)
u = np.sin(np.radians(theta))*44*(1-np.abs(np.sin(np.radians(theta*6)))**0.5/2.5)+512
v = np.cos(np.radians(theta))*44*(1-np.abs(np.sin(np.radians(theta*6)))**0.5/2.5)+90
plt.plot(u,v,'k',lw=2)
u = np.sin(np.radians(theta))*24+512
v = np.cos(np.radians(theta))*24+90
plt.plot(u,v,'#d01d3a',lw=4)
u = np.sin(np.radians(theta))*22*(1-np.abs(np.sin(np.radians(theta*3)))**0.5/2)+512
v = np.cos(np.radians(theta))*22*(1-np.abs(np.sin(np.radians(theta*3)))**0.5/2)+90
plt.plot(u,v,'k',lw=2)
u = np.sin(np.radians(theta))*9+512
v = np.cos(np.radians(theta))*9+90
plt.plot(u,v,'#d01d3a',lw=2)
u = np.sin(np.radians(theta[::1]))*8+512.
v = np.cos(np.radians(theta[::1]))*8+90.
u = np.hstack([u,[512.]])
v = np.hstack([v,[90.]])
plt.tripcolor(u,v,np.stack([np.arange(72),np.arange(1,73),np.ones(72)*73],1),np.zeros(72),cmap=licama(['#000000']),lw=0)

plt.savefig('laibaiphai.png',dpi=100)
plt.close()