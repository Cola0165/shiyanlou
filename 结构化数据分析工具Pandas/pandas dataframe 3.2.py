import pandas as pd


def test():
    d = [
        ['Alice', 'Bob', 'Middle'],
        [10, 12, 0],
        ['在么', '你说呢？', '今晚有事']
    ]

    df = pd.DataFrame(d)
    for i in range(0, len(d)):
        row = df.iloc[i][:2]
        print(row)
        print('')


if __name__ == '__main__':
    test()