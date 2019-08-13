#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/8 17:26
# @Author :zhai shuai
"""
 作用
    一：读取csv的两种方式
 难点
    
 注意点
    
"""

import csv


def read_csv_01():
    """
        <class 'list'>
        ['张三', '22', '1', '中国']
        <class 'list'>
        ['lishi', '52', '2', '四口']
    """
    with open("./files/demo02.csv","r",encoding="utf-8") as ft:
        #reader是一个迭代器
        reader = csv.reader(ft)
        next(reader)#取迭代器的下一行
        for x in reader:
            print(type(x))
            print(x)




def read_csv_02():

    with open("./files/demo02.csv","r",encoding="utf-8") as ft:
        """
            输出：
            <class 'collections.OrderedDict'>
            OrderedDict([('name', '张三'), ('age', '22'), ('class', '1'), ('country', '中国')])
            {'name': '张三', 'age': '22'}
            <class 'collections.OrderedDict'>
            OrderedDict([('name', 'lishi'), ('age', '52'), ('class', '2'), ('country', '四口')])
            {'name': 'lishi', 'age': '52'}
        """
        #reader是一个迭代器，遍历这个迭代器，返回来的是一个字段
        # 使用DictReader不会包含标题那一行的数据
        reader = csv.DictReader(ft)
        for x in reader:
            print(type(x))
            print(x)
            val = {"name":x["name"],"age":x["age"]}
            print(val)



if __name__ == '__main__':
    read_csv_02()