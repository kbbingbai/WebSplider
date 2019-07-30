#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/7/28 15:13
# @Author :zhai shuai
"""
 作用
    一 使用cookiejar我形式，进行cookie信息的自动的保存
 难点
    
 注意点
    
"""
from http.cookiejar import CookieJar
from urllib import request,parse
url_login = 'http://www.renren.com/PLogin.do' #登陆页面
url_main = 'http://www.renren.com/971667441/profile' #登陆后的个人主页
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}
data = {
    "email":"15269106322",
    "password":"binghai2012"
}

#1.1 创建一个cookiejar对象
cookieJar = CookieJar()
#1.2 使用cookiejar对象 得到一个handler
handler = request.HTTPCookieProcessor(cookieJar)
#1.3 使用handler得到一个opener
opener = request.build_opener(handler)
#利用这个opener来进行登陆的操作
req = request.Request(url_login,data=parse.urlencode(data).encode("utf-8"),headers=header)
opener.open(req)


# 下面去访问个人主页
# 获取个人主页的页面的时候，不要新建一个opener,而应使用之前的那个opener,因为之前 的那个已经包含了
# cookie信息

req = request.Request(url_main,headers=header)
resp = opener.open(req)
with open("./files/demo08.html","w",encoding="utf-8") as ft:
    ft.write(resp.read().decode("utf-8"))





