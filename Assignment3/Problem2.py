__author__ = 'Sree Vishant Prabhakaran'
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    np_conds = []
    comp_conds = []
    t = np.arange(-100, 100)

    for x in t:
        A = np.matrix([[2, 1+x],[1+x, 2]])

        eigvals = np.linalg.eigvals(A)
        l_max = max(eigvals)
        l_min = min(eigvals)

        comp_conds.append(np.abs(l_max/l_min))
        np_conds.append(np.linalg.cond(A))

    plt.plot(t, np.log(comp_conds), 'r-', label="Computed Condition Numbers")
    plt.plot(t, np.log(np_conds), 'b-', label="NumPy Condition Numbers")
    plt.legend()
    plt.show()

