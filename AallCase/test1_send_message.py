#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:p
# Datetime:2019/9/16 14:54
# File: test1_send_message.py
"""
注册登录用例
"""
import unittest, yaml,os
# from utx import *
import requests
from ddt import ddt,data,unpack
from Base.runmethod import RunMethod
from Common.Html_miaoshu import miaoshu
from Common.hmacmd5 import new_hmac_md5
import random,string
yaml.warnings({'YAMLLoadWarning': False})
class Register(unittest.TestCase):
    with open('{}'.format(os.path.join(os.path.dirname(os.getcwd()),'Config')+'\conf.yaml'), 'r', encoding="utf-8") as r:
        config = yaml.load(r)  # 解析并读写yaml文件
        app_host = config['new_app_host']
        headers = eval(config['new_app_headers'])
    SigSecret = '204414295c2f3fbc5818f604793f1ba2'
    # 生成随机手机号
    numbers = list(string.digits)
    mobile = ['130', '132', '150', '155', '177', '186']
    phone = random.choice(mobile) + ''.join(random.sample(numbers, 8))
    def test1_SendMsg_Noregister(self):
        """
        注册:发送验证码_用户未注册
        :return:
        """
        contents={"phone":"{}".format(self.phone),"type":2}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'user.sendVerificationCode',
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        # self.assertTrue(res['code'] == 2003, msg="校验code错误")
        miaoshu(url=self.app_host,method='post',data=datas,check={"code and message"},respons=res)


    def test2_SendMsg_right(self):
        """
        注册:发送验证码_用户已注册
        :return:
        """
        contents={"phone":"15715814052","type":2}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'user.sendVerificationCode',
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 2002, msg=res['message'])
        miaoshu(url=self.app_host,method='post',data=datas,check={"code and message"},respons=res)
