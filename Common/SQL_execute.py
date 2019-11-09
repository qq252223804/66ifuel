# -*- coding: utf-8 -*- 
# @Time : 2018/12/19 17:32 
# @Author : taojian 
# @File : SQL_execute.py
# 封装mysql  mysql_info 连接池配置信息
import uuid

import pymysql
from Common.log import Log
#连接数据库
#4.0测试数据库
# config={
#     "host":"rm-uf6fbtdzug5024j6z1o.mysql.rds.aliyuncs.com",
#     "user":"ifuel_new",
#     "port":3306,
#     "password":"ifuel66-new",
#     "database":"", #分库分表无需设置数据库
#     "charset": "utf8"}
#4.0线上
config={
    "host":"rm-uf6fc2xm4p8d7y13fwo.mysql.rds.aliyuncs.com",
    "user":"taojian_test1",
    "port":3306,
    "password":"taojian_test1",
    "database":"", #分库分表无需设置数据库
    "charset": "utf8"}
#外网测试数据库
#连接数据库 port必须为int %d类型
# config={
#     "host":"124.160.35.34",
#     "user":"root",
#     "password":"66ifuel",
#     "port":33066,
#     "database":"ifuel-station",
#     "charset": "utf8"}

try:
    db = pymysql.connect(**config)
except Exception  as a:
    print("数据库连接异常：%s" % a)
    Log().debug("数据库连接异常：%s" % a)

def mysql_execute(sql,data=None, number=None):
    '''执行 单表sql 语句'''
    # with db.cursor(cursor=pymysql.cursors.DictCursor) as cursor:#获取数据库连接的对象以字典形式
    with db.cursor() as cursor:
        try:
            if number == 'one':
                cursor.execute(sql)
                print('执行成功')
            elif number == 'more':
                cursor.executemany(sql,data)
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
            if number == 'one' :
                cursor.execute(sql)
                # print('执行成功')
                row = cursor.fetchone()
                return row
            elif number == 'more':
                cursor.execute(sql)
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
    # sql="DELETE from `ifuel-vehicle`.t_vehicle WHERE `user_id`='16ce4852d8000dc';"
    #
    # mysql_execute(sql,data=None,number='one')
    # 批量增加站
    # a=[i for i in range(100,110)]
    # b=[str(i) for i in range(11000,11010)]
    # station_id = '22222'
    # cp_number=[i for i in range(1, 11)]
    # for id ,pile_id,pile_number in zip(a,b,cp_number):
    #     sql="INSERT INTO `ifuel66-station`.`t_pile` VALUES ({},{},{}, 'MA27U0C07', NULL, pile_number, 1, '201900003', '测试厂家', '阿健牌子', '无敌型号', 2000, 'communicate1.1.1', 'control1.1.1', 'screen1.1.1', 'charging1.1.1', 60, 120, 1569477171635, 1569477171635, 0);" .format(id, pile_id, station_id)
    #     print(sql)
    # 批量增加枪
    # cp_id=[i for i in range(100,110)]
    # cp_connector=[i for i in range(121000,121010)]
    # cp_pile= [str(i) for i in range(11000, 11010)]
    # cp_number = [i for i in range(1, 11)]
    # station_id='22222'
    # for id,connector_id, pile_id ,connector_number in zip(cp_id, cp_connector,cp_pile,cp_number):
    #     sql="INSERT INTO `ifuel66-station`.`t_connector` VALUES ({},{},{},{},'MA27U0C07', {}, 1, 480, 220, 20, 5, 1569649051344, 1569649051344, 0);".format(id,connector_id, pile_id, station_id,connector_number)
    #     print(sql)

    #批量设置电价
    cost_id=[]
    for i in range(0,110):
        a=''.join(str(uuid.uuid1()).split('-'))[0:15]
        cost_id.append(a)
    # print(cost_id)
    station_id=[]
    sql="SELECT station_id from `ifuel66-station`.t_station  order by id desc;"
    b=mysql_getrows(sql, number='more')
    for i in b:
        station_id.append(i[0])
    print(station_id)
    print(len(station_id))

    item_id=[]
    for i in range(0, 110):
        b = ''.join(str(uuid.uuid1()).split('-'))[0:15]
        item_id.append(b)

    price_id=[]
    for i in range(0,110):
        c=''.join(str(uuid.uuid1()).split('-'))[0:15]
        price_id.append(c)
    for cost_id,station_id,item_id,price_id in zip(cost_id,station_id,item_id,price_id):
        # 批量设置成本电价 两条sql
        # sql="INSERT INTO `ifuel66-price`.`t_cost_electricity_price` VALUES (0,'{}','成本',{}, 1573178414000, 4102416000000, 1573178465936, 1573178465936, 0);".format(cost_id,station_id)
        # print(sql)
        # sql2="INSERT INTO `ifuel66-price`.`t_electricity_price_item` VALUES (0, '{}', '{}', 1, '成本区间', 0, 48, 16000, 0, 1573190680091, 1573190680091, 0);".format(item_id,station_id)
        # print(sql2)
        # # 批量设置通用标牌价格
        # sql3="INSERT INTO `ifuel66-price`.`t_electricity_price_item` VALUES (0, '{}', '{}', 0, '标牌价格', 0, 48, 100, 60, 1573199318714, 1573199318714, 0);".format(item_id,price_id)
        # print(sql3)
        # sql4="INSERT INTO `ifuel66-price`.`t_station_electricity_price` VALUES (0, '{}', '全天标牌', '{}', NULL, NULL, 10, 0, 1573199299000, 4102416000000, 1573199318714, 1573199318714, 0);".format(price_id,station_id)
        # print(sql4)
        # # #批量设置通用销售价格
        # sql5 = "INSERT INTO `ifuel66-price`.`t_electricity_price_item` VALUES (0, '{}', '{}', 0, '通用价格', 0, 48, 100, 40, 1573199632441, 1573199632441, 0);".format(item_id, price_id)
        # print(sql5)
        # sql6="INSERT INTO `ifuel66-price`.`t_station_electricity_price` VALUES (0, '{}', '普通销售价', '{}', NULL, NULL, 10, 1, 1573199558000, 4102416000000, 1573199632441, 1573199632441, 0);".format(price_id,station_id)
        # print(sql6)
        # # #批量设置会员标牌价格
        # sql7="INSERT INTO `ifuel66-price`.`t_electricity_price_item` VALUES (0, '{}', '{}', 0, '会员标牌', 0, 48, 100, 60, 1573199778911, 1573199778911, 0);".format(item_id, price_id)
        # print(sql7)
        # sql8="INSERT INTO `ifuel66-price`.`t_station_electricity_price` VALUES (0, '{}', '全天会员标牌', '{}', NULL, NULL, 20, 0, 1573199755000, 4102416000000, 1573199778911, 1573199778911, 0);".format(price_id,station_id)
        # print(sql8)
        # # # 批量设置会员销售价格
        sql9="INSERT INTO `ifuel66-price`.`t_electricity_price_item` VALUES (0, '{}', '{}', 0, '会员价格', 0, 48, 100, 36, 1573199980116, 1573199980116, 0);".format(item_id, price_id)
        print(sql9)
        sql10="INSERT INTO `ifuel66-price`.`t_station_electricity_price` VALUES (0, '{}', '会员销售价', '{}', NULL, NULL, 20, 1, 1573199755000, 4102416000000, 1573199980116, 1573199980116, 0);".format(price_id,station_id)
        print(sql10)
# sql="select validCode FROM cp_messagecode WHERE phone='13279612508';"
# sql="select id from cp_station where name='野风时代935'"
# code=mysql_getrows(sql, number='one')[0]
# print(code)



# print(mysql.mysql_getstring(sql))

# sql="SELECT order_id from shop.t_order WHERE trade_no=2019082512551650955833"
# mysql_execute(sql,number='one')
#     sql="SELECT order_id from shop.t_order WHERE trade_no={}".format(201908251305958672197)
#     print(sql)
#     print(mysql_getrows(sql,number='one')[0])


