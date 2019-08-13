#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/12 11:18
# @Author :zhai shuai
"""
 作用
    一：使用常规的方式来下载 斗图啦 http://www.doutula.com/photo/list
 难点
    
 注意点
    
"""
import requests
from lxml import etree
from urllib import request
import os
import re

def parse_page(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        "Upgrade-Insecure-Requests": "1",
        "Host": "www.doutula.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    }

    resp = requests.get(url,headers=headers)

    html = etree.HTML(resp.text)
    images = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
    for x in images:
        single_img_url = x.xpath("./@data-original")[0]
        single_img_suffix = os.path.splitext(single_img_url)[1]
        single_img_alt = x.xpath("./@alt")[0]
        single_img_alt = re.sub(r'[\\/L:?"><]',"",single_img_alt)
        filename = single_img_alt + single_img_suffix
        #保存图片到文件中
        request.urlretrieve(single_img_url,"D:/webcrawler/2019-08-08/"+filename)

if __name__ == '__main__':
    for x in range(1,101):
        url = "http://www.doutula.com/photo/list/?page=%d"%x
        print(url)
        parse_page(url)



