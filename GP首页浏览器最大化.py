#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

print("浏览器最大化")
driver.maximize_window()

driver.find_element_by_id("u1").find_element_by_name("tj_login").click()

div=driver.find_element_by_class_name("tang-content").find_element_by_name("userName").send_keys("121488054@qq.com")

driver.find_element_by_name("password").send_keys("mima123456")

driver.find_element_by_id("TANGRAM__PSP_8__submit").click()
time.sleep(5)
driver.quit()
