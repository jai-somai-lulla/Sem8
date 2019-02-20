import numpy as np
class FuzzySet:
	def __init__(self, iterable):
		self.f_set = iterable
		self.f_len = len(iterable)
				
	@staticmethod
	def __or__(a,b):
		#print a.f_set
		#print b.f_set
		c={}
		for k in a.f_set:
			c[k]=max(a.f_set[k],b.f_set[k])
		C = FuzzySet(c)	
		return C
		
	@staticmethod
	def __and__(a,b):
		#print a.f_set
		#print b.f_set
		c={}
		for k in a.f_set:
			c[k]=min(a.f_set[k],b.f_set[k])
		C = FuzzySet(c)	
		return C	
	
	@staticmethod
	def __not__(a):
		#print a.f_set
		#print b.f_set
		c={}
		for k in a.f_set:
			c[k]=(1-a.f_set[k])
		C = FuzzySet(c)	
		return C
		
	@staticmethod
	def max_min(a,b):
		
		for k1 in a.f_set:
		
					
	
	def show(self):
		print self.f_set			
				

def main():
	print 'Fuzzy Operations'
	a = FuzzySet({'x1': 0.5, 'x2': 0.7, 'x3': 0.0})
	
	b = FuzzySet({'x1': 0.8, 'x2': 0.2, 'x3': 1.0})
	print "\t--A--"
	a.show()
	print ''
	print "\t--B--"
	b.show()
	print '\n\n'
	
	print '----OR-----'
	c = FuzzySet.__or__(a,b)
	c.show()
	print '\n'

	print '----AND-----'
	c = FuzzySet.__and__(a,b)
	c.show()
	print '\n'
	
	print '----NOT A-----'
	c = FuzzySet.__not__(a)
	c.show()
	print '\n'
	
	print '-----A=>B------'
	c = FuzzySet.__or__(FuzzySet.__not__(a),b)
	c.show()	
	
	
if __name__ == "__main__":
	main()
