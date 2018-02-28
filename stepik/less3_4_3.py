'''
Недавно мы считали для каждого слова количество его вхождений в строку.
Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки)
и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось.
Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:
abc a bCd bC AbC BC BCD bcd ABC
Sample Output:
abc 3

'''
##----------------------------------------------------------------------------------
def find_word(string):
    lst=[x for x in string.lower().split()]
    dct={}
    re=[]
    result=''
    for x in lst:
        dct[x]=lst.count(x)
        
    values=dct.values()
   # print(sorted(values)[-1])
    for key, value in dct.items():
        if sorted(values)[-1] == value: re+= [str(key) + ' '+ str(value)+'\n']
        re=sorted(re)
    for x in re:
        result+=x
    return result
#main            
fl=input('Input file name: ')
s=''
if fl not in ['n','N']:
    with open(fl,'r') as inpt:
        txt=''
        for ln in inpt:
            txt+=ln
            s=find_word(txt)
    with open('3-4-3result.txt','w') as outp:
        if s !='':
            print(s)
            outp.write(s)
            print()
            print("!File 3-4-3result.txt created! Let's check it")
        else: print ('Something goes wrong!!!')
else:
    #ln=input('Test string: ')
    ln='abc a bCd bC AbC BC BCD bcd ABC'
    print (ln)
    print(find_word(ln))
    

'''
красивые решения
v1
with open('dataset_3363_2.txt', 'r') as f:
    s = f.readline().strip()
i = 0
while i < len(s):
    j = i + 1
    while j < len(s) and s[j].isdigit():
        j += 1
    print(s[i] * int(s[i+1:j]), end='')
    i = j

Первый символ - гарантированно буква.
Перебираем все последующие, пока они цифровые или пока не достигнут конец строки.
После внутреннего цикла j либо указывает на следующую букву, либо на конец строки. В обоих случаях между s[i] и s[j] - цифры, составляющие нужное нам число повторов символа s[i].
Печатаем символ нужное число раз, присваиваем i индекс следующей буквы для новой итерации цикла.

v2
with open ('dataset_3363_2.txt','r') as inf:
    s1 = inf.readline().strip()
n=0
k=''
alpha=[]
numbers=[]
for i in range(len(s1)):             #список только с буквами
    if s1[i].isalpha():
        alpha.append(s1[i])
for i in range (len(s1)):             #список только с числами
    if s1[i].isdigit():
        n+=1
        if i == len(s1)-1:
            numbers.append(s1[len(s1)-n:i+1])
    if s1[i].isalpha() and n!=0:
        numbers.append(s1[i-n:i])
        n=0
for i in range(len(alpha)):            #умножаем букву из первого списка на число из второго списка
    k=k+alpha[i]*int(numbers[i])          #складываем все буквы в str переменную
with open ('outfile.txt','w') as ouf:
    ouf.write(k)
'''
