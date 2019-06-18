import unittest, yaml,os
from utx import *
# from ddt import ddt,data,unpack
from Base.runmethod import RunMethod
from Common.variables_func import cms_cookies

yaml.warnings({'YAMLLoadWarning': False})

@skip
class station(unittest.TestCase):



    @classmethod
    def setUpClass(cls):
        with open('{}'.format(os.path.join(os.path.dirname(os.getcwd()),'Config')+'\conf.yaml'), 'r', encoding="utf-8") as r:
            config = yaml.load(r)  # 解析并读写yaml文件
            cls.app_host = config['cms_host']
        cls.session = cms_cookies()

    def test_add_station(self):
        '''
        添加站点
        :return:
        '''
        url=self.app_host+'/station/station/create'
        data={}
        res=self.session.request('post',url=url,data=data)
        print(res.text())

if __name__ == "__main__":
    unittest.main()
