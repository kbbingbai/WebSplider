#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/4 10:55
# @Author :zhai shuai
"""
 作用
    一：中国天气网的抓取的数据
 难点
    
 注意点

    1 在抓取http://www.weather.com.cn/textFC/gat.shtml 这一页数据的时候，我们有一些问题，就是源代码当中的<table>没有闭合
        标签（查看网页源代码可以看出来），这时我们使用html5lib进行解析，它的容错性（补全性）较高
    
"""
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}

import requests
from bs4 import BeautifulSoup


def parse_page(url):
    req = requests.get(url,headers=HEADERS)
    text = req.content.decode("utf-8")
    soup = BeautifulSoup(text,"html5lib")
    singleDateInfo = soup.find("div",attrs={"class":"conMidtab"})
    singleDateTable = singleDateInfo.find_all("table")

    for table in singleDateTable:
        trs = table.find_all("tr")[2:]
        for temp in range (0,len(trs)):
            if temp == 0:
                tds = trs[temp].find_all("td")
                city = tds[1]
                city = list(city.stripped_strings)[0]
                b_tqxx = tds[2].get_text()
                flfx = tds[3]
                b_flfx_1 = list(flfx.stripped_strings)[0]
                b_flfx_2 = list(flfx.stripped_strings)[1]
                b_zgwd = tds[4].get_text()

                h_tqxx = tds[5].get_text()
                flfx = tds[6]
                h_flfx_1 = list(flfx.stripped_strings)[0]
                h_flfx_2 = list(flfx.stripped_strings)[1]
                h_zdqw = tds[7].get_text()
                with open("./files/Demo07.json","a",encoding="utf-8") as ft:
                    t = (city, b_tqxx, b_flfx_1, b_flfx_2, b_zgwd, h_tqxx, h_flfx_1, h_flfx_2, h_zdqw)
                    ft.write(str(list(t)))
                    ft.write("\n")

            else:
                tds = trs[temp].find_all("td")
                city = tds[0].get_text(strip=True)
                b_tqxx = tds[1].get_text()
                flfx = tds[2]
                b_flfx_1 = list(flfx.stripped_strings)[0]
                b_flfx_2 = list(flfx.stripped_strings)[1]
                b_zgwd = tds[3].get_text()

                h_tqxx = tds[4].get_text()
                flfx = tds[5]
                h_flfx_1 = list(flfx.stripped_strings)[0]
                h_flfx_2 = list(flfx.stripped_strings)[1]
                h_zdqw = tds[6].get_text()
                with open("./files/Demo07.json","a",encoding="utf-8") as ft:
                    t = (city,b_tqxx,b_flfx_1,b_flfx_2,b_zgwd,h_tqxx,h_flfx_1,h_flfx_2,h_zdqw)
                    ft.write(str(list(t)))
                    ft.write("\n")

def main():


    weather_list = [
                "http://www.weather.com.cn/textFC/hb.shtml",
                "http://www.weather.com.cn/textFC/db.shtml",
                "http://www.weather.com.cn/textFC/hd.shtml",
                "http://www.weather.com.cn/textFC/hz.shtml",
                "http://www.weather.com.cn/textFC/hn.shtml",
                "http://www.weather.com.cn/textFC/xb.shtml",
                "http://www.weather.com.cn/textFC/xn.shtml",
                "http://www.weather.com.cn/textFC/gat.shtml"
    ]
    for url in weather_list:
        parse_page(url)

if __name__  == "__main__":
    main()