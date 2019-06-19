#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/19 17:32
# @Author  : taojian
# @Site    : 
# @File    : test2_station_status_stats.py
# @Software: PyCharm
import unittest,time,json
from Base.runmethod import RunMethod
from Common.AES_CBC_PKCS5 import encrypt,decrypt
from Common.hmacmd5 import hmac_md5
from Common.Html_miaoshu import miaoshu
from ddt import ddt,data,unpack
@ddt
class Test_get_AccessToken(unittest.TestCase):
    host = 'http://123.157.219.74:8090/evcs/v1/'
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": ""}
    times = time.strftime("%Y%m%d%H%M%S", time.localtime())
    DataSecret = 'bed30540c54dda5d'
    SigSecret = 'a77b249029c22ee5'

    @classmethod
    def setUpClass(cls):
        host = cls.host
        lujing = 'query_token'
        text = '{"OperatorID":"MA35PU38X","OperatorSecret":"08083ebe79bc48a9"}'
        encrypt_data = encrypt(cls.DataSecret, text)
        data = {"OperatorID": "MA35PU38X",
                "Data": "{}".format(encrypt_data),
                "TimeStamp": "{}".format(cls.times),
                "Seq": "0001",
                "Sig": "{}".format(hmac_md5(cls.SigSecret, "MA35PU38X" + encrypt_data+ cls.times + "0001"))}

        headers = cls.headers
        res = RunMethod().run_main('post', host, lujing, data, headers)
        token=eval(decrypt(cls.DataSecret,res['data']))['AccessToken']
        cls.headers['Authorization']=token
        return cls.headers
    @data('{"LastQueryTiME":"","PageNo":,"PageSize":}',
          '{"LastQueryTiME":"","PageNo":3,"PageSize":}',
          '{"LastQueryTiME":"","PageNo":3,"PageSize":20}',
          '{"LastQueryTiME":"","PageNo":}',
          '{"LastQueryTiME":"","PageSize":}',
          '{"LastQueryTiME":""}',
          '')
    def test1_query_stations_info(self,text):
        '''
        查询充电站信息
        :return:
        '''
        host = self.host
        lujing = 'query_stations_info'
        # text = '{"LastQueryTiME":"","PageNo":,"PageSize":}'
        encrypt_data = encrypt(self.DataSecret, text)
        data = {
            "OperatorID": "MA35PU38X",
            "Data": "{}".format(encrypt_data),
            "TimeStamp": "{}".format(self.times),
            "Seq": "0001",
            "Sig": "{}".format(hmac_md5(self.SigSecret, "MA35PU38X" + encrypt_data+ self.times + "0001"))}
        headers = self.headers
        res = RunMethod().run_main('post', host, lujing, data, headers)
        miaoshu(url=host + lujing, method="post", data=data, check="{}", respons=res)

    def test2_notification_stationStatus(self):
        '''
        设备状态变化推送
        :return:
        '''
        host = self.host
        lujing = 'notification_stationStatus'
        text = '{"OperatorID":"MA35PU38X","OperatorSecret":"08083ebe79bc48a9"}'
        encrypt_data = encrypt(self.DataSecret, text)
        data = {
            "OperatorID": "MA35PU38X",
            "Data": "{}".format(encrypt_data),
            "TimeStamp": "{}".format(self.times),
            "Seq": "0001",
            "Sig": "{}".format(hmac_md5(self.SigSecret, "MA35PU38X" + encrypt_data + self.times + "0001"))}
        headers = self.headers
        res = RunMethod().run_main('post', host, lujing, data, headers)
        miaoshu(url=host + lujing, method="post", data=data, check="{}", respons=res)

    def test3_query_stations_status(self):
        '''
        查询充电站信息
        :return:
        '''
        host = self.host
        lujing = 'query_stations_info'
        text = '{"OperatorID":"MA35PU38X","OperatorSecret":"08083ebe79bc48a9"}'
        encrypt_data = encrypt(self.DataSecret, text)
        data = {
            "OperatorID": "MA35PU38X",
            "Data": "{}".format(encrypt_data),
            "TimeStamp": "{}".format(self.times),
            "Seq": "0001",
            "Sig": "{}".format(hmac_md5(self.SigSecret, "MA35PU38X" + encrypt_data + self.times + "0001"))}
        headers = self.headers
        res = RunMethod().run_main('post', host, lujing, data, headers)
        miaoshu(url=host + lujing, method="post", data=data, check="{}", respons=res)

    def test4_query_stations_stats(self):
        '''
        查询充电站信息
        :return:
        '''
        host = self.host
        lujing = 'query_stations_stats'
        text = '{"OperatorID":"MA35PU38X","OperatorSecret":"08083ebe79bc48a9"}'
        encrypt_data = encrypt(self.DataSecret, text)
        data = {
            "OperatorID": "MA35PU38X",
            "Data": "{}".format(encrypt_data),
            "TimeStamp": "{}".format(self.times),
            "Seq": "0001",
            "Sig": "{}".format(hmac_md5(self.SigSecret, "MA35PU38X" + encrypt_data + self.times + "0001"))}
        headers = self.headers
        res = RunMethod().run_main('post', host, lujing, data, headers)
        miaoshu(url=host + lujing, method="post", data=data, check="{}", respons=res)

    def test_query_stations_info(self):
        '''
        查询充电站信息
        :return:
        '''
        host = self.host
        lujing = 'query_stations_info'
        text = '{"OperatorID":"MA35PU38X","OperatorSecret":"08083ebe79bc48a9"}'
        encrypt_data = encrypt(self.DataSecret, text)
        data = {
            "OperatorID": "MA35PU38X",
            "Data": "{}".format(encrypt_data),
            "TimeStamp": "{}".format(self.times),
            "Seq": "0001",
            "Sig": "{}".format(hmac_md5(self.SigSecret, "MA35PU38X" + encrypt_data + self.times + "0001"))}
        headers = self.headers
        res = RunMethod().run_main('post', host, lujing, data, headers)
        miaoshu(url=host + lujing, method="post", data=data, check="{}", respons=res)




if __name__=='__main__':
    unittest.main()