# -*- coding: UTF-8 -*-
from selectolax.parser import HTMLParser

def get_p(html):
    p_list = []
    for node in HTMLParser(html).css("p"):
        # TODO(You): 正确的提取代码
        p_list.append(node.text())
    return p_list

html = '''
    <html>
        <head>
            <title>这是一个简单的测试页面</title>
        </head>
        <body>
            <p class="item-0">body 元素的内容会显示在浏览器中。</p>
            <p class="item-1">title 元素的内容会显示在浏览器的标题栏中。</p>
        </body>
    </html>
    '''

print(get_p(html))