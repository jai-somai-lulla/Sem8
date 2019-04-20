
class Point:
	b=7
	a=0.0
	def __init__(self,x=float('inf'),y=float('inf')):
		self.x=x
		self.y=y
	def show(self):
		print '(',self.x,',',self.y,')'
	
	
	@staticmethod
	def make_point(x):
		y = pow(x**3 + Point.a*(x) + Point.b,0.5)
		return Point(x,y)


	def sanity(self):
		if (not self.is_zero()):
			s= self.y**2 - self.x**3 - Point.a*(self.x) - Point.b
			print "San:",s
			return abs(s)<0.1 
		else:
			return True	
	def neg(self):
		return Point(self.x,-self.y)
		
	def copy(self):
		return Point(self.x,self.y)
		
	def is_zero(self):
		if(self.x>10e10 and self.y>10e10):
			return True			
		return False	
	def equals(self,p):
		return self.x==p.x and self.y==p.y
			
	def add(self,q):
		if(self.is_zero()):
			return q.copy()
		elif(q.is_zero()):
			return self.copy()
		elif(self.equals(q)):
			#try:
			#print 'ger'
				s = float(3*(self.x**2)+Point.a)/(2*self.y)
				#  s = float(3*(self.x**2)+Point.a)/2*self.y
			#except:
			#	return Point()	
		else:
			#try:
				s = float(self.y-q.y)/(self.x-q.x)
			#	print 'ne'
			#except:
			#	return Point()
				
				
		x = s**2 - self.x - q.x
		y = s*(self.x - x) - self.y	
		return Point(x,y)		
				
	def mult(self,scalar):
		i=1
		p = self.copy()
		r = Point()
		while i<=scalar:
			if(i&scalar):
				#r.show()	
				#print i
				r = r.add(p)
			p=p.add(p)
			i<<=1
		#print 'mult'

		return r		
						

def main():
	print 'ECC'
	p = Point.make_point(5)
	print "P"
	p.show()
	
	q = Point.make_point(5)
	print "q"
	q.show()
	p.add(q).show()
	print p.add(q).sanity()
	return
	
#	q = p.neg()
#	q.show()
	
	print "\n\n"
	r = p.mult(2)
	r.show()
	print r.sanity()
	
if __name__ == '__main__':
	main()	