#\\10.12.35.174\Def_Log\YYYY.MM\YY-MM-DD.cap логи звонков лежат в файлах такого вида

# Подключаем модули
import shutil # для копирования 
import datetime # получение даты
import os

now_date = datetime.date.today() # получаем текущую дату
now_time = datetime.datetime.now().strftime("%H:%M:%S") #получаем текущее время
YYYY_MM=now_date.strftime("%Y.%m") # дата в формате YYYY.MM
YY_MM_DD=now_date.strftime("%y-%m-%d") # дата в формате YY-MM-DD
src= '\%s\%s\%s%s'  % ("\\10.12.35.174\Def_Log",YYYY_MM,YY_MM_DD,".cap")
dst= '%s\%s\%s%s'  % ("D:\prog\Python33\Missed_Calls",YYYY_MM,YY_MM_DD,".txt")
Dst_dir='%s\%s'  % ("D:\prog\Python33\Missed_Calls",YYYY_MM)
#print('src=', src)
#print('dst=', dst)
# проверяем наличие директории с данным месяцем
if not os.path.exists(Dst_dir):
		os.mkdir(Dst_dir)
# копируем файлы
shutil.copyfile(src,dst)

#print('#открываем файл с данными')
d_file=open(dst)
#print('# открываем файл для записи результатов')
r_file=open("D:\prog\Python33\Missed_Calls\missed_calls.html","w")

#print('#читаем файл построчно')

d_list=d_file.readlines()
#Ph_num=input('Введите искомый номер  ')
Ph_num="1440" #корп. номер
Mph_num="0"+Ph_num #номер FMC
#создаем список вложенных списков
date_list=[]
time_list=[]
A_list=[]
B_list=[]
t_list=[]
#print('создаем новый список содержащий '+Ph_num+' или '+ Mph_num)
#
#c 1 вариантом цикла возникла проблема иногда нет А номера (пустое поле).В рез-те возникает проблема с условием line3[7]
#for line2 in d_list:
#	line3=line2.split()
#	if (line3[5]==Ph_num or line3[5]==Mph_num or line3[6]==Ph_num or line3[6]==Mph_num) and line3[7]!="9": 
#		#print (line3)
#		date_list.append(line3[0][0:2]+'-'+line3[0][2:4]+'-'+line3[0][4:6]) #дата
#		time_list.append(line3[1][0:2]+':'+line3[1][2:4]) #время
#		#print (time_list)
#		A_list.append(line3[5]) #номер А
#		B_list.append(line3[6]) #номер B
#		t_list.append(line3[7]) #признак звонка
##################################
for line2 in d_list:
	if ((line2[37:51].strip()==(Ph_num or Mph_num)) or (line2[53:75].strip()==(Ph_num or Mph_num))) and line2[76:77].strip()!="9": 
		date_list.append(line2[0:2]+'-'+line2[2:4]+'-'+line2[4:6]) #дата
		time_list.append(line2[7:9]+':'+line2[9:11]) #время
		A_list.append(line2[37:51].strip()) #номер А
		B_list.append(line2[53:75].strip()) #номер B
		t_list.append(line2[76:77].strip()) #признак звонка

##################################

r_file.write('<!DOCTYPE HTML>\n'+
'<html>\n'+
' <head>\n'+
'<meta http-equiv="refresh" content="1; URL=file://localhost/D:/prog/Python33/Missed_Calls/missed_calls.html#tab4">\n'+# не корректно срабатывает
#'  <meta charset="utf-8">\n'+ # не работает РАЗОБРАТЬСЯ!!!
'  <link rel="stylesheet" type="text/css" href="missed_calls.css">\n'+ # файл стилей css в одной папке с missed_calls.html
'  <title>Conversation table for number '+
Ph_num+
'  \n</title>\n'+
' </head>\n' +
' <body>\n'+
' <i> Обновлено в '+now_time+ 
'</i>\n'+
'  <br>\n'+
'  <br>\n'+
' 	<div class="tabsLink">\n'+
'       	<a href="#tab1">Неотвеченые</a>\n'+
'        	<a href="#tab2">Исходящие</a>\n'+
'		<a href="#tab3">Входящие</a>\n'+
'		<a href="#tab4">Все звонки</a>\n'+
'       </div>\n'+
# 1я вкладка   ####################################################     
'       <a class="tabs" id="tab1"></a>\n'+
'       <div class="tab">\n'+
#
'	  	<table>\n'+
'   			<tr>\n'+
'   	 			<th id="th1">Дата</th>\n'+
'    	 			<th id="th2">Время</th>\n'+
'    	 			<th id="th3">Номер A</th>\n'+
'     	 			<th id="th4">Номер B</th>\n'+
#'    	 			<th>Type</th>\n'+
'    			</tr>\n')
i=0
print ('#Неотвеченые')
while i<len(A_list):
	if t_list[i]=="H":
		print(date_list[i]+' | '+time_list[i]+' | '+A_list[i]+' | '+B_list[i]+' | '+t_list[i])
		r_file.write('<tr><td>'+date_list[i]+'</td><td>'+time_list[i]+'</td><td>'+A_list[i]+'</td><td>'+B_list[i]+'</td></tr>\n')
	i+=1
r_file.write(
'  		</table>\n'+
#' </body>\n'+
#'</html>\n'+
'	</div>\n')



# 2я вкладка ################################################################### 
r_file.write('        <a class="tabs" id="tab2"></a>'+
'        <div class="tab">'+

'	  	<table>\n'+
'   			<tr>\n'+
'   	 			<th id="th1">Дата</th>\n'+
'    	 			<th id="th2">Время</th>\n'+
'    	 			<th id="th3">Номер A</th>\n'+
'     	 			<th id="th4">Номер B</th>\n'+
#'    	 			<th>Type</th>\n'+
'    			</tr>\n')
i=0
print ('#Исходящие')
while i<len(A_list):
	if t_list[i]=="7":
#		print(date_list[i]+' | '+time_list[i]+' | '+A_list[i]+' | '+B_list[i]+' | '+t_list[i])
		r_file.write('<tr><td>'+date_list[i]+'</td><td>'+time_list[i]+'</td><td>'+A_list[i]+'</td><td>'+B_list[i]+'</td></tr>\n')
	i+=1
r_file.write('  </table>\n'+
#' </body>\n'+
#'</html>\n'+
'</div>\n')

# 3я вкладка ################################################################### 
r_file.write('        <a class="tabs" id="tab3"></a>'+
'        <div class="tab">'+

'	  	<table>\n'+
'   			<tr>\n'+
'   	 			<th id="th1">Дата</th>\n'+
'    	 			<th id="th2">Время</th>\n'+
'    	 			<th id="th3">Номер A</th>\n'+
'     	 			<th id="th4">Номер B</th>\n'+
#'    	 			<th>Type</th>\n'+
'    			</tr>\n')
i=0
print ('#Входящие')
while i<len(A_list):
	if t_list[i]=="G":
#		print(date_list[i]+' | '+time_list[i]+' | '+A_list[i]+' | '+B_list[i]+' | '+t_list[i])
		r_file.write('<tr><td>'+date_list[i]+'</td><td>'+time_list[i]+'</td><td>'+A_list[i]+'</td><td>'+B_list[i]+'</td></tr>\n')
	i+=1
r_file.write('  </table>\n'+
#' </body>\n'+
#'</html>\n'+
'</div>\n')

# 4я вкладка ################################################################### 
r_file.write('        <a class="tabs" id="tab4"></a>'+
'        <div class="tab">'+

'	  	<table>\n'+
'   			<tr>\n'+
'   	 			<th id="th1">Дата</th>\n'+
'    	 			<th id="th2">Время</th>\n'+
'    	 			<th id="th3">Номер A</th>\n'+
'     	 			<th id="th4">Номер B</th>\n'+
#'    	 			<th>Type</th>\n'+
'    			</tr>\n')
i=0
print ('#Все звонки')
while i<len(A_list):
#	print(date_list[i]+' | '+time_list[i]+' | '+A_list[i]+' | '+B_list[i]+' | '+t_list[i])
	r_file.write('<tr><td>'+date_list[i]+'</td><td>'+time_list[i]+'</td><td>'+A_list[i]+'</td><td>'+B_list[i]+'</td></tr>\n')
	i+=1

r_file.write('  </table>\n'+
'</div>\n'+
' </body>\n'+
'</html>\n')

r_file.flush()
print(' закрываем файлы')
d_file.close
r_file.close
#тест логирования===========
#print('# открываем файл для записи логов')
l_file=open("D:\prog\Python33\Missed_Calls\log.txt","w")
l_file.write(now_date+' '+now_time+' программа завершена')
l_file.close
#===========================


#input("программа завершена. Нажмите Enter.")