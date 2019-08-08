#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/4 14:33
# @Author :zhai shuai
"""
 作用
    一：正则表达式的学习
 难点
    
 注意点
    1 re.match(reg,text)  匹配只能从字符串的最前面进行匹配
    2 代替
        \d == [0-9]
        \D == [^0-9]
        \w == [0-9a-zA-Z_]
        \d == [^0-9a-zA-Z_]
    3 re.match() 是从最开始找    re.search()  是从整个找

    4 在python中默认采用的是贪婪模式，使用非贪婪模式的话，只需要在量词后面直接加上一个问号”?”。
        在第一篇文章中介绍了正则表达式当中的量词一共有五种：*  +   ？  {m}  {m,n}
    
"""
import re

# 1 匹配某个字符串
# text = "hello mhyhea"
# reg = re.match("he",text)#注意只能匹配字符串的最前面进行匹配
# print(reg.group()) #注意如果没有匹配到报错，AttributeError: 'NoneType' object has no attribute 'group'
#

# 2 . 匹配任意字符
# text = "hello mhyhea"
# reg = re.match(".",text)# . 可以匹配任意一个字符，但是不能匹配\n  如：re.match(".","\nadb")
# print(reg.group())

#3 \d 匹配任意一个数字
# text = "1hello mhyhea"
# reg = re.match("\d",text)
# print(reg.group())

# #4 \D 匹配任意的非数字
# text = "hello mhyhea"
# reg = re.match("\D",text)
# print(reg.group())


#5 \s 匹配任意的空白符（\n, \r, \t, 空格） 等价于[\f\n\r\t\v]           \f换页符 \v垂直制表符
# text = " hello mhyhea"
# reg = re.match('\s',text)
# print(reg.group())


#5 \w 匹配 a-z和A-Z和数字和下划线


#6 \W 匹配 和\w相反的


#7 [] 只要满足中括号中的某一项都算匹配成功,
# text = "2019-56"
# reg = re.match('[\d\-]+',text)
# print(reg.group())


#8 ?(0或者1次)，*（任意次），+（0次以上）

#9 {n} 匹配n次  {n,} 至少匹配n次   {n,m}  至少匹配n次 至多匹配m次
# text = "2019456"
# reg = re.match('\d{3}',text)
# print(reg.group())  #输出 201


#10 ^ 已什么开始 如果是放在括号当中，就是取反的操作[^a] 及以开始
# text = "hello"
# reg = re.match("^h",text)
# print(reg.group())

#11 $ 以什么结尾
# text = "xxx@163.com"
# reg = re.match("\w+@163.com$",text)
# print(reg.group())

#12 | 匹配多个字符串或者表达式
# text = "https"
# reg = re.match("(ftp|https|http)",text)
# print(reg.group())

#13 贪婪与非贪婪
text = "0123456789"
reg = re.match("\d+?",text)
print(reg.group())
