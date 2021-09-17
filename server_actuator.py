#!/usr/bin/env python3
#!/usr/bin/python
import sys
import socket
import RPi.GPIO as GPIO
from time import sleep

def setupMain():
    HOST = '192.168.0.146'  # Standard loopback interface address (localhost)
    PORT = 9000        # Port to listen on (non-privileged ports are > 1023)
    LED_PIN = 18
    Buzz_PIN = 3
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN,GPIO.OUT)
    GPIO.setup(Buzz_PIN,GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.LOW)

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((HOST,PORT))
    serversocket.listen()
    actuator(LED_PIN,Buzz_PIN,serversocket)


def actuator(LED_PIN,Buzz_PIN,serversocket):
    try:
        while True:
            c, addr = serversocket.accept()     # Establish connection with client.
            print('Got connection from', addr)
            data = int(c.recv(1024))
            print(data)
            if(data ==1):
                GPIO.output(LED_PIN, GPIO.HIGH)
            else:
                GPIO.output(LED_PIN, GPIO.LOW)
    except KeyboardInterrupt:
        c.close()
        GPIO.output(LED_PIN, GPIO.LOW)
        GPIO.cleanup()


setupMain()
