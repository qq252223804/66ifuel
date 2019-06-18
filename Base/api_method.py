# -*- coding: utf-8 -*- 
# @Time : 2018/12/21 10:30 
# @Author : taojian 
# @File : api_method.py
"""excel 读取用例封装的请求方法"""
import json

from utx import Log
from Common.Operate_Excel import UtilExcel

from Common.variables_func import cms_cookies


def send_requests(session,testdata):
	Log().info("开始发送请求")
	"封装requests请求"
	url = testdata["url"]
	method=testdata["method"]
	# 请求头部headers
	try:
		headers = eval(testdata["headers"])
	except:
		headers = None
	# post请求body类型
	body_type = testdata["type"]
	# 请求的datas参数 # 判断传data数据还是json
	datas=None     #定义一个datas 作为返判断返回值
	if body_type=='from':
		try:
			datas=eval(testdata["datas"]) #取出来的str 需转换为dict
		except:
			datas=None

	elif body_type=='json':
		try:
			datas =json.dumps(testdata["datas"])    #取出来的str 转变成json类型字典
		except:
			datas=None
	#执行的id
	test_nub = testdata['id']
	
	print("*******正在执行用例：-----  %s  ----**********" % test_nub)
	print("请求方式：%s, 请求url:%s" % (method, url))
	# print(type(datas))
	print("请求datas：%s" % datas)
	response = {}  # 接受返回数据  后面写入数据
	res=None        #定义一个res 作为返回值
	is_run= testdata['must']
	# print(is_run)
	if is_run=='yes':  #判断是否执行
		try:
			if method=='get':
				res=session.get(url=url,
				                headers=headers,
				                params=datas,
				                verify=False)
				response["Times"] =str(res.elapsed.total_seconds())
				print("页面返回信息：%s" % res.content.decode("utf-8"))
			elif method=='post':
				res = session.post(
				                  url=url,
				                  headers=headers,
				                  data=datas,
				                  verify=False)
				response["Times"]=str(res.elapsed.total_seconds())
				# print(response["Times"])
				print("页面返回信息：%s" % res.content.decode("utf-8"))
			else:
				print('方法有误')
				return res    # return是用来终止代码运行的  在返回结果后
			response['rowNum'] = testdata['rowNum']
			response["text"] = res.content.decode("utf-8")
			str_response=json.loads(res.text)
			# print(str_response["code"])
			if str_response["code"]!=200:           #如果状态码不为200时写入 Response
				response["Response"]=response["text"]
			else:
				response["Response"]=""   #如果=200则写入空值
			response["Msg"] = ""       #提前定义Msg 默认为空
			if testdata["CheckPoint"] in response["text"]:
				response["Result"]="pass"
			else:
				response["Result"] = "fail"

			print("用例测试结果:   %s---->%s" % (test_nub, response["Result"]))
			return response
		except Exception as msg:
			response["Msg"] = str(msg)
			# print(response)
			return response
	else:
		response=""                    #如果不执行response 赋值为空 后面调用写入方法好判断
		print("用例跳过")
		return response
	
def write_result(response,write_excelPath,sheet_id):
	# 返回结果的行数row_nub

	if response !="":
		row_nub = response['rowNum']-1

		#引入写入的方法 但前提是要读取数据
		# data.write_value(row_nub, 10,333333)
		# table=UtilExcel(excelPath=filename, sheet_id=sheet_id)
		# table.write_value(row_nub,9,response["Response"])
		# table.write_value(row_nub, 10, response["Result"])    #这样只能写入一个 变量赋值原因

		UtilExcel(excelPath=write_excelPath, sheet_id=sheet_id).write_value(row_nub,9,response["Response"])   # 状态码非200时的返回信息
		UtilExcel(excelPath=write_excelPath, sheet_id=sheet_id).write_value(row_nub, 10, response["Result"])    # 写入测试结果
		UtilExcel(excelPath=write_excelPath, sheet_id=sheet_id).write_value(row_nub, 11, response["Times"])   #写入接口执行时间
		UtilExcel(excelPath=write_excelPath, sheet_id=sheet_id).write_value(row_nub, 12, response['Msg'])  # 抛异常
	else:
		# print('111')
		pass
#
if __name__ == "__main__":
	excelPath = "E:\chemofang\Config\cms_api.xlsx"
	sheet_id = 0
	read_data = UtilExcel(excelPath,sheet_id).dict_data()
	# print(read_data[0])
	session= cms_cookies()
	Response = send_requests(session, read_data[5])
	# print(response)
	# print(Response["Response"])
	write_result(Response, write_excelPath=excelPath,sheet_id=sheet_id)