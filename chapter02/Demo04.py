#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/1 17:39
# @Author :zhai shuai
"""
 作用
    一：爬取电影天堂的数据
    二：注意第三页的数据还不能抓取，因为乱码的原因
 难点
    
 注意点
    
"""

from lxml import etree
import time

import requests
BASE_DOMAIN = "http://dytt8.net" #这是一个全局变量
BASE_DOMAIN2 = "https://www.ygdy8.net" #这是一个全局变量
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    "Host": "www.ygdy8.net",
    "Connection": "keep-alive",
    "Cookie": "XLA_CI=05c239951e131e569e6b0528767f3ca9; bz_finger=66c3e115c1195eadfb4b47ea9d84993f; cscpvrich5041_fidx=2"
}

def get_detail_urls(url):
    response = requests.get(url,headers=HEADERS)
    text = response.text
    html = etree.HTML(text)
    urls = html.xpath("//table[@class='tbspan']//tr[position()=2]//a/@href")
    urls = map(lambda url:BASE_DOMAIN2+url,urls)
    return urls

def parse_detail_page(url):
    movie = {}
    req = requests.get(url,headers=HEADERS)
    resp = req.content.decode("gbk")
    html = etree.HTML(resp)
    title = html.xpath("//div[@class='co_area2']//div[@class='title_all']//h1//text()")#电影标题
    movie["title"] = title
    imgs = html.xpath("//div[@id='Zoom']//img")
    if (len(imgs))==2:
        cover = imgs[0].xpath("./@src")#电影海报
        coverjietu = imgs[1].xpath("./@src")#电影视频截图
        movie["cover"] = cover
        movie["coverjietu"] = coverjietu
    elif (len(imgs))==1:
        cover = imgs[0].xpath("./@src")  # 电影海报
        movie["cover"] = cover

    content =  html.xpath("//div[@id='Zoom']//p//text()")

    def parcon(single,rule):
        """
            :param single: 单条数据的信息
            :param rule: 规则
            :return:
        """
        return single.replace(rule,"").strip()

    for index,single in enumerate(content):
       if single.startswith("◎译　　名"):
           yiming =parcon(single,"◎译　　名")
           movie["yiming"] = yiming
       elif single.startswith("◎年　　代"):
           nidai = parcon(single, "◎年　　代")
           movie["nidai"] = nidai
       elif single.startswith("◎主　　演"):#这个地方需要注意一下
           zhuyanList = []
           zhuyan = parcon(single, "◎主　　演")
           zhuyanList.append(zhuyan)
           for x in range(index+1,len(content)):
               zhuyan = content[x].strip()
               if zhuyan.startswith("◎"):
                   break
               zhuyanList.append(zhuyan)
           movie["zhuyan"] = zhuyanList
       elif single.startswith("◎简　　介"):#这个地方需要注意一下
           jianjieList = []
           jianjie = parcon(single, "◎简　　介")
           if jianjie:
               jianjieList.append(jianjie)
           for x in range(index+1,len(content)):
               jianjie = content[x].strip()
               if jianjie.startswith("【下载地址】"):
                   break
               if jianjie:
                   jianjieList.append(jianjie)
           movie["jianjie"] = jianjieList

    downloadurl = html.xpath("//div[@id='Zoom']//table//tr//td//a/@href")[0]
    movie["downloadurl"] = downloadurl
    return movie


def getTotalPage():
    url = "https://www.ygdy8.net/html/gndy/dyzz/index.html"
    mainPage = requests.get(url,headers = HEADERS)
    resp = mainPage.content.decode("gbk")
    html = etree.HTML(resp)
    totalPage = html.xpath("//div[@class='x']//option[last()]/text()")[0]
    return totalPage

def spider():
    totalPage =getTotalPage()
    base_url = "https://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html"
    for x in range(1,int(totalPage)+1):
        print("*"*20+str(x))
        if x != 3:
            url = base_url.format(x)
            movies = get_detail_urls(url)
            for detail_url in movies:
                detail_page = parse_detail_page(detail_url)
                with open("./files/Demo04.json","a",encoding="utf-8") as ft:
                    ft.writelines(str(detail_page))
                    ft.writelines("")

if __name__=="__main__":
    spider()