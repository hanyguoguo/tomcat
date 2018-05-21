#coding=utf-8

import paramiko
import os
import time
import sys
import configparser
import urllib
import requests

from utils import SSHConnection


class Deploy:


    def __init__(self, config_file):
        self.config_file = config_file

    def deploy(self):
        start = int(round(time.time() * 1000))



        NOW = time.strftime('%Y%m%d_%H%M%S')

        print ('loading config file:', self.config_file)
        config = configparser.ConfigParser()
        config.read(self.config_file)
        print ('loading config file success!')

        # global
        project_name = config.get('global', 'project_name')
        war_name = project_name+'-0.1.war'
        config__file_name = 'app-config.properties'

        # ENV = config.get('global', 'env')

        # local
        local_package_dir = config.get('local', 'local_package_dir')
        local_config_dir = config.get('local', 'local_config_dir')
        src = local_package_dir + '/'+war_name
        config_file =local_config_dir + '/'+config__file_name


        # remote
        hostname = config.get('remote', 'hostname')
        port = config.getint('remote', 'port')
        username = config.get('remote', 'username')
        password = config.get('remote', 'password')



        remote_package_dir = config.get('remote', 'remote_package_dir')
        remote_config_dir = config.get('remote', 'remote_config_dir')


        tomcat_home = config.get('remote', 'tomcat_home')
        app_test_url = config.get('remote', 'app_test_url')

        # 建立远程连接
        ssh = SSHConnection.SSHConnection(hostname, port, username, password)
        ssh.SSHClient()

        # war包上传
        # ssh.upload(src, tmp_dir + '/bosspe-01.war')
        ssh.upload(src, remote_package_dir+'/'+war_name)
        ssh.upload(config_file,remote_config_dir+ '/'+config__file_name)



        # 远程关闭tomcat
        print ('stop tomcat....')
        ssh.exec_command(tomcat_home + '/bin/shutdown.sh')
        print ('stop tomcat success')

        print ('kill process....')
        ssh.exec_command('ps -ef | grep ' + tomcat_home + ' | grep -v grep | awk \'{print $2}\' | xargs kill -15')
        print ('kill process success')



        # # 远程解压war到tomcat下
        # print ('unzip war....')
        # # src = tmp_dir + '/bosspe-01.war'
        # src=remote_package_dir +'/'+war_name
        # # dst = tomcat_home + '/webapps/bosspe'
        # dst = tomcat_home + '/webapps/'+project_name
        # ssh.exec_command('unzip -o  %s -d  %s' % (src, dst))
        # print ('unzip war success: %s --> %s' % (src, dst))

        # 远程拷贝config文件到tomcat下
        print ('cp config....')
        src = remote_config_dir + '/'+config__file_name
        dst = tomcat_home + '/webapps/'+project_name+'/WEB-INF/classes'
        ssh.exec_command('cp %s %s' % (src, dst))
        print ('cp config success: %s --> %s' % (src, dst))



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
    deploy = Deploy('E:\\pyTomcat\\config\\config.ini')
    # deploy.config_file
    deploy.deploy()
