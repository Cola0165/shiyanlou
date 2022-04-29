import csv


def dump_list(file, list):
    with open(file, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in list:
            spamwriter.writerow(row)


def load_list(file):
    with open(file, 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            yield row


if __name__ == "__main__":
    rows = [
        ['Spam'] * 5 + ['Baked Beans'],
        ['Spam', 'Lovely Spam', 'Wonderful Spam']
    ]

    list_file = '/tmp/list.csv'
    dump_list(list_file, rows)
    rows = load_list(list_file)
    for row in rows:
        for cell in row:
            print(cell)