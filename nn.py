import numpy as np

class NN:
    def __init__(self,*layers):
        self.weights = []
        self.bias = []
        self.lable = 0
        self.hiddenLayer = []
        for layer in layers:
            if layers.index(layer) == 0:
                self.inputLayer = np.zeros([layer])
            elif layers.index(layer) == len(layers)-1:
                self.outputLayer = np.zeros([layer])
            else:
                self.hiddenLayer.append(np.zeros([layer]))
    
    def loadInput(self,input,lable):
        for i in range(len(input)):
            self.inputLayer[i] = input[i]
        self.lable = lable
    
    def sigmoid(self,ar):
        return 1/(1 + np.exp(-1*ar))
        
    def getRandWeights(self):
        preLayer = self.inputLayer
        for layer in self.hiddenLayer:
            self.weights.append(np.random.randn(len(layer),len(preLayer)))
            preLayer = layer
        self.weights.append(np.random.randn(len(self.outputLayer),len(preLayer)))

    def getRandBias(self):
        for layer in self.hiddenLayer:
            self.bias.append(np.random.randn(len(layer)))
        self.bias.append(np.random.randn(len(self.outputLayer)))

    def feedForward(self,toPrint = True):
        count = 0
        preLayer = self.inputLayer
        for weight in self.weights:
            output = self.sigmoid(np.matmul(weight,preLayer) - self.bias[count])
            if len(self.weights)-count-1 == 0:
                self.outputLayer = output
            else:                
                self.hiddenLayer[count] = output
                preLayer = self.hiddenLayer[count]
            count += 1
        if toPrint:
            print(self.outputLayer)
        return self.outputLayer