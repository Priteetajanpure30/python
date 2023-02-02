import psutil;
import platform;
import os;
from datetime import datetime;

def CPU_Info_OS():
	print("------Prachi CPU Info OS------");
	
	if platform.system() == 'Windows':
		return platform.processor();
	elif platform.system() == 'Darwin':
		command = '/usr/sbin/sysctl -n machdep.cpu.brand_string';
		return popen(command).read().strip();
	elif platform.system == 'Linux':
		command = 'cat/proc/cpuinfo';
		return popen(command).read().strip();
	return 'platform not identified';


def get_size(bytes,suffix = "B"):
	factor = 1024
	for unit in [" ","K","M","G","T","P"]:
		if bytes < factor:
			return(f"{bytes:.2f}{unit}{suffix}");
		bytes/=factor;

def Platform_Info():
	print("---------------Marvellous Infosystem----------------");
	uname = platform.uname();
	print(f"System:{uname.system}");
	print(f"Node Name:{uname.node}");
	print(f"Release:{uname.version}");
	print(f"Version:{uname.machine}");
	print(f"Machine:{uname.machine}");
	print(f"Processor:{uname.processor}");

def Boot_Info():
	print("----------Marvellous Inforsystem-----------");
	boot_time_timestamp = psutil.boot_time();
	bt = datetime.fromtimestamp(boot_time_timestamp);
	print(f"Boot Time : {bt.year}/{bt.month}/{bt.day}{bt.hour}:{nbt.minute}:{bt.second}");

def CPU_Info():
	print("--------------Marvellous Infoosystem--------------");
	print("Physical cores:",psutil.cpu_count(logical = False));
	print("Total cores:",psutil.cpu_count(logical=True));

	cpufreq = psutil.cpu_freq()
	print(f"Max Frequency: {cpufreq.max:.2f}Mhz");
	print(f"Min Frequency: {cpufreq.min:.2f}Mhz");
	print(f"Current Frequency: {cpufreq.current:.2f}Mhz");

	print("CPU Usage Per Core : ");
	for i,percentage in enumerate(psutil.cpu_percent(percpu=True)):
		print(f"Core {i} : {percentage}%);
	print(f"Total CPU Usage : {psutil.cpu_percent()}%");


def RAM_Usage():
	print("-----------Prachi Lappis RAM---------------");
	
	svmem = psutil.virtual_memory();
	print(f"Total:{get_size(svmem.total)}");
	print(f"Available:{get_size(svmem.available)}");
	print(f"Used:{get_size(svm.used)}");
	print(f"Percentage:{svmem.percent}%");
	print("---------SWAP-------");
	swap = psutil.swap_memory();
	print(f"Total : {get_size(swap.total)}");
	print(f"Free : {get_size(swap.free)}");
	print(f"USed : {get_size(swap.used)}");
	print(f"Percentage : {swap.prcent}%");

def Disk_Info():
	print("----------Prachi pc------------");
	print("Partitions and usages : ");

	partitions = psutil.disk_partitions();
	for partition in partitions:
		print(f"=== Device : {Partition.device}===");
		print(f"  Mountpoint: {partition.mountpoint}");
		print(f"  File system type : {partition.fstype}");

		try:
			partitio_usage = psutil.disk_usage(partition.mountpoint);
		except PermissionError:
			continue;

	print(f" Total Size : {get_size(partition_usage.total)}");
	print(f" used : {get_size(partition_usage.used)}");	
	print(f" Free : {get_size(partition_usage.free)}");
	print(f" Percentage : {get_size(partition_usage.percent)}%");
	disk_io = psutil.disk_io_counters();
	print(f" Total read : {get_size(disk_io.read_bytes)}");
	print(f" Total write : {get_size(disk_io.write_bytes)}");

def main():
	CPU_Info_OS();
	#get_size();
	Platform_Info();
	Boot_Info();
	CPU_Info();
	RAM_Usage();
	Disk_Info();


if __name__ == "__main__":
	main();
