#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:p
# Datetime:2019/9/16 14:54
# File: test1_register_user.py
"""
创建用户相关用例
"""
import unittest, yaml,os
# from utx import *
import requests
from ddt import ddt,data,unpack
from Base.runmethod import RunMethod

from Common.Html_miaoshu import miaoshu
from Common.hmacmd5 import new_hmac_md5
import random,string

from Common.redis_operate import get_cluster_value

yaml.warnings({'YAMLLoadWarning': False})

class Register(unittest.TestCase):
    with open('{}'.format(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'Config\conf.yaml')), 'r', encoding="utf-8") as r:
        config = yaml.load(r)  # 解析并读写yaml文件
        app_host = config['new_app_host']
        headers = eval(config['new_app_headers']) #取出来的str-dict
        # print(type(headers))
        nodes=eval(config['nodes'])  #取出来的str-list
        # print(type(nodes))


    token=None
    user_id=None
    SigSecret = '204414295c2f3fbc5818f604793f1ba2'
    # 生成随机手机号
    numbers = list(string.digits)
    mobile = ['130', '132', '150', '155', '177', '186']
    phone = random.choice(mobile) + ''.join(random.sample(numbers, 8))
    new_phone=random.choice(mobile) + ''.join(random.sample(numbers, 8))
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
                "method": 'user.send_verification_code',
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host,method='post',data=datas,check={"code and message"},respons=res)

    def test2_register_errorMsgCode(self):
        '''
        注册:注册用户_错误验证码
        :return:
        '''
        contents = {"phone": "{}".format(self.phone), "verification_code": "000000","area_code":"3301"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'user.register',
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 110001, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)


    def test3_register_right(self):
        '''
        注册:注册用户_正确验证码
        :return:
        '''
        global token,user_id
        MsgCode=get_cluster_value("register_{}".format(self.phone) ,nodes=self.nodes)
        print(MsgCode)
        contents = {"phone": "{}".format(self.phone), "verification_code": "{}".format(MsgCode)}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'user.register',
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


    def test4_register_setPwd(self):
        '''
        注册:设置密码注册
        :return:
        '''

        contents = {"user_id":"{}".format(user_id),"password": "123456"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'user.update_user',
                "access_token":'{}'.format(token),
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)


    def test5_SendMsg_right(self):
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
                "method": 'user.send_verification_code',
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})
        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 110002, msg="校验code错误")
        miaoshu(url=self.app_host,method='post',data=datas,check={"code and message"},respons=res)

    def test6_forgetPwd_SendMsg(self):
        """
        忘记密码:发送验证码
        :return:
        """
        contents={"phone":"{}".format(self.phone),"type":3}
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
        miaoshu(url=self.app_host,method='post',data=datas,check={"code and message"},respons=res)

    def test7_ForgetCheckMsgCode_error(self):
        '''
        忘记密码:校验验证码（验证码错误）
        :return:
        '''
        contents = {"phone": "{}".format(self.phone), "type": 3,"verification_code":"000000"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'user.check_verification_code',
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})
        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 110001, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)

    def test8_ForgetCheckMsgCode_right(self):
        '''
        忘记密码:校验验证码（验证码正确）
        :return:
        '''
        MsgCode = get_cluster_value("forget_password_{}".format(self.phone), nodes=self.nodes)
        print(MsgCode)
        contents = {"phone": "{}".format(self.phone), "type": 3, "verification_code": "{}".format(MsgCode)}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'user.check_verification_code',
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})
        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)

    def test9_Forget_setPwd(self):
        '''
        忘记密码:更改密码
        :return:
        '''
        MsgCode = get_cluster_value("forget_password_{}".format(self.phone), nodes=self.nodes)
        print(MsgCode)

        contents = {"phone":"{}".format(self.phone),"new_password": "666666","verification_code": "{}".format(MsgCode)}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'user.reset_password_by_verification_code',
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)

    def test_10_modifyPwd_sendMsg(self):
        '''
        修改密码:发送验证码
        :return:
        '''
        contents = {"phone": "{}".format(self.phone), "type": 3}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'user.send_verification_code',
                "access_token": '{}'.format(token),
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})
        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)
    def test_11_modifyPwdCheckCode_error(self):
        '''
        修改密码:校验验证码（验证码错误）
        :return:
        '''
        contents = {"phone": "{}".format(self.phone), "type": 3, "verification_code": "000000"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'user.check_verification_code',
                "access_token": '{}'.format(token),
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})
        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 110001, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)
    def test_12_modifyPwdCheckCode_right(self):
        '''
        修改密码:校验验证码（验证码正确）
        :return:
        '''
        MsgCode = get_cluster_value("forget_password_{}".format(self.phone), nodes=self.nodes)
        print(MsgCode)
        contents = {"phone": "{}".format(self.phone), "type": 3, "verification_code": "{}".format(MsgCode)}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'user.check_verification_code',
                "access_token": '{}'.format(token),
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})
        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)
    def test_13_modifyPwdByPhone(self):
        '''
        修改密码:通过验证码来重置密码
        :return:
        '''
        MsgCode = get_cluster_value("forget_password_{}".format(self.phone), nodes=self.nodes)
        print(MsgCode)
        contents = {"phone":"{}".format(self.phone),"new_password": "e10adc3949ba59abbe56e057f20f883e","verification_code": "{}".format(MsgCode)}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'user.reset_password_by_verification_code',
                "access_token": '{}'.format(token),
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)

    def test_14_modifyPwdByOld_olderror(self):
        '''
        修改密码:通过密码来重置密码_原密码错误
        :return:
        '''
        contents={"user_id":"{}".format(user_id),"old_password":"e10adc3949ba59abbe56e057f20f883f","new_password":"666666"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'user.reset_password_by_password',
                "access_token": '{}'.format(token),
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 110006, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)
    def test_15_modifyPwdByOld_right(self):
        '''
        修改密码:通过密码来重置密码_原密码错误
        :return:
        '''
        contents={"user_id":"{}".format(user_id),"old_password":"e10adc3949ba59abbe56e057f20f883e","new_password":"666666"}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'user.reset_password_by_password',
                "access_token": '{}'.format(token),
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})

        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)
    def test_16_modifyPhone_sendMsg_isRegister(self):
        """
        修改手机号:发送验证码_修改后手机号已注册
        :return:
        """
        contents = {"phone": "18657738815", "type": 5}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'user.send_verification_code',
                "access_token": '{}'.format(token),
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})
        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        # self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)
    def test_17_modifyPhone_sendMsg_NoRegister(self):
        """
        修改手机号:发送验证码_修改后手机号未注册
        :return:
        """

        contents = {"phone": "{}".format(self.new_phone), "type": 5}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'user.send_verification_code',
                "access_token": '{}'.format(token),
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})
        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)

    def test_18_modifyPhone_newphone(self):
        '''
        修改手机号:修改用户登录手机号
        :return:
        '''
        MsgCode = get_cluster_value("modify_phone_{}".format(self.new_phone), nodes=self.nodes)
        print(MsgCode)
        contents = {"new_phone": "{}".format(self.new_phone), "user_id": "{}".format(user_id), "verification_code": "{}".format(MsgCode)}
        data = {"app_id": 'b1044830052f359d',
                "timestamp": '2019-9-25 2:35:56',
                "version": '1.0',
                "client": 'android',
                "client_version": '4.0.1',
                "device_id": '123123',
                "method": 'user.modify_phone',
                "access_token": '{}'.format(token),
                "biz_content": '{}'.format(contents),
                }
        datas = dict(sorted(data.items(), key=lambda x: x[0], reverse=False))
        sign = new_hmac_md5(self.SigSecret, datas)
        datas.update({"sign": sign})
        res = requests.post(url=self.app_host, data=datas, headers=self.headers).json()
        self.assertTrue(res['code'] == 0, msg="校验code错误")
        miaoshu(url=self.app_host, method='post', data=datas, check={"code and message"}, respons=res)

    @unittest.skip('未完成用例，跳过')
    def test_19(self):
        '''
        发送验证码_发送次数
        :return:
        '''
        pass

    @unittest.skip('未完成用例，跳过')
    def test_20(self):
        '''
        验证码时效性_有效期之外
        :return:
        '''
        pass
    @unittest.skip('未完成用例，跳过')
    def test_21(self):
        '''，
        验证码已使用需作废不可重复使用
        :return:
        '''
        pass


    @unittest.skip('未完成用例，跳过')
    def test_22(self):
        '''
        语音验证码
        :return:
        '''


