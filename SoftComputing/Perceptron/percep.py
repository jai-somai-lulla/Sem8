
class neuron:
	weight_matrix=[]
	inputs=0
	def __init__(self,inputs):
		for index in range (0,inputs):
			self.weight_matrix.append(index)
		print inputs
		self.inputs=inputs
		
	def predict(self,x):
		sigma=0
		for index in range (0,self.inputs):
			sigma+=self.weight_matrix[index]*x[index]
		if(sigma>0):
			return 1
		else: 
			return 0
					 
	

def main():
	#print ('Percptron')
	n1 = neuron(3)  
	#print n1.weight_matrix
	train_inputs = [[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]]
	train_outputs = [[0, 1, 1, 0]]
  	print train_inputs[0]
  	print n1.predict(train_inputs[3])
		
if __name__=='__main__':
	main()	
