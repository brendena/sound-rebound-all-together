from sklearn import cross_validation
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import OneClassSVM 
from sklearn import cross_validation
from sklearn.grid_search import RandomizedSearchCV
from scipy.spatial.distance import euclidean

from fastdtw import fastdtw
import numpy as np
import pickle
from confusionPlot import ConfusionPlot
from sklearn.externals import joblib

#import tensorflow as tf
from sklearn import metrics
from sklearn import model_selection


'''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    ToDo next
        See if i can save the models for RandomForestClassifier random
        the others

        be able to give a small chunk of the data to knn model.


        eval the modal
    http://scikit-learn.org/stable/modules/model_evaluation.html
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''


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

class ClassifyingClass:
    def __init__(self, file="none"):
        self.file=file
        np.random.seed(123)
        self.clf1 = RandomForestClassifier()
        self.clf1Type = "Random Forest"
        self.clf2 = GaussianNB()
        self.clf2Type = "Naiye Bayes"                                         
        self.clf3 = KNeighborsClassifier(n_neighbors=3, metric=lambda x,y: fastdtw(x, y, dist=euclidean)[0]) #[0] grabs just the distance
        self.clf3Type = "KNN DTW"
        self.eclfSoft = VotingClassifier(estimators=[('rf', self.clf1), ('gnb', self.clf2), ('knn', self.clf3)], voting='soft')
        self.eclSoftType = "soft voting"
        
        

    def setData(self, x,y):
        self.X = np.asarray(x)
        self.Y = np.asarray(y)

    def cross_val(self):
        '''
        for clf, label in zip([self.clf1, self.clf2, self.clf3, self.eclfSoft], [self.clf1Type, self.clf2Type, self.clf3Type,self.eclSoftType]):
            if(label == "KNN DTW"):
                
                1+1
            else: 
                scores = cross_validation.cross_val_score(clf, self.X, self.Y, cv=2)
                print("Accuracy: %0.2f (+/- %0.2f) [%s]" % (scores.mean(), scores.std(), label))

            plot = ConfusionPlot(self.X,self.Y).test(clf,label)
            file = "./images/"+ label+ "_" + self.file + ".png"
            plot.savefig(file)
        '''
        forst_n_estimators = range(1,200)
        forst_criterion = ['gini','entropy']
        self.clf1Params = dict(n_estimators=forst_n_estimators,criterion=forst_criterion)

        '''
        estimators
        https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/learn/python/learn
        
        https://github.com/tensorflow/tensorflow/issues/2030
        '''
        feature_columns = tf.contrib.learn.infer_real_valued_columns_from_input(self.X)
        classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns, hidden_units=[20,40,20],n_classes=5)
        # got to add all the parsm for the bellow search CV
        Params = dict(hidden_units=hidden_units)

        for clf, label, params in zip([self.clf1], [self.clf1Type],[self.clf1Params]):
            rand = RandomizedSearchCV(clf, params, cv=5, scoring='accuracy', n_iter=4)
            rand.fit(self.X, self.Y)
            print(label)
            print("\n")
            print(rand.best_score_)
            print(rand.best_params_)
            print("\n")
        



    def getArrayOfLabelData(self):
        data = {}
        for i in range(0, len(self.Y)):
            label = str(self.Y[i])
            if(label not in data):
                data[label] = [self.X[i]]
            else:
                data[label].append(self.X[i])
        return data
    ''' 
        ensmble
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
        '''
        print(len(laughingBaby))
        print(len(cryingBaby))
  
        
        '''


    def predict(self, data, all = False):
        #cross val predict
        #http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html
        if all == True:
            print(self.clf1.predict(data))
            print(self.clf1Type)
            print(self.clf2.predict(data))
            print(self.clf2Type)
            print(self.clf3.predict(data))
            print(self.clf3Type)
        print(self.eclSoft.predict(data))
        print("soft voting")

    def saveClassifier(self):

        saveClassifiers = {}
        for clf, label in zip([self.clf1, self.clf2, self.clf3, self.eclfSoft], [self.clf1Type, self.clf2Type, self.clf3Type,"soft voiting"]):
            if(label == "KNN DTW"):
                X_train, X_test, y_train, y_test = \
                cross_validation.train_test_split(self.X, self.Y, test_size=.4)
                clf.fit(X_train,y_train)
            else:
                clf.fit(self.X, self.Y)


        '''
        can i created a boosted svm
        randomTree svm.
        So it doesn't overfit
        '''

        saveClassifiers[self.clf1Type] = self.clf1
        saveClassifiers[self.clf2Type] = self.clf2
        #going to have to create these 
        # on the fly because they have knn
        #saveClassifiers[self.clf3Type] = self.clf3
        #saveClassifiers[self.eclSoftType] = self.eclfSoft
        
        saveClassifiers["svm"] = self.one_class_svm();
        #joblib.dump(saveClassifiers, "classifiers.pkl")
        pickle.dump(saveClassifiers, open("classifiers.pickle", "wb"))

    #'''
    def testSVM(self):
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


    def trainNerualNet(self):
        x_train, x_test, y_train, y_test = model_selection.train_test_split(
                                            self.X, self.Y, test_size=0.2, random_state=42)


        feature_columns = tf.contrib.learn.infer_real_valued_columns_from_input(self.X)
        classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns, hidden_units=[20,40,20],n_classes=5, model_dir="./model")
        
        classifier.fit(x_train, y_train, steps=800)
        predictions = list(classifier.predict(x_test, as_iterable=True))
        score = metrics.accuracy_score(y_test, predictions)
        print('Accuracy: {0:f}'.format(score))
        
        print("\n\n\n\n\n")

        new_classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns, hidden_units=[20,40,20],n_classes=5,model_dir="./model")
        predictions = list(new_classifier.predict(x_test, as_iterable=True))
        score = metrics.accuracy_score(y_test, predictions)
        print('Accuracy: {0:f}'.format(score))
        