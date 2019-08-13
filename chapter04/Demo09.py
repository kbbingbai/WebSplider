#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/12 15:43
# @Author :zhai shuai
"""
 作用
    一：selenium的使用,使用selenium打开谷歌浏览器
 难点
    
 注意点
    
"""

from selenium import webdriver

driver_path = r'D:\Software\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com")
print(driver.page_source)
