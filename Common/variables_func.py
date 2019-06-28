#coding:utf-8
"""读取变量封装的方法"""
import yaml,os
import json
import requests, hashlib
from Base.runmethod import RunMethod
yaml.warnings({'YAMLLoadWarning': False})

def write_yaml_variable(key=None,value=None):
	"""
	把返回的变量值写入到yaml文件-yaml中已存在key
	:return:
	"""
	# a 追加写入，w,覆盖写入
	with open('{}'.format(os.path.join(os.path.dirname(os.getcwd()),'Config')+'\Varibales.yaml'),"w", encoding="utf-8") as f:
		#装载数据
		yaml.dump({key: value},f)
		f.close()

def get_yaml_variable(key=None):
	"""
	提取写入yaml的变量值
	:return:
	"""
	#r读取数据，获取文件
	with open('{}'.format(os.path.join(os.path.dirname(os.getcwd()),'Config')+'\Varibales.yaml'),"r", encoding="utf-8") as f:
		# 加载数据
		s=yaml.load(f)
		# print(s[key])
		return s[key]

def user_Session():
	with open('{}'.format(os.path.join(os.path.dirname(os.getcwd()),'Config')+'\conf.yaml'), "r", encoding="utf-8") as r:
		config = yaml.load(r)  # 解析并读写yaml文件
		lujing = '/users/loginByPwd'
		host =config['app_host']
		datas =config['user_info']
		headers =config['app_headers']
		res =RunMethod().run_main("post",host,lujing,datas,headers)
		# print(res)
	
		write_yaml_variable("X-SessionToken-With", res['data'])

def cms_cookies():
	"""
	返回cmscookies
	:return:
	"""
	with open('{}'.format(os.path.join(os.path.dirname(os.getcwd()),'Config')+'\conf.yaml'), "r", encoding="utf-8") as r:
		config = yaml.load(r)  # 解析并读写yaml文件
		s=requests.session()    #session()保留登陆的cookies 返回作为后面请求使用
		data =eval(config['cms_info'])
		host= config['cms_host']
		headers=eval(config['cms_headers'])
		url= host+'/api/user/auth/token'
		res=s.request('get',url,params=data,headers=headers)
		response=json.loads(res.text)
		# print(json.loads(res.text))

		write_yaml_variable(key="Authorization", value='Bearer '+response['data']['access_token'])

		# print(res.cookies.values())
		# return(res.cookies)            # 也可以返回cookies  后面请求加入 cookies=self.cookies

		return s

		
if __name__ == "__main__":
	cms_cookies()


	# write_yaml_variable("X-SessionToken-With",34434)
	# print(get_yaml_variable("X-SessionToken-With"))
	# write_yaml_variable("BBB",2442)
	# print(get_yaml_variable("BBB"))

	# user_Session()
