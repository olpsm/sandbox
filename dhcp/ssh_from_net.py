#!/usr/bin/env python
# -*- coding: utf-8 -*-

# проверка подходитли пароль к оборудованию

 
import paramiko
import os
import socket
import time
import subprocess
 
hostname = ''
port = 22
username = 'root'
password = 'пароль'
i = 0
number = ''
 
print "IP-адресс \t Состояние"
 
while i <= 80:
    
    number = str(i)
    hostname = '10.6.'+number+'.1'  
    paramiko.util.log_to_file('paramiko.log')
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        s.connect(hostname, port, username, password, timeout = 3)
        print (hostname +"\t Пароль Пароль")
    except AuthenticationException:
        print (hostname + "\t Пароль не Пароль")
        pass
    except socket.timeout:
            print(hostname +"\t Адрес свободен")
        pass
    except SSHException:
        print (hostname + "\t Возникла иная ошибка")
        pass
    i = i + 1