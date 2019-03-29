import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import math


def l2(p1,p2):
	#print 'c :',str(p1) ,' p:',str(p2), 'D:',math.sqrt(math.pow(p1[0]-p2[0],2)+math.pow(p1[1]-p2[1],2))

	return math.sqrt(math.pow(p1[0]-p2[0],2)+math.pow(p1[1]-p2[1],2))

def makeplot(centers,data):
	plt.scatter(centers[0,0],centers[0,1],marker='*', c='r', s=100)
	plt.scatter(centers[1,0],centers[1,1],marker='*', c='g', s=100)
	for d in data:
		if(d[2]==0):
			plt.scatter(d[0],d[1],marker='.', c='r', s=30)
		else:
			plt.scatter(d[0],d[1],marker='.', c='g', s=30)
	plt.show()
	plt.clf()
def newCenters(data,k):
	centers=[]
	count=np.zeros(k)
	for i in range(k):
		centers.append((0.0,0.0))
	
	centers=np.array(centers)
	
	
	
	for d in data:
		#print d[0]
		count[int(d[2])]+=1
		centers[int(d[2]),0]+=d[0]
		centers[int(d[2]),1]+=d[1]
	#print centers		
		
	for i in range(k):
		centers[i,:]=centers[i,:]/count[i]	
	return centers	
			
	
def main():
	print 'K-Means'
	points = [(0.1,0.6,-1),(0.15,0.71,-1),(0.08,0.9,-1),(0.16,0.85,-1),(0.2,0.3,-1),(0.25,0.5,-1),(0.24,0.1,-1),(0.3,0.2,-1)]
	data = np.array(points)
	#print data
	#print data
	#print points[0]
	k=2
	centers = [points[0],points[4]]
	centers = np.array(centers)
	#print centers 
	#plt.show()
	#plt.close()
	
	#print df[:,0]
	
	#for p in points:	
	#	print p
	
	#print l2(points[0],points[1])	
	dist=[]
	for i in range(k):
		dist.append(np.zeros(len(data)))
	dist=np.array(dist)
#	print dist
		
	for epoch in range(2):
		print "e",epoch
		i=0
		for c in centers:
			j=0
			for p in points:
				dist[i,j]=l2(c,p)
				#print 'i:',i,'j:',j,' D:',l2(c,p)
				j+=1
			i+=1	
		#Dist Array gen for this Epoch Done
		print dist
		data[:,2]=np.argmin(dist,axis=0)	
		
		raw_input()			
		makeplot(centers,data)
		centers = newCenters(data,k)			 	
if __name__=="__main__":
	main()
		