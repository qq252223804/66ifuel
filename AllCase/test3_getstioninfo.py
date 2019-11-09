#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:p
# Datetime:2019/10/9 10:59
# File: test3_getstioninfo.py
"""
APP站点相关
"""
import unittest, yaml,os
import requests

from Common.Html_miaoshu import miaoshu
from Common.hmacmd5 import new_hmac_md5
from Common.redis_operate import get_cluster_value

yaml.warnings({'YAMLLoadWarning': False})
class Station(unittest.TestCase):

    with open('{}'.format(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'Config\conf.yaml')), 'r', encoding="utf-8") as r:
        config = yaml.load(r)  # 解析并读写yaml文件
        app_host = config['new_app_host']
        headers = eval(config['new_app_headers'])
        nodes = eval(config['nodes'])  # 取出来的str-list
    token = None
    user_id = None
    biz_content=None
    SigSecret = '204414295c2f3fbc5818f604793f1ba2'

    @classmethod
    def setUpClass(self):
        global token
        contents = {"phone": "18657738815", "password": "e10adc3949ba59abbe56e057f20f883e"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'user.login_by_password',
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})
        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        print(res)
        self.token = res['data']['token']
        self.user_id = res['data']['user_id']
        return self.token, self.user_id


    def test1_query_station_list_all(self):
        '''
        查询站点列表信息:查询所有
        :return:
        '''
        contents = {"page":"1","length":"10000","station_name":"站点1"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'station.query_station_list',
                "access_token": '{}'.format(self.token),
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)
    def test2_query_station_list_10(self):
        '''
        查询站点列表信息:查询分页-第一页
        :return:
        '''
        contents = {"page":"1","length":"10","station_name":"站点1"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'station.query_station_list',
                "access_token": '{}'.format(self.token),
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)
    def test3_query_station_list_20(self):
        '''
        查询站点列表信息:查询分页-第二页
        :return:
        '''
        contents = {"page":"2","length":"10","station_name":"站点1"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'station.query_station_list',
                "access_token": '{}'.format(self.token),
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)
    def test4_query_station_list_1(self):
        '''
        查询站点列表信息:搜索查询-精确
        :return:
        '''
        contents = {"page":"1","station_name":"站点1"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'station.query_station_list',
                "access_token": '{}'.format(self.token),
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)
    def test5_query_station_list_more(self):
        '''
        查询站点列表信息:搜索查询-模糊
        :return:
        '''
        contents = {"page":"1","station_name":"站点1"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'station.query_station_list',
                "access_token": '{}'.format(self.token),
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)

    @unittest.skip('未完成用例，跳过')
    def test6_query_station_by_id(self):
        '''
        查询单个站点信息
        :return:
        '''

    def test7_query_periphery_list(self):
        '''
        查询站点周边服务信息
        :return: 
        '''
        contents = {"operator_id": "359705330", "station_id": "15855f931400082"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'station.query_periphery_list',
                "access_token": '{}'.format(self.token),
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})
        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)

    def test8_query_connector_10(self):
        '''
        查询站点终端列表
        :return:
        '''
        contents = {"page": "1","length":"10","station_id":"15855f931400082","operator_id":"359705330"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'station.query_connector_status_by_station_id',
                "access_token": '{}'.format(self.token),
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})
        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)

    def test8_query_connector_20(self):
        '''
        查询站点终端列表
        :return:
        '''
        contents = {"page": "2","length":"10","station_id":"15855f931400082","operator_id":"359705330"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'station.query_connector_status_by_station_id',
                "access_token": '{}'.format(self.token),
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})
        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)