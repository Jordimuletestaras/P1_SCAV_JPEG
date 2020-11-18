import os
import subprocess as sp

if __name__ == '__main__':
    path_in = os.getcwd() + '/Lenna.png'
    line = 'ffmpeg -i ' + path_in + ' -vf hue=s=0 ex3.jpg' #guardamos como.jpg paa mayor compresion
    sp.run(line, shell=True)