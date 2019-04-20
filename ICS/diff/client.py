import socket
import random
ip = '127.0.0.1'
port = 12345

def main():


	print 'Client'
	s = socket.socket()
	s.connect((ip,port))
	p  = int(s.recv(64),2)
	print "P",p
	g  = int(s.recv(64),2)
	print "G",g
	A  = int(s.recv(64),2)
	#print "A:",A
	y = random.randrange(0,p)
	key  = (A**y)%p
	
	B = (g**y)%p
	s.send(bin(B)[2:].zfill(64))
	
	print "SK",key
	
	
	
	
	

if __name__ == '__main__':
	main()