# -*- coding: UTF-8 -*-
# yum install MySQL-python
# pip install MySQL-python
# yum install mysql
# 118.25.49.129运行的是docker启动的mysql实例
import MySQLdb
# host = '127.0.0.1'
# user = 'root'
# db = 'mysql'
# password = 'redhat'
# sql = "select user from user where user = 'root';"
# db_conn = MySQLdb.connect(host=host, user=user, passwd=password, db=db)
# cursor = db_conn.cursor()
# cursor.execute(sql)
# # res = cursor.fetchone()    # fetchone()方法获取一条数据
# # print(type(res))     # tuple类型
# # print(res)
# res = cursor.fetchall()   # # fetchall()方法获取所有匹配的数据
# for line in res:
#     print line
# db_conn.close()


class Db:
    def __init__(self, host1, user1, password1, db1):
        self.host = host1
        self.user = user1
        self.password = password1
        self.db = db1
        self._conn = MySQLdb.connect(host=self.host, user=self.user, passwd=self.password, db=self.db)  # 连接mysql
        self._cursor = self._conn.cursor()   # 创建游标

    def fetchone(self, sql1):
        self._cursor.execute(sql1)   # 执行sql语句
        result = self._cursor.fetchone()    # 获取执行的结果
        return result


host = '127.0.0.1'
user = 'root'
db = 'mysql'
password = 'redhat'
sql = "select user from user where user = 'root';"
if __name__ == '__main__':
    db_conn = Db(host, user, password, db)
    print db_conn.fetchone(sql)
