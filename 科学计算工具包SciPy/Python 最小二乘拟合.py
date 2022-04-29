import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt


def cubic_leastsq_by_np(x, y, sample_count):
    z = np.polyfit(x, y, 3)
    f = np.poly1d(z)

    x = np.linspace(x.min(), x.max(), sample_count)
    y = f(x)
    return x, y


def cubic_leastsq_by_scipy(x, y, sample_count):
    z = leastsq(
        lambda p, x, y: y - np.poly1d(p)(x),
        np.random.rand(3+1),
        args=(x, y)
    )[0]
    f = np.poly1d(z)

    x = np.linspace(x.min(), x.max(), sample_count)
    y = f(x)

    return x, y


if __name__ == "__main__":
    x = np.linspace(-3, 3, 10)
    y = np.cos(x)
    plt.plot(x, y, 'o')

    x1, y1 = cubic_leastsq_by_np(x, y, 20)
    plt.plot(x1, y1, '-')

    x2, y2 = cubic_leastsq_by_scipy(x, y, 20)
    plt.plot(x2, y2, '--')

    assert np.array_equal(x1, x2)
    assert np.array_equal(np.around(y1, decimals=2), np.around(y2, decimals=2))

    plt.show()