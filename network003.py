#!/usr/bin/env python
# IPv4 주소를 다른 포맷으로 변환 (p31)

import socket
from binascii import hexlify

# inet_aton()
# [IP address 문자열 포맷]을 [32-bit packed binary format]으로 변환 한다.
# 주소가 정상적인 것이 아니면 "OSError: illegal IP address string passed to inet_aton" 리턴
# 주소가 정상적인 것이라면 [32-bit packed binary format]을 리턴한다.
# inet_aton() does not support IPv6,
# and inet_pton() should be used instead for IPv4/v6 dual stack support.

# inet_ntoa()
# [32-bit packed binary format]을 [IP address 문자열 포맷]으로 변환 한다.

# hexlify()
# [32-bit packed binary format]을 [16-bit format]으로 표현.

# [binary data].decode('ascii')
# binary data => string

def convert_ip4_address():
    for ip_addr in ['127.0.0.1', '192.168.0.1']:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print("IP address : ", ip_addr, " => Packed : ", hexlify(packed_ip_addr).decode('ascii'), ", Unpacked : ", unpacked_ip_addr)

if __name__ == '__main__':
    convert_ip4_address()