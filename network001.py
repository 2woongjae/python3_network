#!/usr/bin/env python
# 자신의 컴퓨터 이름과 IPv4 주소 출력 (p26)

import socket

def print_machine_info():
    host_name = socket.gethostname();
    ip_address = socket.gethostbyname(host_name);
    print ("Host name : ", host_name)
    print ("IP address : ", ip_address)
    
if __name__ == '__main__':
    print_machine_info()