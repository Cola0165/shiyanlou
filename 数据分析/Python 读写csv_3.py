import pandas as pd


def dump_to_csv(file, table):
    df = pd.DataFrame(data=table)
    df.to_csv(file, encoding='utf_8_sig')


def load_from_csv(file):
    return pd.read_csv(
        file, encoding='utf_8_sig',
        index_col=[0],
        lineterminator="\n"
    )


if __name__ == "__main__":

    table = {
        "name": ["Alice", "Bob"],
        "age": [18, 20]
    }

    dump_to_csv('/tmp/panda_csv.csv', table)

    ret = load_from_csv('/tmp/panda_csv.csv')
    print(ret.head())