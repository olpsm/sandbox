'''
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк,
где в каждой строке записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит
его среднюю оценку по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.

Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике, физике
и русскому языку по всем абитуриентам:

Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом: 

print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']
--------------------------
Sample Input:
Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85
Sample Output:
85.0
94.0
71.666666667
81.0 84.0 85.666666667
---------------------------

'''
##----------------------------------------------------------------------------------
def find_word(string):
    result=[]
    st=[]
    marks=[]
    avg_math=0
    avg_phiz=0
    avg_ruln=0
    for x in string:
        st+=[x.split(';')[0]]
        marks+=[[int(x.split(';')[1]),int(x.split(';')[2]),int(x.split(';')[3])]]
    for x in marks:    
        avg_math+=x[0]/len(marks)
        avg_phiz+=x[1]/len(marks)
        avg_ruln+=x[2]/len(marks)
        result+=[sum(x)/len(x)]
    result+=[[avg_math, avg_phiz, avg_ruln]]
    return result
#main            
fl=input('Input file name: ')
s=''
if fl not in ['n','N']:
    with open(fl,'r') as inpt:
        txt=[]
        for ln in inpt:
            txt+=[ln]
            s=find_word(txt)
    with open('3-4-4result.txt','w') as outp:
        if s !='':
            for i in s:
                if type(i)==list:
                    for j in i:
                        print(j,end=' ')
                        outp.write(str(j)+' ')
                else:
                    outp.write(str(i)+'\n')
                    print(i)
           
            
            print()
            print("!File 3-4-3result.txt created! Let's check it")
        else: print ('Something goes wrong!!!')
else:
    #ln=input('Test string: ')
    ln=['Петров;85;92;78', 'Сидоров;100;88;94', 'Иванов;58;72;85']
    #print (ln)
    for i in find_word(ln):
        if type(i)==list:
            for j in i:
                print(j,end=' ')
        else:
            print(i)
'''
красивые решения
v1
d = {}
num = 0
sums = [0, 0, 0]

with open("output.txt", "w") as out:
  with open("input.txt") as inp:
    for line in inp:
      lst = line.split(";")
      average = 0
      for i in range(3):
        a = int(lst[i + 1])
        average += a
        sums[i] += a
      average /= 3
      out.write(str(average) + "\n")
      num += 1

  for s in sums:
    out.write(str(s / num) + " ")
  out.write("\n")
'''
