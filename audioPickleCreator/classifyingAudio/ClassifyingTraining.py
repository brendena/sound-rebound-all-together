from sklearn import cross_validation
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.svm import OneClassSVM 
from sklearn.grid_search import RandomizedSearchCV
from sklearn import metrics
from sklearn import model_selection

from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import KFold
import tflearn as tf

import numpy as np

#import tensorflow as tf

from classifyingAudio.ClassifyingBase import ClassifyingBase

'''
estimators to getting the neual network better
	https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/learn/python/learn
	https://github.com/tensorflow/tensorflow/issues/2030
'''
class ClassifyingTraining(ClassifyingBase):
	def __init__(self,X,Y):
		ClassifyingBase.__init__(self)
		self.setData(X,Y)
	def gridSearchCVForest(self):
		forst_n_estimators = range(1,200)
		forst_criterion = ['gini','entropy']
		self.clf1Params = dict(n_estimators=forst_n_estimators,criterion=forst_criterion)

		for clf, label, params in zip([self.clf1], [self.clf1Type],[self.clf1Params]):
			rand = RandomizedSearchCV(clf, params, cv=5, scoring='accuracy', n_iter=4)
			rand.fit(self.X, self.Y)
			print(label)
			print("\n")
			print(rand.best_score_)
			print(rand.best_params_)
			print("\n")

	def testGaussianNB(self):
		clf = GaussianNB()
		scores = cross_validation.cross_val_score(clf, self.X, self.Y, cv=3)
		print("Accuracy: %0.2f (+/- %0.2f) [%s]" % (scores.mean(), scores.std(), "GaussianNB"))

	def to1hot(row):
	    one_hot = np.zeros(5)
	    one_hot[row]=1.0
	    return one_hot


	def trainNerualNet(self, frameLength, hopLength):
		dataClassifier = pickle.load( open( "./pickles/FrameLength"+str(frameLength) +"_HopLength_"+str(hopLength)+".pickle", "rb" ) )

		mfcc = np.vstack(dataClassifier['mfcc']).reshape(len(dataClassifier['mfcc']),20, frameLength).astype(np.float32)
		target = np.vstack(dataframe.target)


		input_layer = tflearn.input_data(shape=[None, 20, frameLength], name='input')
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

