#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/12 15:49
# @Author :zhai shuai
"""
 作用
    一： driver.close() 关闭当前窗口  driver.quit() 关闭全部窗口
 难点
    
 注意点
    
"""

from selenium import webdriver
import time

driver_path = r'D:\Software\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com")

time.sleep(10)

driver.close()


