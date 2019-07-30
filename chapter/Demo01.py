#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/7/28 11:17
# @Author :zhai shuai
"""
 作用
    一：测试python3自带的urllib-- request--urlopen
    二 urlopen 还可以有其它的参数 如 data,如果设置了data就变成post请求,
        urlopen返回的是一个http.client.HTTPResponse对象，它还有其它的方法，看官网
 难点
    
 注意点
    一 需要对返回的数据进行解码 resp.read().decode()

    
"""

from urllib import request

resp = request.urlopen("https://www.baidu.com")
print(resp.read().decode())
print(resp.getheaders())
print(resp.msg)