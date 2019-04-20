import socket   
import random             
s = socket.socket()          
print "Socket successfully created"
port = 1234       
s.bind(('127.0.0.1', port))         
print "socket binded to %s" %(port)
s.listen(5)      
print "socket is listening"
p=23
g=5

while True: 
   # Establish connection with client. 
	c, addr = s.accept()      
	print 'Got connection from',addr 
   # send a thank you message to the client.  
	print c.send(str(p).encode())
	print c.send(str(g).encode()) 
	print "Agreed Mod:",p
	print "Agreed Base:",g
	x=random.randrange(0,p)
	print "Private key A",x
	public = (g**x)%p
	print "Public key A(sent):",public
	c.send(str(public).encode())
	
	
	pub_recv = int(c.recv(1024).decode())
	print "Public key B(recv):",pub_recv
	 
	key = (pub_recv**x)%p
	print "Key Gen :",key
	print '\n\n\n\n'
	
	
	# Close the connection with the client 
	c.close() 