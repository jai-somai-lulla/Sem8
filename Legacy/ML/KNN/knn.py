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
	k = 3
	data = [(2,3,'a'),(2,1,'a'),(1,3,'a'),(-2,-3,'b'),(-1,-3,'b'),(-2,-1,'b')]
	df=pd.DataFrame(data)
	test =[(4,4,'a'),(-4,-4,'b')]
	#test=pd.DataFrame(test)
	#print df
	#print test
	correct=0
	for t in test:
		distances=[]
		votes={}
		print "Test point :"+str(t[0:2])
		for x in data :
			dx=distance(t[0:2],x[0:2])
			pair=[dx,x[2]]
			votes[x[2]]=0
			distances.append(pair)
		
		distances.sort()
		
		for index in range(k):
			votes[distances[index][1]]+=1
			
		#print votes
		predicted=max(votes,key=votes.get)
		if predicted==t[2]:
			correct+=1
	print (correct/float(len(test))) * 100.0
		
if __name__=='__main__':
	main()	
