'''
Простейшая система проверки орфографии основана на использовании списка известных слов.
Каждое слово в проверяемом тексте ищется в этом списке и, если такое слово не найдено,
оно помечается, как ошибочное.

Напишем подобную систему.

Через стандартный ввод подаётся следующая структура: первой строкой — количество d
записей в списке известных слов, после передаётся  d строк с одним словарным словом на строку,
затем — количество l строк текста, после чего — l строк текста.

Напишите программу, которая выводит слова из текста, которые не встречаются в словаре.
Регистр слов не учитывается. Порядок вывода слов произвольный. Слова, не встречающиеся в
словаре, не должны повторяться в выводе программы.
---------------------------
Sample Input:
3
a
bb
cCc
2
a bb aab aba ccc
c bb aaa
Sample Output:
aab
aba
c
aaa
---------------------------
Time Limit: 5 seconds
---------------------------

'''
##----------------------------------------------------------------------------------
#Input
Dict=[]
Text=[]
Result=[]
d= int(input())
while d>=1:
    Dict+=[input().strip().lower()]
    d-=1
l= int(input())
while l>=1:
    Text+=[x for x in input().split()]
    l-=1
#print(Dict, Text)

for txt in Text:
    if txt.lower() not in Dict and txt not in Result:
        Result+=[txt]
for res in Result:
    print(res)

