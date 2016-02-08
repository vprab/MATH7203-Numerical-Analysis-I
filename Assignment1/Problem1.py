__author__ = 'Sree Vishant Prabhakaran'
import numpy as np


def my_tanh(x):
    ex = np.exp(x)
    e_minusx = np.exp(-x)

    return (ex - e_minusx)/(ex + e_minusx)

if __name__ == "__main__":
    for x in [10 ** i for i in xrange(-10, 11)]:
        if np.abs(my_tanh(x) - np.tanh(x)) > np.spacing(1):
            raise Exception("Error for x = %.64f too high" % x)

    print "All tests passed!"

    err = (my_tanh(1e-10) - np.tanh(1e-10))/np.tanh(1e-10)
    print "Relative Error for x = 1e-10:", err