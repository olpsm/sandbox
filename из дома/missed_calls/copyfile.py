import shutil # Подключаем модули
import datetime


# тестим копирование файлов по сети Win
#src=r'\\10.12.15.110\swap\test.txt'
#dst=r'D:\temp\test.txt'
#shutil.copyfile(r'\\10.12.15.110\swap\test1.txt', r'D:\temp\test.txt')
#shutil.copyfile(src,dst)


#работа со временем
#----------------------------------------------------------------------------------------------------
#now_date = datetime.date.today() # Текущая дата (без времени)
#now_time = datetime.datetime.now() # Текущая дата со временем
 
#cur_year = now_date.year # Год текущий
#cur_month = now_date.month # Месяц текущий
#cur_day = now_date.day # День текущий
#cur_hour = now_time.hour # Час текущий
#cur_minute = now_time.minute # Минута текущая
#cur_second = now_time.second # Секунда текущие
#num_week = now_date.isoweekday() # узнаем номер недели (от 1 до 7)

#print(now_time.strftime("%d.%m.%Y %I:%M %p")) # форматируем дату
#Наиболее интересные директивы используемые для форматирования времени.
#Расположены не в алфавитном порядке, а в логическом)
#%S — секунды. От 0 до 61
#%M — минуты. От 00 до 59
#%H — час. От 00 до 23
#%I — час. От 1 до 12
#%p -После перед полуднем или после (AM или PM) 
#%d — день. От 1 до 31
#%j — день как номер года. От 001 до 366
#%m — месяц. От 01 до 12
#%y — год в виде 2-х последних чисел. От 00 до 99
#%Y — год в виде полного числа


#результат
#\\10.12.35.174\Def_Log\YYYY.MM\YY-MM-DD.txt логи звонков лежат в файлах такого вида
#----------------------------------------------------------
now_date = datetime.date.today() # получаем текущую дату
YYYY_MM=now_date.strftime("%Y.%m") # дата в формате YYYY.MM
YY_MM_DD=now_date.strftime("%y-%m-%d") # дата в формате YY-MM-DD
#ss="10.12.15.110\swap"
src= '\%s\%s\%s%s'  % ("\\10.12.15.110\swap",YYYY_MM,YY_MM_DD,".txt")
#src= '%s\\\%s\%s\%s%s'  % ("r'",ss,YYYY_MM,YY_MM_DD,".txt'")
dst=r'D:\temp\test.txt'
print('src=', src)
print('dst=', dst)
shutil.copyfile(src,dst)
