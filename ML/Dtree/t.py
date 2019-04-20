import numpy as np
import pandas as pd
from Queue import Queue
from sklearn import tree
from sklearn.model_selection import train_test_split


class node:
	def __init__(self,name,branches,leaf,resultOf,level):
		self.name = name
		self.branches = branches
		self.leaf = leaf
		self.resultOf = resultOf
		self.level = level
	def show(self):
		print ('	'*self.level),self.name,"| Level",self.level,"  |ResultOF:",self.resultOf	
	
	def parse(self):
		L = Queue()
		L.put(self)
		while not L.empty():
			cur=L.get()
			cur.show()
			for b in cur.branches or []:
				L.put(b)


def entropy(s):
	e=0
	vals , counts = np.unique(s['Buys'],return_counts = True)  
#	print vals
	#print len(counts)
	for i in range(len(counts)):
#		print c
		e += -(float(counts[i])/np.sum(counts))*np.log2(float(counts[i])/np.sum(counts))
	#print e
	return e	
		

def makeTree(s,cols,level,resultOf):
	vals , counts = np.unique(s['Buys'],return_counts = True)  
	#print vals
	#print counts
	if len(vals)==1:
		#print 'All of',vals[0]
		return node(vals[0],None,True,resultOf,level)
	if (len(cols)==0):
		#print 'No cols'
		return node(vals[np.where(counts == np.max(counts))],None,True,resultOf,level)	
	if	(len(s)==0):
		return
	
	info_dict = {}
	base_gain = entropy(s)
	
	for c in cols:
		ex = 0
		for r ,rdf in s.groupby(c):
			ex += (float(len(rdf))/len(s))*entropy(rdf)
		info_dict[c] = base_gain - ex
	best = max(info_dict, key = info_dict.get)	
	#print best
	#print info_dic
	cols.remove(best)
	branches = []
	for r ,rdf in s.groupby(best):
		branches.append(makeTree(rdf,cols,level+1,{best:r}))
	return node(best,branches,False,resultOf,level)			
	
	
	
	
	
def lib(data):
	
	target = data.pop('Buys')

	
	#tx , tx , x ,y = train_test_split( data, target, test_size=0.33, random_state=42)	
	#print data
	#return
	#print 'LIB'
	
	clf = tree.DecisionTreeClassifier(criterion='entropy',min_samples_leaf=4)
	one_hot_data = pd.get_dummies(data)
	
	feat = list(one_hot_data)
	clf = clf.fit(one_hot_data,target)
	tree.export_graphviz(clf,out_file='tree.dot',feature_names=feat,class_names=['yes','no']) 
	print clf.score(one_hot_data,target)

	ypred = clf.predict(one_hot_data)
	print ypred 

def main():
	print 'Dtree'
	df = pd.read_csv('data.csv',index_col = 'ID')
	cols = list(df)
	target=cols.pop(len(cols)-1)
	lib(df)
	return
	
	#print cols
	#print target
	entropy(df)
	n = makeTree(df,cols,0,None)
	#n.show()
	n.parse()	
	


if __name__ == '__main__':
	main()
	