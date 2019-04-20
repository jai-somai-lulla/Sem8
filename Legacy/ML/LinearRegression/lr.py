import numpy as np 
import matplotlib.pyplot as plt 
from sklearn import datasets, linear_model, metrics 

def libfunc(x,y):
	n = np.size(x)     
	x_train=x[1:5].reshape(-1, 1)
	y_train=y[1:5].reshape(-1, 1)
	x_test=x[5:n].reshape(-1, 1)
	y_test=y[5:n].reshape(-1, 1)
	
	reg = linear_model.LinearRegression() 	
	reg.fit(x_train, y_train) 
	#plt.scatter(reg.predict(x_train), y_train, color = "green", s = 10, label = 'Train data') 
  	 
	print('Intercept: \n',reg.intercept_)
  	print('Coefficients: \n', reg.coef_)
	#plt.scatter(reg.predict(x_test), reg.predict(x_test) - y_test,color = "blue", s = 10, label = 'Test data') 
	plt.scatter(x_test,y_test,color="green")
	plt.plot(x_test,reg.predict(x_test),color = "blue")
	plt.show() 
	print(reg)
	
def weights(x,y):
	n = np.size(x)     
	m_x = np.mean(x)
	m_y =  np.mean(y) 
    # calculating cross-deviation and deviation about x 
	SS_xy = np.sum(y*x) - n*m_y*m_x 
	SS_xx = np.sum(x*x) - n*m_x*m_x 
    # calculating regression coefficients 
	b_1 = SS_xy / SS_xx 
	b_0 = m_y - b_1*m_x   
	return(b_0, b_1) 	

def plot_regression_line(x, y, b): 
    # plotting the actual points as scatter plot 
    plt.scatter(x, y, color = "m",marker = "o", s = 30) 
  
    # predicted response vector 
    y_pred = b[0] + b[1]*x 
  
    # plotting the regression line 
    plt.plot(x, y_pred, color = "g") 
  
    # putting labels 
    plt.xlabel('x') 
    plt.ylabel('y') 
  
    # function to show plot 
    plt.show() 	

def main():	
	print("Linear Regrssion")
	x=np.array([1,2,3,3,4,4,5,6,8,12])
	x=x+5
	print(x)
	y=np.array([2,4,4,5,8,8,12,12,16,24])
	y=y*3
	
	b=weights(x,y)
	print(b)
	#plot_regression_line(x, y, b)
	libfunc(x,y)	


main()	