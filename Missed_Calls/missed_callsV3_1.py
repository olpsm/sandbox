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
def copy_CAP():
#Функция копирования файла из сети на локальный комп
# проверяем наличие директории с данным месяцем
                if not os.path.exists(Dst_dir):
                                os.mkdir(Dst_dir)
# копирование файла с PC_OEGU
                shutil.copyfile(src,dst)
#############################################
#############################################
def pars_CAP():
# обработка исходного файла *.cap

#print('#открываем файл с данными')
  d_file=open(dst)
#читаем файл построчно
  #d_list=d_file.readlines()
  while True:
    line2 = d_file.readline() # читаем построчно
    if not line2: break
#создаем новый список содержащий '+Ph_num+' или '+ Mph_num
    #print(Ph_num)
    if ((line2[37:51].strip()==(Ph_num or Mph_num)) or (line2[53:75].strip()==(Ph_num or Mph_num))) and line2[76:77].strip()!="9": # отбои не берем
            date_list.append(line2[0:2]+'-'+line2[2:4]+'-'+line2[4:6]) #дата
            time_list.append(line2[7:9]+':'+line2[9:11]) #время
            A_list.append(line2[37:51].strip()) #номер А
            B_list.append(line2[53:75].strip()) #номер B
            t_list.append(line2[76:77].strip()) #признак звонка
  d_file.close
#############################################
#############################################
def read_PHBOOK(phbook):
# чтение ph_book_portal.txt и составление словаря из него
  print(phbook)
  b_file=open(phbook)
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
  return ph_book       
  b_file.close
#############################################
#############################################
def write_TAB(id,type):
# id = tab1, tab2, tab3, tab4
# type = "H","7", "G", None

  r_file.write(
  '        <a class="tabs" id="'+id+'"></a>'+
  '        <div class="tab">'+
  '	  	<table>\n'+
  '   			<tr>\n'+
  '   	 			<th id="th1">Дата</th>\n'+
  '    	 			<th id="th2">Время</th>\n'+
  '    	 			<th id="th3">Номер A</th>\n'+
  '     	 			<th id="th4">Номер B</th>\n')
  if id == 'tab4':
      #print ('HEAD')          
      r_file.write(
      '    	 			<th>Type</th>\n'+
      '    	 			<th>Имя из справочника</th>\n'+
      '    			</tr>\n')
  else:
      r_file.write(
      '    			</tr>\n')          
  i=0
  while i<len(A_list):
     if id == 'tab4':
          #print ('tab4',id)      
          if t_list[i]==("G"):
                ph_name=str(ph_book.get(A_list[i]))
                ph_type='Вход.'
          elif t_list[i]==("H"):
                ph_name=str(ph_book.get(A_list[i]))
                ph_type='Неотв.'
          else:
                ph_name=str(ph_book.get(B_list[i]))
                ph_type='Исход.'
          r_file.write('<tr><td>'+date_list[i]+'</td><td>'+time_list[i]+'</td><td>'+A_list[i]+'</td><td>'+B_list[i]+'</td><td>'+ph_type +'</td><td>'+ ph_name+'</td></tr>\n')
          #print (i)
          
     else:
          #print ('!tab4',id)      
          if t_list[i]==type:
             r_file.write('<tr><td>'+date_list[i]+'</td><td>'+time_list[i]+'</td><td>'+A_list[i]+'</td><td>'+B_list[i]+'</td></tr>\n')
          
     i+=1
  r_file.write(
  '  </table>\n'+
  '</div>\n')
#############################################
'''def write_RESULT()
  r_file.write(
  '<!DOCTYPE HTML>\n'+
  '<html>\n'+
  ' <head>\n'+
  '<meta http-equiv="refresh" content="1; URL=file://localhost/D:/prog/Python33/Missed_Calls/missed_calls.html#tab4">\n'+# не корректно срабатывает
  #'  <meta charset="utf-8">\n'+ # не работает РАЗОБРАТЬСЯ!!!
  '  <link rel="stylesheet" type="text/css" href="missed_calls.css">\n'+ # файл стилей css в одной папке с missed_calls.html
  ' <title>Conversation table for number '+
  Ph_num+
  '  \n</title>\n'+
  ' </head>\n' +
  ' <body>\n'+
  ' <i> Обновлено в '+now_time+ '. Количество звонков:' + str(len(A_list))+
  '</i>\n'+
  '  <br>\n'+
  '  <br>\n'+
  ' 	<div class="tabsLink">\n'+
  '       	<a href="#tab1">Неотвеченые</a>\n'+
  '        	<a href="#tab2">Исходящие</a>\n'+
  '		<a href="#tab3">Входящие</a>\n'+
  '		<a href="#tab4">Все звонки</a>\n'+
  '       </div>\n')

# 1я вкладка   Непринятые ####################################################
# 2я вкладка  Исходящие ################################################################### 
# 3я вкладка '#Входящие'################################################################### 
# 4я вкладка # Все ###################################################################
  tabs=[('tab1',"H"),('tab2',"7"),('tab3',"G"),('tab4','None')]
  for tab in tabs:
  #print(tab[0],tab[1])
     write_TAB(tab[0],tab[1])

  r_file.write(
  ' </body>\n'+
  '</html>\n')
'''
# ОСНОВНАЯ ЧАСТЬ

now_date = datetime.date.today() # получаем текущую дату
now_time = datetime.datetime.now().strftime("%H:%M:%S") #получаем текущее время
YYYY_MM=now_date.strftime("%Y.%m") # дата в формате YYYY.MM
YY_MM_DD=now_date.strftime("%y-%m-%d") # дата в формате YY-MM-DD
src= '\%s\%s\%s%s'  % ("\\10.12.35.174\Def_Log",YYYY_MM,YY_MM_DD,".cap")
dst= '%s\%s\%s%s'  % ("D:\prog\Python33\Missed_Calls",YYYY_MM,YY_MM_DD,".txt")
Dst_dir='%s\%s'  % ("D:\prog\Python33\Missed_Calls",YYYY_MM)
#создаем список вложенных списков
date_list=[]
time_list=[]
A_list=[]
B_list=[]
t_list=[]
#Ph_num=input('Введите искомый номер  ')
Ph_num="1440" #корп. номер
Mph_num="0"+Ph_num #номер FMC

copy_CAP() # копируем файл
pars_CAP() # разбираем файл
ph_book=read_PHBOOK("ph_book_portal.txt") #открываем файл ph_book_portal.txt'
ph_book.update(read_PHBOOK("ph_book_custom.txt")) #открываем файл ph_book_custom.txt' и обновляем словарь


r_file=open("D:\prog\Python33\Missed_Calls\missed_calls.html","w")

# Формируем HTML страницу
r_file.write(
'<!DOCTYPE HTML>\n'+
'<html>\n'+
' <head>\n'+
'<meta http-equiv="refresh" content="1; URL=file://localhost/D:/prog/Python33/Missed_Calls/missed_calls.html#tab4">\n'+# не корректно срабатывает
#'  <meta charset="utf-8">\n'+ # не работает РАЗОБРАТЬСЯ!!!
'  <link rel="stylesheet" type="text/css" href="missed_calls.css">\n'+ # файл стилей css в одной папке с missed_calls.html
' <title>Conversation table for number '+
Ph_num+
'  \n</title>\n'+
' </head>\n' +
' <body>\n'+
' <i> Обновлено в '+now_time+ '. Количество звонков:' + str(len(A_list))+
'</i>\n'+
'  <br>\n'+
'  <br>\n'+
' 	<div class="tabsLink">\n'+
'       	<a href="#tab1">Неотвеченые</a>\n'+
'        	<a href="#tab2">Исходящие</a>\n'+
'		<a href="#tab3">Входящие</a>\n'+
'		<a href="#tab4">Все звонки</a>\n'+
'       </div>\n')
# 1я вкладка   Непринятые ####################################################
# 2я вкладка  Исходящие ################################################################### 
# 3я вкладка '#Входящие'################################################################### 
# 4я вкладка # Все ###################################################################
tabs=[('tab1',"H"),('tab2',"7"),('tab3',"G"),('tab4','None')]
for tab in tabs:
  write_TAB(tab[0],tab[1])

r_file.write(
' </body>\n'+
'</html>\n')

r_file.flush()
print(' закрываем файлы')
r_file.close

#тест логирования===========
#print('# открываем файл для записи логов')
#l_file=open("D:\prog\Python33\Missed_Calls\log.txt","w")
#l_file.write(str(now_date)+' '+str(now_time)+'- программа завершена')
#l_file.close
#===========================

