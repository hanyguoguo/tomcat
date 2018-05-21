# coding: utf-8
from ftplib import FTP
import time
import tarfile
import os
from ftplib import FTP

class FTPConnection:

    def __init__(self,host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.ftp = self.ftpconnect()

    def ftpconnect(self):

        ftp = FTP()
        # ftp.set_debuglevel(2)
        ftp.connect(self.host, 21)
        ftp.login(self.username, self.password)
        return ftp


    # 从ftp下载文件
    def downloadfile(self, remotepath, localpath):
        bufsize = 1024
        fp = open(localpath, 'wb')
        self.ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
        self.ftp.set_debuglevel(0)
        fp.close()


    # 从本地上传文件到ftp
    def uploadfile(self, remotepath, localpath):
        bufsize = 1024
        fp = open(localpath, 'rb')
        self.ftp.storbinary('STOR ' + remotepath, fp, bufsize)
        self.ftp.set_debuglevel(0)
        fp.close()


if __name__ == "__main__":
    ftp = FTPConnection('192.168.15.204','write','123456')
    # ftp.downloadfile("/致医云诊室/研发提测/120/java/workbench/workbench-18858.war", "workbench-18858.war")
    # # 调用本地播放器播放下载的视频
    # os.system('start "C:\Program Files\Windows Media Player\wmplayer.exe" "C:/Users/Administrator/Desktop/test.mp4"')
    # ftp.uploadfile(ftp, "/致医云诊室/研发提测/120/java/test.txt", "test.txt")
    ftp.downloadfile('/致医云诊室/研发提测/120/java/pharmacy/pharmacy-19778.war',u'D:\\致医健康测试项目\\测试安装\\pharmacy1\\pharmacy-19778.war')

    # ftp.quit()
