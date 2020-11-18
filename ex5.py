from scipy.fftpack import dct, idct
import numpy as np
import matplotlib.pylab as plt


# implement 2D DCT
def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')


# implement 2D IDCT
def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')

img = plt.imread("Lenna.png")
imF = dct2(img)
im1 = idct2(imF)

# check if the reconstructed image is nearly equal to the original image
np.allclose(img, im1)
# True

# plot original and reconstructed images with matplotlib.pylab
plt.gray()
plt.subplot(131), plt.imshow(img), plt.axis('off'), plt.title('original', size=20)
plt.subplot(132), plt.imshow(imF), plt.axis('off'), plt.title('DCT', size=20)
plt.subplot(133), plt.imshow(im1), plt.axis('off'), plt.title('reconstructed', size=20)
plt.show()
