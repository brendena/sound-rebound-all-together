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

