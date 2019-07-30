#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/7/28 11:51
# @Author :zhai shuai
"""
 作用
    一：urllib--parse--urlencode(data) 对url进行编码
    二 urllib--parse--parse_qs 对url进行解码
 难点
    
 注意点

 执行的结果：
    name=%E5%A5%BD%E7%9A%84&age=100
    {'name': ['好的'], 'age': ['100']}

"""
from urllib import parse
data = {"name":"好的","age":100}
qs = parse.urlencode(data) #对url进行编码
print(qs)

data = parse.parse_qs(qs)
print(data)

