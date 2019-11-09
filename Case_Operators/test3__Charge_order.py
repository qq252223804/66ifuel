#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 15:23
# @Author  : taojian
# @Site    : 
# @File    : test3__Charge_order.py
# @Software: PyCharm

import time
import unittest
import uuid


from Base.runmethod import RunMethod
from Common.AES_CBC_PKCS5 import encrypt, decrypt
from Common.Html_miaoshu import miaoshu
from Common.hmacmd5 import hmac_md5
from ddt import ddt,data,unpack
@ddt
class Test_Charge_order(unittest.TestCase):
    host = 'http://106.14.157.148:8090/evcs/v1/'
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": ""}
    times = time.strftime("%Y%m%d%H%M%S", time.localtime())
    # order_StartTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # order_EndTime=
    DataSecret = '78BxIeGT7zQYuN12'
    SigSecret = 'b8aEBQGiyFyPmjSc'
    operator_id = '359705330'
    uid = uuid.uuid1()
    uid1 = uuid.uuid1()
    # order='745467123024005023X0L80J7FG'
    # connID='1601068'
    order= ''.join(str(uid).split('-'))[0:22]

    EquipAuthSeq=operator_id+''.join(str(uid).split('-'))[0:22]
    EquipBizSeq=operator_id+''.join(str(uid1).split('-'))[0:22]

    connID=12100
    @classmethod
    def setUpClass(cls):
        host = cls.host
        lujing = 'query_token'
        text = '{"OperatorID":"359705330","OperatorSecret":"gZjHb3GK5ye5en1v"}'
        encrypt_data = encrypt(cls.DataSecret, text)
        data = {"OperatorID": cls.operator_id,
                "Data": "{}".format(encrypt_data),
                "TimeStamp": "{}".format(cls.times),
                "Seq": "0001",
                "Sig": "{}".format(hmac_md5(cls.SigSecret, cls.operator_id + encrypt_data+ cls.times + "0001"))}
        headers = cls.headers
        res = RunMethod().run_main('post', host, lujing, data, headers)
        # res = requests.post(url=host + lujing, data=data, headers=header
        print(res)
        token=eval(decrypt(cls.DataSecret,res['Data']))['AccessToken']
        cls.headers['Authorization']='Bearer ' +token
        return cls.headers

    # @unittest.skip('跳过')
    def test1_query_equip_auth(self):
        '''
        请求设备认证
        :return:
        '''
        host = self.host
        lujing = 'query_equip_auth'
        text = {"EquipAuthSeq":"{}".format(self.EquipAuthSeq),"ConnectorID":self.connID}
        encrypt_data = encrypt(self.DataSecret, str(text))
        data = {
            "OperatorID": self.operator_id,
            "Data": "{}".format(encrypt_data),
            "TimeStamp": "{}".format(self.times),
            "Seq": "0001",
            "Sig": "{}".format(hmac_md5(self.SigSecret, self.operator_id + encrypt_data + self.times + "0001"))}
        headers = self.headers
        res = RunMethod().run_main('post', host, lujing, data, headers)
        undata = eval(decrypt(self.DataSecret, res['Data']))
        miaoshu(url=host + lujing, method="post", data=text, check="{Ret and Msg}", respons=undata)

    def test2_query_equip_business_policy(self):
        '''
        查询业务策略信息结果
        :return:
        '''
        host = self.host
        lujing = 'query_equip_business_policy'
        text = {"EquipBizSeq": "{}".format(self.EquipBizSeq), "ConnectorID": self.connID}

        encrypt_data = encrypt(self.DataSecret, str(text))
        data = {
            "OperatorID": self.operator_id,
            "Data": "{}".format(encrypt_data),
            "TimeStamp": "{}".format(self.times),
            "Seq": "0001",
            "Sig": "{}".format(hmac_md5(self.SigSecret, self.operator_id + encrypt_data + self.times + "0001"))}
        headers = self.headers
        res = RunMethod().run_main('post', host, lujing, data, headers)
        undata = eval(decrypt(self.DataSecret, res['Data']))
        miaoshu(url=host + lujing, method="post", data=text, check="{Ret and Msg}", respons=undata)

    # # @unittest.skip('跳过')
    def test3_query_start_charge(self):
        '''
        请求开始充电
        :return:
        '''
        host = self.host
        lujing = 'query_start_charge'
        text={"StartChargeSeq":"{}".format(self.order),"ConnectorID":"{}".format(self.connID)}
        encrypt_data = encrypt(self.DataSecret,str(text))
        data = {
            "OperatorID": self.operator_id,
            "Data": "{}".format(encrypt_data),
            "TimeStamp": "{}".format(self.times),
            "Seq": "0001",
            "Sig": "{}".format(hmac_md5(self.SigSecret, self.operator_id + encrypt_data + self.times + "0001"))}
        headers = self.headers
        res = RunMethod().run_main('post', host, lujing, data, headers)
        undata = eval(decrypt(self.DataSecret, res['Data']))
        miaoshu(url=host + lujing, method="post", data=text, check="{Ret and Msg}", respons=undata)
        self.assertTrue(res['Ret'] == 0, msg="状态码不正确")
        self.assertTrue(res['Msg'] == "请求成功", msg="返回msg不正确")

    @data({"StartChargeSeq": "{}".format(order), "ConnectorID": "{}".format(connID),"StartChargeSeqStat":1,"StartTime":times},
        {"StartChargeSeq": "{}".format(order), "ConnectorID": "{}".format(connID),"StartChargeSeqStat":2,"StartTime":times},
        {"StartChargeSeq": "{}".format(order), "ConnectorID": "{}".format(connID), "StartChargeSeqStat": 3,"StartTime": times},
        {"StartChargeSeq": "{}".format(order), "ConnectorID": "{}".format(connID), "StartChargeSeqStat": 4,"StartTime": times},
        {"StartChargeSeq": "{}".format(order), "ConnectorID": "{}".format(connID), "StartChargeSeqStat": 5,"StartTime": times}
          )
    def test4_query_notification_start_charge_result(self,text):
        '''
        推送充电结果
        :return:
        '''
        host = self.host
        lujing = 'query_notification_start_charge_result'
        # text = {"StartChargeSeq": "{}".format(self.order), "ConnectorID": "{}".format(self.connID)}
        encrypt_data = encrypt(self.DataSecret, str(text))
        data = {
            "OperatorID": self.operator_id,
            "Data": "{}".format(encrypt_data),
            "TimeStamp": "{}".format(self.times),
            "Seq": "0001",
            "Sig": "{}".format(hmac_md5(self.SigSecret, self.operator_id + encrypt_data + self.times + "0001"))}
        headers = self.headers
        res = RunMethod().run_main('post', host, lujing, data, headers)
        print(res)
        # undata = eval(decrypt(self.DataSecret, res['Data']))
        miaoshu(url=host + lujing, method="post", data=text, check="{Ret and Msg}", respons=res)
        # self.assertTrue(res['Ret'] == 0, msg="状态码不正确")
        # self.assertTrue(res['Msg'] == "请求成功", msg="返回msg不正确")
    # @unittest.skip('跳过')
    def test2_query_equip_charge_status(self):
        '''
        查询充电状态
        :return:
        '''
        host = self.host
        lujing = 'query_equip_charge_status'
        text = {"StartChargeSeq":  "{}".format(self.order)}
        encrypt_data = encrypt(self.DataSecret, str(text))
        data = {
            "OperatorID": self.operator_id,
            "Data": "{}".format(encrypt_data),
            "TimeStamp": "{}".format(self.times),
            "Seq": "0001",
            "Sig": "{}".format(hmac_md5(self.SigSecret, self.operator_id + encrypt_data + self.times + "0001"))}
        headers = self.headers
        res = RunMethod().run_main('post', host, lujing, data, headers)
        miaoshu(url=host + lujing, method="post", data=text, check="{Ret and Msg}", respons=res)
        self.assertTrue(res['Ret'] == 0, msg="状态码不正确")
        self.assertTrue(res['Msg'] == "请求成功", msg="返回msg不正确")


    # @unittest.skip('跳过')
    # def test3_query_stop_charge(self):
    #     '''
    #     请求停止充电
    #     :return:
    #     '''
    #     host = self.host
    #     lujing = 'query_stop_charge'
    #     text = {"StartChargeSeq": "{}".format(self.order),"ConnectorID":"{}".format(self.connID)}
    #     str1 = str(text)
    #     encrypt_data = encrypt(self.DataSecret, str1)
    #     data = {
    #         "OperatorID": "745467123",
    #         "Data": "{}".format(encrypt_data),
    #         "TimeStamp": "{}".format(self.times),
    #         "Seq": "0001",
    #         "Sig": "{}".format(hmac_md5(self.SigSecret, "745467123" + encrypt_data + self.times + "0001"))}
    #     headers = self.headers
    #     res = RunMethod().run_main('post', host, lujing, data, headers)
    #     miaoshu(url=host + lujing, method="post", data=text, check="{Ret and Msg}", respons=res)
    #     self.assertTrue(res['Ret'] == 0, msg="状态码不正确")
    #     self.assertTrue(res['Msg'] == "请求成功", msg="返回msg不正确")



if __name__=='__main__':
    unittest.main()
