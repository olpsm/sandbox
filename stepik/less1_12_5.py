'''
Напишите программу, которая получает на вход три целых числа, по одному числу в строке,
и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.
--------------------
Sample Input 1:
8
2
14
Sample Output 1:
14
2
8
Sample Input 2:
23
23
21
Sample Output 2:
23
21
23
Time Limit: 5 seconds
--------------------
'''
#----------------------------------------------------------------------------------------
s=[]
i=0
while i<3:
    s.append(int(input()));i+=1
s.sort()
print(s[2])
print(s[0])
print(s[1])

    


