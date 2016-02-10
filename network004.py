#!/usr/bin/env python
# 주어진 포트 번호와 프로토콜 정보로 서비스 이름 찾기 (p32)

import socket

def find_service_name():
    protocolname = 'tcp'
    for port in [80, 25]:
        print("Port : ", port, " => service name : ", socket.getservbyport(port, protocolname))
    
    print("Port : ", 53, " => service name : ", socket.getservbyport(53, 'udp'))
    
if __name__ == '__main__':
    find_service_name()