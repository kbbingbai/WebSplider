#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/13 11:03
# @Author :zhai shuai
"""
 作用
    一：页面切换，使用javascript进行打开一个页面

    虽然在窗口中切换到了新的页面，但是driver中还没有切换，
    如果想要在代码中切换到新的页面，并且做一些爬虫
    那么应该使用driver.switch_to.window来切换到指定的窗口
    从driver.window_handlers中取出第几个窗口
    driver.window_handlers是一个窗口列表，里面装的都是窗口句柄。
    他们会按照打开页面的顺序来存储窗口的句柄

 难点
    
 注意点
    
"""

from selenium import webdriver

driver_path = r'D:\Software\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

# 1 注意下面的方式和二个页面会把第一个页面给替换掉
# driver.get("https://www.baidu.com")
# driver.get("https://www.doutula.com")

# 2 使用javascipt进行打开一个页面，注意第二个页面不会把第一个页面覆盖掉,但是driver.current_url 不是在第一个url
# driver.get("https://www.doutula.com")
# driver.execute_script("window.open('https://www.baidu.com')")
# print(driver.current_url)

# 3 切换window 窗口
driver.get("https://www.doutula.com")
driver.execute_script("window.open('https://www.baidu.com')")
driver.switch_to.window(driver.window_handles[1]) #这个是句柄 window_handles[] 是人0开始的
print(driver.current_url)



