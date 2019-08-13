#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/9 10:56
# @Author :zhai shuai
"""
 作用
    一：mysql的连接,
 难点
    
 注意点
    1 在mysql中定义的deptId字段是一个整数，那么 insert into tbl_emp(name,deptId,inserttime) values(%s,%s,%s)，在进行传的时候需要传入%s，而不是%d
    2 如果mysql中的字段是 timestamp 那么 传入的时候传入一个字符串就可以了  now = datetime.datetime.now()
                                                                      now = now.strftime("%Y-%m-%d %H:%M:%S")
    3 insertSql = "insert into tbl_emp(name,deptId,inserttime) values(%s,%s,%s)"
        cursor.execute(insertSql,['lishi',2,now]) 这样定义也是 可以的cursor.execute(insertSql,('lishi',2,now))


    
"""

import pymysql,datetime
conn = pymysql.connect(host="localhost", user="root", password="123456",
                 database="test", port=3306)
cursor = conn.cursor()

# 1 插入数据库

# insertSql = "insert into tbl_emp(name,deptId) value ('aa',1)"
# cursor.execute(insertSql)
# conn.commit()
# conn.close()

# 2 插入数据库
# now = datetime.datetime.now()
# now = now.strftime("%Y-%m-%d %H:%M:%S")
# insertSql = "insert into tbl_emp(name,deptId,inserttime) values(%s,%s,%s)"
# cursor.execute(insertSql,['lishi',2,now])
# conn.commit()
# conn.close()


# 3 查询数据库
"""
fetchone()  这个方法每次只获取一条数据
fetchall()  获取所有的数据
fetchmany(size)  可以获取指定条数的数据
"""

# fetchone() 借用这个取出全部的数据 下面的fetchall()  fetchmany() 这个就不演示了
# sql = "select * from tbl_emp"
# cursor.execute(sql)
# while True:
#     result = cursor.fetchone()
#     if result:
#         print(result[3])
#     else:
#         break



#4 删除数据
# sql = "delete from tbl_emp where id=%s"
# cursor.execute(sql,(1))
# conn.commit()
# conn.close()


#5 更新数据
sql = "update tbl_emp set name=%s where id=%s"
cursor.execute(sql,('ww',3))
conn.commit()
conn.close()




