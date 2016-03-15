# coding = utf-8
from selenium import webdriver
import time
browser = webdriver.Firefox()

browser.get("http://www.baidu.com")
browser.implicitly_wait(100)
browser.find_element_by_id("kw").send_keys("selemium")
browser.find_element_by_id("su").click()


browser.quit()
