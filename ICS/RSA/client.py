import socket
import random
IP='127.0.0.1'
PORT=12345

def encrypt(N,e,pt):
	return (pt**e)%N

def main():
	print '--Client--'
	s = socket.socket()
	s.connect((IP,PORT))
	N=int(s.recv(64),2)
	e=int(s.recv(64),2)
	print "E,N",e,N
	data = random.randrange(0,N)
	cipher = encrypt(N,e,data)

	s.send(bin(cipher)[2:].zfill(64))
	print data,"Sent"
	#print "Cipher",cipher

if __name__ == '__main__':
	main() 