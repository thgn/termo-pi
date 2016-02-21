import ConfigParser,paramiko
#import opciones as conf

#Author JV
#Given a file to write options, a section, an option to modify and his value 
#opens the file and writes the value
#example: setOpciones('parametros.cfg','temperaturas','hab1',13)

def setOpciones(file, section, option, value):
	configNew = ConfigParser.RawConfigParser()
	configNew.read(file)
	configNew.set(section,option,value)
	with open(file, 'wb') as configfile:
        	configNew.write(configfile)
	return;

#--------------------------------------------------------------------------#
#Author JV
#Given a file to read options, a section and an option 
#opens the file and returns the value
#example: print getOpciones('parametros.cfg','temperaturas','hab1')

def getOpciones(archivo,section,option):
	config = ConfigParser.RawConfigParser()
	config.read(archivo)
	hab1=config.getint(section,option)
	return hab1;

#--------------------------------------------------------------------------#
#Author JV
#Given a 10 lines file to read inserts an int at the bottom of the file
#
#example: insertLast('file', 15) 
 
def insertLast(file, value):
	with open(file,'r') as fIn:
		data = fIn.read().splitlines(True)
	fIn.close()
	with open(file,'w') as fOut:
		fOut.writelines(data[1:])
		fOut.writelines(str(value)+"\n")
	fOut.close()
	return;

#--------------------------------------------------------------------------#
#Author JV
#Given the rele IP and the temperature file returns an integer with the remote temperature
#
#example: getTemp('192.168.X.X','file')

def getTemp(ip,file):
	#Opening SSH connection
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(ip)

	sftp = ssh.open_sftp()
	thermoFile = sftp.open(file,'r')
	temp = thermoFile.read()
	thermoFile.close()

	#converting to int format
	temp = temp.split("\n")[1].split(" ")[9]
	temp = int(temp[2:]) / 1000

	sftp.close()
	ssh.close()

	return temp;



