import unittest, string,random
# from ddt import ddt,data,unpack
from Common.SQL_execute import *
from Common.variables_func import *

yaml.warnings({'YAMLLoadWarning': False})


class login(unittest.TestCase):
    with open('{}'.format(os.path.join(os.path.dirname(os.getcwd()),'Config')+'\conf.yaml'), 'r', encoding="utf-8") as r:
        config = yaml.load(r)  # 解析并读写yaml文件
        app_host = config['app_host']
        headers = config['app_headers']

    #生成随机手机号
    numbers = list(string.digits)
    mobile = ['130', '132', '150', '155', '177', '186']
    phone=random.choice(mobile) + ''.join(random.sample(numbers, 8))
    def test_check_user(self):
        '''
        验证手机号是否注册
        :return:
        '''
        host = self.app_host
        headers = self.headers
        lujing = '/customer/v1/member/check_phone'
        print(self.phone)
        data = {"phone": self.phone}
        res = RunMethod().run_main('post', host, lujing, data, headers)
        self.assertTrue(res['code'] == 0, msg=res['msg'])
        print(res)

    def test_send_CreatPhone_mess(self):
        '''
        发送注册验证码
        :return:
        '''
        host = self.app_host
        headers = self.headers
        lujing = '/system/v1/message_code/send'
        data = {"phone": self.phone, "type": 1, "voice": 0}

        res = RunMethod().run_main('post', host,lujing, data,headers)
        self.assertTrue(res['code'] == 0, msg=res['msg'])
        print(res)

    def test_creat_user(self):
        '''
        注册用户-检查验证码
        :return:
        '''
        sql="select validCode FROM cp_messagecode WHERE phone={};".format(self.phone)
        code=mysql_getrows(sql, number='one')
        host = self.app_host
        headers = self.headers
        lujing = '/system/v1/message_code/check'
        data = {"phone": self.phone, "code":code[0]}
        res = RunMethod().run_main('post', host, lujing, data, headers)
        self.assertTrue(res['code'] == 0, msg=res['msg'])
        print(res)
        code_session=res['data']['code_session']
        # print(code_session)
        write_yaml_variable("code_session", code_session)

    def test_set_user_pwd(self):
        '''
        注册用户-设置密码
        :param datas:
        :return:
        '''
        host = self.app_host
        a='86442603'
        id=a+''.join(random.sample(self.numbers, 8))
        device_id={"66-device-id":id}
        headers=eval(self.headers)
        headers.update(device_id)
        # print(headers)
        lujing = '/customer/v1/member/create'
        data = {"phone":self.phone,"password":"dc483e80a7a0bd9ef71d8cf973673924",
                "code_session":get_yaml_variable("code_session"),
                "invitation_code":self.phone}
        res = RunMethod().run_main('post', host,lujing,data,headers)
        self.assertTrue(res['code'] == 0, msg=res['msg'])
        print(res)

    def test_login_pwd(self):
        '''
        66快充登录:刚注册进行密码登录
        :return:
        '''
        host = self.app_host
        headers = self.headers
        lujing = '/customer/v1/member/login'
        data={"phone":self.phone,"password":"dc483e80a7a0bd9ef71d8cf973673924"}
        res = RunMethod().run_main('post', host, lujing, data, headers)
        self.assertTrue(res['code'] == 0, msg=res['msg'])
        print(res)

if __name__ == "__main__":
    unittest.main()

