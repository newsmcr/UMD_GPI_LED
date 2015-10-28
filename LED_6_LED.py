import socket
import time
import RPi.GPIO as GPIO
import videohubtools_config
from videohubtools_config import *


#establish GPIOS
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(XLR_LAMP1, GPIO.OUT)#XLR_LAMP1
GPIO.setup(XLR_LAMP2, GPIO.OUT)#XLR_LAMP2
GPIO.setup(XLR_LAMP3, GPIO.OUT)#XLR_LAMP3
GPIO.setup(XLR_LAMP4, GPIO.OUT)#XLR_LAMP4
GPIO.setup(XLR_LAMP5, GPIO.OUT)#XLR_LAMP5
GPIO.setup(XLR_LAMP6, GPIO.OUT)#XLR_LAMP6
# Establish TCP/IP sockets
def ALL_OFF():
    GPIO.output(XLR_LAMP1,False)
    GPIO.output(XLR_LAMP2,False)
    GPIO.output(XLR_LAMP3,False)
    GPIO.output(XLR_LAMP4,False)
    GPIO.output(XLR_LAMP5,False)
    GPIO.output(XLR_LAMP6,False)

ALL_OFF()


sockBMD_Videohub = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect sockets with devices
server_address = (BMD_Videohub, 9990) 
sockBMD_Videohub.connect(server_address)
time.sleep(0.4)
data = sockBMD_Videohub.recv(8888)

#parse outputrouting
sockBMD_Videohub.send("video output routing:\n\n")
time.sleep(0.1)
outrouting = sockBMD_Videohub.recv(4096)
outrouting = outrouting.split('\n')
i = 0
while i <> 3:
    a = outrouting.pop(0)
    i += 1

#print (outrouting)#routing komplett

i = 0

while i <= BMD_VideohubOutput:
    ausgabe = outrouting[i].split(' ')
    i += 1
    inputinteger = int(ausgabe[0])
    if inputinteger == BMD_VideohubOutput:
        #print(ausgabe[1])
        outputinteger = int(ausgabe[1])

if outputinteger == IN1:
    #print ("in1")
    GPIO.output(XLR_LAMP1,True)
if outputinteger == IN2:
    #print ("in2")
    GPIO.output(XLR_LAMP2,True)
if outputinteger == IN3:
    #print ("in3")
    GPIO.output(XLR_LAMP3,True)
if outputinteger == IN4:
    #print ("in4")
    GPIO.output(XLR_LAMP4,True)
if outputinteger == IN5:
    #print ("in5")
    GPIO.output(XLR_LAMP5,True)
if outputinteger == IN6:
    #print ("in6")
    GPIO.output(XLR_LAMP6,True)


#delete first rows


#wait for changings in Output routing
#WARTEN()
i = 0
while i <> 3:
    a = outrouting.pop(0)
    i += 1

O = BMD_VideohubOutput
while O <> BMD_VideohubOutput:
    ausgabe = outrouting[O].split(' ')
    outputinteger = int(ausgabe[1])
    O += 1

while 1:
    switch = sockBMD_Videohub.recv(4096)
    switch = switch.split("\n")
    time.sleep(0.1)
    ALL_OFF()
    if switch[0] == "VIDEO OUTPUT ROUTING:":
        ausgabe = switch[1].split(' ')
        outputinteger = int(ausgabe[1])
        if outputinteger == IN1:
            #print ("in1")
            GPIO.output(XLR_LAMP1,True)
        if outputinteger == IN2:
            #print ("in2")
            GPIO.output(XLR_LAMP2,True)
        if outputinteger == IN3:
            #print ("in3")
            GPIO.output(XLR_LAMP3,True)
        if outputinteger == IN4:
            #print ("in4")
            GPIO.output(XLR_LAMP4,True)
        if outputinteger == IN5:
            #print ("in5")
            GPIO.output(XLR_LAMP5,True)
        if outputinteger == IN6:
            #print ("in6")
            GPIO.output(XLR_LAMP6,True)
time.sleep(0.1)

print 'Programm beendet.'
sockBMD_Videohub.close()