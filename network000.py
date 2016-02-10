#!/usr/bin/env python
# 자신의 컴퓨터 이름과 IPv4 주소 출력 (p26)
# 대화식 인터프리터 연습

import socket

host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)

print ("Host name : {0}".format(host_name))
print ("IP address : {0}".format(ip_address))