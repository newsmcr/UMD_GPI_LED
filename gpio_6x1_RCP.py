#!/usr/bin/python
import RPi.GPIO as GPIO
import socket
import sys
import time
from videohubtools_config import *

#Define switcher Output
#output = 15

#Define inputs Numbers start from 0
#IN1 = 42
#IN2 = 43
#IN3 = 44
#IN4 = 45
#IN5 = 46
#IN6 = 47
#establish GPIOS
GPIO.setmode(GPIO.BCM)
GPIO.setup(XLR_BUTTON1, GPIO.IN, pull_up_down = GPIO.PUD_UP)#XLR_BUTTON1
GPIO.setup(XLR_BUTTON2, GPIO.IN, pull_up_down = GPIO.PUD_UP)#XLR_BUTTON2
GPIO.setup(XLR_BUTTON3, GPIO.IN, pull_up_down = GPIO.PUD_UP)#XLR_BUTTON3
GPIO.setup(XLR_BUTTON4, GPIO.IN, pull_up_down = GPIO.PUD_UP)#XLR_BUTTON4
GPIO.setup(XLR_BUTTON5, GPIO.IN, pull_up_down = GPIO.PUD_UP)#XLR_BUTTON5
GPIO.setup(XLR_BUTTON6, GPIO.IN, pull_up_down = GPIO.PUD_UP)#XLR_BUTTON6
time.sleep(3)
# Establish TCP/IP sockets
#BMD_Videohub --> Switcher
sockBMD_Videohub = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (BMD_Videohub, 9990)
sockBMD_Videohub.connect(server_address)
time.sleep(0.4)
data = sockBMD_Videohub.recv(8888)


while True:
	#Button01
	if(GPIO.input(XLR_BUTTON1) == 0):
		#print('Button 1 pressed')
		sockBMD_Videohub.send("VIDEO OUTPUT ROUTING:\n" + str(BMD_VideohubOutput) + " " + str(IN1) + "\n\n")
		time.sleep(0.1)
	#Button02
	if(GPIO.input(XLR_BUTTON2) == 0):
		#print('Button 2 pressed')
		sockBMD_Videohub.send("VIDEO Output ROUTING:\n" + str(BMD_VideohubOutput) + " " + str(IN2) + "\n\n")
		time.sleep(0.1)
	#Button03
	if(GPIO.input(XLR_BUTTON3) == 0):
		#print('Button 3 pressed')
		sockBMD_Videohub.send("VIDEO OUTPUT ROUTING:\n" + str(BMD_VideohubOutput) + " " + str(IN3) +  "\n\n")
		time.sleep(0.1)
	#Button04
	if(GPIO.input(XLR_BUTTON4) == 0):
		#print('Button 4 pressed')
		sockBMD_Videohub.send("VIDEO OUTPUT ROUTING:\n" + str(BMD_VideohubOutput) + " " + str(IN4) +  "\n\n")
		time.sleep(0.1)
	#Button05
	if(GPIO.input(XLR_BUTTON5) == 0):
		#print('Button 5 pressed')
		sockBMD_Videohub.send("VIDEO OUTPUT ROUTING:\n" + str(BMD_VideohubOutput) + " " + str(IN5) +  "\n\n")
		time.sleep(0.1)		
	#Button06
	if(GPIO.input(XLR_BUTTON6) == 0):
		#print('Button 6 pressed')
		sockBMD_Videohub.send("VIDEO OUTPUT ROUTING:\n" + str(BMD_VideohubOutput) + " " + str(IN6) +  "\n\n")
		time.sleep(0.1)		


		
GPIO.cleanup()
