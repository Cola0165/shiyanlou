import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt


def easy_inter(x, y, sample_count, kind):
    f = None
    if kind == 'linear':
        f = interpolate.interp1d(x, y, kind='linear')
    elif kind == 'cubic':
        f = interpolate.interp1d(x, y, kind='cubic')
    elif kind == 'spline':
        f = interpolate.UnivariateSpline(x, y)
    else:
        return None

    x = np.linspace(x.min(), x.max(), sample_count)
    y = f(x)
    return x, y


if __name__ == "__main__":
    x = np.linspace(-12, 12, 10)
    y = np.cos(x)+np.sin(x)
    plt.plot(x, y, 'o')

    x, y = easy_inter(x, y, 20, "linear")
    plt.plot(x, y, '-')

    x, y = easy_inter(x, y, 20, "cubic")
    plt.plot(x, y, '--')

    x, y = easy_inter(x, y, 20, "spline")
    plt.plot(x, y, ':')

    plt.show()