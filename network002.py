#!/usr/bin/env python
# 외부 컴퓨터의 IP 주소 가져오기 (p29)

import socket

def get_remote_machine_info():
    remote_host = 'www.vtouchinc.com';
    try:
        print("IP address of ", remote_host, " : ", socket.gethostbyname(remote_host))
    except(socket.error, err_msg):
        print(remote_host, " : ", err_msg)
        
if __name__ == '__main__':
    get_remote_machine_info()