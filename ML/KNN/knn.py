from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier  
from sklearn.metrics import classification_report, confusion_matrix  
from matplotlib import pyplot as plt
from operator import itemgetter
def l2(a,b):
	return pow(((a[0]-b[0])**2 + (a[1]-b[1])**2),0.5)

def knn(x,y,tx,ty):
	k=5
	
	
	ypred=[]
	yactual=[]
	for t in range(len(tx)):
		testcasex = tx.iloc[t].values
		testcasey = ty.iloc[t]
		print 
		plt.scatter(testcasex[0],testcasex[1],c='black')
		plt.scatter(x.iloc[np.where(y=='M')[0],0],x.iloc[np.where(y=='M')[0],1],c='b')
		plt.scatter(x.iloc[np.where(y=='L')[0],0],x.iloc[np.where(y=='L')[0],1],c='r')
		votes={}
		distance = []
		for i in range(len(x)):
			distance.append((l2(testcasex,x.iloc[i].values),y.iloc[i],x.iloc[i].values))
			votes[y.iloc[i]]=0
		
		distance.sort(key = lambda test_list: test_list[0])	
		#print distance
		for i in range(k):
			#print i,distance[i][2][0]
			votes[distance[i][1]]+=1
			#print distance[i][1]#,distance[i][2][1]
			
			plt.plot([distance[i][2][0],testcasex[0]],[distance[i][2][1],testcasex[1]],c='black')		
			
		#print 'ffefe',max(votes,key=votes.get)	
		ypred.append(max(votes,key=votes.get))
		#yactual.append(testcasey)
		plt.pause(2)
		plt.clf()
		
	return ypred
	
def score(yactual,ypred):
	cf=confusion_matrix(yactual, ypred)
	#print yactual
	#print ypred
	print cf	
	print classification_report(yactual, ypred)

def lib(x,y,tx,ty):
	
	classifier = KNeighborsClassifier(n_neighbors=5)  
	classifier.fit(x, y)
	ypred = classifier.predict(tx)
	return ypred 
	

def main():
	print 'knn'
	df = pd.read_csv('data.csv')
	print df
	x,tx,y,ty = train_test_split(df[['Height' , 'Weight']],df['Size'])
	ypred = knn(x,y,tx,ty)
	score(ty,ypred)
	print '\n\n\n'
	ypred = lib(x,y,tx,ty)
	score(ty,ypred)
	
	print ypred
	
if __name__ == '__main__':
	main()	