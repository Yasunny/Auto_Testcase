#coding=utf-8
import unittest
from selenium import webdriver
class maximize_window(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_maximize_window(self):
        driver = self.driver
        driver.get("http://www.baidu.com")
        self.assertIn('360',driver.title)
        driver.maximize_window()
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

