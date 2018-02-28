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

# пример для вывода части команд

# tn.write("command1\r\n")
# ret1 = tn.read_eager()
# print ret1 #or use however you want
# tn.write("command2\r\n")
# print tn.read_eager()
# ... and so on

# для вывода всего 
#sess_op = tn.read_all()
#print sess_op
#-------------------------------

# пример для вывода лога в файл
"""import time, telnetlib

host    = "host.example.com"
port    = 223
timeout = 9999

try:
   session = telnetlib.Telnet(host, port, timeout)
except socket.timeout:
    print ("socket timeout")
else:
    session.write("command1\n")
    session.write("command2\n")
    with open("test.xml", "w") as logfile:
        output = session.read_some()
        while output:
            logfile.write(output)
            time.sleep(0.1)  # let the buffer fill up a bit
            output = session.read_some()
"""
# еще один пример
"""
time.sleep(1)
    output = tn.read_until("#")
    print output
"""
#try:
  
"""	#except socket.timeout:	
	print ("socket timeout")
	output +="socket timeout \r\n"
	out2 +="socket timeout\n"
#	else:
"""	
"""
#выходим
tn.write(b"BYE\r\n")
tn.read_until(b"\r\nDisconnect Now? (Y/N)",5)
tn.write(b"y\r\n")
"""

#================================================================================
#import getpass
import telnetlib
import time # Берем текущее время и задержку sleep

HOSTS=['172.16.0.250','192.168.8.254','172.16.0.252']
#HOST = "172.16.0.250"
user = "admin"
password = "dremel"

logfile=open("log.txt","a") # файл для полных логов
log_f=open("s_log.txt","a") # файл для кратких логов

#################################################################
def telnet_host(hst):
  output="=============================================================\n"
  output+=time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
  output +="\n-------------------\n"+ hst +"\r\n-------------------\n"
  out2=time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())+" - "+ hst + " - "
  try:
    tn = telnetlib.Telnet(hst,23,20)
  except IOError:	
    print ("socket timeout")
    output +="socket timeout \r\n"
    out2 +="socket timeout\n"
  else:  
    tn.set_debuglevel(3)#пробуем задебажтиь
    tn.read_until(b"\r\nUser:",5)
    tn.write(user.encode('ascii') + b"\r\n")
    if password:
        tn.read_until(b"\r\nPassword:",5)
        tn.write(password.encode('ascii') + b"\r\n")
    tn.read_until(b"[[/]]\r\n>",5)
    # проверяем статус портов
    tn.write(b"curr st \r\n")
    time.sleep(1)
    tn.write(b"\r\n")
    output += tn.read_until(b"[[/]]\r\n> ",5).decode('ascii')
    # перезагрузка Restarting...
    tn.write(b"RESTART\r\n")
    tn.read_until(b"Now? (Y/N)",5)
    tn.write(b"y\r\n")
    output += tn.read_until(b"\r\nRestarting...").decode('ascii')+"\r\n"
    out2 += "Rebooted \n"
    print (output)
    tn.close()
  finally:
    # сохраняем лог
    logfile.write(output)
    log_f.write(out2)
    output=""
    out2=""
##################################################################
# Main#

for HOST in HOSTS:
  telnet_host(HOST)

logfile.close
log_f.close






