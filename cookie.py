#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://zhidao.baidu.com")

#print("浏览器最大化")
#driver.maximize_window()

cookie=driver.get_cookies()

print(cookie)

driver.add_cookie({'name':'key-aaaaaa','value':'value-bbbb'})

for cookie in driver.get_cookies():
    print ("%s-> %s"%(cookie['name'],cookie['value']))
time.sleep(2)
driver.delete_cookie("CookieName")
print(cookie)
time.sleep(2)
driver.delete_all_cookies()
print(cookie)

time.sleep(2)
#获得当前窗口
"""
nowhandle=driver.current_window_handle


#打开注册新窗口
driver.find_element_by_link_text("知道栏目").click()
driver.find_element_by_link_text("真相问答机").click()
#获得所有窗口
allhandles=driver.window_handles

#循环判断窗口是否为当前窗口
for handle in allhandles:
    if handle != nowhandle:
        driver.switch_to_window(handle)

        print("now register window!")
        driver.find_element_by_id("kw").send_keys("苹果")
        driver.find_element_by_id("search-btn").click()

        js="var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js)
        time.sleep(5)
        js="var q=document.documentElement.scrollTop=0"
        driver.execute_script(js)
        time.sleep(5)
   
driver.switch_to_window(nowhandle)
driver.find_element_by_id("kw").send_keys("苹果")
driver.find_element_by_id("search-btn").click()
time.sleep(5)

js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(5)
js="var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
time.sleep(5)
"""
driver.quit()
