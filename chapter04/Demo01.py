#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/9 13:59
# @Author :zhai shuai
"""
 作用
    一: 线程的基础知识
    (1) 获取线程的名字
    (2) 获取一共有多少个线程
    (3) 使用threading.Thread的方法实现多线程
 难点
    
 注意点
    
"""
import time,threading

# 一: 普通的执行方式，同步的方式，
# def coding():
#     for x in range(3):
#         print("正在执行的代码%s"%(x))
#         time.sleep(1)
#
#
# def drawing():
#     for x in range(3):
#         print("画图%s"%(x))
#         time.sleep(1)
#
# if __name__ == "__main__":
#     coding()
#     drawing()



# 二: 异步的执行方式
def coding():
    for x in range(3):
        print("正在执行的代码%s"%(threading.current_thread()))
        time.sleep(1)


def drawing():
    for x in range(3):
        print("画图%s"%(threading.current_thread()))
        time.sleep(1)

if __name__ == "__main__":
    t1 = threading.Thread(target=coding,name="线程一")
    t2 = threading.Thread(target=drawing,name="线程二")

    t1.start()
    t2.start()
    print(threading.enumerate())# 线程的总数  [<_MainThread(MainThread, started 20140)>, <Thread(Thread-1, started 5880)>, <Thread(Thread-2, started 19172)>]

