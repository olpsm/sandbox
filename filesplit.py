# Подключаем модули
import shutil # для копирования 
import os

def pars_CAP():
# обработка исходного файла *.cap

#print('#открываем файл с данными')
  d_file=open(src)
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
  
  # ОСНОВНАЯ ЧАСТЬ


#src= "D:\tmp\R4D1 results_sorted.csv"
Dst_dir="D:\tmp\R4_1 scripts"


#pars_CAP() # разбираем файл
ph_book=read_PHBOOK("ph_book_portal.txt") #открываем файл ph_book_portal.txt'
ph_book.update(read_PHBOOK("ph_book_custom.txt")) #открываем файл ph_book_custom.txt' и обновляем словарь


r_file=open("D:\prog\Python33\Missed_Calls\missed_calls.html","w")