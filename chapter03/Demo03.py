#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/9 10:41
# @Author :zhai shuai
"""
 作用
    一 写入csv文件的两种方式
 难点
    
 注意点
    
"""
import csv

def write_csv01():
    header = ["username","age","height"]
    values = [
        ("牙",22,44),
        ("中国", 22, 44)
    ]

    with open("./files/demo03.csv","w",encoding="utf-8",newline="") as ft:
        writer = csv.writer(ft)
        writer.writerow(header)
        writer.writerows(values)


def write_csv02():
    header = ["username", "age", "height"]
    values = [
        {"username": "站三", "age": 2, "height": 234},
        {"username": "站三", "age": 2, "height": 234},
        {"username": "站三", "age": 2, "height": 234},
    ]

    with open("./files/demo03_02.csv", "w", encoding="utf-8", newline="") as ft:
        writer = csv.DictWriter(ft,header)
        writer.writeheader()
        writer.writerows(values)


with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


if __name__ == '__main__':
    write_csv01()
    write_csv02()

