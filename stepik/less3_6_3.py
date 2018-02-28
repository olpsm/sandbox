'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора. 

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
---------------------------

'''
##----------------------------------------------------------------------------------

import requests
name=input('Please input file name: ')

with open(name) as srcfl:
    srcurl=srcfl.readline().strip()
while True:
    r = requests.get(srcurl)
    if r.text.split()[0]=="We": break
    else: srcurl = "https://stepic.org/media/attachments/course67/3.6.3/"+r.text.strip()
print(r.text)

'''

'''
