
#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/7/28 16:51
# @Author :zhai shuai
"""
 作用
    一：cookie信息的保存到文件中,并可以实现把文件当中的cookie加载进来
 难点
    
 注意点
    
"""
from urllib import request
from http.cookiejar import MozillaCookieJar

#------------------把cookie信息保存到文件当中---------------
url = 'http://httpbin.org/cookies/set?a=A&b=B'
cookiejar = MozillaCookieJar("./files/cookieinfo.txt")#保存到文件当中
cookiejar.load(ignore_discard=True) #从文件中把cookie信息加载到内存

handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}

req = request.Request(url=url,headers=header)
resp = opener.open(req)
cookiejar.save(ignore_discard=True)

#------------------从文件当中把cookie加载到cookie对象当中---------------
cookiejar = MozillaCookieJar("./files/cookieinfo.txt")#保存到文件当中
cookiejar.load(ignore_discard=True)
for temp in cookiejar:
    print(temp)
