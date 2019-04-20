import numpy as np
import pandas as pd 
#import matplotlib.pyplot as plt 

def cost_function(X, Y, B):
    if(type(Y) == np.int64):
    	m=1
    else:
    	m = len(Y)
    	
    J = np.sum((X.dot(B) - Y) ** 2)/(m*2)
    return J

def gradient_descent(X, Y, B, alpha, iterations):
	cost_history = [0] * iterations
	m = len(Y)
    
	for iteration in range(iterations):
        # Hypothesis Values for entire set data
		h = X.dot(B)
        # Difference b/w Hypothesis and Actual Y
		loss = h - Y
        # Gradient Calculation
		gradient = X.T.dot(loss) / m
        # Changing Values of B using Gradient
		B = B - alpha * gradient
        # New Cost Value
		cost = cost_function(X, Y, B)
		cost_history[iteration] = cost
        
	return B, cost_history
    
    
def main():	
	print("Linear Regrssion")
	x=np.array([1,2,3,3,4,4,5,6,8,12])
	x0 = np.ones(len(x))
	X = np.array([x0, x]).T
	Y=np.array([2,4,4,5,8,8,12,12,16,24])
	B = np.array([0, 0])
	print cost_function(X[0],Y[0],B)
	inital_cost = cost_function(X, Y, B)
	print("Initial Cost: "+str(inital_cost))
	B,ch = gradient_descent(X, Y, B, 0.01, 10)
	print "Weights :"+str(B)
	print "Cost_History :"+str(ch)
	
	
if __name__ == "__main__":
	main()	
