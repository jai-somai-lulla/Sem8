import numpy as np

class neuron:
	weight_matrix=[]
	inputs=0
	learning_rate=1
	def __init__(self,inputs):
		#for index in range (0,inputs):
		#	self.weight_matrix.append(index)
		#print inputs
		self.weight_matrix = np.random.random((inputs)) * 2 - 1
		print self.weight_matrix
		self.inputs=inputs
		
	def predict(self,x):
		sigma=0
		for index in range (0,self.inputs):
			sigma+=self.weight_matrix[index]*x[index]
		if(sigma>0):
			return 1
		else: 
			return 0
	def adjust(self,X,Y):
		#print "n: "+n
		print "X: "+str(X)
		print "Y: "+str(Y)
		calc = self.predict(X)
		error = Y - calc
		for i in range(self.inputs):
			correction = error*X[i]*self.learning_rate #E * X * ALPHA
			self.weight_matrix[i] += correction
def main():
	#print ('Percptron')
	n1 = neuron(3)  
	#print n1.weight_matrix
	train_inputs = [[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]]
	train_outputs = [0, 1, 1, 1]
  	#print train_inputs[0]
  	#print n1.predict(train_inputs[3])
	for epoch in range(0,10):
		print "Epoch ",(epoch)
		print n1.weight_matrix		
		for x in range(0,4):
			n1.adjust(train_inputs[x],train_outputs[x])
		
	
  	for x in range(0,4):
		print 'Y: '+str(train_outputs[x])+' Y(Predicted):'+str(n1.predict(train_inputs[x])) 
		
if __name__=='__main__':
	main()	
