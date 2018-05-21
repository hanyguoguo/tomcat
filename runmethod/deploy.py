#coding=utf-8

import paramiko
import os
import time
import sys
import configparser
import urllib
import requests

from utils import SSHConnection
from utils import FTPConnection
from data.get_data import GetData

class Deploy:


    def __init__(self):
        # self.config_file = config_file
        self.mydata=GetData()
        self.backup_dir = '/home/ceshi/backup'
        # self.now = time.strftime('%Y%m%d_%H%M%S')
        # self.myftp = FTPConnection.FTPConnection('192.168.15.204','write','123456')
    def deploy(self):

        # start = int(round(time.time() * 1000))
        NOW = time.strftime('%Y%m%d_%H%M%S')
        row_count = self.mydata.get_lines()
        print type(row_count)
        for i in range(1,row_count):
            is_run = self.mydata.get_isrun(i)
            if is_run:
                project_name=self.mydata.get_proname(i)
                print 'project name: '+project_name
                war_name = self.mydata.get_warname(i)
                print 'war name: '+war_name
                config_name = self.mydata.get_configname(i)
                print 'config_name:'+config_name
                local_dir = self.mydata.get_localdir(i)
                print 'local dir: '+local_dir
                ftp_dir = self.mydata.get_ftpdir(i)
                print 'ftp dir '+ ftp_dir
                ftp_war = ftp_dir+'/'+war_name
                # ftp_war=ftp_war.encode('utf-8')
                remote_config = self.mydata.get_remote_config(i)
                print 'remote_config: '+remote_config
                remote_package = self.mydata.get_remote_package(i)
                print 'remote_package: '+remote_package
                tomcat_dir = self.mydata.get_tomcatdir(i)
                print 'tomcat_dir: '+tomcat_dir
                test_url = self.mydata.get_testurl(i)
                print 'test_url: '+test_url
                src_war = local_dir + '\\'+war_name
                print 'src_war: '+src_war
                src_config = local_dir + '\\'+config_name
                print 'src_config: '+src_config
                hostname = self.mydata.get_remoteIP(i)
                print 'hostname: '+hostname

                # 建立远程连接
                ssh = SSHConnection.SSHConnection(hostname, 22, 'root','123456')
                ssh.SSHClient()






                # #从ftp下载包到本地
                # print 'download war from ftp...'+ftp_dir+'/'+war_name
                # myftp = FTPConnection.FTPConnection('192.168.15.204','write','123456')
                # myftp.downloadfile(ftp_war.encode('utf-8'),src_war)
                # print "download war from ftp success"
                #
                #
                #
                # # war包上传
                # # ssh.upload(src, tmp_dir + '/bosspe-01.war')
                # print 'start upload war...'+remote_package+'/'+war_name
                # ssh.upload(src_war, remote_package+'/'+war_name)
                print 'start upload cinfig...'+remote_config+ '/'+config_name
                ssh.upload(src_config,remote_config+ '/'+config_name)


                # 远程关闭tomcat
                print 'stop tomcat....'
                ssh.exec_command(tomcat_dir + '/bin/shutdown.sh')
                print 'stop tomcat success'

                print 'kill process....'
                ssh.exec_command('ps -ef | grep ' + tomcat_dir + ' | grep -v grep | awk \'{print $2}\' | xargs kill -15')
                print 'kill process success'

                #
                # # 远程备份配置文件
                # print ('backup webapp....')
                # ssh.exec_command('cp -r ' + tomcat_dir + '/webapps/'+project_name+'/WEB-INF/classes/app-config.properties'  self.backup_dir + '/'+project_name+'/'+NOW)
                # print ('backup webapp success')


                #删除项目目录下的所有文件
                print 'delete all files...'
                ssh.exec_command('rm -rf '+tomcat_dir + '/webapps/'+project_name+'/*')
                print 'delete all files success!'

                # 远程解压war到tomcat下
                print 'unzip war....'
                src_war=remote_package +'/'+war_name

                #clinicpad 项目解压路径
                if project_name =='clinicpad' and hostname=='192.168.14.64':
                    dst_war = tomcat_dir + '/webapps/ROOT'
                else:
                    dst_war = tomcat_dir + '/webapps/'+project_name


                ssh.exec_command('unzip -o  %s -d  %s' % (src_war, dst_war))
                print ('unzip war success: %s --> %s' % (src_war, dst_war))

                # 远程拷贝config文件到tomcat下
                print ('cp config....')
                src_config = remote_config + '/'+config_name
                dst_config = dst_war+'/WEB-INF/classes'
                ssh.exec_command('cp %s %s' % (src_config, dst_config))
                print ('cp config success: %s --> %s' % (src_config, dst_config))



                # # 远程启动tomcat
                # print ('start tomcat....')
                # ssh.exec_command(tomcat_dir + '/bin/startup.sh')
                # print ('start tomcat success')
                #
                # #关闭连接
                # ssh.close()
                #
                # # 检测是否成功
                # print 'connectionning', test_url, '....'
                # response = requests.get(test_url)
                # print 'connection', test_url, ' http code:', response.status_code
                # if response.status_code == 200:
                #     print ('Success!')
                # else:
                #     print ('Fail !!!')
                #
                # end = int(round(time.time() * 1000))
                #
                # print ('deploy %s use time %dms.' % (project_name, (end - start)))


if __name__ == '__main__':
    deploy = Deploy()
    # deploy.config_file
    deploy.deploy()
