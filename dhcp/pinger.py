#!/usr/bin/python3.3

import ping, socket
HOST=172.16.24.199
count=3
try:
    ping.verbose_ping(host, count)
    delay = ping.Ping('www.wikipedia.org', timeout=2000).do()
except socket.error, e:
    print "Ping Error:", e
