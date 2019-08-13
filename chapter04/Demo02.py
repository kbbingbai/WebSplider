#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/9 14:10
# @Author :zhai shuai
"""
 作用
    一： 线程的基础知识
    （1） 使用类继承的方式实现多线程
 难点
    
 注意点
    
"""

import threading
import time

class MyThread01(threading.Thread):
    def run(self):
        for x in range(3):
            print("**%s线程的名称为:%s"%(x,threading.current_thread()))
            time.sleep(1)

class MyThread02(threading.Thread):
    def run(self):
        for x in range(3):
            print("%s:%s"%(x,threading.current_thread()))
            time.sleep(1)

if __name__ == "__main__":
    t1 = MyThread01()
    t2 = MyThread02()
    t1.start()
    t2.start()



















