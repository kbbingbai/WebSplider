#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/2 15:15
# @Author :zhai shuai
"""
 作用
    一：BeautifulSoup的使用
    二 需求：
        1 获取所有的tr标签
        2 获取第二个tr标签
        3 获取所有的class等于even的tr标签
        4 将所有的id等于test,class等于test的a标签提取出来
        5 获取所有的a标签
        6 获取所有的职位信息（纯文本）
 难点
    
 注意点
    一：在# 5 获取所有的a标签中
       第一种情况：tds[4].get_text(strip=True) 会去空格
           输出   1996a标签里面的
       第二种情况：tds[4].get_text
           输出   <bound method Tag.get_text of <td>2019-05<br/><a href="java">a标签里面的</a></td>>
        第三种情况：tds[4].get_text()，它不会去掉空格
          输出    2019-05a标签里面的
        第四种情况：
        publicDate = tds[4]
        list(publicDate.stripped_strings)[0] 输出1996
    
"""

from bs4 import BeautifulSoup, Tag

html = """
  <table>
	<tbody>
		<tr class="even">
			<td>职位名称</td>
			<td>职位类别</td>
			<td>人数</td>
			<td>地点</td>
			<td>发布时间<a href="info">是一个目标</a></td>
		</tr>
		<tr class="even sp" id="my">
			<td>java</td>
			<td>java类别</td>
			<td>22</td>
			<td>山东</td>
			<td>2019-05<br><a href="java">a标签里面的</a></td>
		</tr>
		<tr>
			<td>c#</td>
			<td>c#类别</td>
			<td>12</td>
			<td>山西</td>
			<td>201509<a href="#" id="test">a标签里面的</a></td>
		</tr>
		<tr>
			<td>python</td>
			<td>python类别</td>
			<td>12</td>
			<td>关东</td>
			<td>1996<a href="python" id="test" class="test">a标签里面的</a></td>
		</tr>
	</tbody>
</table>
"""

soup = BeautifulSoup(html, "lxml")

#1 获取所有的tr标签
    # trs = soup.find_all("tr")
    # for tr in trs:
    #     print(tr)
    #     print(type(tr))
    #     print("*"*20)

#2 获取第二个tr标签
#注意soup.find_all返回的是一个列表
# trs = soup.find_all("tr",limit=2)[1]
# print(trs)

#3 获取所有的class等于even的tr标签
# trs = soup.find_all("tr",class_="even") #或者使用soup.find_all("tr",attrs={"class":"even"})
# for tr in trs:
#     print(tr)


#4 将所有的id等于test,class也等于test的a标签提取出来
# a = soup.find_all("a",class_="test",id="test")#或者使用soup.find_all("tr",attrs={"class":"even","id":"test"})
# for tr in a:
#     print(tr)



# 使用get_text()方法可以获取当前标签下的所有文字，包括其子标签的,该方法可自动剔除其余的修饰标签
# 若当前标签的子节点是文字，可使用.string获得其下的文本内容

# 5 获取所有的a标签
trList = soup.find_all("tr")[1:] #过虑掉第一个tr
for tr in trList:
    tds = tr.find_all("td")
    name = tds[0].string #提取标签里面的内容
    category = tds[1].string
    count = tds[2].string
    address = tds[3].string
    publicDate = tds[4].get_text()

    print(name,category,count,address,publicDate)


#
# tr = soup.find("tr")#<class 'bs4.element.Tag'>
# trs = soup.find_all("tr")#<class 'bs4.element.ResultSet'>，每一个元素，就是一个Tag,实际上，ResoutSet，继承了list,
#














