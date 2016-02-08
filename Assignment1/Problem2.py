__author__ = 'Sree Vishant Prabhakaran'
import numpy as np


def my_arctanh(x):
    ans = 0
    den = 1
    val = x
    next_val = val/np.float(den)

    while np.abs(next_val) >= 1e-9:
        ans += next_val
        den += 2
        val *= x*x
        next_val = val/np.float(den)

    return ans

if __name__ == "__main__":
    for x in np.arange(-0.95, 0.96, 0.01):
        if np.abs(my_arctanh(x) - np.arctanh(x)) > 1e-8:
            raise Exception("Error for x = %.64f too high" % x)

    print "All tests passed!"

