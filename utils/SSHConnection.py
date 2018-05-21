# ! /usr/bin/python

import os
import paramiko


class SSHConnection:
    __hostname = ''
    __port = 22
    __username = ''
    __password = ''
    __ssh = ''

    def __init__(self, hostname, port, username, password):
        self.__hostname = hostname
        self.__port = port
        self.__username = username
        self.__password = password

    def SSHClient(self):
        print ('ssh %s@%s ....' % (self.__username, self.__hostname))
        try:
            self.__ssh = paramiko.SSHClient()
            self.__ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.__ssh.connect(hostname=self.__hostname, username=self.__username, port=self.__port,
                               password=self.__password)
            print ('ssh %s@%s success!!!' % (self.__username, self.__hostname))
        except Exception as e:
            print ('ssh %s@%s: %s' % (self.__username, self.__hostname, e))
            os._exit(0)

    def exec_command(self, command):

        print ('command:', command)
        stdin, stdout, stderr = self.__ssh.exec_command(command)

        err_list = stderr.readlines()
        if len(err_list) > 0:
            print ('ssh exec remote command [%s] error: %s' % (command, err_list[0]))
        print (stdout.read().decode('utf-8'))

    def upload(self, src, dst):

        try:
            sftp = self.__ssh.open_sftp()
        except Exception as e:
            print ('open sftp failed:', e)
            os._exit(0)

        try:
            print ('uploading file: %s --> %s' % (src, dst))
            sftp.put(src, dst)
            print ('uploaded file: %s --> %s' % (src, dst))
            sftp.close()
        except Exception as e:
            print ('uploading file failed:', e)
            os._exit(0)

    def close(self):
        self.__ssh.close()
