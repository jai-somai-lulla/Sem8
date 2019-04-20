class Perceptron(object) :

    def __init__(self, weights, bias, alpha):
        self.weights = weights
        self.bias = bias
        self.alpha = alpha

    def fire(self, inputs, outputs):
        yin = sum([i*w for (i,w) in zip(inputs, self.weights)]) + self.bias
        yout = self.activate(yin)
        self.compare(yout, outputs, yin, inputs)
        return yout

    def activate(self, summation):
        if summation > 0 :
            return 1
        else :
            return 0
    
    def compare(self, yout , outputs, yin , inputs) :
        if yout != outputs :
            updated_weights = []
            for i, w in zip( inputs , self.weights ) :
                updated_weights.append( w + (self.alpha * (outputs-yin) * i ) )
            self.weights = updated_weights
            self.bias += self.alpha*(outputs-yin)
            
if __name__ == '__main__':

    inputs = [(0,0), (0,1) , (1,0) , (1,1), (-1,0) , (-1,-1) , (0.5, -0.2)]
    outputs = [0, 1, 1, 1, 0, 0, 0]

    perceptron = Perceptron([1,1], 0, 1)
    
    for epochs in range(0,2) :
        print("\nEPOCH NUMBER -->" , epochs, "\n")
        for i,o in zip(inputs, outputs) : 
            print( "For input values " , i , "\tacutal vs calculated output is : ", o , perceptron.fire(i,o) )

    print("\n",perceptron.weights , perceptron.bias)

