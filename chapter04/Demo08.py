#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/12 13:19
# @Author :zhai shuai
"""
 作用
    一：利用生产者与消费者异步爬虫完成 斗图啦 http://www.doutula.com/photo/list
 难点
    
 注意点
    
"""
import threading
from queue import Queue
import requests
from lxml import etree
from urllib import request
import os
import time
import re
import sys

gLock = threading.Lock()

class Producer(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Producer, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            time.sleep(4)
            self.parse_page(url)

    def parse_page(self,url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
            "Upgrade-Insecure-Requests": "1",
            "Host": "www.doutula.com",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",

        }
        resp = requests.get(url, headers=headers)
        html = etree.HTML(resp.text)
        images = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
        for x in images:
            single_img_url = x.xpath("./@data-original")[0]
            single_img_suffix = os.path.splitext(single_img_url)[1]
            single_img_alt = x.xpath("./@alt")[0]
            single_img_alt = re.sub(r'[\\/L:?"><]', "", single_img_alt)
            filename = single_img_alt + single_img_suffix
            print("生产的url  "+filename+"url"+ single_img_url)
            self.img_queue.put((single_img_url,filename))


class Consumer(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Consumer, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty() and self.img_queue.empty():
                break
            single_img_url,filename = self.img_queue.get()
            request.urlretrieve(single_img_url,"D:/webcrawler/2019-08-06/"+filename)

if __name__ == '__main__':

    page_queue = Queue(100)
    img_queue = Queue(1000)

    #预备page_queue数据
    for x in range(1,10):
        url = "http://www.doutula.com/photo/list/?page=%d" % x
        page_queue.put(url)

    for x in range(1,5):
        p = Producer(page_queue,img_queue)
        p.start()

    for x in range(1,5):
        c = Consumer(page_queue,img_queue)
        c.start()

