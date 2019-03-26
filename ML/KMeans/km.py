import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from copy import deepcopy
#0.1489

def main():
	print 'K-Means'
	data = np.array([(0.1,0.6),(0.15,0.71),(0.08,0.9),(0.16,0.85),(0.2,0.3),(0.25,0.5),(0.24,0.1),(0.3,0.2)])
	#data = np.array([(2,3),(2,1),(1,3),(-2,-3),(-1,-3),(-2,-1)])
	centers = np.array([(0.1,0.6),(0.3,0.2)])
	n = data.shape[0]
	c = data.shape[1]
	k = centers.shape[0]
	print data
	print centers
	clusters = np.zeros(n)
	distances = np.zeros((n,k))
	
	centers_old = np.zeros(centers.shape) # Store old centers
	centers_new = deepcopy(centers) # Store new centers
	error = np.linalg.norm(centers_new - centers_old)
	print "Error 1:"+str(error)
	#0.41
	
	#distances[:,0] = np.linalg.norm(data - centers[0], axis=1)
	#return 
	
	p=0
	while p != 7:
		print 'P:'+str(p)
		p+=1
		for i in range (k):
			distances[:,i] = np.linalg.norm(data - centers[i], axis=1)
		clusters = np.argmin(distances, axis = 1) 			
		print distances		
		print clusters
   		centers_old = deepcopy(centers_new)
		
		for i in range(k):
			centers_new[i] = np.mean(data[clusters == i], axis=0)
		error = np.linalg.norm(centers_new - centers_old)
		print centers_new     
				 	
	#plt.scatter(data[:,0], data[:,1], s=7)
	print "Clusters"
	print clusters
	print "Clusters data[clusters == 0]" 
	#print data[clusters == 0,0]
	plt.scatter(data[clusters == 0,0],data[clusters == 0,1], s=7, c='b')
	plt.scatter(data[clusters == 1,0],data[clusters == 1,1], s=7, c='r')
	plt.scatter(centers_new[0,0], centers_new[0,1], marker='*', c='b', s=150)
	plt.scatter(centers_new[1,0], centers_new[1,1], marker='*', c='r', s=150)
	plt.show()
	

			 	
if __name__=="__main__":
	main()