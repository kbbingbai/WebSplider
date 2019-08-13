#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/9 14:33
# @Author :zhai shuai
"""
 作用
    一：线程不安全的问题的演示，以及线程不安全问题的解决，使用threading.Lock()
 难点
    
 注意点
    
"""
import threading
VALUE = 0
gLock = threading.Lock()

def addvalue():
    global VALUE #如果一个方法里面要使用全局变量，要在方法里面声明一下,要使用global
    gLock.acquire()
    for x in range(1000000):
        VALUE += 1
    gLock.release()
    print(VALUE)

if __name__ == '__main__':
    for x in range(1,4):#注意如果这个range(3)是3的话，那么这个x就是1 2 3
        print(x)

    for x in range(3): #注意如果这个range(3)是3的话，那么这个x就是1 2
        print(x)
        t = threading.Thread(target=addvalue)
        t.start()

