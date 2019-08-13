#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/12 17:41
# @Author :zhai shuai
"""
 作用
    一：selenium 当中的cookie信息的处理
 难点
    
 注意点
    
"""

from selenium import webdriver

driver_path = r'D:\Software\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com")

cookies = driver.get_cookies()
# 1 得到所有的cookie
for cookie in cookies:
    print(cookie)

# 2 按名称得到cookie
print("=================")
print(driver.get_cookie("BD_UPN"))
print("=================")


# 3 删除某个cookie
driver.delete_cookie("PSTM")

# 删除一个cookie信息后，再打印就没有cookie 得到所有的cookie
for cookie in driver.get_cookies():
    print(cookie)

# 4 删除所有的cookie信息
driver.delete_all_cookies()