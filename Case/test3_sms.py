'''
验证码相关的接口,单接口测试
'''
import unittest,os
from utx import *
from Base.runmethod import RunMethod
import yaml,time
yaml.warnings({'YAMLLoadWarning': False})

# @skip
class sms(unittest.TestCase):
    def setUp(self):
        self.run = RunMethod()
        with open('{}'.format(os.path.join(os.path.dirname(os.getcwd()),'Config')+'\conf.yaml'), "r", encoding="utf-8") as r:
            config = yaml.load(r)  # 解析并读写yaml文件
            self.app_host=config['app_host']
            self.headers=config['app_headers']

    def tearDown(self):
        pass

    @data({"phone":"18657738815","type":3,"voice":0},
          {"phone":"18657738816","type":1,"voice":0},
          {"phone":"18657738817", "type": 2, "voice": 0},
          {},unpack=False)
    def test_send_sms(self,data):
        """
        登录页发送短信验证码
        :return:
        """
        # time.sleep()
        host = self.app_host
        headers = self.headers
        lujing = '/system/v1/message_code/send'
        res = self.run.run_main('post', host, lujing,data, headers)
        # self.assertTrue(res['code'] == 0, msg=res['msg'])
        print(res)



if __name__ == "__main__":
    unittest.main()
