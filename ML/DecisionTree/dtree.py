import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report 
#import sklearn

def splitdataset(df): 
  	
  	X = df.values[:, 0:4] 
	Y = df.values[:, 4]
	#print(list(X))
	#print(list(Y))
	  
	X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3, random_state = 100)       
	return X, Y, X_train, X_test, y_train, y_test 

def cal_accuracy(y_test, y_pred):   
	print("Confusion Matrix: ", 
	confusion_matrix(y_test, y_pred))       
	print ("Accuracy : ", 
	accuracy_score(y_test,y_pred)*100)       
	print("Report : ", 
	classification_report(y_test, y_pred)) 
    
def libdtree(X_train, X_test, y_train):
	model = DecisionTreeClassifier( 
            criterion = "entropy", random_state = 100, 
            max_depth = 3, min_samples_leaf = 5) 
	model.fit(X_train, y_train) 
	y_pred = model.predict(X_test) 	
	return y_pred
	      
def main():
	print("Decision Tree\n")
	df = pd.read_csv("data.csv",index_col='ID') 		
	print(df)
	df[:] = df[:].astype('category')
	X, Y, X_train, X_test, y_train, y_test = splitdataset(df) 	
	y_pred = libdtree(X_train, X_test, y_train)
	#cal_accuracy(y_test,y_pred)
	
if __name__=="__main__": 
    main()
    