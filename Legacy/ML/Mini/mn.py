import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
import math, time 
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix


start = time.time() 

df = pd.read_csv('mnist_test.csv', sep=',' , header=None)
MNIST_train_small_df = df.iloc[0:200]
#print MNIST_train_small_df.head(3)
print MNIST_train_small_df.shape
print MNIST_train_small_df.loc[:,0].value_counts()
X_tr = MNIST_train_small_df.iloc[:,1:] # iloc ensures X_tr will be a dataframe
y_tr = MNIST_train_small_df.iloc[:, 0]
X_train, X_test, y_train, y_test = train_test_split(X_tr,y_tr,test_size=0.2, random_state=30, stratify=y_tr)

steps = [('scaler', StandardScaler()), ('SVM', SVC(kernel='poly'))]
pipeline = Pipeline(steps) # define Pipeline object

parameters = {'SVM__C':[0.001, 0.1, 100, 10e5], 'SVM__gamma':[10,1,0.1,0.01]}
grid = GridSearchCV(pipeline, param_grid=parameters, cv=5)

grid.fit(X_train, y_train)

print "score = %3.2f" %(grid.score(X_test, y_test))

print "best parameters from train data: ", grid.best_params_

#GET ALL PREDICTIONS AND CHECK A FEW
y_pred = grid.predict(X_test)
print y_pred[100:105]
print y_test[100:105]


print "confusion matrix: \n ", confusion_matrix(y_test, y_pred)

for i in (np.random.randint(0,10,6)):
	two_d = (np.reshape(X_test.values[i], (28, 28)) * 255).astype(np.uint8)
	plt.title('predicted label: {0}'. format(y_pred[i]))
	plt.imshow(two_d, interpolation='nearest', cmap='gray')
	plt.show()
	raw_input("PRESS ANY KEY TO CONTINUE.")
	#plt.close(two_d)
	