#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/6 8:28
# @Author :zhai shuai
"""
 作用
    一：split  使用正则来分割字符串
    二：compile  对于一些经常用到的正则表达式，可以使用compile进行编译，后期再使用的时候可以下拉 拿过来使用
        ，执行效率会更快，而且compile还可以指定flag=re.VERBOSE,在写正则表达式的时候可以做好注释，示例代码如下
 难点
    
 注意点

 结果：['hello ', ' dfd', 'd']

    
"""

import re

# text = "hello & dfd*d"
#使用&和*来分割
# reg = re.split("&|\*",text)
# print(reg)




text = "the num is 20.50"
reg = re.compile(r"""
            \d+ #小数点前面的数字
            \.? #小数点
            \d+ #小数点后面的数字
            """,re.VERBOSE)

ret = re.search(reg,text)
print(ret.group()) #输出20.50
