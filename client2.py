#!/usr/bin/python

import  socket 
#            type of ip v4 ,      type of protocol UDP  
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
u=raw_input("enter username")
p=raw_input("enter password")


s.sendto(u,("192.168.10.144",9999))
s.sendto(p,("192.168.10.144",9999))

#checking response from server
response=s.recvfrom(20)

if response[0] == 'allow':
	while 4>2 :   #can also be used
		msg=raw_input("Enter command: ")
	
		s.sendto(msg,("192.168.10.144",9999))

		#recive output data

		print s.recvfrom(10000)

else :
	print response[0]

s.close()
