import pandas as pd

if __name__ == '__main__':
    index = pd.Index(range(1, 10))
    d = {}
    for i in range(1, 10):
        columns = []
        for j in range(1, 10):
            if j < i:
                columns.append('')
            else:
                columns.append(f"{i} x {j} = {i*j}")
        d[f'{i}'] = columns

    df = pd.DataFrame(index=index, data=d)
    print(df.head(9))