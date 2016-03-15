# coding = utf-8
from selenium import webdriver
import time
browser = webdriver.Firefox()

browser.get("http://www.baidu.com")
time.sleep(0.3)
browser.find_element_by_id("kw").send_keys("selemium")
browser.find_element_by_id("su").click()

time.sleep(2)
browser.quit()
