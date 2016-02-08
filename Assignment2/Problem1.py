__author__ = 'Sree Vishant Prabhakaran'
import numpy as np
import matplotlib.pyplot as plt


def trailing_average(t, x, N):
    return t[N-1:], [np.float(sum(x[i:i+N]))/N for i in range(0, len(x)-N+1)]

if __name__ == "__main__":
    t = np.arange(0, 2, 0.01)
    y = np.sin(2*np.pi*t) + 0.1*np.random.randn(len(t))

    plt.plot(t, y, 'ro', label="Noisy Sine Wave")
    tf, yf = trailing_average(t, y, 3)
    plt.plot(tf, yf, 'bo', label="Filtered Sine Wave (N=3)")

    plt.legend()
    plt.show()

    plt.plot(t, y, 'ro', label="Noisy Sine Wave")
    tf, yf = trailing_average(t, y, 7)
    plt.plot(tf, yf, 'bo', label="Filtered Sine Wave (N=7)")

    plt.legend()
    plt.show()

    plt.plot(t, y, 'ro', label="Noisy Sine Wave")
    tf, yf = trailing_average(t, y, 11)
    plt.plot(tf, yf, 'bo', label="Filtered Sine Wave (N=11)")

    plt.legend()
    plt.show()


