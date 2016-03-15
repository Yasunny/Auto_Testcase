#coding = utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()

first_url="http://wp.163.com/filehub/login.jsp"
driver.get(first_url)
time.sleep(5)
nowhandle=driver.current_window_handle


driver.find_element_by_xpath("//input[@id='userName']").send_keys("is_pan@yeah.net")

driver.find_element_by_id("password").send_keys("fendou520")

driver.find_element_by_id("submit").click()

time.sleep(10)
'''driver.find_element_by_id("TANGRAM__PSP_23__closeBtn").click()

time.sleep(5)
driver.find_element_by_id("_disk_id_12").click()'''


driver.find_element_by_class_name("pFile-uploadBtn-moniter").click()
#send_keys("C:\\Users\Administrator\Desktop\图片\问问.jpg")

time.sleep(5)


