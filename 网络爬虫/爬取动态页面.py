# -*- coding: UTF-8 -*-
import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get(url)
Thread.sleep(1000)

page_size = 10
for i in range(page_size):
    time.sleep(2)
    js = "var q=document.documentElement.scrollTop=10000"
    driver.execute_script(js)

page = BeautifulSoup(driver.page_source, 'lxml')
print(page.text)