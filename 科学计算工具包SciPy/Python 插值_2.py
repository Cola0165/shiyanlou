from scipy.interpolate import BSpline


def B(x, k, i, t):
    if k == 0:
        return 1.0 if t[i] <= x < t[i+1] else 0.0
    if t[i+k] == t[i]:
        c1 = 0.0
    else:
        c1 = (x - t[i])/(t[i+k] - t[i]) * B(x, k-1, i, t)
    if t[i+k+1] == t[i+1]:
        c2 = 0.0
    else:
        c2 = (t[i+k+1] - x)/(t[i+k+1] - t[i+1]) * B(x, k-1, i+1, t)
    return c1 + c2


def bspline(x, t, c, k):
    n = len(t) - k - 1
    assert (n >= k+1) and (len(c) >= n)
    return sum(c[i] * B(x, k, i, t) for i in range(n))


if __name__ == "__main__":
    k = 2
    t = [0, 1, 2, 3, 4, 5, 6]
    c = [-1, 2, 0, -1]

    ret1 = bspline(2.5, t, c, k)
    print("手工实现的B样条 bspline(2.5, t, c, k)",  ret1)

    spl = BSpline(t, c, k)
    ret2 = spl(2.5)
    print("SciPy的B样条 BSpline(t, c, k)(2.5)=", ret2)

    assert ret1 == ret2