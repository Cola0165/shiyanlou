import pandas as pd

if __name__ == '__main__':
    d = {
        'name': ['Alice', 'Bob', 'Middle'],
        'age': [10, 12, 0],
        'send': ['在么', '你说呢？', '今晚有事']
    }

    df = pd.DataFrame(d, columns=['name', 'age', 'send'])

    print("取出name不等于‘Middle'的数据")
    alice_bob = df.loc[df['name'] != 'Middle']
    print(alice_bob)