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

        projects=config.get('global','project_name')

        projects_list = projects.split(',')



if __name__=='__main__':
    mydeploy = Deploy('E:\\pyTomcat\\config\\config.ini')
    print type(mydeploy.deploy())