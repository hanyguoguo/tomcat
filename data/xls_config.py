#__author__ = 'liuyj'
#coding=utf-8
import time
class XlsConfiger:
    #case_id
    def __init__(self):
        self.Id = '0'
        self.name = '1'
        self.isrun='2'
        self.localdir = '3'
        self.ftpdir ='4'
        self.remote_package = '5'
        self.remote_config = '6'
        self.tomcatdir = '7'
        self.warname = '8'
        self.configname = '9'
        self.remoteIP = '10'
        self.testurl = '11'


    def col_id(self):
        return self.Id

    def col_name(self):
        return self.name

    def col_isrun(self):
        return self.isrun

    def col_localdir(self):
        return self.localdir


    def col_ftpdir(self):
        return self.ftpdir

    def col_remote_package(self):
        return self.remote_package

    def col_remote_config(self):
        return self.remote_config

    def col_tomcatdir(self):
        return self.tomcatdir

    def col_warname(self):
        return self.warname

    def col_configname(self):
        return self.configname

    def col_remoteIP(self):
        return self.remoteIP

    def col_testurl(self):
        return self.testurl


if __name__=="__main__":

    gv=XlsConfiger()
    print gv.col_id()
    print gv.col_name()
    print gv.col_isrun()

    print gv.col_remote_config()
    print gv.remote_package


