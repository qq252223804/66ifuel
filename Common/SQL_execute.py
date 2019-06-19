# -*- coding: utf-8 -*- 
# @Time : 2018/12/19 17:32 
# @Author : taojian 
# @File : SQL_execute.py
# 封装mysql  mysql_info 连接池配置信息

#连接数据库
#测试数据库
# config={
#     "host":"192.168.3.216",
#     "user":"root",
#     "password":"66ifuel",
#     "database":"charging",
#     "charset": "utf8"}
#外网测试数据库
import pymysql
from Common.log import Log

#连接数据库 port必须为int %d类型
config={
    "host":"123.157.219.74",
    "user":"root",
    "password":"66ifuel",
    "port":33066,
    "database":"charging",
    "charset": "utf8"}

try:
    db = pymysql.connect(**config)
except Exception  as a:
    print("数据库连接异常：%s" % a)
    Log().debug("数据库连接异常：%s" % a)

def mysql_execute(sql, number=None):
    '''执行 单表sql 语句'''
    # with db.cursor(cursor=pymysql.cursors.DictCursor) as cursor:#获取数据库连接的对象以字典形式
    with db.cursor() as cursor:
        try:
            if number == 'one':
                cursor.execute(sql)
                print('执行成功')
            elif number == 'more':
                cursor.executemany(sql)
            else:
                pass
        except Exception as a:
            db.rollback()  # sql 执行异常后回滚
            Log().debug("执行 SQL 语句出现异常：%s" % a)
        # print("执行 SQL 语句出现异常：%s"%a)
        else:
            cursor.close()
            cursor.commit()  # sql 无异常时提交
            db.close()
def mysql_getrows(sql, number=None):
    ''' 返回查询结果'''
    with db.cursor() as cursor:
        try:
            if number == 'one':
                cursor.execute(sql)
                # print('执行成功')
                row = cursor.fetchone()
                return row
            elif number == 'more':
                cursor.executemany(sql)
                rows =cursor.fetchall()
                return rows
            else:
                pass
        except Exception as a:
            print("查询结果错误：%s" % a)
            Log().debug("查询结果错误：%s" % a)
        else:
            cursor.close()
            db.close()
def mysql_getstring(sql):
    '''查询一行的所有值'''
    rows = mysql_getrows(sql, 'one')
    if rows != None:
        for row in rows:
            print(row)

        # for i in row:
        # 	print(i)

# sql="select validCode FROM cp_messagecode WHERE phone='13279612508';"
# code=mysql_getrows(sql, number='one')[0]
# print(code)



# sql1 = "select * from order_info where order_no='20201812191425320005'"
# sqls = "UPDATE order_pledge SET status = 'CLOSED_DEALER' where user_id= '5b42f9b7cec76d75f185d4ec'"
# sql2 = "select * from dealer_car where car_info_id= '5a5ec113943d0b515a43b33a' ORDER BY id DESC "
# mysql.mysql_execute(sql1, number='one')
# mysql.mysql_execute(sqls, number='one')
# mysql.mysql_execute(sql2, number='one')
# print(mysql.mysql_getrows(
#
#
#
#
#
#
#
#
#
#
#
#
#

# sql1,'one'))
# print(mysql.mysql_getrows(sqls,'one'))

# print(mysql.mysql_getstring(sql))

