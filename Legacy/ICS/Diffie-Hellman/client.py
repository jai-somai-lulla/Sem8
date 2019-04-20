# Import socket module 
import socket                
import random 
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 1234                
  
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 
  
# receive data from the server 
p =  int(s.recv(2).decode())
print "Agreed Mod:",p 
g =  int(s.recv(1).decode())
print "Agreed Base:",g
# close the connection 
pub_recv = int(s.recv(8).decode()) 
print "Public Key A(recv)",pub_recv


x = random.randrange(0,p)
print "Private keyB(Client)",x
public = (g**x)%p
print "Public key B(sent):",public
s.send(str(public).encode())

key = (pub_recv**x)%p
print "Key Gen :",key

s.close()        
