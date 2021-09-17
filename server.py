#!/usr/bin/env python3
#!/usr/bin/python
import sys
import Adafruit_DHT
import socket
from time import sleep

HOST = '192.168.0.146'  # Standard loopback interface address (localhost)
PORT = 9000        # Port to listen on (non-privileged ports are > 1023)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((HOST,PORT))

serversocket.listen()

while True:
    try:
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        data = b"""temp:%f,humidity:%f"""%(temperature,humidity)
        c, addr = serversocket.accept()     # Establish connection with client.
        print('Got connection from', addr)
        c.sendall(data)
    except KeyboardInterrupt:
        c.close()
