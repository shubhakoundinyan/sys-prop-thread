#! /usr/bin/python
# encoding: utf-8

import re
import os
import sys
import platform
import psutil
import subprocess

def lin_process():

	process = psutil.Process(os.getpid())

	# Displays the physical memory usage of the system

	print "\n ########## PHYSICAL MEMORY USAGE ##########"
	print "\n Memory Currently Used: "+str(process.memory_full_info().rss)
	print "\n Percentage Memory Used: "+str(process.memory_percent())

	# Displays the system disk utlization. USED vs. AVAILABLE

	print "\n ########## DISK UTILIZATION for RESIDING FILE SYSTEM ##########"

	bash_command_u = "df -h|grep /dev/disk1|awk '{print $3}' "										# Change the hdd location here. So instead of /dev/sda1|awk - it should reflect your mount address
	
	print "\n Used Disk Space: "+str(subprocess.check_output(['bash', '-c', bash_command_u]))
	
	bash_command_a = "df -h|grep /dev/disk1|awk '{print $4}' "										# Change the hdd location here. So instead of /dev/sda1|awk - it should reflect your mount address
	
	print " Available Disk Space: "+str(subprocess.check_output(['bash', '-c', bash_command_a]))

	# Displays the virtual memory usage

	print " ########## VIRTUAL MEMORY USAGE ##########"

	print "\n Virtual Memory Used: "+str(psutil.virtual_memory().used)
	print "\n Virtual Memory Available: "+str(psutil.virtual_memory().available)

	print "\n ########## SWAP MEMORY USAGE ##########"	
	
	# Displays the swap memory usage

	print "\n Swap Memory Used: "+str(psutil.swap_memory().used)
	print "\n Swap Memory Available: "+str(psutil.swap_memory().free)
	
	'''
	# This chunk of code that is commented out checks for the CPU temperature.
	# It has a few pre-requisites that need to be in place before it can run successfully. 
	
	print "\n ########## CPU TEMPATURE CHECK ##########"
	print psutil.sensors_temperatures()
	if subprocess.check_output("sensors") ==1:
		print "No sensors found or available!"
	else:
	
		temperatures = {match[0]: float(match[1]) for match in re.findall("^(.*?)\:s+\+?(.*?)°C", sensors, re.MULTILINE)}
		disk = "/dev/sda"
		output = subprocess.check_output(["smartctl", "-A", disk])
      	temperatures[disk] = int(re.search("Temperature.*\s(\d+)\s*(?:\([\d\s]*\)|)$", output, re.MULTILINE).group(1))
		print "\nTemperature:"+str(temperatures[disk])
		print "\nSensors temperature:"+str(psutil.sensors_temperatures())
	'''

	sleep(10)

def main():

	# Operating system and platform validation

	if platform.system()=="Linux" or platform.system()=="Darwin":

		# Thread executes the number of times given in the argument list

		t1 = threading.Thread(target = lin_process,args = (5,))
		t1.start()
		t1.join()
	elif platform.system()=="Windows":
		win_process()

if __name__=="__main__":
	main()