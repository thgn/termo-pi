import time
from utils import insertLast,getTemp
import opciones as conf



insertLast('/home/pi/termostato/datos-hab1',getTemp(conf.rele1,conf.fTemp1))
