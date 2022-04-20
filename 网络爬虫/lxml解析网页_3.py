# -*- coding: UTF-8 -*-
from lxml import etree

def fetch_text(html):
    # TODO(You): 请在此实现代码
    html = etree.HTML(html)
    result = html.xpath("//p[@class='item-1']/text()")
    return result

if __name__ == '__main__':
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
    imgs = fetch_text(html)
    print(imgs)