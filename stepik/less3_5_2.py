'''
Напишите программу, которая подключает модуль math и, используя значение числа π
из этого модуля, находит для переданного ей на стандартный ввод радиуса круга периметр
этого круга и выводит его на стандартный вывод.
---------------------------
Sample Input:
10.0
Sample Output:
62.83185307179586
---------------------------

'''
##----------------------------------------------------------------------------------

from math import pi
#import math

r=input()
print(str(2*pi*float(r)))
