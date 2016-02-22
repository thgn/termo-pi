#Temperaturas de las habitaciones
Thab1 = 18
Thab2 = 20
Thab3 = 20

#IP raspberries
rele1="192.168.17.176"
rele2=""
rele3=""

#Temperature file
fTemp1 = "/sys/bus/w1/devices/28-000007097ac7/w1_slave" 
fTemp2 = ""
fTemp3 = ""

#Rele file
relayFile = "/home/pi/temperatura/estado_rele"

#Temperaturas de cada termostato
LastTs = [0,0,0,0,0,25,0,0,4,40]
Last1Ts = []


#Valor de bloqueo del rele - TODO

#enable programador
activado = 1

#Tiempo de parada de emergencia
EmPar=5
