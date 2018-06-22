#!usr/bin/python


import socket


# type of ip , type of protocol
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


#bind current ip and port

s.sendto("hello there",("192.168.102.182",8000))
