import socket
import random
IP,PORT = '127.0.0.1',12345
g=11
class Point:
	a=0.0
	b=7
	# y**2 = x**3 + a* x + b
	def __init__(self,x=float('inf'),y=float('inf')):
		self.x =x
		self.y =y
		
	@staticmethod	
	def makepoint(x):
		y = pow(x**3 + Point.a*(x) +Point.b,0.5)
		return Point(x,y)
		
	def copy(self):
		return Point(self.x,self.y)	
	
	def neg(self):
		return Point(self.x,-self.y)		
		
	def is_zero(self):
		if (self.x>10e10 and self.y>10e10):
			return True
		return False
	
	def sanity(self):
		if(self.is_zero()):
			return True
		return abs(self.y**2-self.x**3 - Point.a*(self.x) - Point.b)<0.1
	
	def equals(self,p):
		return self.x == p.x and self.y == p.y
	
	def show(self,p):
		print p,'(',self.x,',',self.y,')	',self.sanity()
	
	def add(self,q):
		if(self.is_zero()):
			return q.copy()
		elif(q.is_zero()):
			return self.copy()
		elif(self.equals(q)):
			s = 3*((self.x**2)+Point.a)/(2*self.y)	
		else :
			s =(self.y-q.y)/(self.x - q.x)
			
		x = s**2 +- self.x - q.x
		y = s*(self.x - x) - self.y			
		return Point(x,y)			

	def mult(self,n):
		p = self.copy()
		r = Point()
		i=1
		while(i<=n):
			if(i&n):
				r = r.add(p)
			p=p.add(p)
			i=i<<1
		return r
				

def main():
	print 'Ecc Server'
	s=socket.socket()
	s.bind((IP,PORT))
	s.listen(5)
	G = Point.makepoint(g)
	private = (random.randrange(1,100))
	public = G.mult(private)
	#c,addr = s.accept()
	G.show("G:")
	#c.send(struct.pack('!d', public.x))
	#c.send(struct.pack('!d', public.y))
	
	#CLient
	x = (random.randrange(1,100))
	clue = G.mult(x)
	mask = public.mult(x)
	data = Point.makepoint(69)
	cipher = data.add(mask)
	cipher.show("Cipher:")
	
	#Server
	amask = clue.mult(private)
	amask.show('Amask:')
	nmask = amask.neg()
	plain = cipher.add(nmask)
	plain.show("DEC Plain:")
	
	
	

	
	
					

if __name__ == '__main__':
	main()	
								