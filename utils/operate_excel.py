#__author__ = 'liuyj'
#coding=utf-8
import xlrd
from xlutils.copy import copy
import os
import sys
sys.path.append('E:/pyTomcat')


class OperationExcel:

    def __init__(self,file_name=None,sheet_id=None):

        if file_name:
            self.file_name=file_name
            self.sheet_id=sheet_id

        else:
            self.file_name = '../data/java.xlsx'
            self.sheet_id = 0
        # self.file_name=self.file_name.decode('utf-8')
        self.data = self.get_data()

    #获取sheet的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables
    #获取单元格的行数
    def get_lines(self):
        tables =self.data
        return tables.nrows

    #获取某个单元格的内容
    def get_cell_value(self,row,col):
        tables=self.data
        return tables.cell_value(row,col)

    #获取某一列的内容
    def get_cols_data(self,col_id=None):
        if col_id!=None:
            cols_data = self.data.col_values(col_id)
        else:
            cols_data = self.data.col_values(0)
        return cols_data

    #根据case_id找到对应的行数
    def get_row_num(self,case_id):
        num = 0
        cols_data = self.get_cols_data()
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num = num +1
        return num

    #根据行数获取行的内容
    def get_row_values(self,row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    #根据case_id获取行的内容
    def get_rows_data(self,case_id):
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_values(row_num)
        return rows_data


    #写入数据
    def write_value(self,row,col,value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data =copy(read_data)
        sheet_data=write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)
        # #删除旧的excel,并重命名
        # os.remove(self.file_name)
        # os.rename('Interface1.xls',self.file_name)


if __name__=='__main__':
    opers = OperationExcel()
    print opers.get_data()
    print opers.get_lines()
    print opers.get_cell_value(1,1)

