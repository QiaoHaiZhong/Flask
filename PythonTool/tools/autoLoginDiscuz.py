#coding=utf-8
#!/usr/bin/env Python
from selenium import webdriver
import time

browser=webdriver.Firefox()

browser.get('http://bbs.pyshell.com')
time.sleep(3)
print 1
browser.find_element_by_xpath("//img[@class='vm']").click()
time.sleep(3)
browser.find_element_by_xpath("//span[@class='img_out_focus']").click()
#browser.find_element_by_xpath("//img[@class='face']").click()

#browser.find_element_by_css_selector("a.face").click()
print 2

time.sleep(10)
browser.quit()