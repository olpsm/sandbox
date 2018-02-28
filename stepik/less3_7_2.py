'''
Дополнительная

В какой-то момент в Институте биоинформатики биологи перестали понимать,
что говорят информатики: они говорили каким-то странным набором звуков. 

В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении
подстановочный шифр, т.е. заменяли каждый символ исходного сообщения на соответствующий ему другой символ.
Биологи раздобыли ключ к шифру и теперь нуждаются в помощи: 

Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки.
Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита,
на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом,
и ещё одна строка, которую нужно расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d,
c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра.
Получаем следующие строки, которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac

Sample Input 1:
abcd
*d%#
abacabadaba
#*%*d*%
Sample Output 1:
*d*%*d*#*d*
dacabac

Sample Input 2:
dcba
badc
dcba
badc

Sample Output 2:
badc
dcba
---------------------------

'''
##----------------------------------------------------------------------------------

key1=input('key1:')
key2=''
while len(key2) != len(key1):
    key2=input('key2: ')
istr1=input('string 1:')
istr2=input('string 2:')
'''
key1='abcd'
key2='*d%#'
istr1='abacabadaba'
istr2='#*%*d*%'
'''
rstr1=''
rstr2=''
mdf={}
mdr={}
for i in range(len(key1)):
    mdf[key1[i]]=key2[i];
    mdr[key2[i]]=key1[i];
for i in istr1:
    rstr1+=mdf[i]
for i in istr2:
    rstr2+=mdr[i]

#answ1='*d*%*d*#*d*'
#answ2='dacabac'
print (rstr1)#, answ1==rstr1)
print (rstr2)#, answ2==rstr2)
"""
# put your python code here
alpha=input()
alpha_ciph=input()
line_ciph=input()
line_deciph=input()

for k in (line_ciph):
	i=alpha.find(k)
	print(alpha_ciph[i],end='')
	
print()
for k in (line_deciph):
	i=alpha_ciph.find(k)
	print(alpha[i],end='')




v2
plain, cipher = list(input()), list(input())
print(''.join([dict(zip(plain, cipher))[c] for c in list(input())]), ''.join([dict(zip(cipher, plain))[c] for c in list(input())]), sep='\n')

v3
a,b,c,d=[i for i in input()],[i for i in input()],{},{}
for i in range(len(a)):
    c[a[i]]=b[i]
    d[b[i]]=a[i]
a,b=[c[i] for i in input()], [d[i] for i in input()]
for i in [a,b]:
    for j in i:
        print(j, end='')
    print()

"""
