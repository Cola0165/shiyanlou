# -*- coding: UTF-8 -*-
from autoscraper import AutoScraper

def get_similar_result(url, wanted_list):
    scraper = AutoScraper()
    # TODO(You): 正确的提取代码
    result = scraper.build(url, wanted_list)
    return result

url = 'https://stackoverflow.com/search?q=autoscraper&s=7b5866da-920e-4926-8c33-09fb7d32886b'
wanted_list = ["AutoScraper module not found in Python Autoscraper library"]
print(get_similar_result(url, wanted_list))