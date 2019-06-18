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
        data={"OperatorID":"12345ABCD",
              "Data":"mYvffpNoFf4E/ZTC1tOw4xAtlzJ8iDQ7piNNiKgQpHlhTiJwbO5Ehc1CPOF1fk9JngohSuu7jgBIEPvCb2PILg==",
              "TimeStamp":"20170822113232",
              "Seq":"0001",
              "Sig":"C863EB33E0D56A89182B4B987E48D369"}
        headers=self.headers
        res=RunMethod().run_main('post', host, lujing, data, headers)
        print(res)

if __name__=='__main__':
    unittest.main()
