#!/usr/bin/env python
# 자신의 컴퓨터 이름과 IPv4 주소 출력 (p26)

import socket

host_name = socket.gethostname()
print ("Host name : ", host_name)

print ("IP address : ", socket.gethostbyname(host_name))