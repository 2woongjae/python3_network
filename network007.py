#!/usr/bin/env python
# 소켓 에러를 간결하면서도 자연스럽게 처리하기 (p37)

import sys
import socket
import argparse

def main():
    # setup argument parsing
    parser = argparse.ArgumentParser(description='Socket Error Examples')
    parser.add_argument('--host', action="store", dest="host", required=False)
    parser.add_argument('--port', action="store", dest="port", type=int, required=False)
    parser.add_argument('--file', action="store", dest="file", required=False)
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file
    
    print("host : ", host, ", port : ", port, "filename : ", filename)
    
    # First try-except block -- create socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except(socket.error, e):
        print("Error creating socket : ", e)
        sys.exit(1)
    
    # Second try-except block -- connect to given host/port
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print(e)
        sys.exit(1)
    except:
        print("Address-related error connecting to server : ")
        sys.exit(1)
    
    #except(socket.error, e):
    #    print("Connection error : ", e)
    #    sys.exit(1)
        
    print("check")
    sys.exit(1)
    
    # Third try-except block -- sending data
    try:
        s.sendall("GET ", filename, " HTTP/1.0\r\n\r\n")
    except(socket.error, e):
        print("Error sending data : ", e)
        sys.exit(1)
        
    while 1:
        # Fourth try-except block -- waiting to receive data from remote host
        try:
            buf = s.recv(2048)
        except(socket.error, e):
            print("Error receiving data : ", e)
            sys.exit(1)
            
        if not len(buf):
            break
            
        # write the received data
        sys.stdout.write(buf)
                
if __name__ == '__main__':
    main()