import time,math,ConfigParser
from utils import *
import opciones as conf
from subprocess import call
##----------------------------------------------------------------------------------##
archivo= "'parametros.cfg'"

#Procedimiento para calcular la media ultimos 10 minutos
suma=0
f = open('/home/pi/termostato/datos-hab1', 'r')
line=""
#Linea de prueba, se puede borrar - setOpciones('parametros.py','temperaturas','hab1',13)

Thab1=getOpciones('/home/pi/termostato/parametros.cfg','temperaturas','hab1')


for line in f:
	suma=suma+int(line)

media=suma/10
print Thab1

if media < Thab1:
	call(["ssh", "pi@192.168.17.176", "echo", "1", ">", "/home/pi/temperatura/estado_rele"])
	print "activado"
else:
	call(["ssh", "pi@192.168.17.176", "echo", "0", ">", "/home/pi/temperatura/estado_rele"])
	print "desactivado"
f.close()
