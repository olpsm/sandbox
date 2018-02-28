'''
Скачайте файл. В нём указан адрес другого файла, который нужно скачать с использованием модуля requests
и посчитать число строк в нём.

Используйте функцию get для получения файла
(имеет смысл вызвать метод strip к передаваемому параметру, чтобы убрать пробельные символы по краям). 

После получения файла вы можете проверить результат, обратившись к полю text.
Если результат работы скрипта не принимается, проверьте поле url на правильность.
Для подсчёта количества строк разбейте текст с помощью метода splitlines.

В поле ответа введите одно число или отправьте файл, содержащий одно число.

Описание модуля и примеры работы с ним
http://docs.python-requests.org/en/master/user/quickstart/#make-a-request
Установка модуля: python -m pip install requests
---------------------------

'''
##----------------------------------------------------------------------------------

import requests
name=input('Please input file name: ')
with open(name) as srcfl:
    srcurl=srcfl.readline().strip()
#print(srcurl)
r = requests.get(srcurl)
#print (r.text.splitlines())
print(len(r.text.splitlines()))

'''
from requests import get
with open('dataset_3378_2.txt') as file:
    print(len(get(file.readline().strip()).text.splitlines()))
'''
