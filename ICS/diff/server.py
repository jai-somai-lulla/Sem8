import socket
import random
ip = '127.0.0.1'
port = 12345
p = 23
g = 7



def main():
	print 'Server'
	x = random.randrange(0,23)
	A = (g**x)%p
	soc = socket.socket()
	soc.bind((ip,port))
	soc.listen(5)
	
	while True:
		c,addr = soc.accept()
		print "Client",addr
	
		c.send(bin(p)[2:].zfill(64))
		c.send(bin(g)[2:].zfill(64))
		c.send(bin(A)[2:].zfill(64))
		B = int(c.recv(64),2)
		key = (B**x)%p
		print "SK:",key	
	
	soc.close()


if __name__ == '__main__':
	main()