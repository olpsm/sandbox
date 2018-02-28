#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print ('connected:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    print (data, '/r')
    #conn.send(data.upper())

conn.close()
print ('disconnected:', addr)
