#!/usr/bin/python3.3

import telnetlib
import time # Берем текущее время и задержку sleep
import sys

#ЛУВДТ- Vlan 905, FXO: 192.168.1.2, FXS: 192.168.1.3
#ГТЦФТО- Vlan 314, FXO: 172.16.0.93, FXS: 172.16.0.89
#ДРП- Vlan 314, FXO1: 172.16.0.19, FXS1: 172.16.0.17, FXO2: 172.16.0.20, FXS2: 172.16.0.18

#
HOSTS=['192.168.1.2', '192.168.1.3','172.16.0.93','172.16.0.89','172.16.0.19', '172.16.0.17', '172.16.0.20', '172.16.0.18']
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
    tn = telnetlib.Telnet(hst,23,5)
  except:
    output +="Error: \r\n"
    out2 +="Error:"
    out2+=str(sys.exc_info())
    output+=str(sys.exc_info())
    #print (str(sys.exc_info()))
  else:  
   # tn.set_debuglevel(3)#пробуем задебажтиь
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
    out2 += "Rebooted\n"
  #  print (output)
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






