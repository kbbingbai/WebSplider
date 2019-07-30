#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/7/28 12:04
# @Author :zhai shuai
"""
 作用
    一：urllib--parse--urlparse(urlstring) 对url各个部分进行分隔
 难点
    
 注意点
    一 注意urlparse 与urlsplit的不同点，urlsplit没有urlsplit

 运行的结果
    ParseResult(
        scheme='https',
        netloc='dl.dropboxusercontent.com',
        path='/u/95587456/Evenimente/1.jpg',
        urlsplit='hello',
        query='name=zs&age=11',
        fragment='a'
    )

    SplitResult(
        scheme='https',
        netloc='dl.dropboxusercontent.com',
        path='/u/95587456/Evenimente/1.jpg;hello',
        query='name=zs&age=11',
        fragment='a'
     )

"""


from urllib import parse
url = "https://dl.dropboxusercontent.com/u/95587456/Evenimente/1.jpg;hello?name=zs&age=11#a"
par = parse.urlparse(url)
print(par)

parse1 = parse.urlsplit(url)
print(parse1)
