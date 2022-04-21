# -*- coding: UTF-8 -*-
from requests_html import HTMLSession

def get_url(url):
    session = HTMLSession()
    r = session.get(url)
    # TODO(You): 正确的提取代码
    urls = r.html.links
    return urls

print(get_url("https://www.baidu.com/"))