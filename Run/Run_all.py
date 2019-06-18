#coding:utf-8
import os

from Common.Email import send_email
import unittest,time
from BeautifulReport import BeautifulReport

#报告生成目录路径
report_path = os.path.join(os.path.dirname(os.getcwd()), "Report_html")
if not os.path.exists(report_path): os.mkdir(report_path)


# 发送文件路径
file_path =report_path+r"\测试报告.html"
print(file_path)

if __name__=='__main__':
	suit=unittest.defaultTestLoader.discover('Case',pattern='test*_*.py')
	report=BeautifulReport(suit)
	report.report(filename='测试报告'.format(time),description='66快充流程接口报告',report_dir=report_path,log_path=file_path)
	send_email(file_path)


