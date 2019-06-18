#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import datetime
import os,time
import unittest
from utx.log import Log
from utx.BSTestRunner import BSTestRunner


# curpath = os.path.dirname(os.path.realpath(__file__))
# case_path = os.path.join(curpath, "Case")
# print(case_path)

class TestRunner:

    def __init__(self):
        self.case_dirs = []

    def add_case_dir(self, dir_path):
        """添加测试用例文件夹，多次调用可以添加多个文件夹，会按照文件夹的添加顺序执行用例

            runner = TestRunner()
            runner.add_case_dir(r"testcase\chat")
            runner.add_case_dir(r"testcase\battle")
            runner.run_test(report_title='接口自动化测试报告')

        :param dir_path:
        :return:
        """
        if not os.path.exists(dir_path):
            raise Exception("测试用例文件夹不存在：{}".format(dir_path))
        if dir_path in self.case_dirs:
            Log().warning("测试用例文件夹已经存在了：{}".format(dir_path))
        else:
            self.case_dirs.append(dir_path)

    def run_test(self, report_title='接口自动化测试报告'):

        if not self.case_dirs:
            raise Exception("请先调用add_case_dir方法，添加测试用例文件夹")

        # report_dir = os.path.abspath("report")
        report_path = os.path.join(os.path.dirname(os.getcwd()), "report")
        if not os.path.exists(report_path): os.mkdir(report_path)

        # suit=unittest.defaultTestLoader.discover('Case', pattern='test*_*.py')
        suit = unittest.TestSuite()
        for case_path in self.case_dirs:
            suit.addTests(unittest.TestLoader().discover(case_path))
        BSTestRunner(report_dir=report_path, report_title=report_title).run(suit)
        print("测试完成，请查看报告")

