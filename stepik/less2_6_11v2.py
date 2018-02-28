'''
Выведите таблицу размером n×n, заполненную числами от 1 до n2 по спирали,
выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
-------------------------------
Sample Input:
5
Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
-------------------------------

'''
##----------------------------------------------------------------------------------

        
a=int(input())
m = [[0 for j in range(a)] for i in range(a)]
i=0
j=0
c=1
Min=0
Max=a
step=0
while c <=a**2:
    
    for j in range(Min+step,Max-step):
        m[i][j]=c
        c+=1
    
    for i in range(Min+1+step,Max-step):
        m[i][j]=c
        c+=1
    
    for j in range(Max-2-step,Min-1+step,-1):
        m[i][j]=c
        c+=1
    
    for i in range(Max-2-step,Min+step,-1):
        m[i][j]=c
        c+=1
    
    step+=1

for i in range(a):
    for j in range(a):
        print(m[i][j], end=' ')
    print()
