#coding = utf-8
from selenium import webdriver
import time

browser = webdriver.Firefox()

first_url="http://www.baidu.com"

print ("now access %s"%(first_url))
browser.get(first_url)
time.sleep(2)
second_url="http://www.baike.baidu.com"

print ("now access %s"%(second_url))
browser.get(second_url)
time.sleep(2)

print("back to %s"%(first_url))
broswer.back()

print("back to %s"%(second_url))
broswer.forward()

print ("浏览器最大化")
browser.maximize_window()
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(3)

browser.quit()
