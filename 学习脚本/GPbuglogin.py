#coding = utf-8
from selenium import webdriver
import time

browser = webdriver.Firefox()

first_url="http://192.168.0.250/"

print ("now access %s"%(first_url))
browser.get(first_url)
time.sleep(2)
print ("浏览器最大化")
browser.maximize_window()


browser.find_element_by_id("zentao").click()
browser.find_element_by_id("account").send_keys("liuhuanan")
browser.find_element_by_name("password").send_keys("123456")
browser.find_element_by_id("submit").click()

time.sleep(3)

browser.quit()

