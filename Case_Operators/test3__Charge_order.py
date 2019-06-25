#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 15:23
# @Author  : taojian
# @Site    : 
# @File    : test3__Charge_order.py
# @Software: PyCharm

import unittest,time,json
from Base.runmethod import RunMethod
from Common.AES_CBC_PKCS5 import encrypt,decrypt
from Common.hmacmd5 import hmac_md5
from Common.Html_miaoshu import miaoshu
from ddt import ddt,data,unpack
import time
import uuid

class Test_Charge_order(unittest.TestCase):
    host = 'http://123.157.219.74:8090/evcs/v1/'
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": ""}
    times = time.strftime("%Y%m%d%H%M%S", time.localtime())
    # order_StartTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # order_EndTime=
    DataSecret = 'b8f0549a8efbacfc'
    SigSecret = '8h9sf4zd5cbtlu8x'

    uid = uuid.uuid1()
    order = ''.join(str(uid).split('-'))[0:27]
    connID=1800688
    @classmethod
    def setUpClass(cls):
        host = cls.host
        lujing = 'query_token'
        text = '{"OperatorID":"745467123","OperatorSecret":"vfkh4k740lfg88kq"}'
        encrypt_data = encrypt(cls.DataSecret, text)
        data = {"OperatorID": "745467123",
                "Data": "{}".format(encrypt_data),
                "TimeStamp": "{}".format(cls.times),
                "Seq": "0001",
                "Sig": "{}".format(hmac_md5(cls.SigSecret, "745467123" + encrypt_data+ cls.times + "0001"))}

        headers = cls.headers
        res = RunMethod().run_main('post', host, lujing, data, headers)
        token=eval(decrypt(cls.DataSecret,res['Data']))['AccessToken']
        cls.headers['Authorization']='Bearer ' +token
        return cls.headers


    def test1_query_start_charge(self):
        '''
        请求开始充电
        :return:
        '''
        host = self.host
        lujing = 'query_start_charge'
        text={"StartChargeSeq":"{}".format(self.order),"ConnectoID":"{}".format(self.connID),"QRCode":"http://www.66ifuel.com/scans/result.html?data=1800688"}
        str1=str(text)
        encrypt_data = encrypt(self.DataSecret,str1)
        data = {
            "OperatorID": "745467123",
            "Data": "{}".format(encrypt_data),
            "TimeStamp": "{}".format(self.times),
            "Seq": "0001",
            "Sig": "{}".format(hmac_md5(self.SigSecret, "745467123" + encrypt_data + self.times + "0001"))}
        headers = self.headers
        res = RunMethod().run_main('post', host, lujing, data, headers)

        miaoshu(url=host + lujing, method="post", data=text, check="{Ret and Msg}", respons=res)
        self.assertTrue(res['Ret'] == 0, msg="状态码不正确")
        self.assertTrue(res['Msg'] == "请求成功", msg="返回msg不正确")
    def test2_query_equip_charge_status(self):
        '''
        查询充电状态
        :return:
        '''
        host = self.host
        lujing = 'query_equip_charge_status'
        text = {"StartChargeSeq": "201711271121090001"}
        str1 = str(text)
        encrypt_data = encrypt(self.DataSecret, str1)
        data = {
            "OperatorID": "745467123",
            "Data": "{}".format(encrypt_data),
            "TimeStamp": "{}".format(self.times),
            "Seq": "0001",
            "Sig": "{}".format(hmac_md5(self.SigSecret, "745467123" + encrypt_data + self.times + "0001"))}
        headers = self.headers
        res = RunMethod().run_main('post', host, lujing, data, headers)
        miaoshu(url=host + lujing, method="post", data=text, check="{Ret and Msg}", respons=res)
        self.assertTrue(res['Ret'] == 0, msg="状态码不正确")
        self.assertTrue(res['Msg'] == "请求成功", msg="返回msg不正确")
    def test3_query_stop_charge(self):
        '''
        请求停止充电
        :return:
        '''
        host = self.host
        lujing = 'query_stop_charge'
        text = {"StartChargeSeq": "{}".format(self.order),"ConnectoID":"{}".format(self.connID)}
        str1 = str(text)
        encrypt_data = encrypt(self.DataSecret, str1)
        data = {
            "OperatorID": "745467123",
            "Data": "{}".format(encrypt_data),
            "TimeStamp": "{}".format(self.times),
            "Seq": "0001",
            "Sig": "{}".format(hmac_md5(self.SigSecret, "745467123" + encrypt_data + self.times + "0001"))}
        headers = self.headers
        res = RunMethod().run_main('post', host, lujing, data, headers)
        miaoshu(url=host + lujing, method="post", data=text, check="{Ret and Msg}", respons=res)
        self.assertTrue(res['Ret'] == 0, msg="状态码不正确")
        self.assertTrue(res['Msg'] == "请求成功", msg="返回msg不正确")



if __name__=='__main__':
    unittest.main()
