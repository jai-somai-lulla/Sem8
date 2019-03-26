import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from copy import deepcopy

def main():
	print 'K-Means'
	#data = np.array([(2,3),(2,1),(1,3),(-2,-3),(-1,-3),(-2,-1)])
	data = np.array([(0.1,0.6),(0.15,0.71),(0.08,0.9),(0.16,0.85),(0.2,0.3),(0.25,0.5),(0.24,0.1),(0.3,0.2)])
	#df=pd.DataFrame(data)
	test =[(4,4),(-4,-4)]
	centers = np.array([(0,3),(3,0)])
	k = 2
	n = data.shape[0]
	c = data.shape[1]
	#print df
	
	centers_old = np.zeros(centers.shape) # Store old centers
	centers_new = deepcopy(centers) # Store new centers
	error = np.linalg.norm(centers_new - centers_old)
	clusters = np.zeros(n)
	distances = np.zeros((n,k))

	p=0
	while error != 0:
		print 'P:'+str(p)
		p+=1
		for i in range (k):
			 distances[:,i] = np.linalg.norm(data - centers[i], axis=1)
		
		clusters = np.argmin(distances, axis = 1)
   		centers_old = deepcopy(centers_new)
		
		for i in range(k):
			centers_new[i] = np.mean(data[clusters == i], axis=0)
		
		error = np.linalg.norm(centers_new - centers_old)
		
		print centers_new     
	
	
	print(data)
	print('---')
	print(centers_new)
			 	
	plt.scatter(data[:,0], data[:,1], s=7)
	plt.scatter(centers_new[:,0], centers_new[:,1], marker='*', c='g', s=150)
	plt.show()
	
			 	
if __name__=="__main__":
	main()
		
