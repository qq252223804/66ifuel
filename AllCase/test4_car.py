#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:p
# Datetime:2019/10/10 11:05
# File: test4_car.py
"""
车辆信息
"""
import unittest, yaml,os
import requests

from Common.Html_miaoshu import miaoshu
from Common.SQL_execute import mysql_execute
from Common.hmacmd5 import new_hmac_md5
from Common.redis_operate import get_cluster_value

yaml.warnings({'YAMLLoadWarning': False})
class Car(unittest.TestCase):

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

    def test1_create_vehicle_notoken(self):
        '''
        新增/修改车辆信息:无token
        :return:
        '''
        contents = {"user_id":"{}".format(self.user_id),"vehicle_number":"浙AJ1800","vehicle_model":"法拉利"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'vehicle.create_vehicle',
                "access_token": '{}'.format(None),
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 100001, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)
    def test2_create_vehicle_number_exist(self):
        '''
        新增/修改车辆信息:有token_车牌号不存在
        :return:
        '''
        sql = "DELETE from `ifuel-vehicle`.t_vehicle WHERE `user_id`='15d6aa852800318';"
        mysql_execute(sql, number='one')
        contents = {"user_id":"{}".format(self.user_id),"vehicle_number":"浙AJ1800","vehicle_model":"法拉利"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'vehicle.create_vehicle',
                "access_token": '{}'.format(self.token),
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)

    def test3_create_vehicle_right(self):
        '''
        新增/修改车辆信息:有token_车牌号已存在
        :return:
        '''

        contents = {"user_id":"{}".format(self.user_id),"vehicle_number":"浙AJ1800","vehicle_model":"法拉利"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'vehicle.create_vehicle',
                "access_token": '{}'.format(self.token),
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 124001, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)

    def test4_query_vehicle_by_user_id(self):
        '''
        查询车辆信息
        :return:
        '''
        contents = {"user_id": "{}".format(self.user_id)}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'vehicle.query_vehicle_by_user_id',
                "access_token": '{}'.format(self.token),
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)


