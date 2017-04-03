from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.svm import OneClassSVM 
import pickle
import numpy as np
#import tensorflow as tf

from classifyingAudio.ClassifyingBase import ClassifyingBase

class ClassifyingSave(ClassifyingBase):
    def __init__(self,X,Y):
        ClassifyingBase.__init__(self)
        self.setData(X,Y)
        self.classifierPickleFile = "classifiers.pickle"
        self.svmPickleFile = "oneClassSVM.pickle"
        np.random.seed(123)

    def saveClassifiers(self):
        self.clf1 = RandomForestClassifier(n_estimators=122, criterion="gini")
        self.clf1Type = "Random Forest"
        self.clf1.fit(self.X,self.Y)
        #'''
        self.clf2 = GaussianNB()
        self.clf2Type = "Naiye Bayes"
        self.clf2.fit(self.X,self.Y)



    def saveSVM(self):
        saveSVM = {}
        saveSVM["svm"] = self.one_class_svm() 
        pickle.dump(saveSVM, open("./pickles/TrainedSVM.pickle", "wb"))


    def one_class_svm(self):
        #passdef
        #OneClassSvm
        arrayLabels = self.getArrayOfLabelData()
        print(len(arrayLabels))
        dictClassifiers = {}
        for label in range(1,len(arrayLabels)+1):
            clf = OneClassSVM()
            print("svm_Label_" + str(label))
            clf.fit(arrayLabels[str(label)])
            
            dictClassifiers["svm_Label_" + str(label)] = clf


        return dictClassifiers
