# -*- coding: utf-8 -*- 
# @Time : 2018/12/20 14:53 
# @Author : taojian 
# @File : redis_operate.py

import redis
from rediscluster import RedisCluster
#此处只能安装pip install redis-py-cluster 1.3.6版本不然无StrictRedisCluster

import sys
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
# pool1=redis.ConnectionPool(host='192.168.3.143',password='66ifuel-test', port=7001,db=0)
# r=redis.Redis(connection_pool=pool1)
# r.delete('CMS_USER_ON_LINE')
# print(r.exists('CMS_USER_ON_LINE'))

# str=str(r.get('register_18627318049').decode())
# print(str)
class simple_Redis():
    '''
    单机redis
    '''

    def __init__(self, **kwargs):
        try:
            self.pool = redis.ConnectionPool(**kwargs)
            self.link= redis.Redis(connection_pool=self.pool)

        except Exception as e:
            print("Connect Error!", e)
            sys.exit(1)
    def set(self,key,value):
        self.link.set(key,value)
    def get_value(self,key):
        """
        :param key:
        :param kwargs: 传字典 redis的配置
        :return:
        """
        value = str(self.link.get('{}'.format(key)).decode())
        return value

class many_Redis():
    '''
    集群redis
    '''
    def __init__(self,nodes):
        try:
            # 访问集群设置密码
            self.conn = RedisCluster(startup_nodes=nodes,password='66ifuel-test')

        except Exception as e:
            print("Connect Error!",e)
            sys.exit(1)
    def set(self,key,value):
        self.conn.set(key,value)

    def get_cluster_value(self,key):
        value=str(self.conn.get('{}'.format(key)).decode())
        return value

if __name__ == '__main__':

    # cont={"host":'192.168.3.143',"password":'66ifuel-test', "port":7003,"db":0}
    # a = simple_Redis(**cont)
    # print(a.get_value("register_18000000001"))

    nodes = [
        {"host": "192.168.3.143", "port": "7001"},
        {"host": "192.168.3.143", "port": "7002"},
        {"host": "192.168.3.143", "port": "7003"},
    ]
    b=many_Redis(nodes)

    # list = [
    #     '02200000001',
    #     '02200000002',
    #     '02200000003',
    #     '02200000004',
    #     '02200000005',
    #     '02200000006',
    #     '02200000007',
    #     '02200000008',
    #     '02200000009',
    #     '02200000010',
    #     '02200000010'
    # ]
    # for i in range(0, len(list)):
    #     b.set('test_phone_' + list[i], '111111')
    #     print(b.get_cluster_value('test_phone_' + list[i]))
    #取2个key值相同的 value不同
    b.set('test_phone_02200000010', '111111')
    b.set('test_phone_02200000010', '222222')
    print(b.get_cluster_value('test_phone_02200000010'))