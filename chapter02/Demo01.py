#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/7/31 11:38
# @Author :zhai shuai
"""
 作用
    一：使用lxml，并使用xpath来解析html

 难点
    
 注意点
    
"""

from lxml import etree
text = """
    <table>
	<tbody>
		<tr>
			<td>职位名称</td>
			<td>职位类别</td>
			<td>人数</td>
			<td>地点</td>
			<td>发布时间</td>
		</tr>
		<tr>
			<td>java</td>
			<td>java类别</td>
			<td>22</td>
			<td>山东</td>
			<td>2019-05</td>
		</tr>
		<tr>
			<td>c#</td>
			<td>c#类别</td>
			<td>12</td>
			<td>山西</td>
			<td>201509</td>
		</tr>
		<tr>
			<td>python</td>
			<td>python类别</td>
			<td>12</td>
			<td>关东</td>
			<td>1996</td>
		</tr>
	</tbody>
</table>
"""



#解析文本
def parse_text(text):
    htmlElement = etree.HTML(text)
    print(type(htmlElement))#<class 'lxml.etree._Element'>
    print(etree.tostring(htmlElement,encoding="utf-8").decode("utf-8"))

#解析文件
def parse_file(file):
    """
    会有如下的错误,这是由于html代码不规范造成的：怎样去解决--使用HTMLParser
        lxml.etree.XMLSyntaxError: Opening and ending tag mismatch: input line 38 and div, line 68, column 23
    """
    parser = etree.HTMLParser(encoding="utf-8")
    htmlElement = etree.parse(file,parser=parser)
    print(etree.tostring(htmlElement, encoding="utf-8").decode("utf-8"))

if __name__ == "__main__":
    parse_file("files/Deme01.html")



