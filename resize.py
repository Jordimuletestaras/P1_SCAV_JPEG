

import os
import subprocess as sp
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    path_in = os.getcwd()+'/Lenna.png' #path de la input imagen
    img = plt.imread("Lenna.png") #cargamos la imagen de entrada
    iw = np.size(img, 0) #dimesiones de la imagen de entrada
    ih = np.size(img, 1)
    scaleW = 0.5 #factor de escalado
    scaleH = 0.5
    outW = str(iw*scaleW) #dimesiones de la imagen de salida
    outH = str(ih*scaleH)
    line = 'ffmpeg -i '+path_in+' -vf scale='+outW+':'+outH+' rescaled.png' #aplicamos el resize
    sp.run(line, shell=True)
