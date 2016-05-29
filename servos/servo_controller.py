#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import socket
import sys
from time import sleep

# setup servos
GPIO.setmode(GPIO.BOARD)

# head motor
motor_1a = -1
motor_1b = -1
motor_1e = -1

# arm motor
motor_2a = -1
motor_2b = -1
motor_2e = -1

# hip motor
motor_3a = -1
motor_3b = -1
motor_3e = -1

GPIO.setup(motor_1a, GPIO.OUT)
GPIO.setup(motor_1b, GPIO.OUT)
GPIO.setup(motor_1e, GPIO.OUT)

GPIO.setup(motor_2a, GPIO.OUT)
GPIO.setup(motor_2b, GPIO.OUT)
GPIO.setup(motor_2e, GPIO.OUT)

# setup socket connection to computer
host = '169.254.0.2'
port = 51717

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)

# create connection and spin motors depending on value
while True:
    (conn, address) = s.accept()

    try:
        while True:
            output = conn.recv(1024)
            command = str(output.strip())
            print command

      # move head
            if command == 'head':
                pass
            elif command == 'arm':
                pass
            elif command == 'hip':
                pass
            elif command == 'nocommand':
                pass
            else:
                conn.sendall(str(-1))
    finally:
        conn.close()
        GPIO.cleanup()

