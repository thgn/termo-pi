import time,os
from utils import insertLast,getTemp
import opciones as conf

path = os.path.dirname(os.path.realpath(__file__)) + '/datos-hab1'

insertLast(path,getTemp(conf.rele1,conf.fTemp1))
print (getTemp(conf.rele1,conf.fTemp1))	
	
