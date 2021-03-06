import sys,os,time,math,ConfigParser,paramiko,logging
from utils import *
import opciones as conf
from subprocess import call

##----------------------------------------------------------------------------------##
#Procedimiento para calcular la media ultimos 10 minutos
suma=0
line=""
logging.basicConfig(filename='termostato.log',level=logging.INFO)

logging.info(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))

datos1 = os.path.dirname(os.path.realpath(__file__)) + '/datos-hab1'
if os.path.exists(datos1):
	f = open(datos1, 'r+')
else:
	f = open(datos1, 'w+')

param = os.path.dirname(os.path.realpath(__file__)) + '/parametros.cfg'

Thab1=getOpciones(param,'temperaturas','hab1')
for line in f:
	suma=suma+int(line)
f.close()
media=suma/10
logging.info(("Average: ",media))

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(conf.rele1)

sftp = ssh.open_sftp()
estadoRele = sftp.open(conf.relayFile,'w')

config = ConfigParser.RawConfigParser()
config.read(param)
intervalo1= [e.strip() for e in config.get('horarios','int1').split(',')]
intervalo2= [e.strip() for e in config.get('horarios','int2').split(',')]
logging.info(("Interval: ",intervalo1))
logging.info(("Interval: ",intervalo2))

a=int(time.strftime("%H", time.gmtime()))
c=int(time.strftime("%M", time.gmtime()))
b=int(((a+1)*60)+c)
logging.info(("Minutes: ",b))

#Check if enabled --> if average is ok --> if interval of operation is correct
if (getOpciones(param,'act','enable') == 1):
	if media < Thab1:
		if ((b>int(intervalo1[0])) and (b<int(intervalo1[1]))) or ((b>int(intervalo2[0])) and (b<int(intervalo2[1]))):
			estadoRele.write("1")
			logging.info("rele-activado")
		else:
                	estadoRele.write("0")
                	logging.info("rele-desactivado: FUERA-HORA")
	else:
		estadoRele.write("0")
		logging.info("rele-desactivado: MEDIA")
else:
	estadoRele.write("0")
	logging.info("rele-desactivado: DESACTIVADO")

estadoRele.close()
sftp.close()
ssh.close()
