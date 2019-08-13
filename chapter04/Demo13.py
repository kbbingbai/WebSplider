#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/12 17:23
# @Author :zhai shuai
"""
 作用
    一：selenium的行为链
 难点
    
 注意点
    
"""
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

driver_path = r'D:\Software\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com")

input = driver.find_element_by_id("kw")
btn = driver.find_element_by_id("su")

actionchain = ActionChains(driver)
actionchain.move_to_element(input)
actionchain.send_keys_to_element(input,'python')
actionchain.move_to_element(btn)
actionchain.click(btn)
actionchain.perform()

