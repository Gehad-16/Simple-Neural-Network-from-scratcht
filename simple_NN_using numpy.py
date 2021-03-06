# -*- coding: utf-8 -*-
"""ass_2_Simple_NN_Numpy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sZgEQlfUyk_qPYKIMdTEvGZCSBEeZNFK
"""

import numpy as np
neuron = 10

def sigmoid(x):
    return 1.0/(1+ np.exp(-x))

def sigmoid_derivative(x):
    return x * (1.0 - x)

class Simple_NN:
    def __init__(self, X_train, y_train):
        self.X_train      = X_train
        print('inputs \n' , self.X_train)
        print()
        np.random.seed(43)
        self.weight_1   = np.random.rand(self.X_train.shape[1],neuron) 
        print('weights1 \n',self.weight_1)
        print()
        np.random.seed(100)
        self.weight_2   = np.random.rand(neuron,1)                 
        print('weights2 \n',self.weight_2)
        print()
        self.y_train         = y_train
        print('y \n',self.y_train)
        print()
        self.out_1     = np.zeros(self.y_train.shape) # y hat
        # print('output \n',self.output)
        print()
        
    def Feedforward(self):
        self.layer1 = sigmoid(np.dot(self.X_train, self.weight_1))
        #print(np.dot(self.input, self.weights1))
#        print('layer 1 \n',self.layer1)
#        print()        
        self.out_1 = sigmoid(np.dot(self.layer1, self.weight_2))
#        print('output \n',self.output)
#        print()
        
    def Backpropagation(self):
        self.E = 0.005
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 =self.E * ( np.dot(self.layer1.T, ((self.y_train - self.out_1) * sigmoid_derivative(self.out_1))) )
        # print('d_weights2  \n',d_weights2  )
        # print()        
        d_weights1 = self.E * ( np.dot(self.X_train.T,
                            (np.dot((self.y_train - self.out_1) * sigmoid_derivative(self.out_1),
                                    self.weight_2.T) * sigmoid_derivative(self.layer1))) )
        # print('d_weights1 \n',d_weights1)
        # print()        

        # update the weights with the derivative (slope) of the loss function
        self.weight_1 =self.weight_1+ d_weights1
        self.weight_2 =self.weight_2+ d_weights2

X_train = np.array( [[1,1,1],[1,2,1],[1,4,1],[2,5,1],[4,4,1],[2,2,1],[2,3,1],[3,3,1],[3,4,1],[6,1,1],[5,5,1],[5,3,1],[3,5,1],[2,4,1],[3,2,1],[4,3,1],[7,3,1],[3,1,1],[5,2,1]])  
y_train = np.array( [[0],[0],[0],[1],[1],[0],[0],[1],[1],[0],[0],[0],[1],[1],[1],[1],[0],[1],[0]] )

NN = Simple_NN(X_train,y_train)

for i in range(100):
    NN.Feedforward()
    NN.Backpropagation()
#    print('--------------------------------')
#

Y_predict=np.zeros([NN.out_1.shape[0],1])
for i in range(NN.out_1.shape[0]):
  Y_predict[i][0]=round(NN.out_1[i][0] , 3)

print('Y_predict',Y_predict)

for i in range(Y_predict.shape[0]):
  if (Y_predict[i][0]>=0.5):
    Y_predict[i][0]=1
  else:
    Y_predict[i][0]=0

print()

print('Y_predict',Y_predict)

def Calculate_accuracy(predicted_y , y):
    counter=0
    index=0
    for item in predicted_y:
        if predicted_y [index] == y [index]:
            counter=counter+1
        index=index+1  
    length=len(y)
    # print (counter)
    # print (length)
    return ((counter/length)*100)

# Calculate_accuracy for test 
Calculate_accuracy(Y_predict , y_train)