def test():
    installs = [
        "1. pip install matplotlib",
        "3. 还可以试试豆瓣的源：pip install matplotlib -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com",
        "2. 如果装不了，就试试阿里的源：pip install matplotlib -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com",
    ]

    installs.sort(key=lambda i: i[0])
    for step in installs:
        items = step.split("：")
        print(items[0])
        if len(items) > 1:
            for i in range(1, len(items)):
                print(f"  {items[i]}")


if __name__ == '__main__':
    test()