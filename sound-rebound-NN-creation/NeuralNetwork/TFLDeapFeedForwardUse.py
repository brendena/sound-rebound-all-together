#using this example
#https://github.com/tflearn/tflearn/blob/master/examples/images/dnn.py
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
import tflearn.datasets.mnist as mnist
import numpy as np

import pickle
import numpy as np
data = pickle.load( open( "./audioForNeuralNetwork.pickle", "rb" ) )

def to1hot(row):
    one_hot = np.zeros(2)
    one_hot[row]=1.0
    return one_hot

data["one_hot_encoding"] = data.target.apply(to1hot)

data["mfcc_flatten"] = data.mfcc.apply(lambda mfcc: mfcc.flatten())



test_data = data[160:]
testX = np.vstack(test_data.mfcc_flatten).reshape(test_data.shape[0],20, 87,1).astype(np.float32)
testY = np.vstack(test_data["one_hot_encoding"])

n_nodes_hl1 = 1500
n_nodes_hl2 = 1500

n_classes = 2
batch_size = 20
hm_epochs = 10



input_layer = tflearn.input_data(shape=[None, 20, 87, 1], name='input')

dense1 = tflearn.fully_connected(input_layer, n_nodes_hl1, activation='tanh',
								regularizer='L2', weight_decay=0.001)



dropout1 = tflearn.dropout(dense1, 0.8)
dense2 = tflearn.fully_connected(dropout1, n_nodes_hl2, activation='tanh',
                                 regularizer='L2', weight_decay=0.001)




dropout2 = tflearn.dropout(dense2, 0.8)
softmax = tflearn.fully_connected(dropout2, n_classes, activation='softmax')



# Regression using SGD with learning rate decay and Top-3 accuracy
sgd = tflearn.SGD(learning_rate=0.1, lr_decay=0.96, decay_step=1000)
top_k = tflearn.metrics.Top_k(3)
net = tflearn.regression(softmax, optimizer=sgd, metric=top_k,
                         loss='categorical_crossentropy')



#use
model = tflearn.DNN(net)
model.load('my_model.model')

print( np.round(model.predict([testX[1]])[0]) )
print(testY[1])

for i in range(10):
	print("guess " + str(i))
	print( np.array_str(testY[i]) + "  realValue" )
	print( np.round(model.predict([testX[i]])[0])  )
