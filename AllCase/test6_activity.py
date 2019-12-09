#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:p
# Datetime:2019/12/3 17:09
# File: test6_activity.py
"""
推荐有奖活动
"""
import unittest, yaml,os
import requests

from Common.Html_miaoshu import miaoshu
from Common.hmacmd5 import new_hmac_md5


yaml.warnings({'YAMLLoadWarning': False})
class Activity(unittest.TestCase):

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
        contents = {"phone": "18657738817", "password": "d7ef70eea3c962820e0c6b3ae25d465a"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-12-3 17:24:2',
                "version": '1.0',
                "client": 'ios',
                "client_version": '4.0.1',
                "device_id": 'iPhone8cb2aa6fb3296abb',
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


    def test1_promote_activity(self):
        '''
        获取活动详情
        :return:
        '''
        contents = {"area_code": "330100"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.2',
                "device_id": '123123',
                "method": 'promote.activity',
                "access_token": '{}'.format(self.token),
                "biz_content": '{}'.format(contents)
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)

    def test2_promote_share(self):
        '''
        分享活动
        :return:
        '''
        contents = {"area_code": "330100","phone":"18657738817"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.2',
                "device_id": '123123',
                "method": 'promote.share',
                "access_token": '{}'.format(self.token),
                "biz_content": '{}'.format(contents)
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        # self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)