#!/usr/bin/env python
# 기본 소켓 타임아웃 값을 설정하거나 얻기 (p35)

import socket

def test_socket_timeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Default socket timeout : ", s.gettimeout())
    s.settimeout(100)
    print("Current socket timeout : ", s.gettimeout())
    
if __name__ == '__main__':
    test_socket_timeout()