import numpy as np


class Point:
	b=7
	a=0.0
	def __init__(self, x=float('inf'), y=float('inf')):
		self.x = x
		self.y = y
	
	def show(self,s=""):
		print s,"\t X:",self.x,"Y:",self.y
	
	def is_zero(self):
		return self.x > 1e20 or self.x < -1e20
	
	def neg(self):
		return Point(self.x,-self.y)	#mod q	
	
	def copy(self):
		return Point(self.x,self.y)	#mod q	
   
	def dbl(self):
		if self.is_zero():
			return self.copy()
		try:
			L = (3 * self.x * self.x) / (2 * self.y)
		except ZeroDivisionError:
			return Point()
		x = L * L - 2 * self.x
		return Point(x, L * (self.x - x) - self.y)	
	
	def add(self,q):
		l=0
		if(self.is_zero()):
			return q
		
		elif(q.is_zero()):
			return self
		
		elif(self.x==q.x and self.y==q.y):	
			#return self.dbl()	
			try:
				l=((3*(self.x*self.x)+Point.a)/(2*self.y))#mod q
			except ZeroDivisionError:
				return Point()				
		else:
			try:
				l=(q.y-self.y)/(q.x-self.x)	#mod q
			except ZeroDivisionError:
				return Point()				
		
		x=((l**2)-self.x-q.x) #mod q
		y=(l*(self.x-x)-self.y)	#mod q
		return Point(x,y)
	
	def mult(self, n):
		p = self.copy()
		r = Point()
		i = 1
		while i <= n:
			if i&n:
				#r.show("R"+str(i))
				#p.show("P"+str(i))	
				r = r.add(p)
			p = p.add(p)
			i <<= 1
		return r

	#Check fxn not performing correctly for >10000 due to lack of precision
	def smult(self, n):
		p = self.copy()
		r = Point()
		for i in range(n):
			#r.show("R"+str(i))
			r = r.add(p)
		return r 	
	def sanity(self):
		return abs(self.y**2 - self.x**3 - Point.a*self.x - Point.b)<0.1
		
	@staticmethod
	def make_point(y):
	#y^2 = x^3 + ax + b 
	#a=0 b=7
		temp=(y*y)-Point.b
		if temp>0:
			x=pow(temp,1.0/3.0)
		else: 
			x=-(pow(-temp,1.0/3.0))	
		return Point(x,y)
		
		
				
		
def main():
	print "ECC"
	'''p=Point.make_point(1)
	p.show("P:")
	q=Point.make_point(2)
	q.show("Q:")
	print p.sanity()
	#print p.is_zero()
	#r=p.scalarMult(4)
	r=p.add(q)
	r.show("P+Q")
	print r.sanity()
	#s=r.neg()
	#s.show()

	#t=s.add(r)
	#t.show()
	
	a=p.mult(1234)
	a.show("FMul:")
	print a.sanity()
	
	sa=p.smult(1234)
	sa.show("Slow MULT:")
	print sa.sanity()'''
	
	G = Point.make_point(9) #Public Gen-Point
	G.show("Gen-Point")
	print '\n'
	#a,b of curve is public y^2 = x^3 + ax + b
	 
	#A Generating Private and Distributing Public key
	da = 7 #Private
	print 'Private Key:',da
	qa = G.mult(da) #Public Key
	qa.show("Public Key")
	print '\n'
	#B has info about (Gen-Point(G),Curve(a,b),publickey(qa))
	x = 5 #secret Random Number
	print 'Secret Random Number:',x
	clue = G.mult(x)
	clue.show("Clue (x.G)")
	print '\n'
	
	data = Point.make_point(69)# data converted to point (x,69)
	data.show("Data to Send pt(69)")
	mask = qa.mult(x) #public key reflected x(secret) times
	mask.show("Mask (x.Qa)")
	cipher = data.add(mask)
	cipher.show("Cipher Text (Mask+data)")
	print '\n'
	#B sends (clue,cipher to A)
	
	#A Decryption
	#Availabe info Curve,da(private Key),clue,cipher
	
	Amask = clue.mult(da)#making the mask using clue and da(private Key)
	mask.show("AMask (da.CLUE)")
	antiMask = Amask.neg()	#making the antimask
	antiMask.show("AntiMask")
	plain = cipher.add(antiMask)
	plain.show("Plain text:")
	print '\n'
	 
	
	
	
	

if __name__=="__main__":
	main()	