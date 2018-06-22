#!usr/bin/python


import socket


# type of ip , type of protocol
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


#bind current ip and port


s.bind(("192.168.102.128",8000))

#buffer size to recieve

#print s.recvfrom(10)

for i in range(10000):   			#to get from all clients
	data=s.recvfrom(100)
	print commands.getout(data[0])

#upto here was server side
'''
for i in range(10000):   			#to get from all clients
	data=s.recvfrom(100)
	if 'date' in data[0]:
		print commands.getoutput('date')
	elif 'cal' in data[0]
		print commands.getoutput('cal')
'''
