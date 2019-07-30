#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/7/28 13:26
# @Author :zhai shuai
"""
 作用
    一：urllib--request--proxyHandler   代理
 难点
    
 注意点
    
"""

from urllib import request

#没有使用代理的方式，运行结果 ： {"origin": "60.208.82.10, 60.208.82.10"}
url = 'http://httpbin.org/ip'
# resp = request.urlopen(url)
# print(resp.read().decode())

#使用代理的方式
# 1 使用ProxyHandler 创建一个handler ,传入代理（字典）
handler = request.ProxyHandler({"http":"125.123.120.68:9000"})
# 使用handler 创建一个opener
opener = request.build_opener(handler)
resp = opener.open(url)
print(resp.read())
