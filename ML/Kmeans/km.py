import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from pprint import pprint

points = [(0.1,0.6),(0.15,0.71),(0.08,0.9),(0.16,0.85),(0.2,0.3),(0.25,0.5),(0.24,0.1),(0.3,0.2)]


def lib(X):
	kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
	print kmeans.labels_
	print kmeans.cluster_centers_
	X[3] = kmeans.labels_	
	print 
	plt.scatter(X[0][np.where(X[3]==0)[0]],X[1][np.where(X[3]==0)[0]],c='b')
	plt.scatter(X[0][np.where(X[3]==1)[0]],X[1][np.where(X[3]==1)[0]],c='r')
	
	plt.scatter(kmeans.cluster_centers_[0][0],kmeans.cluster_centers_[0][1],c='b',marker='*')
	
	plt.scatter(kmeans.cluster_centers_[1][0],kmeans.cluster_centers_[1][1],c='r',marker='*')
	plt.pause(5)
	return kmeans.cluster_centers_
	

def l2(a,b):
	return pow((a[0]-b[0])**2 + (a[1]-b[1])**2,0.5)
	
def kmeans(s):
	k=2
	g = 7
	centers = np.array([[0.0,0.0]]*k)
	print s
	centers[0] =  s.iloc[0,:]
	centers[1] =  s.iloc[1,:]
	print centers


	for i in range(g):
		darray = np.array([[0.0]*len(s)]*k)
		#print darray
		#print 'Epoch :',i
		for cno in range(k):
			for dp in range(len(s)):		
				darray[cno,dp] = l2(centers[cno],s.iloc[dp,:])
		#pprint(darray)
		locs = np.where(darray == np.min(darray,axis=0))
		#print locs
		old = np.array(centers)
		plt.scatter(old[0][0],old[0][1],c='r',marker="*",s=80)
		plt.scatter(old[1][0],old[1][1],c='g',marker="*",s=80)
		centers = np.array([[0.0,0.0]]*k)		
		counts = [0]*k 
		for l in range(len(locs[0])):
			if locs[0][l]==0:
				plt.scatter(s.iloc[l,0],s.iloc[l,1],c='g')
			else :
				plt.scatter(s.iloc[l,0],s.iloc[l,1],c='r')
				
				
			centers[locs[0][l]]+=s.iloc[locs[1][l],:]
			counts[locs[0][l]]+=1
		#pprint(centers)
		#print counts	 		 	
		for q in range(k):
			centers[q]/=counts[q]
		
		
		plt.pause(2)
		plt.clf()
	return centers	
			
def main():
	print 'Kmean'
	df = pd.DataFrame(points)
	#print df
	#pprint(lib(df))
	pprint(kmeans(df))
	pprint(lib(df))
	
if __name__ == '__main__':
	main()		