import numpy as np
import pandas as pd

def distance(a,b):
	e=0
	for e1,e2 in zip(a,b):
		#print str(e1)+" "+str(e2)
		e+=(e1-e2)*(e1-e2)
	return e


def main():
	print ('K Nearest')
	data = [(2,3,'a'),(2,1,'a'),(1,3,'a'),(-2,-3,'b'),(-1,-3,'b'),(-2,-1,'b')]
	df=pd.DataFrame(data)
	test =[(4,4,'a'),(-4,-4,'b')]
	test=pd.DataFrame(test)
	#print df
	distances=[]
	for t in test:
		print t['0','1']
		
	#print distance([2,3],[2,1])
	
	
		
if __name__=='__main__':
	main()	
