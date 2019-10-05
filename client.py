#!/usr/bin/python

import  socket #importing socket module for connection
#            type of ip v4 ,      type of protocol UDP 

# creaing the socket object
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


for i in range(10000): 
	msg=raw_input("Enter command")
	print("message you are sending", msg)
	s.sendto(msg,("192.168.10.182",8000))




