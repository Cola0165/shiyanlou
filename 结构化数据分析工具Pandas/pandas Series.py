import pandas as pd
import math

if __name__ == '__main__':
    d = {}
    count = 1000
    step = 3.14/1000
    index = []
    for i in range(0, count):
        x = i*step
        y = math.cos(x)
        index.append(x)
        d[x] = y

    ser = pd.Series(data=d, index=index, dtype=float)
    print(ser)