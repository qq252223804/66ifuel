# -*- coding: utf-8 -*- 
# @Time : 2018/12/17 12:47 
# @Author : taojian 
# @File : Operate_Excel.py
import os
import sys

import xlrd
from xlutils.copy import copy

from utx import Log


class UtilExcel:
    def __init__(self, excelPath, sheet_id):
        if not os.path.exists(excelPath):
            Log().error('测试用例文件不存在！')
            sys.exit()
        self.excelPath=excelPath
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheets()[sheet_id]
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        """
        读取excel数据
        :return:
        """
        Log().info('开始读取excel数据')
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in list(range(self.rowNum-1)):   #循环行
                s = {}
                # 从第二行取对应values值
                s['rowNum'] = i + 2
                values = self.table.row_values(j)
                # print(values)
                for x in list(range(self.colNum)):  # 在行的循环下进行 循环列
                    s[self.keys[x]] = values[x]
                    # # print(self.keys[x])
                    # print( values[x])
                r.append(s)
                j += 1
            return r

    # # 写入数据
    # def write_value(self, row, col, value):
    #     """
    #     复制excel 并写入每个列值
    #     :param row:
    #     :param col:
    #     :param value:
    #     :return:
    #     """
    #     # 拿到的数据复制一份
    #     write_data = copy(self.data)
    #     #临时的表
    #     sheet_data = write_data.get_sheet(0)
    #     sheet_data.write(row, col, value)
    #     #写入后保存
    #     write_data.save(self.excelPath)
    def write_value(self, row, col, value):
        """
        复制excel 并写入每个列值
        :param row:
        :param col:
        :param value:
        :return:
        """
        write_data = copy(self.data)
        # 临时的表
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        # 写入后保存
        write_data.save(self.excelPath)

    @staticmethod
    def write_ceshi():
     
        UtilExcel(excelPath="E:\chemofang\Config\cms_api.xlsx", sheet_id=0).write_value(1, 9, '测试写入实际值')
        UtilExcel(excelPath="E:\chemofang\Config\cms_api.xlsx", sheet_id=0).write_value(1, 10, 'pass')


if __name__ == "__main__":
    filepath = "E:\chemofang\Config\cms_api.xlsx"
    sheet_id=0
    data = UtilExcel(filepath,sheet_id)
    print(data.dict_data())
    print(data.dict_data()[0])
    print(data.dict_data()[0]['Response'])
    print(data.dict_data()[0]['method'])

    
    UtilExcel.write_ceshi()
