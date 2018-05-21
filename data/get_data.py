#__author__ = 'liuyj'
# -*- coding:utf-8 -*-
import json
import time
from utils.operate_excel import OperationExcel
from xls_config import XlsConfiger


class GetData:

    def __init__(self):
        self.opera_excel = OperationExcel()
        self.xls_config = XlsConfiger()


    #获取excel行数（case个数）
    def get_lines(self):
        return self.opera_excel.get_lines()

    #获取是否执行
    def get_isrun(self,row):
        flag = None
        col = int(self.xls_config.col_isrun())
        run_model = self.opera_excel.get_cell_value(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    #获取项目名
    def get_proname(self,row):
        col = int(self.xls_config.col_name())
        name = self.opera_excel.get_cell_value(row,col)
        return name

    #获取本地目录
    def get_localdir(self, row):
        col = int(self.xls_config.col_localdir())
        localdir = self.opera_excel.get_cell_value(row,col)
        return localdir

    #获取ftp目录
    def get_ftpdir(self, row):
        col = int(self.xls_config.col_ftpdir())
        ftpdir = self.opera_excel.get_cell_value(row,col)
        return ftpdir

    #获取remote上war包的目录
    def get_remote_package(self, row):
        col = int(self.xls_config.col_remote_package())
        remote_package = self.opera_excel.get_cell_value(row,col)
        return remote_package

    #获取remote上config文件的目录
    def get_remote_config(self, row):
        col = int(self.xls_config.col_remote_config())
        remote_config = self.opera_excel.get_cell_value(row,col)
        return remote_config

    #获取tomcat目录
    def get_tomcatdir(self, row):
        col = int(self.xls_config.col_tomcatdir())
        tomcatdir = self.opera_excel.get_cell_value(row,col)
        return tomcatdir

    #获取war包文件名
    def get_warname(self, row):
        col = int(self.xls_config.col_warname())
        warname = self.opera_excel.get_cell_value(row,col)
        return warname

    #获取配置文件名
    def get_configname(self, row):
        col = int(self.xls_config.col_configname())
        configname = self.opera_excel.get_cell_value(row,col)
        return configname

    #获取remoteIP
    def get_remoteIP(self, row):
        col = int(self.xls_config.col_remoteIP())
        remoteIP = self.opera_excel.get_cell_value(row,col)
        return remoteIP

    #获取remoteIP
    def get_testurl(self, row):
        col = int(self.xls_config.col_testurl())
        testurl = self.opera_excel.get_cell_value(row,col)
        return testurl



if __name__=='__main__':
    mydata = GetData()
    print mydata.get_proname(2)
    print mydata.get_isrun(2)
    print mydata.get_localdir(2)
    print mydata.get_ftpdir(2)
    print mydata.get_remote_package(2)
    print mydata.get_remote_config(2)
    print mydata.get_tomcatdir(2)
    print mydata.get_testurl(2)









