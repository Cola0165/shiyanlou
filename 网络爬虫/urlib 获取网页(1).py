# -*- coding: UTF-8 -*-
import urllib.request

def get_html(url):
    # TODO(You): 请在此实现代码
    response = urllib.request.urlopen(url)
    buff = response.read()
    html = buff.decode("utf8")
    return html

if __name__ == '__main__':
    url = "http://www.baidu.com"
    html = get_html(url)
    print(html)