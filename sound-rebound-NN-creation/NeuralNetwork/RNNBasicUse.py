import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
import tflearn.datasets.mnist as mnist
import numpy as np

from CI_RNNBasic import MusicData

#https://github.com/tflearn/tflearn/blob/master/examples/images/rnn_pixels.py

musicData = MusicData()

print(musicData.myShape)


net = tflearn.input_data(shape=musicData.myShape)
net = tflearn.lstm(net, 87, return_seq=True)
net = tflearn.lstm(net, 87)
net = tflearn.fully_connected(net, 2, activation='softmax')
net = tflearn.regression(net, optimizer='adam',
                         loss='categorical_crossentropy', name="output1")


model = tflearn.DNN(net)
model.load('my_model.model')

#technically works


for i in range(20):
	print("guess " + str(i))
	print( np.array_str(musicData.testY[i]) + "  realValue" )
	print( np.round(model.predict([musicData.testX[i]])[0])  )