# -*- coding: UTF-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        # TODO(You): 请正确实现浏览器自动化测试需求
        driver = self.driver
        driver.get("https://www.csdn.net/")
        self.assertIn("CSDN", driver.title)

        elem = driver.find_element_by_id("toolbar-search-input")
        elem.send_keys("OpenCV 技能树")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        time.sleep(10)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()