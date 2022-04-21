# -*- coding: UTF-8 -*-
from pyspider.libs.base_handler import *

class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self): 
        '''该函数是入口函数，pyspider 命令启动 run 之后会调用该入口函数'''
        self.crawl('http://scrapy.org/', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        '''该函数的 response 参数是一个 Response* 对象. 
        它通过了一组类似jQuery 的 API 用来查询和提取网页数据。
        '''
        for each in response.doc('a[href^="http"]').items():
            # 添加了一个爬虫任务到PySpider，
            # 回调函数调用了 self.index_page 成员方法
            self.crawl(each.attr.href, callback=self.detail_page)

    def detail_page(self, response):
        '''该函数返回一个字典对象. 返回值会被 resultdb 捕获. '''
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }