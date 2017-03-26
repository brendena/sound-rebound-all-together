from sklearn import cross_validation
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.svm import OneClassSVM 

import numpy as np
import pickle

#import tensorflow as tf

'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

voiting link here
http://scikit-learn.org/stable/modules/ensemble.html
http://sebastianraschka.com/Articles/2014_ensemble_classifier.html

fastdtw
https://pypi.python.org/pypi/fastdtw


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''

#/////////////////////////////////////////////////////////
#differnt type of algorithms i can UserWarning
#http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
# i can play with the distance
# dtw page
# https://pypi.python.org/pypi/fastdtw
#
#   skflow
#       http://terrytangyuan.github.io/2016/03/14/scikit-flow-intro/
#       https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/learn/iris.py
#/////////////////////////////////////////////////////////


class ClassifyingBase:
    def __init__(self):
        np.random.seed(123)
        self.clf1 = RandomForestClassifier()
        self.clf1Type = "Random Forest"
        self.clf2 = GaussianNB()
        self.clf2Type = "Naiye Bayes"                                         
        #self.eclfSoft = VotingClassifier(estimators=[('rf', self.clf1), ('gnb', self.clf2), ('knn', self.clf3)], voting='soft')
        #self.eclSoftType = "soft voting"
        self.tfFiles = "./TensorFlowModel"



    def setData(self, x,y):
            self.X = np.asarray(x)
            self.Y = np.asarray(y)
            #self.X = np.array(x)
            #self.Y = np.array(y)
    def getArrayOfLabelData(self,type="classifier"):
        data = {}
        for i in range(0, len(self.Y)):
            label = str(self.Y[i])
            if(label not in data):
                print(label)
                data[label] = [self.X[i]]
            else:
                data[label].append(self.X[i])
        return data

    