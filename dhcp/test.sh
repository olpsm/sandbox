#!/bin/bash
#!/usr/bin/expect

#объявим переменные
adres="192.168.100.1"
user="root"
pass="admin"

#спрашиваем у пользователя IP
echo "IP адрес" $adres
echo  "пользователь " $user
echo "пароль " $admin


#скрипт на expect 
expect -c '
spawn telnet '$adres' 23
expect "User name:"
send '$user'
expect "User password:"
send '$pass'
expect ">"
send "disp ver"
set results $expect_out(buffer)
'
echo $results

