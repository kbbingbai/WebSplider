#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/7/28 14:38
# @Author :zhai shuai
"""
 作用
    一：cookie的使用，一些网站，如果不带cookie就不能访问，下面讲的是访问的时候，带上cookie信息
    二：这种方式是比较的粗暴的，它把cookie信息给写死了，Demo08 可以把cookie写活
 难点
    
 注意点
    
"""
from urllib import request

url = 'http://www.renren.com/971666141/newsfeed/photo' #个人主页，必须登陆才能看到
header = {
     "Referer": "https://www.lagou.com/jobs/list_python?px=default&city=%E5%8C%97%E4%BA%AC",
     "Cookie": "anonymid=jymlc04s-sczjki; depovince=SD; _r01_=1; JSESSIONID=abcUwA7UTxOxteiG7s3Ww; "
               "ick_login=88dfc8ad-d46e-4733-bbf7-68d30fd8643c; t=1d292504ebd1da841c56af61714f5f5a1; "
               "societyguester=1d292504ebd1da841c56af61714f5f5a1; id=971666141; xnsid=c8b3eb5a; "
               "ver=7.0; loginfrom=null; "
               "jebe_key=b2abb330-8254-4b9f-aff7-c13a20c7a2b0%7Cb9c8b45293e4a5d99cb25ec1eb1cf9bd%7C1564295830827%7C1%7C1564295832743; "
               "jebe_key=b2abb330-8254-4b9f-aff7-c13a20c7a2b0%7Cb9c8b45293e4a5d99cb25ec1eb1cf9bd%7C1564295830827%7C1%7C1564295832747; "
               "wp_fold=0; jebecookies=0a5f2990-49f6-499e-9c8e-dc30961b538e|||||"
}
req = request.Request(url = url,headers = header)
resp = request.urlopen(req)

with open("./files/demo07.html","w",encoding="utf-8") as fp:
    fp.write(resp.read().decode("utf-8"))

