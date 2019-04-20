class MCP_Neuron(object):

    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def fire(self, inputs):
        summed = sum([i*w for (i,w) in zip(inputs, self.weights)])
        return self.AND_threshold(summed + self.bias), self.OR_threshold(summed + self.bias), self.NAND_threshold(summed + self.bias), self.NOR_threshold(summed + self.bias), self.XOR_threshold(summed + self.bias)

    def AND_threshold(self, weighted_sum):
        if weighted_sum == 2:
            return 1
        else:
            return 0

    def OR_threshold(self, weighted_sum):
        if weighted_sum >= 1:
            return 1
        else:
            return 0

    def NAND_threshold(self, weighted_sum):
        if weighted_sum == 2:
            return 0
        else:
            return 1

    def NOR_threshold(self, weighted_sum):
        if weighted_sum >= 1:
            return 0
        else:
            return 1

    def XOR_threshold(self, weighted_sum):
        if weighted_sum == 1:
            return 1
        else:
            return 0


if __name__ == '__main__':

    inputs = [(0,0), (0,1), (1,0) , (1,1)]

    neuron_1 = MCP_Neuron([1,1], 0)

    print("Inputs are :\t\t","AND OR NAND NOR XOR");

    for i in inputs :

        print('For input', i, "\t", neuron_1.fire(i));
