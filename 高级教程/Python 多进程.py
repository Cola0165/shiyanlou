from multiprocessing import Process


def fact(n):
    sum = 1
    for i in range(0, n):
        sum *= (i+1)
    print(sum)


if __name__ == '__main__':
    process_list = []
    for i in range(5):
        p = Process(target=fact, args=(10+i,))
        p.start()
        process_list.append(p)

    for i in process_list:
        p.join()