#!/usr/bin/python3.3

#\\10.12.35.174\Def_Log\YYYY.MM\YY-MM-DD.cap логи звонков лежат в файлах такого вида
# ph_book.txt - телефонный справочник

# признак звонка
# H - входящий, неотвеченный, отбой с А
# G - входящий, ответ абон
# 9 - отбой
# 7 - исходящий



# Подключаем модули
import shutil # для копирования 
import datetime # получение даты
import os


#############################################
# копирование файла с PC_OEGU
now_date = datetime.date.today() # получаем текущую дату
now_time = datetime.datetime.now().strftime("%H:%M:%S") #получаем текущее время
YYYY_MM=now_date.strftime("%Y.%m") # дата в формате YYYY.MM
YY_MM_DD=now_date.strftime("%y-%m-%d") # дата в формате YY-MM-DD
src= '\%s\%s\%s%s'  % ("\\10.12.35.174\Def_Log",YYYY_MM,YY_MM_DD,".cap")
dst= '%s\%s\%s%s'  % ("D:\prog\Python33\Missed_Calls",YYYY_MM,YY_MM_DD,".txt")
Dst_dir='%s\%s'  % ("D:\prog\Python33\Missed_Calls",YYYY_MM)

# проверяем наличие директории с данным месяцем
if not os.path.exists(Dst_dir):
                os.mkdir(Dst_dir)
# копируем файлы
shutil.copyfile(src,dst)

#############################################
# обработка исходного файла *.cap
#print('#открываем файл с данными')
d_file=open(dst)
#print('# открываем файл для записи результатов')
r_file=open("D:\prog\Python33\Missed_Calls\missed_calls.html","w")
#читаем файл построчно
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
#создаем новый список содержащий '+Ph_num+' или '+ Mph_num
for line2 in d_list:
	if ((line2[37:51].strip()==(Ph_num or Mph_num)) or (line2[53:75].strip()==(Ph_num or Mph_num))) and line2[76:77].strip()!="9": # отбои не берем
		date_list.append(line2[0:2]+'-'+line2[2:4]+'-'+line2[4:6]) #дата
		time_list.append(line2[7:9]+':'+line2[9:11]) #время
		A_list.append(line2[37:51].strip()) #номер А
		B_list.append(line2[53:75].strip()) #номер B
		t_list.append(line2[76:77].strip()) #признак звонка

#############################################

# чтение ph_book_portal.txt и составление словаря из него
print('#открываем файл ph_book_portal.txt')
b_file=open("ph_book_portal.txt")
i=0
#dubl={} # проверочный словарь для дублирующихся номеров
ph_book={} # словарь с номерами и фамилями Key- номер телефона
while True:
    line = b_file.readline() # читаем построчно
    if not line: break
    i+=1
    line=line.split(':') # получаем список из 2
    if line[0] in ph_book: # проверяем есть ли уже такой номер, если есть подрезаем список до фамилии и добавляем новую фамилию
        old_v=ph_book.get(line[0])[0:ph_book.get(line[0]).find(' ')]
        new_v=line[1][0:line[1].find(' ')]
        #dubl[line[0]]=None
        ph_book[line[0]]=old_v+','+new_v+' '
    else:    
        ph_book[line[0]]=line[1]

#############################################
# Формируем HTML страницу
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
		#print(date_list[i]+' | '+time_list[i]+' | '+A_list[i]+' | '+B_list[i]+' | '+t_list[i])
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
'    	 			<th>Type</th>\n'+
'    	 			<th>Имя из справочника</th>\n'+
'    			</tr>\n')
i=0
print ('#Все звонки')
while i<len(A_list):
                if t_list[i]==("G"):
                                ph_name=str(ph_book.get(A_list[i]))
                                #if ph_name=='None'
                                ph_type='Вход.'
                elif t_list[i]==("H"):
                                ph_name=str(ph_book.get(A_list[i]))
                                ph_type='Неотв.'
                else:
                                ph_name=str(ph_book.get(B_list[i]))
                                ph_type='Исход.'
              
                r_file.write('<tr><td>'+date_list[i]+'</td><td>'+time_list[i]+'</td><td>'+A_list[i]+'</td><td>'+B_list[i]+'</td><td>'+ph_type+'</td><td>'+ ph_name +'</td></tr>\n')
                i+=1

r_file.write('  </table>\n'+
'</div>\n'+
' </body>\n'+
'</html>\n')

r_file.flush()
print(' закрываем файлы')
d_file.close
r_file.close
b_file.close
#тест логирования===========
#print('# открываем файл для записи логов')
l_file=open("D:\prog\Python33\Missed_Calls\log.txt","w")
l_file.write(str(now_date)+' '+str(now_time)+'- программа завершена')
l_file.close
#===========================

