import pandas as pd
import tflearn
import pickle
import numpy as np

# Data loading and preprocessing
import tflearn.datasets.mnist as mnist

dataClassifier = pickle.load( open( "./pickles/FrameLength_10_HopLength_10.pickle", "rb" ) )

def to1hot(row):
    one_hot = np.zeros(5)
    one_hot[row]=1.0
    return one_hot

dataframe = pd.DataFrame({
    'target' : pd.Series(dataClassifier['target'])
})

dataframe.target = dataframe.target.apply(to1hot)
mfcc = np.vstack(dataClassifier['mfcc']).reshape(len(dataClassifier['mfcc']),20, 10).astype(np.float32)
target = np.vstack(dataframe.target)
#''

net = tflearn.input_data(shape=[None, 20, 10] )

#net = tflearn.embedding(net, input_dim=200, output_dim=128)
net = tflearn.lstm(net, 87, return_seq=True)
net = tflearn.lstm(net, 87)
net = tflearn.fully_connected(net, 5, activation='softmax')
net = tflearn.regression(net, optimizer='adam',
                         loss='categorical_crossentropy', name="output1")



model = tflearn.DNN(net, tensorboard_verbose=2)

model.fit(mfcc,target, n_epoch=40, validation_set=0.1, show_metric=True,
snapshot_step=100)

#model.save('./TensorFlowModel/my_model.model')


#'''