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
		
	def show(self):
		print self.f_set			
	
	@staticmethod
	def maxmin(x,y):
		print 'Max-Min'
		#z = []
		z = [[0 for i in range(x.shape[0])] for i in range(y.shape[1])] 
		row=0
		for x1 in x:
			#print 'X:'+str(x1)
			#row
			col=0
			for y1 in y.T:
				#print 'Y:'+str(y1)
				mix=[0,0,0]
				for i in range (x1.shape[0]):
					#print "Min"+str(x1[i])+","+str(y1[i])
					mix[i]=min(x1[i],y1[i])
				#print mix
				#print max(mix)
				
				z[row][col]=max(mix)
				#print 'ZZ::'
				#print z
				#print '--ZZ--'
				col+=1
			row+=1
		print z			
		
	@staticmethod
	def maxproduct(x,y):
		print 'Max-Product'
		#z = []
		z = [[0 for i in range(x.shape[0])] for i in range(y.shape[1])] 
		row=0
		for x1 in x:
			#print 'X:'+str(x1)
			#row
			col=0
			for y1 in y.T:
				#print 'Y:'+str(y1)
				mix=[0,0,0]
				for i in range (x1.shape[0]):
					#print "Min"+str(x1[i])+","+str(y1[i])
					mix[i]=(x1[i]*y1[i])
				#print mix
				#print max(mix)
				
				z[row][col]=max(mix)
				#print 'ZZ::'
				#print z
				#print '--ZZ--'
				col+=1
			row+=1
		print z			
			#print ''
			
	@staticmethod
	def cartProduct(a,b):
		print 'Cart Product'
		a.show()
		b.show()
		
		z = [[0 for i in range(len(a.f_set))] for i in range(len(b.f_set))] 
		
		row=0
		for k in a.f_set:
			#print a.f_set[k]
			col=0
			for j in b.f_set:
				#print b.f_set[j]
				z[row][col]=min(a.f_set[k],b.f_set[j])	
				col+=1
			row+=1
		print z	
		return z
		
						
				

def main():
	print 'Fuzzy Operations'
	a = FuzzySet({'x1': 0.5, 'x2': 0.7, 'x3': 0.0})
	
	b = FuzzySet({'x1': 0.8, 'x2': 0.2, 'x3': 1.0})
	
	
	r1 = np.array([[1, 0, 0.7], [0.3, 0.2, 0], [0, 0.5, 1]])
	r2 = np.array([[0.6, 0.6, 0], [0, 0.6, 0.1], [0, 0.1, 0]])	
	
	
	FuzzySet.cartProduct(a,b)
	return
	
	FuzzySet.maxmin(r1,r2)
	FuzzySet.maxproduct(r1,r2)
	return
	 
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
