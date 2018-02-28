'''
Паша очень любит кататься на общественном транспорте, а получая билет, сразу проверяет,
счастливый ли ему попался. Билет считается счастливым, если сумма первых трех цифр
совпадает с суммой последних трех цифр номера билета.

Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу,
которая проверит равенство сумм и выведет "Счастливый", если суммы совпадают,
и "Обычный", если суммы различны.

На вход программе подаётся строка из шести цифр.

Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.
--------------------
Sample Input 1:
090234
Sample Output 1:
Счастливый
Sample Input 2:
123456
Sample Output 2:
Обычный
--------------------
'''
#----------------------------------------------------------------------------------------
while True:
    a=input()
    if len(a)!=6: print('Некорректный номер')
    elif (int(a[0])+int(a[1])+int(a[2])== int(a[-1])+int(a[-2])+int(a[-3])): print("Счастливый")
    else: print("Обычный")

#красиво
##bilet = [int(x) for x in list(input())] # приведение списка строк к списку типа int
##print("Счастливый" if sum(bilet[:3]) == sum(bilet[3:]) else "Обычный")
##
##2
##i=input()
##print('Счастливый'if int(i[0])+int(i[1])+int(i[2])==int(i[3])+int(i[4])+int(i[5]) else 'Обычный')
