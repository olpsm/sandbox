##время для его сна составляет X минут.
##Коля хочет поставить себе будильник так, чтобы он прозвенел ровно через XX минут после полуночи,
##однако для этого необходимо указать время сигнала в формате часы, минуты.

## ждем ввода минут
s_min=int(input())
## считаем часы
print (s_min//60)
## считаем минуты
print (s_min%60)

