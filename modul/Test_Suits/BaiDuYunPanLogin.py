

#coding=utf-8
import unittest
import time
#import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class BaiDuYunPan(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login(self):
        driver = self.driver
        driver.get("http://pan.baidu.com/")
        elem = driver.find_element_by_xpath("//input[@id='TANGRAM__PSP_4__userName'][@name='userName']")
        elem.send_keys("121488054@qq.com")
        elem = driver.find_element_by_id("TANGRAM__PSP_4__password")
        elem.send_keys("mima123456")
        elem.send_keys(Keys.RETURN)


        time.sleep(5)
        #self.assertIn("登录成功", driver.page_title)
        elem = driver.find_element_by_id("TANGRAM__PSP_23__closeBtn")
        elem.click()
        #driver.find_element_by_id("TANGRAM__PSP_23__closeBtn").click()

        time.sleep(5)
        assert "No results found." not in driver.page_source
        #driver.find_element_by_id("_disk_id_12").click()
        #time.sleep(5)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

'''    testunit=unittest.TestSuite()

    testunit.addTest(TestCase1("test_search_python_org"))
    testunit.addTest(TestCase1("test_python_window"))


filename='F:\\selenium_python\\report\\report.html'
fp=open(filename,"wb")

runner=HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'python search report',
    description=u'testcase relation')

runner.run(testunit)'''''





