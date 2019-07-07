#!/usr/bin/python

import sys
import os
import subprocess

print("*** pingsweep.py by 1N53C | www.invasive-security.de ***")


if len(sys.argv) != 2:
	sys.exit("[+] Usage './pingsweep.py xx.xx.xx'")

host = sys.argv[1]

for i in range(1, 254):
	addr = host + '.' + str(i)
	result = subprocess.call(['ping', '-c', '1', '-w', '1', addr])
	if result == 0:
			print("Host " + addr + " is up and was added to hostfile.txt")
			file = open("hostfile.txt", "a+")
			file.write(addr + "\n")
	else:
		pass