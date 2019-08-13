#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/12 11:04
# @Author :zhai shuai
"""
 作用
    一：队列的使用
 难点
    
 注意点
    1 def get(self, block=True, timeout=None):
      它的默认值block为true表示，当队列为空时，我就一直阻塞在这个地方，直到队列有值

    2 def put(self, item, block=True, timeout=None):
      它的默认值block为true表示，当队列为满时，我就一直阻塞在这个地方，直到队列有位置让塞

 输出
    12
    True
    False
    1
    False
    0
    True


"""

from queue import Queue

queue = Queue(12)
queue.put(11)

# print(queue.maxsize)
# print(queue.empty())
# queue.put(0)
# print(queue.empty())
# print(queue.qsize())
# print(queue.full())
# print(queue.get())
# print(queue.empty())

while True:
    x = queue.get()
    print(x)
