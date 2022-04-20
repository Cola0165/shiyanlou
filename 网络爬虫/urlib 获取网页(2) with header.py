# -*- coding: UTF-8 -*-
import urllib.request

def get_html(url, headers):
    # TODO(You): 请在此实现带头部信息的网页请求
    req = urllib.request.Request(url)
    for key in headers:
        req.add_header(key, headers[key])
    response = urllib.request.urlopen(req)
    buff = response.read()
    html = buff.decode("utf8")
    return html

if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
    }
    url = "http://www.baidu.com"
    html = get_html(url, headers)
    print(html)