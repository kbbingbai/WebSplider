#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/9 17:57
# @Author :zhai shuai
"""
 作用
    一：Condition版本的生产者与消费者模式
    由于Lock版本的生产者与消费者可以正常的运行，但是存在一个不足，在消费者中，总是通过while 死循环并且上锁的方式去判断钱不够，
    上锁是一个很多费cpu资源的行为，因此这种方式不是最好 的，还有一种更好的方式是用threading.Condition来实现，
    threading.Condition可以在没有数据的时候处于阻塞等待状态，一旦有合适的数据了，还可以使用notify相关的函数来通知其它
    等待状态的线程，这样就可以不用做一些无用的上锁和解锁的操作，可以提高程序 的性能，首先对threading.Condition相关的函数做个介绍，
    threading.Condition类似threading.Lock 可以在修改全局数据的时候进行上锁，也可以在修改完毕后进行解锁，以下将一些常用的函数做个简单的介绍
    1 acquire 上锁
    2 release 解锁
    3 wait 将当前线程等待状态，并且会释放锁，可以被其它县城使用notify和notify_all函数唤醒，被唤醒后会继续等待上锁，上锁后继续执行下面的代码
    4 notify  通知所有正在等待的线程，默认是第一个线程
    5 notify 通知所有正在等待的线程，notify 和notify_all不会释放锁，并且需要在release前调用



 难点
    
 注意点
    
"""

# !/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/9 16:55
# @Author :zhai shuai
"""
 作用
    一：这个是生产者与消费者,是使用的是 lock.acquire() 和 lock.release()
 难点

 注意点

"""

import threading, time, random

gTotalMoney = 1000
gTotalTime = 10
gTime = 0
gCondition = threading.Condition()


class Consumer(threading.Thread):
    def run(self):
        global gTotalMoney
        global gTime
        while True:
            randMoney = random.randint(100, 1000)  # 用来生产一个数字
            gCondition.acquire()  # 获得锁这个对象
            while randMoney > gTotalMoney:
                if gTime >= gTotalTime:
                    gCondition.release()
                    print("消费者已经够了次数")
                    return
                print("%s消费%d元，不足" % (threading.current_thread(), randMoney))
                gCondition.wait()
            gTotalMoney -= randMoney
            print("%s消费了%d元，还剩%d元"%(threading.current_thread(),randMoney,gTotalMoney))
            gCondition.release()
            time.sleep(1)


class Producer(threading.Thread):
    def run(self):
        global gTotalMoney
        global gTime
        while True:
            randMoney = random.randint(100, 1000)  # 用来生产一个数字
            gCondition.acquire()  # 获得锁这个对象
            if gTime >= gTotalTime:
                gCondition.release()
                break
            gTotalMoney += randMoney
            print("第%d次，%s生产者生产了%d元，剩余%d元钱" % (gTime, threading.current_thread(), randMoney, gTotalMoney))
            gTime += 1
            gCondition.notify_all()
            gCondition.release()
            time.sleep(1)


if __name__ == '__main__':
    for x in range(3):#x会有0 1 2
        c = Consumer(name="消费者：%d" % x)
        c.start()

    for x in range(3):
        p = Producer(name="生产者：%d" % x)
        p.start()

