#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/4 15:34
# @Author :zhai shuai
"""
 作用
    一：常用的匹配规则
 难点
    
 注意点
    
"""

import re

#手机号码的匹配  开关必须是1 第二位可以是34587，后面9位就随意了
# re.match("1[34587]\d{9}","xx")
#
# #邮箱的匹配，是由数字，字母，下划线，绑成然后是@称号，后面是域名
# re.match("\w+@\w+\.[a-zA-Z]+","xx")
#
# #url  url的规则是最前面是http或者是https或者是ftp 然后一个冒号，再加上一个斜杆，再后面就可以出现任意非空白字符了
# re.match("(http|https|ftp)://[^\s]+","xx")
#
#
# #身份证号  前17位是数字，最后一位可以是数字或者x或者X
# re.match("\d{17}[\dxX]","xx")
#
#
# # 匹配0-100之间的数字
# reg = re.match('[1-9]\d?$|100$|0')
#
