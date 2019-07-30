#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/7/28 17:46
# @Author :zhai shuai
"""
 作用
    一：requests的使用，主要是理解 resp.text(经过解码后的数据，但是解码的字符集有可能不对，造成乱码) 与 resp.content(没有经过解码后的数据)
 难点
    
 注意点
    
"""
import requests

resp = requests.get("http://www.baidu.com")
print(resp.text)#解码后的数据
print(resp.content) #没有解码的数据，就是编码后的字符串，它的类型是<class 'bytes'>,它可以直接存储在硬盘当中或者直接在网络中传输的
print(resp.content.decode("utf-8")) #进行解码
print(resp.encoding)#ISO-8859-1