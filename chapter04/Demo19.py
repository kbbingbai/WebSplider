#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/14 13:26
# @Author :zhai shuai
"""
 作用
    一：采用selenium进行爬虫 请求拉勾网的数据
 难点
    
 注意点

    1 #职位描述
     html.xpath("//*[@id='job_detail']/dd[2]//text()") 这样返回来是一个list
     我们可以采用这样的方式进行处理
     "".join(html.xpath("//*[@id='job_detail']/dd[2]//text()")).strip()
    2 注意在进行EC判断的时候，我们不能这样
        EC.presence_of_element_located((By.XPATH, "//div[@class='job-name']//h4[@class='company']//text()"))
        它不能判断//text()里有没有值，它只会判断标签存在不存在
        EC.presence_of_element_located((By.XPATH, "//div[@class='job-name']//h4[@class='company']"))
    3 注意切换窗口
        self.driver.execute_script("window.open('%s')"%singleDetailUrl)#用一个窗口打开新的详情页面
        self.driver.switch_to.window(self.driver.window_handles[1]) #切换到第二个窗口
        当打开了一个新的窗口（execute_script）后，必须要执行self.driver.switch_to.window 要不然，得到的
        self.driver.page_source 不是新打开的页面的page_source
"""
from selenium import webdriver
from lxml import etree
import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LagouSpider(object):
    driver_path = r'D:\Software\chromedriver\chromedriver.exe'
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=LagouSpider.driver_path)
        self.url = "https://www.lagou.com/jobs/list_python?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput="
        self.reg = re.compile(r"[\s/]")
        self.positions = []
        self.nums = 0

    def run(self):
        self.driver.get(self.url) #请求第一页的数据
        while True:
            WebDriverWait(driver=self.driver,timeout=15).until(
                EC.presence_of_element_located((By.XPATH,"//div[@class='pager_container']//span[last()]"))
            )
            source = self.driver.page_source
            self.parse_list_page(source) #解析列表页面
            next_page_btn = self.driver.find_element_by_xpath("//div[@class='pager_container']//span[last()]")
            if "pager_next pager_next_disabled" in next_page_btn.get_attribute("class"):
                break
            else:
                next_page_btn.click() #请求下一页的数据


            time.sleep(5) #第一页要隔5秒请求

    def parse_list_page(self,source):
        html = etree.HTML(source)
        single_page_position_links = html.xpath("//a[@class='position_link']/@href")
        for singleDetailUrl in single_page_position_links:
            self.parse_detail(singleDetailUrl)
            time.sleep(5) #每一个详情页面的爬去需要等待三秒

    def parse_detail(self,singleDetailUrl):

        """
        注意解析详情页面的时候在要新的页面打开，而不能覆盖列表页面，因为我们要做翻页的操作
        :param singleDetailUrl:
        :return:
        """
        self.nums = self.nums+1
        print("正在爬取第%d"%(self.nums))
        self.driver.execute_script("window.open('%s')"%singleDetailUrl)#用一个窗口打开新的详情页面
        self.driver.switch_to.window(self.driver.window_handles[1]) #切换到第二个窗口

        WebDriverWait(driver=self.driver, timeout=10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='job-name']//h4[@class='company']"))
        )
        singleDetailSource = self.driver.page_source
        html = etree.HTML(singleDetailSource)
        company_name = html.xpath("//div[@class='job-name']//h4[@class='company']/text()")[0]
        positionname = html.xpath("//div[@class='job-name']//h2[@class='name']/text()")[0]

        salary = html.xpath("//dd[@class='job_request']//span[@class='salary']/text()")[0]
        workPlace = html.xpath("//dd[@class='job_request']//span[position()=2]/text()")[0]
        workPlace = re.sub(self.reg,"",workPlace)
        jingyan = html.xpath("//dd[@class='job_request']//span[position()=3]/text()")[0]
        jingyan = re.sub(self.reg,"",jingyan)
        xueli = html.xpath("//dd[@class='job_request']//span[position()=4]/text()")[0]
        xueli = re.sub(self.reg, "", xueli)
        zaizhifangshi = html.xpath("//dd[@class='job_request']//span[position()=5]/text()")[0]
        zaizhifangshi = re.sub(self.reg, "", zaizhifangshi)
        #职位标签
        bq = []
        biaoqians = html.xpath("//ul[@class='position-label clearfix']//li")
        for biaoqian in biaoqians:
            bq.append(biaoqian.xpath("./text()")[0])

        #职位诱惑
        zaizhifangshi = html.xpath("//*[@id='job_detail']/dd[1]/p/text()")[0]
        #职位描述,
        zhiweimiaoshu = "".join(html.xpath("//*[@id='job_detail']/dd[2]//text()")).strip()

        position = [company_name,positionname,salary,workPlace,jingyan,xueli,zaizhifangshi,bq,zaizhifangshi,zhiweimiaoshu]
        print(position)
        self.positions.append(position)
        self.driver.close()#关闭新打开的详情页面
        self.driver.switch_to.window(self.driver.window_handles[0])  # 继续切换到列表页面




if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()