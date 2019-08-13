#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/13 12:50
# @Author :zhai shuai
"""
 作用
    一：WebElement 继承 object
    二：WebDriver 继承 WebDriver
 难点
    
 注意点
    
"""

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver




driver_path = r'D:\Software\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

# 1 注意下面的方式和二个页面会把第一个页面给替换掉
driver.get("https://www.baidu.com")

print(type(driver))

inputTag = driver.find_element_by_id("kw")
print(type(inputTag)) # <class 'selenium.webdriver.remote.webelement.WebElement'>