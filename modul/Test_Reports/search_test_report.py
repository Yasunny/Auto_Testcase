#coding=utf-8
import unittest
import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class TestCase1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source



    def test_python_window(self):
        driver = self.driver
        driver.get("http://www.baidu.com")
        self.assertIn('360',driver.title)
        driver.maximize_window()
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    testunit=unittest.TestSuite()

    testunit.addTest(TestCase1("test_search_python_org"))
    testunit.addTest(TestCase1("test_python_window"))


filename='F:\\selenium_python\\report\\report.html'
fp=open(filename,"wb")

runner=HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'python search report',
    description=u'testcase relation')

runner.run(testunit)
