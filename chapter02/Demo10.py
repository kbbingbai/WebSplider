#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/6 7:52
# @Author :zhai shuai
"""
 作用
    一：
        这一讲主要讲的是分组

        1 match 在字符串中找满足条件的字符，如果找到，就返回，只会找第一个满足条件的
        2 search 在全文中查找，且只会找到第一个满足条件的
        3 分组 在正则表达式中，可以对过滤的字符串进行分组，分组使用员括号的方式
            （1） group:和group(0) 是等价的，返回的是整个满足条件的字符串
            （2）groups 返回的是元组的，索引从1开始
            （3） group(1) 返回的是第一个子组，可以传入多个_
 难点
    
 注意点

 运行的结果：
    # apple price is $889,orange price is $22
    # apple price is $889,orange price is $22
    # $889
    # $22
    # ('$889', '$22')
    
"""
import re

text = "apple price is $889,orange price is $22"
reg = re.search(r".*(\$\d+).*(\$\d+)",text)
print(reg.group())
print(reg.group(0))
print(reg.group(1))
print(reg.group(2))
print(reg.groups())


