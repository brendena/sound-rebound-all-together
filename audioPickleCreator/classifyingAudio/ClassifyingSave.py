from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.svm import OneClassSVM 
import pickle
import numpy as np
#import tensorflow as tf

from classifyingAudio.ClassifyingBase import ClassifyingBase

class ClassifyingSave(ClassifyingBase):
    def __init__(self):
        ClassifyingBase.__init__(self)
        self.setData(X,Y)
        self.classifierPickleFile = "classifiers.pickle"
        self.svmPickleFile = "oneClassSVM.pickle"
        np.random.seed(123)

    def saveClassifiers(self):
        dataClassifier = pickle.load( open( "./pickles/FrameLength_3_HopLength_6.pickle", "rb" ) )
        self.clf1 = RandomForestClassifier(n_estimators=151, criterion="gini")
        self.clf1Type = "Random Forest"
        self.clf1.fit(dataClassifier["mfcc"],dataClassifier["target"])
        #'''
        dataClassifier = pickle.load( open( "./pickles/FrameLength_10_HopLength_10.pickle", "rb" ) )
        self.clf2 = GaussianNB()
        self.clf2Type = "Naiye Bayes"
        self.clf2.fit(dataClassifier["mfcc"],dataClassifier["target"])





