#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:p
# Datetime:2019/9/29 9:27
# File: test2_login.py
"""
登录相关用例
"""
import unittest, yaml,os
import requests

from Common.Html_miaoshu import miaoshu
from Common.hmacmd5 import new_hmac_md5
from Common.redis_operate import get_cluster_value

yaml.warnings({'YAMLLoadWarning': False})

class Lgoin(unittest.TestCase):

    # with open('{}'.format(os.path.join(os.path.dirname(os.getcwd()),'Config')+'\conf.yaml'), 'r', encoding="utf-8") as r:
    with open('{}'.format(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'Config\conf.yaml')), 'r', encoding="utf-8") as r:
        config = yaml.load(r)  # 解析并读写yaml文件
        app_host = config['new_app_host']
        headers = eval(config['new_app_headers'])
        nodes = eval(config['nodes'])  # 取出来的str-list
    token = None
    user_id = None
    biz_content=None
    SigSecret = '204414295c2f3fbc5818f604793f1ba2'
    # 生成随机手机号
    # numbers = list(string.digits)
    # mobile = ['130', '132', '150', '155', '177', '186']
    # phone = random.choice(mobile) + ''.join(random.sample(numbers, 8))

    def test1_login_NoRegister(self):
        '''
        登录-用户未注册
        :return:
        '''
        contents = {"phone": "19000000000"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'user.judge_phone_is_registered',
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 110003, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)
    def test2_login_byPwd_EorPwd(self):
        '''
        登录-用户存在，密码错误
        :return:
        '''
        contents = {"phone": "18657738815","password":"123456"}
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
        self.assertTrue(res['code'] == 110005, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)
    def test3_login_byPwd_rightPwd(self):
        '''
        登录-用户存在，密码正确
        :return:
        '''
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
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)
    def test4_login_sendMsg(self):
        '''
        登录: 发送验证码
        :return:
        '''
        contents = {"phone": "18657738815", "type": 1}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'user.send_verification_code',
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})
        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)

    def test5_login_errorMsgCode(self):
        '''
        登录:输入错误验证码
        :return:
        '''
        contents = {"phone": "18657738815", "verification_code": "000000"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'user.login_by_verification_code',
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 110001, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)


    def test6_login_rightMsgCode(self):
        '''
        登录:输入正确验证码
        :return:
        '''
        global token,user_id
        MsgCode=get_cluster_value("login_{}".format(18657738815) ,nodes=self.nodes)
        print(MsgCode)
        contents = {"phone": "18657738815", "verification_code": "{}".format(MsgCode)}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'user.login_by_verification_code',
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})
        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)
        # print(res['data']['token'])
        token=res['data']['token']
        user_id=res['data']['user_id']
        return token,user_id

    def test7_loginOut(self):
        '''
        登出
        :return:
        '''
        contents={"token":"{}".format(token)}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'user.logout',
                "access_token":'{}'.format(token),
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)

    def test8_query_user_by_user_id(self):
        '''
        根据userId查询_无登录Token
        :return:
        '''
        contents = {"userId": "15d6aa852800318"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'user.logout',
                "access_token": '{}'.format(None),
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 1000, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)
    def test8_query_user_by_user_id_1(self):
        '''
        根据userId查询_有登录Token
        :return:
        '''
        contents = {"userId": "15d6aa852800318"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'user.query_user_by_user_id',
                "access_token": '{}'.format(token),
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)