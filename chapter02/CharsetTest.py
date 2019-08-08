#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/2 9:04
# @Author :zhai shuai
"""
 作用
    一：这一篇是讲字符集的
 难点
    
 注意点
    
"""

import requests
import chardet

req = requests.get("http://www.baidu.com")
print(req.encoding)

print(type(req.text))

print(type(req.content))

print(req.apparent_encoding)

print(chardet.detect(req.content))