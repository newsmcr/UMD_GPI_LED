#!/usr/bin/env python
import socket
import sys
import time
from videohubtools_config import *
#UMD
import max7219.led as led
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT

#############################################################################
# 																			#
#  Displays Source Name for switched Output x (absolut value) in lenght L	#
#																			#
#############################################################################

device = led.matrix(cascaded=8)
device.orientation(90)
device.orientation(90)

#Values
#BMD_Videohub = '192.168.1.60'
time.sleep(6)
#Anzeigare Zeichen
L = 8
#define Display Output Absolut!!
#BMD_VideohubOutput = 16

# Establish TCP/IP sockets
#BMD_Videohub --> Switcher

sockBMD_Videohub = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect sockets with devices
server_address = (BMD_Videohub, 9990) 
sockBMD_Videohub.connect(server_address)
time.sleep(0.4)
data = sockBMD_Videohub.recv(8888)

#receive labels
sockBMD_Videohub.send("input labels:\n\n")
time.sleep(0.1)
ilabels = sockBMD_Videohub.recv(4096)
ilabels = ilabels.split('\n')

#parse outputrouting
sockBMD_Videohub.send("video output routing:\n\n")
time.sleep(0.1)
outrouting = sockBMD_Videohub.recv(4096)
outrouting = outrouting.split('\n')

#delete first rows
i = 0
while i <> 3:
	a = outrouting.pop(0)
	i += 1

O = BMD_VideohubOutput-1

while O <> BMD_VideohubOutput+1:
	ausgabe = outrouting[O].split(' ')
	outputinteger = int(ausgabe[0])
	input = ilabels[int(ausgabe[1])+3][2:]
	O += 1

	name = input.lstrip(' ')

device.brightness(0)
device.show_message(name, font=proportional(CP437_FONT), delay=0.015)
laenge = len(name[:8])
i=0
while i < laenge:
		device.letter(i, ord(str(str(name)[i])))
		i += 1

#wait for changings in Output routing
while 1:
	switch = sockBMD_Videohub.recv(4096)
	switch = switch.split("\n")
	time.sleep(0.1)
	if switch[0] == "VIDEO OUTPUT ROUTING:":
		ausgabe = switch[1].split(' ')
		outputinteger = int(ausgabe[0])
		if(outputinteger) == BMD_VideohubOutput:
			input = ilabels[int(ausgabe[1])+3][2:]
			name = input.lstrip(' ')
			device.brightness(0)
			z=1
			while z < 9:
				device.scroll_down()
				time.sleep(0.03)
				z += 1
				time.sleep(0.1)
			device.show_message(name, font=proportional(CP437_FONT), delay=0.015)
			laenge = len(name[:8])
			i=0
			while i < laenge:
				device.letter(i, ord(str(str(name)[i])))
				i += 1
	time.sleep(0.1)

print 'Programm beendet.'
sockBMD_Videohub.close()
