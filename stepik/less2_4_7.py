'''
Узнав, что ДНК не является случайной строкой, только что поступившие в Институт
биоинформатики студенты группы информатиков предложили использовать алгоритм сжатия,
который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых
символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом
и выводит закодированную последовательность на стандартный вывод. Кодирование должно
учитывать регистр символов.

-------------------------------
Sample Input 1:
aaaabbcaa
Sample Output 1:
a4b2c1a2
Sample Input 2:
abc
Sample Output 2:
a1b1c1
-------------------------------

'''
##----------------------------------------------------------------------------------
string=input()
result=''
i=0
while i<len(string):
    count=1
    j=i+1
    while j<len(string)and string[i]== string[j]: count+=1;j+=1; 
    result=result+string[i]+str(count)
    i=j
print(result)
'''    
a=input()
s=1
a=a+'0'
for j in range (0,len(a)-1):
    if a[j]==a[j+1]:
     s+=1
    else:
     print((a[j]+str(s)),end='')
     s=1
'''

    


