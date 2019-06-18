#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 12:26
# @Author  : taojian
# @Site    : 
# @File    : test1_get_AccessToken.py
# @Software: PyCharm


import unittest,time,json
from Base.runmethod import RunMethod

class Test_get_AccessToken(unittest.TestCase):
    host='http://192.168.3.142:8090/evcs/v1/'
    headers={
        "Content-Type": "application/json; charset=utf-8"}
    times = time.strftime("%Y%m%d%H%M%S", time.localtime())

    def test_alldata_right(self):
        '''
        检验所有参数正确
        :return:
        '''
        host=self.host
        lujing='query_token'
        data={"OperatorID":"MA35PU38X",
              "Data":"2/cNwWYNSKtY94JOwMyBdNfXm8xlA+CjCJGFm1+/Hr53BWx9N2Kt5qiHBaWEn3Qth7am4MTQ8t1d9TE884ht6g==",
              "TimeStamp":"20190618174537",
              "Seq":"0001",
              "Sig":"43932EB5EBEAB5598525FDFE9B58C8EC"}
        headers=self.headers
        res=RunMethod().run_main('post', host, lujing, data, headers)
        print(res)

if __name__=='__main__':
    unittest.main()
