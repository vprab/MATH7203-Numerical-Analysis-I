__author__ = 'Sree Vishant Prabhakaran'
import numpy as np


def min_hops(adj, s, g):
    n = np.copy(adj)

    count = 0
    while n[s, g] == 0:
        n = n * adj
        count += 1

        if count > np.shape(adj)[0]:
            return -1

    return count


def find_connections(adj, s, n):
    return np.sum((adj ** n)[s] > 0) - 1

if __name__ == "__main__":
    adj_matrix = np.matrix([[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                            [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                            [1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
                            [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                            [0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                            [0, 0, 0, 0, 0, 0, 1, 1, 0, 0]])

    assert (adj_matrix.transpose() == adj_matrix).all()

    print "Minimum number of people to contact from A to G (non-inclusive): ", min_hops(adj_matrix, 0, 6)
    print "Number of connections to person A within 4 hops: ", find_connections(adj_matrix, 0, 4)


