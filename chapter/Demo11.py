#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/7/30 8:34
# @Author :zhai shuai
"""
 作用
    一：requests代理
 难点
    
 注意点
    
"""

import requests
proxy = {
    "http":"117.90.5.62:9000"
}

resp = requests.get("http://httpbin.org/ip",proxies=proxy)
print(resp.text)