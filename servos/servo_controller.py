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
            if command == 'arm_up':
                conn.sendall('arm up received')
                print 'arm up received'
            elif command == 'arm_down':
                conn.sendall('arm down received')
                print 'arm down received'
            elif command == 'bow':
                conn.sendall('bow received')
                print 'bow received'
            elif command == 'nocommand':
                conn.sendall('no command received')
                print 'no command received'
            else:
                conn.sendall('no movement received')
    finally:
        conn.close()
        GPIO.cleanup()

