import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate2d
import imageio
n = 512
g = 20
for i,f in enumerate(plt.get_cmap('Set2')(np.linspace(0,1,6))[:,:3],1):
    z = np.random.uniform(0.5,1,[n+g-1,n+g-1])
    z = correlate2d(z,np.ones([g,g]),'valid')
    z = (z-z.min())/(z.max()-z.min())*0.5+0.5
    z = z[:,:,None]*np.array(f)
    imageio.imsave('na%d.jpg'%i,z)