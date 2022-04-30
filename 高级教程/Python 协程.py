import os
import hashlib
import requests
import asyncio


def url_file_name(url):
    ext = os.path.splitext(url)[-1]
    hash_name = hashlib.md5(url.encode('utf-8')).hexdigest()
    return hash_name+ext


async def download_img(img_url):
    img_bytes = requests.get(img_url).content
    file_name = url_file_name(img_url)
    output = f'/tmp/{file_name}'
    with open(output, 'wb') as f:
        f.write(img_bytes)
    print(f'img downloaed at: {output}')
    await asyncio.sleep(1)


def test():
    urls = [
        "https://img-ask.csdnimg.cn/upload/1623844642974.jpg",
        "https://img-ask.csdnimg.cn/upload/1623844642974.jpg",
        "https://img-mid.csdnimg.cn/release/static/image/mid/ask/754909759626128.jpg",
        "https://img-ask.csdn.net/upload/201510/22/1445491909_384819.jpg",
    ]

    tasks = [download_img(url) for url in urls]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == '__main__':
    test()