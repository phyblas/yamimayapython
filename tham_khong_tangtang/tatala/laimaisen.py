# -*- coding: utf-8 -*-
import numpy as np
from scipy.misc import imsave
ku = 1024
kv = 1024
u,v = np.meshgrid(np.arange(0.,ku),np.arange(0.,kv))

z = np.random.normal(0,1,[kv,ku])
z -= z.mean(0)
z = z.cumsum(0)
z = 1-(z-z.min())/(z.max()-z.min())
z = np.stack([0.43*z,0.27*z,0.17*z],2)

imsave('laimai-.png',np.uint8(z*255))