__author__ = 'Sree Vishant Prabhakaran'
import numpy as np


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

    for j in range(1, 500):
        Aj = b*Ajm1 + a*Ajm2
        Bj = b*Bjm1 + a*Bjm2
        yn = Aj/Bj

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

    return yn

if __name__ == "__main__":
    for x in np.arange(-0.95, 0.96, 0.01):
        if np.abs(my_arctanh_cf(x) - np.arctanh(x)) > 1e-8:
            raise Exception("Error for x = %.64f too high" % x)

    print "All tests passed!"