# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# กระดองเต่า
plt.figure(figsize=[8,4])
for j in [0,1]:
    ax = plt.axes([0.5*j,0,0.5,1],xlim=[-50,50],ylim=[-50,50],aspect=1)
    for i in range(11):
        plt.plot([-50,50],[i*20-150,i*20-50],'#a46529',lw=5,zorder=0)
        plt.plot([-50,50],[i*20-50,i*20-150],'#a46529',lw=5,zorder=0)
        plt.plot([-50,50],[i*20-150,i*20-50],'#7e4b1b',lw=2,zorder=1)
        plt.plot([-50,50],[i*20-50,i*20-150],'#7e4b1b',lw=2,zorder=1)
    plt.axis('off')
plt.savefig('langtao.png',dpi=128,facecolor='k')
plt.close()

# ใบหน้าเต่า
plt.figure(figsize=[4,4])
ax = plt.axes([1./3,1./3,1./3,1./3],xlim=[-5,5],ylim=[-5,5],aspect=1)
ax.add_patch(mpl.patches.Ellipse([-2,1.8],0.4,0.9,color='#ddeeee'))
ax.add_patch(mpl.patches.Ellipse([2,1.8],0.4,0.9,color='#ddeeee'))
theta = np.radians(np.linspace(-60,60,21))
x = np.sin(theta)*2
y = -np.cos(theta)*1.5
plt.plot(x,y,'#ddeeee',lw=3)
plt.axis('off')
plt.savefig('natao.png',dpi=128,facecolor='k')
plt.close()
