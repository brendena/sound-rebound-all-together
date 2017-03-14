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
#net = tflearn.embedding(net, input_dim=200, output_dim=128)
net = tflearn.lstm(net, 87, return_seq=True)
net = tflearn.lstm(net, 87)
net = tflearn.fully_connected(net, 2, activation='softmax')
net = tflearn.regression(net, optimizer='adam',
                         loss='categorical_crossentropy', name="output1")

#, checkpoint_path="./checkpoints"
# i think checkpoints are if it fails

model = tflearn.DNN(net, tensorboard_verbose=2)

model.fit(musicData.X, musicData.Y, n_epoch=10, validation_set=0.1, show_metric=True,
snapshot_step=100)

model.save('my_model.model')

#technically works