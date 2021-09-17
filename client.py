#!/usr/bin/env python3
import socket
from time import sleep

def main():
    HOST = '192.168.0.146'  # The server's hostname or IP address
    PORT = 9000        # The port used by the server
    fl = open('data.csv','w').close
    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    reader(HOST,PORT)
    #s.connect((HOST, PORT))

def reader(HOST,PORT):
    while True: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        data = s.recv(1024)
        print('Received', repr(data))
        rec = str(repr(data))
        logger(rec)
        s.close()
        sleep(1)

def logger(data):
    fl = open('data.csv','a')
    fl.write(data+"\n")
    fl.close()
main()
