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

n_nodes_hl1 = 300
n_nodes_hl2 = 300
n_nodes_hl3 = 300

n_classes = 5
batch_size = 20
hm_epochs = 10



input_layer = tflearn.input_data(shape=[None, 20, 10], name='input')

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

# Training
model = tflearn.DNN(net, tensorboard_verbose=0)
model.fit(mfcc, target, n_epoch=30, validation_set=0.1,
show_metric=True, run_id="dense_model")

model.save('./TensorFlowModel/my_model.model')


#'''