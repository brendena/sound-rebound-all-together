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






























	def bagginSVM(self):
		'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		/	http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold
		/	
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
		kf = KFold(n_splits=50)
		self.svmList = []
		arrayLabels = self.getArrayOfLabelData()
		count = 0
		#for train_index, test_index in kf.split(arrayLabels["1"]):
		splitAmount = 10
		testType = "4"
		for train_index in range(splitAmount,len(arrayLabels[testType]),splitAmount):
			X_train = np.array(arrayLabels[testType])[train_index-splitAmount: train_index]
			clf = OneClassSVM()
			clf.fit(X_train)
			string = "clf" + str(count)
			#self.svmList.append((string, clf))
			self.svmList.append(clf)

		#eclf = VotingClassifier(estimators=self.svmList, voting='hard')
		#eclf.predict(arrayLabels["1"])
		sumList = []
		for svm in self.svmList:
			value = svm.predict(arrayLabels["4"])
			if(sumList == []):
				sumList = value 
			else:
				sumList = [x + y for x, y in zip(sumList, value)]
		print(sumList)
		sumList = np.array(sumList)
		print("denied " + str(sumList[sumList < 0].size))
		print("valid " + str(sumList[sumList > 0].size))
		print("even " + str(sumList[sumList == 0].size))

		
	def one_class_svm(self):
		#passdef
		#OneClassSvm

		
		arrayLabels = self.getArrayOfLabelData()
		print(len(arrayLabels))
		dictClassifiers = {}
		for label in range(1,len(arrayLabels)+1):
			clf = OneClassSVM()
			clf.fit(arrayLabels[str(label)])
			outcome = clf.predict(arrayLabels[str(label)])
			print("\n")
			print("label " + str("1"))
			print("denied " + str(outcome[outcome == -1].size))
			print("valid " + str(outcome[outcome == 1].size))
			print("\n")
			outcome = clf.predict(arrayLabels["2"])
			print("label " + str("2"))
			print("denied " + str(outcome[outcome == -1].size))
			print("valid " + str(outcome[outcome == 1].size))
			print("\n")
			outcome = clf.predict(arrayLabels["3"])
			print("label " + str("3"))
			print("denied " + str(outcome[outcome == -1].size))
			print("valid " + str(outcome[outcome == 1].size))
			print("\n")
			outcome = clf.predict(arrayLabels["4"])
			print("label " + str("4"))
			print("denied " + str(outcome[outcome == -1].size))
			print("valid " + str(outcome[outcome == 1].size))
			dictClassifiers["svm_Label_" + str(label+1)] = clf

		return dictClassifiers

        









	
	
