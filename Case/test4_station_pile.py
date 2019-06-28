import unittest, yaml,os

# from ddt import ddt,data,unpack
from Common.variables_func import cms_cookies
from Common.Html_miaoshu import miaoshu
yaml.warnings({'YAMLLoadWarning': False})
import random
from Common.variables_func import get_yaml_variable
from Common.SQL_execute import mysql_getrows

# @unittest.skip('未完成用例，跳过')
class station(unittest.TestCase):



    @classmethod
    def setUpClass(cls):
        with open('{}'.format(os.path.join(os.path.dirname(os.getcwd()),'Config')+'\conf.yaml'), 'r', encoding="utf-8") as r:
            config = yaml.load(r)  # 解析并读写yaml文件
            cls.app_host = config['cms_host']
            cls.cms_headers=eval(config['cms_headers'])
        cls.session = cms_cookies()
        cls.cms_headers['Authorization'] =get_yaml_variable('Authorization')

        cls.stationName="野风时代"+str(random.randint(1,1000))
        cls.spot_code=random.randint(100000,999999)
        return cls.cms_headers

    def test1_add_station(self):
        '''
        添加站点
        :return:
        '''

        url=self.app_host+'/api/station/station/create'
        data={"address":"野风现代中心B座1001室","address_en":"","area":"41","charge_speed_type":"1","city":"330100","ext_info":"","lat":"30.285421","lng":"120.176592",
              "name":self.stationName,"name_en":"","parking_fee_info":"","type":"0"}
        headers=self.cms_headers
        res=self.session.request('post',url=url,data=data,headers=headers).json()
        self.assertTrue(res['code']==200,msg=res)
        miaoshu(url=url,method='post',data=data,check={'code': 200,},respons=res)

    def test2_update_station(self):
        '''
        编辑站点
        :return:
        '''
        sql="select id from cp_station where name='{}'".format(self.stationName)
        station_id=mysql_getrows(sql,number='one')[0]
        url = self.app_host + '/api/station/station/update'
        data = {"address": "野风现代中心B座1001室", "address_en": "", "area": "41", "charge_speed_type": "1", "city": "330100",
                "ext_info": "", "lat": "30.285421", "lng": "120.176592",
                "name": self.stationName, "name_en": "", "parking_fee_info": "免停2小时", "station_id": "{}".format(station_id),"type":"0"}
        headers = self.cms_headers
        res = self.session.request('post',url=url,data=data,headers=headers).json()
        self.assertTrue(res['code'] == 200, msg=res)
        miaoshu(url=url, method='post', data=data, check={'code': 200,}, respons=res)
    def test3_get_station_list(self):
        '''
        查询充电站列表
        :return:
        '''

        url = self.app_host + '/api/station/station/list'
        data = {"area":"","city":"","page":"1","page_size":"10","type":"0"}
        headers = self.cms_headers
        res = self.session.request('post',url=url,data=data,headers=headers).json()
        self.assertTrue(res['code'] == 200, msg=res)
        miaoshu(url=url, method='post', data=data, check={'code': 200, }, respons=res)
    def test4_get_static_brand(self):
        '''
        获取桩品牌信息
        :return:
        '''

        url = self.app_host + '/api/station/static/brand'
        data = ""
        headers = self.cms_headers
        res = self.session.request('post',url=url,data=data,headers=headers).json()
        self.assertTrue(res['code'] == 200, msg=res)
        miaoshu(url=url, method='post', data=data, check={'code': 200, }, respons=res)
    def test5_add_spot(self):
        '''
        添加充电桩
        :return:
        '''

        url = self.app_host + '/api/station/station/list'
        data = {"area":"","city":"","page":"1","page_size":"10","type":"0"}
        headers = self.cms_headers
        res = self.session.request('post',url=url,data=data,headers=headers).json()
        self.assertTrue(res['code'] == 200, msg=res)
        miaoshu(url=url, method='post', data=data, check={'code': 200, }, respons=res)

    def test6_add_spot_pile(self):
        '''
        添加桩与枪
        :return:
        '''
        sql = "select id from cp_station where name='{}'".format(self.stationName)
        station_id = mysql_getrows(sql, number='one')[0]
        url = self.app_host + '/api/station/charging-spot/edit'
        data = {
	"parking_lock%5Bbrand%5D": "科士达",
	"parking_lock%5Bcommunication_board_sn%5D": "000000",
	"parking_lock%5Bkey%5D": "000000",
	"parking_lock%5Bmac%5D": "000000",
	"parking_lock%5Bmodel%5D": "",
	"parking_lock%5Bscrapped_time%5D": "",
	"parking_lock%5Bstart_time%5D": "",
	"parking_lock%5Bversion%5D": "V1",
	"pile%5Bbrand%5D": "10001",
	"pile%5Bcharge_no%5D": "1",
	"pile%5Bcharge_type%5D": "1",
	"pile%5Bsn%5D": "{}".format(self.spot_code),
	"pile%5Bversion%5D": "1",
	"pile_charge_ext%5Bbrand%5D": "",
	"pile_charge_ext%5Bcharge_time%5D": "",
	"pile_charge_ext%5Bcurrent%5D": "",
	"pile_charge_ext%5Blength%5D": "",
	"pile_charge_ext%5Bmodel%5D": "",
	"pile_charge_ext%5Bproduction_time%5D": "",
	"pile_charge_ext%5Bscrap_time%5D": "",
	"pile_charge_ext%5Buse_time%5D": "",
	"pile_charge_ext%5Bvoltage%5D": "",
	"pile_ext%5Bbrand%5D": "科士达",
	"pile_ext%5Bcharge_type%5D": "1",
	"pile_ext%5Bcurrent%5D": "",
	"pile_ext%5Bmodel%5D": "",
	"pile_ext%5Bpile_no%5D": "1",
	"pile_ext%5Bpower%5D": "",
	"pile_ext%5Bproduction_time%5D": "",
	"pile_ext%5Brated_input%5D": "",
	"pile_ext%5Bsn%5D": "",
	"pile_ext%5Bsoft_version%5D": "",
	"pile_ext%5Bversion%5D": "1",
	"pile_ext%5Bvoltage%5D": "",
	"sort": "1",
	"station_id": "{}".format(station_id),
	"vlpr%5Baccept_at%5D": "",
	"vlpr%5Bbrand%5D": "",
	"vlpr%5Bdiscard_at%5D": "",
	"vlpr%5Bip%5D": "",
	"vlpr%5Blogin_pwd%5D": "",
	"vlpr%5Blogin_username%5D": "",
	"vlpr%5Bmodel%5D": "",
	"vlpr%5Bname%5D": "",
	"vlpr%5Bport%5D": "",
	"vlpr%5Bsn%5D": ""
}
        headers = self.cms_headers
        res = self.session.request('post',url=url,data=data,headers=headers).json()
        self.assertTrue(res['code'] == 200, msg=res)
        miaoshu(url=url, method='post', data=data, check={'code': 200, }, respons=res)
    @unittest.skip('跳过')
    def test7_add_spot(self):
        '''
        停用充电桩
        :return:
        '''

        url = self.app_host + '/api/station/station/list'
        data = {"area":"","city":"","page":"1","page_size":"10","type":"0"}
        headers = self.cms_headers
        res = self.session.request('post',url=url,data=data,headers=headers).json()
        self.assertTrue(res['code'] == 200, msg=res)
        miaoshu(url=url, method='post', data=data, check={'code': 200, }, respons=res)

    @unittest.skip('跳过')
    def test8_add_spot(self):
        '''
        停用充电站
        :return:
        '''

        url = self.app_host + '/api/station/station/list'
        data = {"area":"","city":"","page":"1","page_size":"10","type":"0"}
        headers = self.cms_headers
        res = self.session.request('post',url=url,data=data,headers=headers).json()
        self.assertTrue(res['code'] == 200, msg=res)
        miaoshu(url=url, method='post', data=data, check={'code': 200, }, respons=res)
if __name__ == "__main__":
    unittest.main()
