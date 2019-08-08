#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/1 7:35
# @Author :zhai shuai
"""
 作用
    一：
    1 获取所有的tr标签
    2 获取第2个tr标签
    3 获取所有的class包含'even sp' 并且id包含'my'的tr标签
    4 获取所有的class='even sp' 并且id='my'的tr标签
    5 获取所有的a标签的href属性
    6 获取所有的职位信息

 难点
    
 注意点
 <tr class="even">
			<td>职位名称</td>
			<td>职位类别</td>
			<td>人数</td>
			<td>地点</td>
			<td>发布时间<a href="info"></a></td>
 </tr>

 如果我们获取了hr,如果我们想获取每个tr下面的a标签，那么我们该怎样做(注意tr--->td--->a)

 tr.xpath(".//a") 表示在当前tr标签下面所有的a标签，不能这样写tr.xpath("//a") 如果这样写，那么他会忽视tr，变成在整个文档中寻早a标签
 -----------------------------
 a = tr.xpath("./td[last()]/a")
 a[0].xpath("./@href")

 等价于
 tr.xpath("./td[last()]/a/@href")
----------------------------------
    <td>td里面的内容<a>a标签里的内容</a></td>
    如果想拿到td里面的文本，如果只想取出td里面的内容：td里面的内容，就应该这样：td.xpath("./text()")
   如果想拿到td里面的文本，如果取出：td里面的内容和a标签文本，就应该这样：td.xpath(".//text()")
-------------------------------------

"""
from lxml import etree

parser = etree.HTMLParser(encoding="utf-8")
html = etree.parse("files/Demo02.html",parser=parser)

#1 获取所有的tr标签
def getAllTr():
    trs = html.xpath("//tr")
    print(type(trs))# 返回的是一个list
    for tr in trs:
        print(etree.tostring(tr,encoding="utf-8").decode("utf-8"))

#2 获取第2个tr标签
def getSecondTr():
    tr = html.xpath("//tr[2]")#返回的仍然是list
    print(etree.tostring(tr[0], encoding="utf-8").decode("utf-8"))

#     3 获取所有的class包含'even sp' 并且id包含'my'的tr标签
def getEvenTr():
    trs = html.xpath("//tr[contains(@class,'even sp')][contains(@id,'my')]")  # 返回的仍然是list
    for tr in trs:
        print(etree.tostring(tr,encoding="utf-8").decode("utf-8"))


#4 获取所有的class='even sp' 并且id='my'的tr标签
def getEvenTr2():
    trs = html.xpath("//tr[@class='even sp' and @id='my']")  # 返回的仍然是list
    for tr in trs:
        print(etree.tostring(tr,encoding="utf-8").decode("utf-8"))


def getHrefValue():
    """
    5 获取所有的a标签的href属性
    :return:
    """
    a = html.xpath("//a/@href")
    for tr in a:
        print(tr)

def getTotal():
    """"
    6 获取所有的职位信息
    """
    trs = html.xpath("//tr[position()>1]")
    for tr in trs:
        # a = tr.xpath("./td[last()]//text()")
        # print(a)
        a = tr.xpath("./td[last()]/a")
        href = a[0].xpath("./@href")[0]#取出a标签的href属性
        atext = a[0].xpath("./text()")[0]#取出a标签文本内容
        title = tr.xpath("./td[1]//text()")[0]
        category = tr.xpath("./td[2]/text()")[0]
        nums = tr.xpath("./td[3]/text()")[0]
        address = tr.xpath("./td[4]/text()")[0]
        publicdate = tr.xpath("./td[5]/text()")[0]
        print(href,atext,title,category,nums,address,publicdate)


if __name__ == "__main__":
    getTotal()