import os
import hashlib
import requests


def download_img(url):
    img_bytes = requests.get(url).content

    ext = os.path.splitext(url)[-1]
    hash_name = hashlib.md5(url.encode('utf-8')).hexdigest()
    file_name = hash_name+ext

    output = f'/tmp/{file_name}'
    with open(output, 'wb') as f:
        f.write(img_bytes)
    print('[image] downnload image: {}'.format(output))


if __name__ == '__main__':
    urls = [
        "https://img-ask.csdnimg.cn/upload/1623844642974.jpg",
        "https://img-ask.csdnimg.cn/upload/1623844642974.jpg",
        "https://img-mid.csdnimg.cn/release/static/image/mid/ask/754909759626128.jpg",
        "https://img-ask.csdn.net/upload/201510/22/1445491909_384819.jpg",
    ]
    for url in urls:
        download_img(url)