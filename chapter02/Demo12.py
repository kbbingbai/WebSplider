#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/6 8:21
# @Author :zhai shuai
"""
 作用
    一：sub 提取出来标签内的内容
 难点
    
 注意点

 输出

    省/直辖市
    城市
    周日(8月4日)白天
    周日(8月4日)夜间
     


    天气现象
    风向风力
    最高气温
    天气现象
    风向风力
    最低气温
    
"""

import re

text = """
<td rowspan="2" width="74">省/直辖市</td>
<td rowspan="2" width="83">城市</td>
<td colspan="3" height="37">周日(8月4日)白天</td>
<td colspan="3">周日(8月4日)夜间</td>
<td class="last" rowspan="2" width="49"> </td>
</tr>
<tr>
<td height="23" width="89">天气现象</td>
<td width="162">风向风力</td>
<td width="92">最高气温</td>
<td width="98">天气现象</td>
<td width="177">风向风力</td>
<td width="86">最低气温</td>
"""

reg = re.sub("<.*?>","",text)
print(reg)
