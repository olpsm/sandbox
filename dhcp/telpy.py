#!/usr/bin/python3.3

#import sys
#import telnetlib
#import time


#tn = telnetlib.Telnet("172.16.24.10", 23) #подключаемся к узлу 
#tn.read_until("Router  >") # отлавливаем приглашение, которое заканчивается "Router  >"
#tn.write("enable\r") # вводим команду (Обратить внимание на \r)
#
#tn.read_until("Password:") #отлавливаем приглашение с вводом пароля
#tn.write("my_pass\r") # вставляем пароль (Обратить внимание на \r)
#
#tn.read_until("telnet@BigIron Router#") #отлавливаем приглашение, информирующее о входе в систему
#tn.write("show chassis\r") # выполняем команду
#s = tn.read_until(" C degrees") # считываем результат до определенного слова
#
#print type(s) #навсякий случай узнаем что мы получили, а то мало ли
#
#tn.close(); #закрываем сессию
#print s # выводим полученный результат.

#прмер с оф сайта

import getpass
import telnetlib

HOST = "172.16.24.198"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST,23,20)

#tn.set_debuglevel(3)#пробуем задебажтиь

tn.read_until(b"\r\nUser name:",5)
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"\r\nUser password:",5)
    
   # print(tn.read_all().decode('ascii'))

    tn.write(password.encode('ascii') + b"\n")

tn.write(b"disp ver\n")

tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
tn.close()
