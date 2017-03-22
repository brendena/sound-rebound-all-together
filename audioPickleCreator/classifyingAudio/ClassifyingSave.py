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
        '''
        self.clf2 = GaussianNB()
        self.clf2Type = "Naiye Bayes"
        self.clf2.fit(self.X,self.Y)

        #feature_columns = tf.contrib.learn.infer_real_valued_columns_from_input(self.X)
        #self.clf3 = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns, 
        #                                            hidden_units=[20,40,20],
        #                                            n_classes=5, model_dir= self.tfFiles)
        self.clf3Type = "Neural Net"

        #currently can't do soft voting for 
        #for neural net
        #so i'm going to have to hard voting in the mean time
        self.eclfSoft = VotingClassifier(estimators=[('rf', self.clf1), ('gnb', self.clf2)], voting='soft')
        self.eclSoftType = "soft voting"

        #self.eclfSoft.fit(self.X,self.Y)
        '''
        saveClassifiers = {}
        saveClassifiers[self.clf1Type] = self.clf1
        #saveClassifiers[self.clf2Type] = self.clf2
        pickle.dump(saveClassifiers, open("./pickles/TrainedClassifiers.pickle", "wb"))
        print("news stuff")

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
