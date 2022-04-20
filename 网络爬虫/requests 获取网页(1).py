# -*- coding: UTF-8 -*-
import requests

def get_html(url):
    # TODO(You): 请在此实现代码
    response = requests.get(url=url)
    result = response.text
    return result

if __name__ == '__main__':
    url = "http://www.baidu.com"
    html = get_html(url)
    print(html)