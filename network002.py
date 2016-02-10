#!/usr/bin/env python
# 외부 컴퓨터의 IP 주소 가져오기 (p29)

import socket

def get_remote_machine_info():
    remote_host = 'www.vtouchinc.com';
    try:
        print("IP address of {0} : {1}".format(remote_host, socket.gethostbyname(remote_host)))
    except socket.error as e:
        print(remote_host, " : ", e)
        
if __name__ == '__main__':
    get_remote_machine_info()