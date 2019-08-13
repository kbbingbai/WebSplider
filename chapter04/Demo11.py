#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/12 15:55
# @Author :zhai shuai
"""
 作用
    一：selenium的常用选择元素方法的使用

 难点
    
 注意点
    一： 如果只是想要 解析网页中的数据，那么推荐将网页源代码扔给lxml底层，因为lxml底层使用的是c语言，所以解析效率会更高

         如果是想要 对元素进行一些操作，比如给一个文本框输入值，或者是点击 某个按钮，那么就必须 使用selenium给我们提供的查找元素的方法
    
"""

from selenium import webdriver
driver_path = r'D:\Software\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com")

# inputTag = driver.find_element_by_id("kw")
# inputTag = driver.find_element_by_class_name("s_ipt")
# inputTag = driver.find_element_by_css_selector("input[class='s_ipt'][id='kw']")
# inputTag = driver.find_element_by_name("wd")
inputTag = driver.find_element_by_xpath('//*[@id="kw"]')

print(inputTag)
inputTag.send_keys("python")