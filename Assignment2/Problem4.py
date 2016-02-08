__author__ = 'Sree Vishant Prabhakaran'
import numpy as np
from matplotlib import image
from matplotlib import pyplot as plt

if __name__ == "__main__":
    img = image.imread('HuskyBW.png')
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20*np.log(np.abs(fshift))

    m, n = np.shape(magnitude_spectrum)
    center_m, center_n = m/2, n/2

    for i in range(m):
        for j in range(n):
            if ((i-center_m)**2) + ((j-center_n)**2) > 15**2:
                fshift[i, j] = 0

    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)

    plt.subplot(131),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(132),plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.subplot(133),plt.imshow(img_back, cmap = 'gray')
    plt.title('Filtered Image'), plt.xticks([]), plt.yticks([])
    plt.show()
