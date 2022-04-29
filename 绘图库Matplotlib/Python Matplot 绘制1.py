import numpy as np
import matplotlib.pyplot as plt


def sum(m, n, s):
    if n < 1:
        plt.show()
        return
    X = np.linspace(-s*np.pi, s*np.pi, m, endpoint=True)
    C, S = np.cos(X), np.sin(X)
    for i in range(1, n+1):
        Cn, Sn = i*np.cos(X/i), i*np.sin(X/i)
        C += Cn
        S += Sn

    return X, C+S


if __name__ == '__main__':
    X, Y = sum(256, 10, 10)
    plt.plot(X, Y)

    X, Y = sum(256, 20, 10)
    plt.plot(X, Y)

    plt.show()