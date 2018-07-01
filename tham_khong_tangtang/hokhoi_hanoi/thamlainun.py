import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource
from skimage import io
def norm(x):
    return (x-x.min())/(x.max()-x.min())

ls = LightSource(304,34)

chue = [
    ['lai_banpratu.png','nun_banpratu.png','tobira.png',1],
    ['lai_bannatang.png','nun_bannatang.png','mado.png',1],
    ['lai_khopnatang.jpg','nun_khopnatang.png','madowaku.jpg',1],
    ['lai_phuenit.jpg','nun_phuenit.jpg','yuka.jpg',1],
    ['lai_phanangit.jpg','nun_phanangit.jpg','kabe.jpg',1],
    ['lai_than.jpg','nun_than.jpg','kaidan.jpg',1],
    ['lai_thanit.jpg','nun_thanit.jpg','kiso.jpg',1],
    ['lai_mai.jpg','nun_ruamai.jpg','tesuri.jpg',1],
    ['lai_mai.jpg',0,'hashira.jpg',1],
    ['lai_khoppratu.jpg',0,'tobirawaku.jpg',1],
    ['lai_saomum.jpg',0,'sekichuu.jpg',1],
]
for c in chue:
    lai = io.imread(c[0]).astype(float)
    lai = lai/255.
    if(c[1]):
        nun = io.imread(c[1]).astype(float)
        nun = norm(nun)
    else:
        nun = np.ones_like(lai[:,:,0])
    z = ls.shade_rgb(lai,nun,blend_mode='overlay')
    io.imsave(c[2],z)