#для удаления пробелов
import re

#обработка файлов

print('#открываем файл с данными')

d_file=open("test_log.txt")

print('# открываем файл для записи результатов')
r_file=open("result.txt","w")

print('#читаем файл построчно')

d_list=d_file.readlines()

#for line in d_list
 #if 1440 of 01440 in line
#	print line

#with open('/var/log/syslog', 'r') as logfile:
    #for line in logfile.readlines():
      #  if 'USB' in line:
      #      print line

print ('распечатываем d_list')
#print (d_list)

#print (line for line in d_list)	
#for line in d_list: print (line)
#line1=d_list[1]
#sline1=(line1.replace("  ","")).split(" ")

#создаем список вложенных списков
m_list=[]
#for line2 in d_list: m_list.append(re.sub("\s+", " ", line2))
#for line2 in d_list: m_list.append(re.sub("\s+", " ", line2))#.split(' '))
#for line2 in m_list:
#	if line2.find(' 1822 ')>11:
#		print (line2)
i=0
print('создаем новый список содержащий "1822"')
for line2 in d_list:
	if line2.find(' 1822 ')>11: 
		m_list.append(re.sub("\s+", " ", line2).split(' '))
		#print (line2)
i=0
while i<len(m_list):
	print(m_list[i][0]+' | '+m_list[i][1]+' | '+m_list[i][5]+' | '+m_list[i][6]+' | '+m_list[i][7])
	i+=1

print (m_list)
print ('пишем d_list в файл r_file')
r_file.write("")
r_file.write("результирующие строки")
r_file.write('\n')
#r_file.writelines(d_list)
for line in m_list:
	r_file.write()
#for line in d_list: r_file.write(list)
#r_file.flush()
print(' закрываем файлы')
d_file.close
r_file.close

#input("программа завершена. Нажмите Enter.")