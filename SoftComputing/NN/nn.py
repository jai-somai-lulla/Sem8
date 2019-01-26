import numpy as np
import pandas as pd

def sigmoid(x):  
	return 1/(1+np.exp(-x))

def sigmoid_derv(x):  
	return sigmoid(x)*(1-sigmoid(x))

def cross_entropy(pred, real):
	res = pred - real
	return res

class NeuralNetwork:
	def __init__(self, x, y):
		self.hidden = 4
		self.input = x
		self.y = y
		self.lr = 0.1
		self.w1 = np.random.rand(self.input.shape[1],self.hidden) 
		self.w2 = np.random.rand(self.hidden,1) 
		self.output = np.zeros(y.shape)
		self.a1=0
		self.a2=0
		#print 'Weights 1  :'
		#print str(self.w1)
		#print 'Weights 2  :'
		#print str(self.w2)                
		
	def feedforward(self,row):
		z1 = np.dot(row,self.w1)  	
		print "Z1 :"+ str(z1)
		self.a1 = sigmoid(z1)
		print "A1 :"+ str(self.a1)
		z2 = np.dot(self.a1, self.w2)	
		print "Z2 :"+ str(z2)
		self.a2 = sigmoid(z2)
		print "A2 :"+ str(self.a2)
		return self.a2
		
	def train(self):
		epochs=1
		for e in range(epochs):
			for index, row in self.input.iterrows():
				#print row
				#print index
				self.feedforward(row)
				#print self.y.iloc[index]
				
				actual= self.y.iloc[index,0]
				#self.backprop(row,actual)
				#print xi
				
	def backprop(self,x,actual):	
		a2_delta = cross_entropy(self.a2, actual) # w2
		z1_delta = np.dot(a2_delta, self.w2.T)
		a1_delta = z1_delta * sigmoid_derv(self.a1) # w1
		
		print "A2_DELTA :"+ str(a2_delta)
		print "Z1_DELTA :"+ str(z1_delta)
		print "A1_DELTA :"+ str(a1_delta)
		
		
		#print "A1.T :"+str(self.a1.T)
		#print a2_delta	
		print "W2 :"+str(self.w2)
		print "W1 :"+str(self.w1)
		
		self.w2 -= self.lr * (self.a1.T * a2_delta)
		
		self.w1 -= self.lr * np.dot(self.x.T, a1_delta)
		
			
			
def main():
	print 'Neural Network'
	train_inputs = [[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]]
	train_outputs = [0, 1, 1, 1]
	op=pd.DataFrame(train_outputs)
	ip=pd.DataFrame(train_inputs)
	#print ip.shape[1]
	nn = NeuralNetwork(ip,op)
	nn.train()
		
if __name__=="__main__":
	main()		