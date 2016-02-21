import RPi.GPIO as GPIO
import time
import math


f = open('/home/pi/temperatura/estado_rele','r')

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) ## GPIO 17 como salida

line = f.read()
if int(line) == 1:
	GPIO.output(17, True)
else:
	GPIO.output(17, False)
