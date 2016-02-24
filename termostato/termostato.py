import sys,os,time,math,ConfigParser,paramiko
from utils import *
import opciones as conf
from subprocess import call
##----------------------------------------------------------------------------------##

#Procedimiento para calcular la media ultimos 10 minutos
suma=0
line=""
if os.path.exists("./datos-hab1"):
	f = open('./datos-hab1', 'r+')
else:
	f = open('./datos-hab1', 'w+')

param = os.path.dirname(os.path.realpath(__file__)) + '/parametros.cfg'

Thab1=getOpciones(param,'temperaturas','hab1')
for line in f:
	suma=suma+int(line)

media=suma/10
f.close()


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(conf.rele1)

sftp = ssh.open_sftp()
estadoRele = sftp.open(conf.relayFile,'w')

if media < Thab1:
	estadoRele.write("1")
else:
	estadoRele.write("0")

estadoRele.close()
sftp.close()
ssh.close()
