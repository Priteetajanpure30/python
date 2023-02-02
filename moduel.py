import psutil
import platform 
from os import *;
form datetime import *;

def CPU_Info_OS():
	print("Marvellous Infosysten CPU Info OS");
	
	if platform.system() == 'Windows';
		return platform.processor();
	elif platform.system() == 'Darwin';
		cmmand = '/usr/sbin/sysctl -n machdep.cpu.brand_string'
		return popen(command).reaad().strip();
	elif 
