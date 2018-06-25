#!usr/bin/python


import socket


# type of ip , type of protocol
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


#bind current ip and port


s.bind(("192.168.102.128",8000))

#buffer size to recieve

user=s.recvfrom(10)
password=s.recvfrom(10)


if user[0] == 'root' and password =='123' :
	s.sendto("allow",password[1])			#ip of client
#print s.recvfrom(10)

	for i in range(10000):   			#to get from all clients
		data=s.recvfrom(100)
		#showing client ip and port	
		print commands.getout(data[0])


		#return something to client
		s.sendto(output,data[1])

else :
	print "bad username and password"
	s.sendto("login failed",password[1])
	
'''
for i in range(10000):   			#to get from all clients
	data=s.recvfrom(100)
	if 'date' in data[0]:
		print commands.getoutput('date')
	elif 'cal' in data[0]
		print commands.getoutput('cal')
'''
