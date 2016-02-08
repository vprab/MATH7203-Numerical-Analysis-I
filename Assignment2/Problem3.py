__author__ = 'Sree Vishant Prabhakaran'
import numpy as np
import matplotlib.pyplot as plt


def triangle_fourier(n, x):
    return sum(8.0*np.cos(i*np.pi*x)/(i*i*np.pi*np.pi) for i in range(1, n+1, 2))


def triangle_rms(n, y_true):
    y_comp = np.array([triangle_fourier(n, i) for i in np.arange(-1, 1, 0.01)])
    return np.sqrt(np.mean(np.square(y_comp - y_true)))

if __name__ == "__main__":
    t = np.arange(-1, 1, 0.01)

    y = [triangle_fourier(1, x) for x in t]
    plt.plot(t, y, 'r-')

    plt.title("Triangle Wave Fourier Series \n Highest Order N = 1")
    plt.legend()
    plt.show()

    y = [triangle_fourier(5, x) for x in t]
    plt.plot(t, y, 'b-')

    plt.title("Triangle Wave Fourier Series \n Highest Order N = 5")
    plt.legend()
    plt.show()

    y = [triangle_fourier(10, x) for x in t]
    plt.plot(t, y, 'g-')

    plt.title("Triangle Wave Fourier Series \n Highest Order N = 10")
    plt.legend()
    plt.show()

    y = [triangle_fourier(100, x) for x in t]
    plt.plot(t, y, 'c-')

    plt.title("Triangle Wave Fourier Series \n Highest Order N = 100")
    plt.legend()
    plt.show()

    y = [triangle_fourier(1000, x) for x in t]
    plt.plot(t, y, 'm-')

    plt.title("Triangle Wave Fourier Series \n Highest Order N = 1000")
    plt.legend()
    plt.show()

    y_true = np.array([1-2*np.abs(i) for i in t])
    rms = [triangle_rms(i, y_true) for i in range(1, 100)]

    plt.plot(range(1, 100), rms, '-')
    plt.title("RMS Error for Fourier Series with Highest Order N")

    plt.show()