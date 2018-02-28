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

di,dj=1,1
Min=0
Max=a-1
while c <=a**2:
    m[i][j]=c
    print (di,dj,i,j, c,m)
    c+=1
    if Min<=j<Max:
        j+=dj
    elif Min<=i<Max:
        i+=di
    elif i==j and j==Max:
        Max-=1
        
        j-=1
        di=-di
        dj=-dj
    elif i==j and i==Min:
        di=-di
        dj=-dj
        Min+=1
        
        
#print(m)     
for i in range(a):
    for j in range(a):
        print(m[i][j], end='')
    print()
