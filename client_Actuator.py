#!/usr/bin/env python3
import socket
from time import sleep
from datetime import datetime

def main():
    HOST = '192.168.0.146'  # The server's hostname or IP address
    PORT = 9000        # The port used by the server
    fl = open('data.csv','w').close
    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    reader(HOST,PORT)
    #s.connect((HOST, PORT))

def reader(HOST,PORT):
    try:
        while True: 
            ch = input("1: Turn on LED \n 2: Turn OFF LED")
            if(ch == "1"):
                logger(str(datetime.now())+ " Led turned On")
            elif(ch == "2"):
                logger(str(datetime.now())+ " Led turned Off")
            else:
                print("Invalid Choise")
                continue
            ch = int(ch)
            ch = b"""%d"""%(ch)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            s.sendall(ch)
    except KeyboardInterrupt:
        pass

def logger(data):
    print(data)
    fl = open('data.csv','a')
    fl.write(data+"\n")
    fl.close()
main()
