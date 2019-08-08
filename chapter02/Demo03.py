#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/1 14:27
# @Author :zhai shuai
"""
 作用
    一：爬取豆瓣电影数据
 难点
    
 注意点
    
"""
import requests
from lxml import etree

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}

url = "https://movie.douban.com/cinema/nowplaying/beijing/"

"""
response.text  返回的是一个字符串str(unicode)类型
response.content 返回的是一个字符串，就是从网页上抓取下来的，没有经过处理的字符串，是一个bytes类型
"""
#2进行网页的请求
resp = requests.get(url,headers=header)
text = resp.text

#2进行数据请求
html = etree.HTML(text)
nowplayingMovieDiv = html.xpath("//div[@id='nowplaying']")[0]
nowplayingMovieLi = nowplayingMovieDiv.xpath(".//ul[@class='lists']/li")

for single in nowplayingMovieLi:
    movieId = single.xpath("./@id")#电影id
    movieName = single.xpath("./@data-title")#电影名称
    movieScore = single.xpath("./@data-score")#电影评分
    movieStar = single.xpath("./@data-star")#电影星星数据
    movierelease = single.xpath("./@data-release")#电影上映日期
    movierduration = single.xpath("./@data-duration")#电影时长
    movieregion = single.xpath("./@data-region")#出产地区
    movieactors = single.xpath("./@data-actors")#电影主要演员
    movievotecount = single.xpath("./@data-votecount")#电影评价数
    moviepicurl = single.xpath(".//img/@src")#电影海报url
    print(movieId,movieName,movieScore,movieStar,movierelease,movierduration,movieregion,movieactors,movievotecount,moviepicurl)

#打印出的一条的数据为：
# ['26794435'] ['哪吒之魔童降世'] ['8.7'] ['45'] ['2019'] ['110分钟'] ['中国大陆'] ['吕艳婷 / 囧森瑟夫 / 瀚墨'] ['408887'] ['https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2563780504.jpg']







