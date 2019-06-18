# -*- coding: utf-8 -*- 
# @Time : 2018/12/20 14:53 
# @Author : taojian 
# @File : redis_operate.py

import redis
# pool=redis.ConnectionPool(host='192.168.31.174',password='qiwoauto_test', port=6379,db=2)
# coon=redis.Redis(connection_pool=pool)
#
# #1.string 操作
# # set,mset 批量插入查找  默认不存在则创建，存在则修改
# coon.set('foo','bar')
# coon.mset({"name3":'zhangsan1', "name4":'lisi1'})
# coon.append("name3","zhuijia")
# print(coon.get("name3"))
# #设置过期时间
# coon.psetex('foo',5000,'bar')
# print(coon.get('foo'))
#
# #2.Hash 操作
# # hset(name, key, value) #name对应的hash中设置一个键值对（不存在，则创建，否则，修改）
#
# coon.hset('dic_name','a1','aa')
# coon.hmset("dic_name",{"a2":"aa2","b1":"bb"})
# print(coon.hgetall("dic_name")) #获取name对应hash的所有键值
#
# print(coon.hlen("dic_name"))    #hlen(name) 获取hash中键值对的个数
# print(coon.hkeys("dic_name")) #hkeys(name) 获取hash中所有的key的值
# print(coon.hvals("dic_name"))  #hvals(name) 获取hash中所有的value的值
#
# #删除
# coon.hdel("dic_name","a1")  #删除指定name对应的key所在的键值对
#
# print(coon.hgetall("dic_name"))
#
# # 6通用操作
# coon.delete('name3')     #根据name删除redis中的任意数据类型
# print(coon.exists('name3')) #检测redis的name是否存在


#实战  删除cms 后台在线登陆用户数
pool1=redis.ConnectionPool(host='192.168.31.174',password='qiwoauto_test', port=6379,db=1)
r=redis.Redis(connection_pool=pool1)
r.delete('CMS_USER_ON_LINE')
print(r.exists('CMS_USER_ON_LINE'))

print(r.get('CMS_USER_OFF_LINE'))
