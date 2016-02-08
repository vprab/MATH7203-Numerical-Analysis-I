__author__ = 'Sree Vishant Prabhakaran'
import numpy as np
import matplotlib.pyplot as plt


def my_arctanh(x):
    ans = 0
    den = 1
    val = x
    next_val = val/np.float(den)
    iterations = 0

    while np.abs(next_val) >= 1e-9:
        ans += next_val
        den += 2
        val *= x*x
        next_val = val/np.float(den)
        iterations += 1

    return iterations


def my_arctanh_cf(x):
    x_sqr = x*x

    a = x
    b = 1

    Ajm2 = 1
    Bjm2 = 0
    Ajm1 = 0
    Bjm1 = 1

    ynm1 = 0
    tol = 1e-9

    iterations = 0
    for j in range(1, 500):
        Aj = b*Ajm1 + a*Ajm2
        Bj = b*Bjm1 + a*Bjm2
        yn = Aj/Bj

        iterations += 1

        if np.abs(yn - ynm1) < tol:
            break

        a = -j*j*x_sqr
        b += 2

        ynm1 = yn

        Ajm2 = Ajm1
        Bjm2 = Bjm1
        Ajm1 = Aj
        Bjm1 = Bj

        if j is 499:
            raise Exception("Failed to converge")

    return iterations

if __name__ == "__main__":
    x = np.arange(-0.95, 0.96, 0.01)
    power_series = [my_arctanh(i) for i in x]
    cont_frac = [my_arctanh_cf(i) for i in x]

    plt.plot(x, power_series, 'ro', label="Series Expansion")
    plt.plot(x, cont_frac, 'bo', label="Continued Fraction")
    plt.legend()
    plt.show()


