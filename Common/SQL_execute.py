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
    "host":"124.160.35.34",
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
            db.commit()  # sql 无异常时提交
            cursor.close()
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

if __name__ == '__main__':

# sql="select validCode FROM cp_messagecode WHERE phone='13279612508';"
# sql="select id from cp_station where name='野风时代935'"
# code=mysql_getrows(sql, number='one')[0]
# print(code)



# print(mysql.mysql_getstring(sql))

# sql="SELECT order_id from shop.t_order WHERE trade_no=2019082512551650955833"
# mysql_execute(sql,number='one')
    sql="SELECT order_id from shop.t_order WHERE trade_no={}".format(201908251305958672197)
    print(sql)
    print(mysql_getrows(sql,number='one')[0])

