#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/7/30 8:47
# @Author :zhai shuai
"""
 作用
    一：requests的session，

 难点
    
 注意点
    
"""
import requests

url_login = 'http://www.renren.com/PLogin.do' #登陆页面
url_main = 'http://www.renren.com/971667441/profile' #登陆后的个人主页
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}
data = {
    "email":"15269106322",
    "password":"binghai2012"
}

sess = requests.session()
sess.post(url_login,data=data,headers=header)#进行登陆，登陆后，就有相应的cookie信息了，cookie信息保存在了session中,以后的访问共享cookie信息

resp = sess.get(url_main)

with open("./files/demo13.html","w",encoding="utf-8") as fp:
    fp.write(resp.content.decode("utf-8"))