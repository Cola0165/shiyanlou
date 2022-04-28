import pandas as pd
import numpy as np

# def add_val(num):
#     if num > 0:
#         return 1
#     else:
#         return 0

if __name__ == '__main__':
    data = {
        'cloumn_one': pd.Series(np.random.randint(-10, 10, size=5)),
        'cloumn_two': pd.Series(np.random.randint(0, 10, size=5)),
        'cloumn_three': pd.Series(np.random.randint(0, 10, size=5))
    }
    data_df = pd.DataFrame(data)

    def add_val(num):
        return 1 if num>0 else 0

    data_df['label_one'] = data['cloumn_one'].apply(add_val)
    # data_df['label_one'] = data['cloumn_one'].apply(lambda num: 1 if num>0 else 0)

    print(data_df)