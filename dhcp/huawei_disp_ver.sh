#!/bin/bash
count="1"
while [ $count -gt 0 ]; do
IP_LIST="192.168.100.$count"

echo Value of count is: $IP_LIST

for IP in $IP_LIST; do
	expect -c '
	spawn telnet '$IP'
	expect "User name:"
	send "root\r"
	expect "User password:"
	send "dremel\r"
	expect {	
			">"
					{
			send "enable\r"
			expect "#"
			send "configure terminal\r"
			expect "(config)#"
			send "sntp interval 3600\r"
			expect "#"
			send "sntp server address 10.12.15.2\r"
			expect "#"
			send "sntp time-zone + 4\r"
			expect "#"
			send "write\r"
			expect "{ <cr>|generate-carrier-config<K> }:"
			send "\r"
			expect "#"
			send "exit\r"
			expect "#"
			send "exit\r"
			set results $expect_out(buffer)  
       		set file [open "/var/log/expect/log.txt" a+];  
       		puts $file $results
 			puts $file $ip
       		close $file 
					}

		#echo "It's Huawei"




done

 let count=count-1
done 
