#!/usr/bin/python
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
import requests
@ddt
class Test_statinon_info(unittest.TestCase):
    host = 'http://106.14.157.148:8090/evcs/v1/'
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": ""}
    times = time.strftime("%Y%m%d%H%M%S", time.localtime())
    DataSecret = '78BxIeGT7zQYuN12'
    SigSecret = 'b8aEBQGiyFyPmjSc'
    operator_id='359705330'
    operatorSecret='gZjHb3GK5ye5en1v'

    stationID=22222
    connID = 12100

    @classmethod
    def setUpClass(cls):
        host = cls.host
        lujing = 'query_token'
        text = '{"OperatorID":"359705330","OperatorSecret":"gZjHb3GK5ye5en1v"}'
        encrypt_data = encrypt(cls.DataSecret, text)
        print(encrypt_data)
        data = {"OperatorID": cls.operator_id,
                "Data": "{}".format(encrypt_data),
                "TimeStamp": "{}".format(cls.times),
                "Seq": "0001",
                "Sig": "{}".format(hmac_md5(cls.SigSecret, cls.operator_id+ encrypt_data+ cls.times + "0001"))}

        headers = cls.headers
        res = RunMethod().run_main('post', host, lujing, data, headers)

        token=eval(decrypt(cls.DataSecret,res['Data']))['AccessToken']
        cls.headers['Authorization']='Bearer ' +token
        return cls.headers


    @data('{"LastQueryTiME":"","PageNo":,"PageSize":}',
          '{"LastQueryTiME":"","PageNo":1,"PageSize":10}',
          '{"LastQueryTiME":"","PageNo":3,"PageSize":20}',
          '{"PageNo":}',
          '{"PageSize":}',
          '{"LastQueryTiME":""}',
          '')
    def test1_query_stations_info(self,text):

        '''
        查询充电站信息
        :return:
        '''
        print(self.headers)
        host = self.host
        lujing = 'query_stations_info'
        encrypt_data = encrypt(self.DataSecret, text)
        data = {
            "OperatorID": self.operator_id,
            "Data": "{}".format(encrypt_data),
            "TimeStamp": "{}".format(self.times),
            "Seq": "0001",
            "Sig": "{}".format(hmac_md5(self.SigSecret, self.operator_id + encrypt_data+ self.times + "0001"))}
        headers = self.headers
        res = RunMethod().run_main('post', host, lujing, data, headers)
        miaoshu(url=host + lujing, method="post", data=text, check="{Ret and Msg}", respons=res)
    # @unittest.skip("数据需求方实现此接口,基础设施运营商方调用")
    def test2_notification_stationStatus(self):
        '''
        设备状态变化推送
        :return:
        '''
        host = self.host
        lujing = 'notification_stationStatus'
        text = {"ConnectorStatusInfo":[{"ConnectorID":"{}".format(self.connID),"Status":1}]}
        encrypt_data = encrypt(self.DataSecret, str(text))
        data = {
            "OperatorID": self.operator_id,
            "Data": "{}".format(encrypt_data),
            "TimeStamp": "{}".format(self.times),
            "Seq": "0001",
            "Sig": "{}".format(hmac_md5(self.SigSecret, self.operator_id+ encrypt_data + self.times + "0001"))}
        headers = self.headers

        res = RunMethod().run_main('post', host, lujing, data, headers)
        miaoshu(url=host + lujing, method="post", data=text, check="{'Ret': 0, 'Msg': '请求成功',}", respons=res)
        self.assertTrue(res.status_code == 200, msg="状态码不正确")


    def test3_query_station_status(self):
        '''
        设备接口状态查询
        :return:
        '''
        host = self.host
        lujing = 'query_station_status'
        text = {"StationIDs":["{}".format(self.stationID)]}
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
        miaoshu(url=host + lujing, method="post", data=text, check="{'StationIDs', 'ConnectorStatusInfos'}", respons=undata)
        self.assertTrue(res['Ret'] == 0, msg="状态码不正确")
        self.assertIn('StationStatusInfos', undata, msg='返回内容不正确')
    #
    def test4_query_stations_stats(self):
        '''
        查询统计信息
        :return:
        '''
        host = self.host
        lujing = 'query_station_stats'
        text = {"StationID":"{}".format(self.stationID),"StartTime":"2019-10-20","EndTime":"2019-11-20"}

        encrypt_data = encrypt(self.DataSecret, str(text))
        data = {
            "OperatorID": self.operator_id,
            "Data": "{}".format(encrypt_data),
            "TimeStamp": "{}".format(self.times),
            "Seq": "0001",
            "Sig": "{}".format(hmac_md5(self.SigSecret, self.operator_id + encrypt_data + self.times + "0001"))}
        headers = self.headers
        res = RunMethod().run_main('post', host, lujing, data, headers)
        # res = requests.post(url=host + lujing, json=data, headers=headers)
        undata = eval(decrypt(self.DataSecret, res['Data']))
        miaoshu(url=host + lujing, method="post", data=text, check="{'Ret': 0, 'Msg': '请求成功',}", respons=undata)
        self.assertTrue(res['Ret'] == 0, msg="状态码不正确")
        self.assertIn('StationStatsInfo',undata,msg='返回内容不正确')





if __name__=='__main__':
    unittest.main()