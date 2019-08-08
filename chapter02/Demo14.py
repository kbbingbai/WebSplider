#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/6 13:18
# @Author :zhai shuai
"""
 作用
    一：古诗文的匹配 https://www.gushiwen.org
 难点
    
 注意点
    
"""
import requests,re

def url_parse():
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
    }
    url = "https://www.gushiwen.org/index.aspx"
    response = requests.get(url,header)
    text = response.text

    titleReg = r'<div\sclass="cont">.*?<b>(.*?)</b>'
    title = re.findall(titleReg,text,re.DOTALL)

    chaodaiReg = r'<p\sclass="source">.*?<a\s.*?>(.*?)</a>'
    chaodai = re.findall(chaodaiReg, text, re.DOTALL)

    authorReg = r'<p\sclass="source">.*?<a\s.*?>.*?</a>.*?<a\s.*?>(.*?)</a>'
    author = re.findall(authorReg, text, re.DOTALL)

    contentReg = r'<div class="contson" .*?>(.*?)</div>'
    content = re.findall(contentReg, text, re.DOTALL)

    reg = r'<.*?>'
    print(title)
    print(chaodai)
    print(author)
    for temp in content:
        x = re.sub(reg,"",temp)
        print(x)

def main():
    url_parse()

if __name__ == "__main__":
    main()