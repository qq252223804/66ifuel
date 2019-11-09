#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:p
# Datetime:2019/10/10 14:16
# File: test5_coupon.py
"""
优惠卷信息
"""
import unittest, yaml,os
import requests

from Common.Html_miaoshu import miaoshu
from Common.hmacmd5 import new_hmac_md5


yaml.warnings({'YAMLLoadWarning': False})
class Coupon(unittest.TestCase):

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
        contents = {"phone": "13185097298", "password": "e10adc3949ba59abbe56e057f20f883e"}
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
        self.token = res['data']['token']
        self.user_id = res['data']['user_id']
        return self.token, self.user_id

    def test1_user_coupon_count(self):
        '''
        查询优惠券数量
        :return:
        '''

        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'coupon.user_coupon_count',
                "access_token": '{}'.format(self.token),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)

    def test2_coupon_list_Notused_10(self):
        '''
        查询优惠券列表-未使用-翻页10
        :return:
        '''
        contents={"status":"0","page":"1","page_size":"10"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'coupon.user_coupon_list',
                "access_token": '{}'.format(self.token),
                "biz_content": '{}'.format(contents)
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)
    def test3_coupon_list_Notused_20(self):
        '''
        查询优惠券列表-未使用-翻页10
        :return:
        '''
        contents={"status":"0","page":"2","page_size":"10"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'coupon.user_coupon_list',
                "access_token": '{}'.format(self.token),
                "biz_content": '{}'.format(contents)
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)


    def test4_coupon_list_used(self):
        '''
        查询优惠券列表-未使用
        :return:
        '''
        contents={"status":"1","page":"1","page_size":"10"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'coupon.user_coupon_list',
                "access_token": '{}'.format(self.token),
                "biz_content": '{}'.format(contents)
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)

    def test5_coupon_list_Expired(self):
        '''
        查询优惠券列表-已过期
        :return:
        '''
        contents={"status":"2","page":"1","page_size":"10"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'coupon.user_coupon_list',
                "access_token": '{}'.format(self.token),
                "biz_content": '{}'.format(contents)
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)