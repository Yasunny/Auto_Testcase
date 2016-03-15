#coding = utf-8
from selenium import webdriver
import time

browser = webdriver.Firefox()

browser.get("http://www.baidu.com")

print ("浏览器最大化")
browser.maximize_window()
time.sleep(2)

print (browser.title)

browser.quit()
