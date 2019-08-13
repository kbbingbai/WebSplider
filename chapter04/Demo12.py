#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/12 16:14
# @Author :zhai shuai
"""
 作用
    一：selenium常用的操作表单元素
 难点
    
 注意点
    
"""
from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time

driver_path = r'D:\Software\chromedriver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://docs.python.org/zh-cn/3.7/index.html")


# 1 操作 input标签

# inputTag = driver.find_element_by_id("kw")
# inputTag.send_keys("python")
# time.sleep(5)
# inputTag.clear()

# 2 操作checkbox标签
# remeber = driver.find_element_by_name('remember')
# remeber.click()

# 3 操作select标签
select = Select(driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]/span[2]/select"))
select.select_by_index(2)
select.select_by_value("3.7")
select.select_by_visible_text("xx")

