import pandas as pd
import numpy as np


def test():
    s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
    t = pd.Series(np.random.randn(4), index=["a", "b", "c", "d"])
    for i in s.index:
        if t.get(i) is not None:
            print(f"配对 <{s[i]}, {t[i]}>")


if __name__ == '__main__':
    test()