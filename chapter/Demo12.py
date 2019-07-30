#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/7/30 8:42
# @Author :zhai shuai
"""
 作用
    一：requests的cookie,这里返回的cookie信息好像不完全
 难点
    
 注意点
    
"""
import requests


url = "http://www.baidu.com"
resp = requests.get(url)
print(resp.cookies.get_dict()) #{'BDORZ': '27315'}