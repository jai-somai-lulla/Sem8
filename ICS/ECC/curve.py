
#y**2  =  X**3 + B 
class Point:
	b=7
	def __init__(self,x=float('inf'),y=float('inf')):
		self.x = x
		self.y = y
	@staticmethod 
	def make(x):
		y = pow(x**3  + Point.b,0.5)
		return Point(x,y)
	def copy(self):
		return Point(self.x,self.y)
	def neg(self):
		return Point(self.x,-self.y)
	def sanity(self):
		if(self.isinf()): return True
		return abs((self.y**2)-(self.x**3+Point.b))<0.1		
	def show(self):
		print "(",self.x,",",self.y,")"	
	def equals(self,q):
		return self.x == q.x and self.y == q.y
	def isinf(self):
		return 	self.x > 10e10 and self.y > 10e10	
	def add(self,q):
		if(self.isinf()):
			return q.copy()
		elif(q.isinf()):
			return self.copy()
		elif(self.equals(q)):
			try:
				s = 3*(self.x**2)/(2*self.y)
			except:
				return Point()
		else:
			s = (q.y-self.y)/(q.x-self.x)
			print s
		
		x = (s**2) - self.x - q.x
		y = s*(self.x-x) - (self.y)
		return Point(x,y)
	def mult(self,scalar):
		i=1
		p = self.copy()
		r = Point()
		while i<=scalar:
			if(i&scalar):
				r=r.add(p)
			p=p.add(p)
			i<<=1
		return r		
								
def main():
	print '--ecc--'
	p=Point.make(5)
	p.show()
	q=Point.make(2)
	q.show()
	r=q.mult(51)
	r.show()
	print r.sanity()
if __name__ == '__main__':
	main()		