#!/usr/bin/env python
# 호스트 컴퓨터와 네트워크 바이트 순서에 맞게 정수를 변환하기 (p34)

import socket

def convert_integer():
    data = 1234
    
    # 32-bit
    print("Original : {0} => [Long] host byte order : {1}, Network byte order : {2}".format(data, socket.ntohl(data), socket.htonl(data)))
    
    # 16-bit
    print("Original : {0} => [Short] host byte order : {1}, Network byte order : {2}".format(data, socket.ntohs(data), socket.htons(data)))
    
if __name__ == '__main__':
    convert_integer()