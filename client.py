#!/usr/bin/python

import  socket 
#            type of ip v4 ,      type of protocol UDP  
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


for i in range(10000): 
	msg=raw_input("Enter command")
	s.sendto(msg,("192.168.10.182",8000))




