#coding = utf-8
from selenium import webdriver
import time

browser = webdriver.Firefox()

first_url="http://117.176.128.179:9000/"

print ("now access %s"%(first_url))
browser.get(first_url)
time.sleep(2)
print ("浏览器最大化")
browser.maximize_window()

'''cookie=browser.get_cookies()

print(cookie)
for cookie in browser.get_cookies():
    print ("%s"%(cookie['name']))'''

browser.find_element_by_link_text("立即登录").click()

time.sleep(5)
browser.find_element_by_id("mobile").send_keys("15888869878")
browser.find_element_by_id("password").send_keys("mima123456")


time.sleep(20)
browser.find_element_by_class_name("btn-two").click()

time.sleep(5)
browser.find_element_by_css_selector("a[title=\"关闭\"]").click()


time.sleep(3)


