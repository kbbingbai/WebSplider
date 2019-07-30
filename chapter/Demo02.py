#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/7/28 11:31
# @Author :zhai shuai
"""
 作用
    一：测试 urllib -- request.urlretrieve() 可以把请求的数据，保存到一个文件当中去
 难点
    
 注意点
    
"""
from urllib import request
resp = request.urlretrieve("http://www.baidu.com/","./files/demo02.html")
