import socket
import random
IP = '127.0.0.1'
PORT = 12345
p = 17
q = 11


def gcd(p,q):
	g=0
	for i in range(1,min(p,q)):
		if(p%i==0 and q%i==0):
			g=i
	return g		
def genKey():
	N = p*q
	dn = (p-1)*(q-1)
	e=0
	d=0
	
	while((e*d)%dn != 1):
		while True:
			e = random.randrange(2,dn)
			#print e
			if(gcd(e,dn)==1):
				break
	
		d=-1
		for i in range(100):
			if((float(dn*i+1)/e)%1==0):
				d=int((dn*i)+1)/e
				break
	
		#print d
	print "Sanity ",(e*d)%dn
	
	return N,e,d		
	
	#e = randrange(0,dn)
	
def decrypt(N,d,ct):
	return (ct**d)%N	

def main ():
	print '--Server--'
	s = socket.socket()
	s.bind((IP,PORT))
	s.listen(5)
	
	while True:

		c, addr = s.accept()
		N,e,d = genKey()
		print "N:",N
		print "E:",e
		print "D:",d
		c.send(bin(N)[2:].zfill(64))
		c.send(bin(e)[2:].zfill(64))
		cipherText = int(c.recv(64),2)
		#print "Cipher",cipherText
		plain=decrypt(N,d,cipherText)
		print plain,"recieved"
		print ''
	

if __name__ == '__main__':
	main()