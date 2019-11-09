#!/usr/bin/python
#coding:utf-8

import os
import unittest

from BeautifulReport import BeautifulReport

from Common.Email import send_email

#报告生成目录路径
report_path = os.path.join(os.path.join(os.getcwd(),'Report_html'))
# print(report_path)
if not os.path.exists(report_path): os.mkdir(report_path)


# 发送文件路径
file_path =('{}').format(os.path.join(os.getcwd(),'Report_html')+'\测试报告.html')
print(file_path)


# ,report_dir=report_path
if __name__=='__main__':

	suit=unittest.defaultTestLoader.discover('Case',pattern='test*_*.py')
	# suit=unittest.defaultTestLoader.discover('Case',pattern='addmage')
	report=BeautifulReport(suit)
	report.report(filename='测试报告',description='66快充流程接口报告',log_path='Report_html')
	send_email(file_path)
	os.system("start {}".format(os.path.join(os.getcwd(),'Report_html')))


