#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/12 17:57
# @Author :zhai shuai
"""
 作用
    一：selenium显示等待与隐式等待

    1 隐式等待 调用driver.implicitly_wait,那么在获取 不可用的元素之用，会先等待10秒的等待时间

    2 显示等待 显示等待是表明某个条件成立后才执行获取元素的操作，也可以在等待的时候指定一个最大的时间，如果超过这个时间那么就抛一个异常，
            显示等待应该使用selenium.webdriver.support.excepted_conditions 期望的条件
           和selenium.webdriver.support.ui.WebDriverWait来配合完成
 难点
    
 注意点
    
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1 显示等待
# driver_path = r'D:\Software\chromedriver\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get("https://www.baidu.com")
# driver.implicitly_wait(10)


# 2 显示等待

driver_path = r'D:\Software\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com")
try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"kw"))
    )
finally:
    driver.quit()