#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/9 16:55
# @Author :zhai shuai
"""
 作用
    一：这个是生产者与消费者,是使用的是 lock.acquire() 和 lock.release()
 难点
    
 注意点

"""

import threading,time,random

gTotalMoney = 1000
gTotalTime = 10
gTime = 0
lock = threading.Lock()

class Consumer(threading.Thread):
    def run(self):
        global gTotalMoney
        global gTime
        while True:
            randMoney = random.randint(100,1000)#用来生产一个数字
            lock.acquire()  # 获得锁这个对象
            if gTotalMoney >= randMoney:
                gTotalMoney -= randMoney
            else:
                lock.release()
                break
            print("%s消费者消费了%d元，剩余%d元钱"%(threading.current_thread(),randMoney,gTotalMoney))
            lock.release()
            time.sleep(1)


class Producer(threading.Thread):
    def run(self):
        global gTotalMoney
        global gTime
        while True:
            randMoney = random.randint(100, 1000)  # 用来生产一个数字
            lock.acquire()  # 获得锁这个对象
            if gTime >= gTotalTime:
                lock.release()
                break
            gTotalMoney += randMoney
            print("第%d次，%s生产者生产了%d元，剩余%d元钱" % (gTime,threading.current_thread(), randMoney, gTotalMoney))
            gTime += 1
            lock.release()
            time.sleep(1)



if __name__ == '__main__':
    for x in range(3):
        c = Consumer(name="消费者：%d"%x)
        c.start()

    for x in range(3):
        p = Producer(name="生产者：%d"%x)
        p.start()




























