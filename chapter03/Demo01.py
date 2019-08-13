#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/8 16:30
# @Author :zhai shuai
"""
 作用
    一 掌握json 当中的dumps(对象--串) dump(对象--文件)  loads(串--对象) load(文件--对象) 的作用
 难点
    
 注意点
    
"""

import json

data = [
    {
        "name":"张三",
        "age":22,
        "country":"chian"
    },
    {
        "name":"lishi",
        "age":22,
        "country":"caoxian"
    }
]

#把对象转成一个str
"""
输出的结果是：

<class 'str'>
[{"name": "张三", "age": 22, "country": "chian"}, {"name": "lishi", "age": 22, "country": "caoxian"}]
<class 'str'>
[{"name": "\u5f20\u4e09", "age": 22, "country": "chian"}, {"name": "lishi", "age": 22, "country": "caoxian"}]

"""
a = json.dumps(data,ensure_ascii=False)
ｂ = json.dumps(data)
print(type(a))
print(a)
print(type(ｂ))
print(ｂ)


#把对象写入文件
with open("./files/demo01.json","w",encoding="utf-8") as ft:
    json.dump(data,ft,ensure_ascii=False)

#字符串转成对象
json_str = '[{"title":"mytitle","name":"中国"},{"title":"mytitle","name2":"中国2"}]'
data = json.loads(json_str)
print(data)


#文件转成对象
with open("./files/demo01.json","r",encoding="utf-8") as ft:
    data = json.load(ft)
    print(data)