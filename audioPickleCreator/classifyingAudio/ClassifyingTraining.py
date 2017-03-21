from sklearn import cross_validation
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.svm import OneClassSVM 
from sklearn.grid_search import RandomizedSearchCV
from sklearn import metrics
from sklearn import model_selection

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

	def gridSearchCV_SVM(self):
		pass
		'''
		data = pickle.load( open( "./classifiers.pickle", "rb" ))
		allData = self.getArrayOfLabelData()
		for i in data['svm']:
			print("!!!!!!!!!!!!!!!!!!11")
			print(i);

		for test in allData:
			outcome = data['svm'][i].predict(allData[test])
			print("\n")
			print("label " + str(test))
			print("denied " + str(outcome[outcome == -1].size))
			print("valid " + str(outcome[outcome == 1].size))
		'''
	def one_class_svm(self):
		#passdef
		#OneClassSvm
		arrayLabels = self.getArrayOfLabelData()
		print(len(arrayLabels))
		dictClassifiers = {}
		for label in range(0,len(arrayLabels)):
			clf = OneClassSVM()
			clf.fit(arrayLabels[str(label+1)])
			dictClassifiers["svm_Label_" + str(label+1)] = clf


		return dictClassifiers

        
	def trainNerualNet(self):
		x_train, x_test, y_train, y_test = model_selection.train_test_split(self.X, self.Y, 
																		test_size=0.2, random_state=42)


		feature_columns = tf.contrib.learn.infer_real_valued_columns_from_input(self.X)
		classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns, hidden_units=[20,40,20],n_classes=5, model_dir= self.tfFiles)

		classifier.fit(x_train, y_train, steps=800)
		predictions = list(classifier.predict(x_test, as_iterable=True))
		score = metrics.accuracy_score(y_test, predictions)
		print('Accuracy: {0:f}'.format(score))

		print("\n\n\n\n\n")

		new_classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns, hidden_units=[20,40,20],n_classes=5,model_dir= self.tfFiles)
		predictions = list(new_classifier.predict(x_test, as_iterable=True))
		score = metrics.accuracy_score(y_test, predictions)
		print('Accuracy: {0:f}'.format(score))








	
	
