__author__ = 'Sree Vishant Prabhakaran'
import numpy as np
import matplotlib.pyplot as plt


def compute_stresses(weight, theta):
    c, s = np.cos(theta*np.pi/180), np.sin(theta*np.pi/180)

    force_matrix = np.matrix([[0, 0, c, 0, 0, 0, 1, 0, 0, 0],
                              [0, 0, s, 0, 0, 0, 0, -1, 0, 0],
                              [-1, -c, 0, 0, 0, 0, 0, 0, -1, 0],
                              [0, -s, 0, 0, 0, 0, 0, 0, 0, 1],
                              [0, c, c, 0, 0, -c, 0, 0, 0, 0],
                              [0, s, -s, 1, 0, s, 0, 0, 0, 0],
                              [1, 0, 0, 0, -1, 0, 0, 0, 0, 0],
                              [0, 0, 0, -1, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 1, c, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, s, 0, 0, 0, 0]])

    w = np.matrix([[0, 0, 0, 0, 0, 0, 0, 0, 0, weight]]).transpose()

    return np.linalg.inv(force_matrix) * w

if __name__ == "__main__":
    t = np.arange(1, 90, 0.1)
    max_tension = []
    max_compression = []
    min_theta = np.inf

    for theta in t:
        stresses = compute_stresses(10, theta)
        max_tension.append(np.max(stresses))
        max_compression.append(np.abs(np.min(stresses)))

        if theta < min_theta and np.max(stresses) <= 15 and np.abs(np.min(stresses)) <= 25:
            min_theta = theta

    print "Minimum angle to support a 10 pound weight:", min_theta, "degrees"

    plt.plot(t, max_tension, 'r-', label="Max Tension")
    plt.plot(t, max_compression, 'b-', label="Max Compression")

    plt.legend()
    plt.show()