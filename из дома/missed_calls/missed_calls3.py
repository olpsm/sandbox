﻿#для удаления пробелов
#import re

#обработка файлов
#from imp import reload           -- для перезагрузки модуля в IDLE reload(missed_calls2)

print('#открываем файл с данными')

d_file=open("13-10-23.cap")

print('# открываем файл для записи результатов')
r_file=open("result.html","w")

print('#читаем файл построчно')

d_list=d_file.readlines()
#print ('распечатываем d_list')
#print (d_list)
Ph_num=input('Введите искомый номер  ')

#создаем список вложенных списков
#m_list=[]
#k=0
date_list=[]
time_list=[]
A_list=[]
B_list=[]
t_list=[]
print('создаем новый список содержащий '+Ph_num)
for line2 in d_list:
	if line2.find(Ph_num)>11: 
		date_list.append(line2[0:2]+'-'+line2[2:4]+'-'+line2[4:6]) #дата
		time_list.append(line2[7:9]+':'+line2[9:11]) #время
		A_list.append(line2[37:51].lstrip()) #номер А
		B_list.append(line2[53:75].lstrip()) #номер B
		t_list.append(line2[76:77]) #признак звонка




r_file.write('<!DOCTYPE HTML>\n'+
'<html>\n'+
' <head>\n'+
'  <meta charset="utf-8">\n'+
'  <title>Conversation table</title>\n'+
' </head>\n' +
' <body>\n'+
'  <table border="1">\n'+
'   <caption>All conversation table</caption>\n'+
'   <tr>\n'+
'    <th>Date</th>\n'+
'    <th>Time</th>\n'+
'    <th>Number A</th>\n'+
'    <th>Number B</th>\n'+
'    <th>Type</th>\n'+
'   </tr>\n')

i=0
while i<len(A_list):
	print(date_list[i]+' | '+time_list[i]+' | '+A_list[i]+' | '+B_list[i]+' | '+t_list[i])
	r_file.write('<tr><td>'+date_list[i]+'</td><td>'+time_list[i]+'</td><td>'+A_list[i]+'</td><td>'+B_list[i]+'</td><td>'+t_list[i]+'</td></tr>\n')
	#r_file.write(date_list[i]+' | '+time_list[i]+' | '+A_list[i]+' | '+B_list[i]+' | '+t_list[i]+ '\n')
	i+=1


r_file.write('  </table>\n'+
' </body>\n'+
'</html>\n')


#print (m_list)
#print ('пишем d_list в файл r_file')
#r_file.write("")
#r_file.write("результирующие строки")
#r_file.write('\n')
#r_file.writelines(d_list)
#for line in m_list:
#	r_file.write()
#for line in d_list: r_file.write(list)
r_file.flush()
print(' закрываем файлы')
d_file.close
r_file.close

#input("программа завершена. Нажмите Enter.")