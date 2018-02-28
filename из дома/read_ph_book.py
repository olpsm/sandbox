#!/usr/bin/python3.3

# чтение ph_book.txt и составление словаря из него

print('#открываем файл ph_book.txt')
b_file=open("ph_book.txt")
i=0
dubl={}
ph_book={}
while True:
    line = b_file.readline()
    if not line: break
    i+=1
    line=line.split(':')
    if line[0] in ph_book:
        #print (line[0],'|',ph_book.get(line[0]))
        old_v=ph_book.get(line[0])[0:ph_book.get(line[0]).find(' ')]
        new_v=line[1][0:line[1].find(' ')]
        dubl[line[0]]=None
        ph_book[line[0]]=old_v+','+new_v+' '
    else:    
        ph_book[line[0]]=line[1]
    
#print ('номера ', ph_book.keys())
print ('размер словаря',len(ph_book))
print('обраотано строк',i)
#print('dubl_',dubl.keys())
# вывод дублирующихся строк
for eh in dubl.keys():
    print (eh,ph_book[eh])
    
print ('закрываем файлы')
b_file.close