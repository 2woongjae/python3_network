#!/usr/bin/env python
# 호스트 컴퓨터와 네트워크 바이트 순서에 맞게 정수를 변환하기 (p34)

import socket

def convert_integer():
    data = 1234
    
    # 32-bit
    print("Original : ", data, " => [Long] host byte order : ", socket.ntohl(data), ", Network byte order : ", socket.htonl(data))
    
    # 16-bit
    print("Original : ", data, " => [Short] host byte order : ", socket.ntohs(data), ", Network byte order : ", socket.htons(data))
    
if __name__ == '__main__':
    convert_integer()