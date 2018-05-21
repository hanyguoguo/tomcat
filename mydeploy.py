#coding=utf-8

import paramiko
import os
import time
import sys
import configparser
import urllib
import requests

from utils import SSHConnection
from data.get_data import GetData

class Deploy:


    def __init__(self):
        # self.config_file = config_file
        self.mydata=GetData()
    def deploy(self):
        start = int(round(time.time() * 1000))
        NOW = time.strftime('%Y%m%d_%H%M%S')
        row_count = self.mydata.get_lines()

        for i in row_count:
            is_run = self.mydata.get_isrun(i)
            if is_run:
                project_name=self.mydata.get_proname(i)
                war_name = self.mydata.get_warname(i)
                config_name = self.mydata.get_configname(i)
                local_dir = self.mydata.get_localdir(i)
                remote_dir = self.mydata.get_remotedir(i)
                tomcat_dir = self.mydata.get_tomcatdir(i)
                test_url = self.mydata.get_testurl(i)
                src_war = local_dir + '/'+war_name
                src_config =local_dir + '/'+config_name
                hostname = self.mydata.get_remoteIP(i)

                # 建立远程连接
                ssh = SSHConnection.SSHConnection(hostname, 22, 'root','123456')
                ssh.SSHClient()

                # war包上传
                # ssh.upload(src, tmp_dir + '/bosspe-01.war')
                ssh.upload(src_war, remote_dir+'/'+war_name)
                ssh.upload(src_config,remote_dir+ '/'+config_name)

                # 远程关闭tomcat
                print ('stop tomcat....')
                ssh.exec_command(tomcat_dir + '/bin/shutdown.sh')
                print ('stop tomcat success')

                print ('kill process....')
                ssh.exec_command('ps -ef | grep ' + tomcat_dir + ' | grep -v grep | awk \'{print $2}\' | xargs kill -15')
                print ('kill process success')

                # # 远程解压war到tomcat下
                # print ('unzip war....')
                # # src = tmp_dir + '/bosspe-01.war'
                # src=remote_dir +'/'+war_name
                # # dst = tomcat_home + '/webapps/bosspe'
                # dst = tomcat_dir + '/webapps/'+project_name
                # ssh.exec_command('unzip -o  %s -d  %s' % (src, dst))
                # print ('unzip war success: %s --> %s' % (src, dst))
                #
                # # 远程拷贝config文件到tomcat下
                # print ('cp config....')
                # src = remote_dir + '/'+config_name
                # dst = tomcat_dir + '/webapps/'+project_name+'/WEB-INF/classes'
                # ssh.exec_command('cp %s %s' % (src, dst))
                # print ('cp config success: %s --> %s' % (src, dst))



        # # 远程启动tomcat
        # print ('start tomcat....')
        # ssh.exec_command(tomcat_home + '/bin/startup.sh')
        # print ('start tomcat success')

        # 关闭连接
                ssh.close()

        # # 检测是否成功
        # print 'connectionning', app_test_url, '....'
        # response = requests.get(app_test_url)
        # print 'connection', app_test_url, ' http code:', response.status_code
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
