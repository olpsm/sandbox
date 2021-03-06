'''
Напишите программу, на вход которой подаётся прямоугольная матрица в виде
последовательности строк, заканчивающихся строкой, содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый элемент
в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
-------------------------------
Sample Input 1:
9 5 3
0 7 -1
-5 2 9
end
Sample Output 1:
3 21 22
10 6 19
20 16 -1
Sample Input 2:
1
end
Sample Output 2:
4
-------------------------------

'''
##----------------------------------------------------------------------------------

b=[]
a=[]
c=''
while True:
    c=input()
    if c!='end': b=[int(i) for i in c.split()];a+=[b];
    else: break

#a=[[9, 5, 3], [0, 7, -1], [-5, 2, 9]]
#b=[9, 5, 3]
k,m=len(a), len(b)
#print (a, len(a), len(b))
b = [[0 for j in range(m)] for i in range(k)]
for i in range(k):
    for j in range(m):
        for d in (-1, 1):
            ai = i + d
            aj = j + d # (ai, aj)
            if  ai >= k: ai=0
            if aj >= m: aj= 0
            b[i][j]+=a[i][aj]+a[ai][j]

#print(b)
for i in range(k):
    for j in range(m):
        print(b[i][j], end=' ')
    print()
