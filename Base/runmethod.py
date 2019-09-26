#coding=utf-8
"""接口模块/流程性封装的请求方法"""
import requests

from Common.hmacmd5 import new_hmac_md5
from Common.log import Log


class RunMethod():

	def post_main(self,host,lujing,data,headers=None):      #host 为基础url ，lujing为路径
		try:
			if lujing !=None:
				url = host + lujing
			else:
				url=host
			# print(url)
			# print(type(data))
			if type(data)==dict:          #判断是否为dict 类型

				data=data
			else:
				# print("nooo")
				data=eval(data)        #如果data 不是dict 类型 就必须先是str 然后转成dict
			if headers != None:
				if type(headers)==dict:

					headers=headers
				else:
					headers=eval(headers)        #如果data 不是dict 类型 就必须先是str 然后转成dict

				res=requests.post(url=url,json=data,headers=headers,verify=False)

			else:
				res=requests.post(url=url,json=data,verify=False)
			if 	res.status_code != 200:      #判断响应状态码是否不为200
				print('响应状态码不等于200,实际为:{}'.format(res))
				Log().info(res)

		except Exception as e:
			Log().info('post 请求错误 错误原因为%s'%e)
		else:  # 响应状态码正确转为json
			response = res.json()  # 将返回的数据转换为json格式的 字典
			return response


			
		
	def get_main(self,host,lujing=None,data=None,headers=None):
		try:
			if lujing !=None:
				url = host + lujing
			else:
				url=host

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
				print('响应状态码不等于200,实际为:{}'.format(res))
				Log().info(res)

		except Exception as e:
			Log().info('post 请求错误 错误原因为%s' % e)
		else:  # 响应状态码正确转为json
			response = res.json()  # 将返回的数据转换为json格式的 字典
			return response

	def run_main(self,method,host,lujing=None,data=None,headers=None):
		if method=='post':
			res=self.post_main(host,lujing,data,headers)
			return res
		if method=='get':
			res=self.get_main(host,lujing,data,headers)
			return res


if __name__ == '__main__':
	run = RunMethod()  # 实例化
	# host='https://service.66ifuel.com'
	# lujing='/customer/v1/member/login'
	# datas={"phone":"18657738815","password":"dc483e80a7a0bd9ef71d8cf973673924"}
	#
	# headers={"Content-Type":"application/json; charset=utf-8"}

	host='http://124.160.35.34:8091/service.do/'

	data={"app_id": 'b1044830052f359d',
      "timestamp": '2019-9-25 2:35:56',
      "version": '1.0',
      "client": 'android',
      "client_version": '4.0.1',
      "device_id": '123123',
      "method": 'user.sendVerificationCode',
      "biz_content": '{"phone":"13185097298","type":1}',
      }
	headers={
   "Content-Type": "application/x-www-form-urlencoded",
   "Connection": "keep-alive"
   }
	SigSecret = '204414295c2f3fbc5818f604793f1ba2'
	datas=dict(sorted(data.items(),key=lambda x:x[0],reverse=False))
	sign = new_hmac_md5(SigSecret, datas)
	datas.update({"sign":sign})
	print(datas)
	res=requests.post(url=host,data=datas,headers=headers).json()
	# res=run.run_main('post',host,datas,headers)
	print(res)
	# print(type(res))

