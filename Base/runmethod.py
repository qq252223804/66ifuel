#coding=utf-8
"""接口模块/流程性封装的请求方法"""
import requests

from utx import Log


class RunMethod():

	def post_main(self,host,lujing,data,headers=None):      #host 为基础url ，lujing为路径
		try:
			# print(type(data))
			if type(data)==dict:          #判断是否为dict 类型
				data=data
			else:
				# print("nooo")
				data=eval(data)        #如果data 不是dict 类型 就必须先是str 然后转成dict
				
			url=host+lujing
			# print(url)
			if headers != None:
				if type(headers)==dict:

					headers=headers
				else:
					headers=eval(headers)        #如果data 不是dict 类型 就必须先是str 然后转成dict

				res=requests.post(url=url,json=data,headers=headers,verify=False)

			else:
				res=requests.post(url=url,json=data,verify=False)
			if 	res.status_code != 200:      #判断响应状态码是否不为200
				Log().info(res.json())
			response =res.json()   #  将返回的数据转换为json格式的 字典
			return   response
		except Exception as e:

			Log().info('post 请求错误 错误原因为%s'%e)
			return('post 请求错误 错误原因为%s'%e)

			
		
	def get_main(self,host,lujing,data=None,headers=None):
		try:
			url = host + lujing

			if headers != None:
				# print("ok")
				if type(headers) == dict:
					headers = headers
				else:
					headers = eval(headers) # 如果data 不是dict 类型 就必须先是str 然后转成dict
				res=requests.get(url=url,data=data,headers=headers,verify=False)
				# print(res)
			else:
				res=requests.get(url=url,data=data,verify=False)
			if res.status_code != 200:  # 判断响应状态码是否不为200
				Log().info(res.json())
			response = res.json()  # 将返回的数据转换为json格式的 字典
			return response
		except Exception as e:

			Log().info('post 请求错误 错误原因为%s' % e)
			return ('post 请求错误 错误原因为%s' % e)
	def run_main(self,method,host,lujing,data=None,headers=None):
		if method=='post':
			res=self.post_main(host,lujing,data,headers)
			return res
		if method=='get':
			res=self.get_main(host,lujing,data,headers)
			return res


if __name__ == '__main__':
	run = RunMethod()  # 实例化
	host='https://service.66ifuel.com'
	lujing='/customer/v1/member/login'
	datas={"phone":"18657738815","password":"dc483e80a7a0bd9ef71d8cf973673924"}

	headers={"Content-Type":"application/json; charset=utf-8"}
	res=run.run_main('post',host,lujing,datas,headers)
	print(res)

