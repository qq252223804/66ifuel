''''
# 完善登陆模块/类似模块接口测试
采取ddt+自动读取
@data 传入数据 将接口结果写入到excel
'''
import unittest, yaml,os
from utx import *
# from ddt import ddt,data,unpack
from Base.runmethod import RunMethod

yaml.warnings({'YAMLLoadWarning': False})

print(os.path.dirname('conf.yaml'))
class login(unittest.TestCase):
    with open('{}'.format(os.path.join(os.path.dirname(os.getcwd()),'Config')+'\conf.yaml'), 'r', encoding="utf-8") as r:
        config = yaml.load(r)  # 解析并读写yaml文件
        app_host = config['app_host']
        headers = config['app_headers']
    @data({"phone": "18657738815", "password": "dc483e80a7a0bd9ef71d8cf973673924"},
          {"phone": "18657738815", "password": "a123456"},
          {"phone": "18600000000", "password": "a123456"},
          {"phone": "", "password": "a123456"},
          {"phone": "18657738815", "password": ""},
            {},unpack=False)
    def test_login_pwd(self, data):
        '''
        66快充登录:密码方式
        :param datas:
        :return:
        '''
        host = self.app_host
        headers = self.headers
        lujing = '/customer/v1/member/login'
        res = RunMethod().run_main('post', host, lujing, data, headers)
        # self.assertTrue(res['code'] == 0, msg=res['msg'])
        print(res)


if __name__ == "__main__":
    unittest.main()
