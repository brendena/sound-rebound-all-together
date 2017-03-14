from sklearn import cross_validation
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import OneClassSVM 
from sklearn import cross_validation
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
import numpy as np
import pickle
from confusionPlot import ConfusionPlot
from sklearn.externals import joblib

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


'''
#/////////////////////////////////////////////////////////
#differnt type of algorithms i can UserWarning
#http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
# i can play with the distance
# dtw page
# https://pypi.python.org/pypi/fastdtw
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
        self.X = x
        self.Y = y

    def cross_val(self):
        X_train, X_test, y_train, y_test = \
            cross_validation.train_test_split(self.X, self.Y, test_size=0.2)

        self.clf3.fit(X_train,y_train)

        for clf, label in zip([self.clf1, self.clf2, self.clf3, self.eclfSoft], [self.clf1Type, self.clf2Type, self.clf3Type,"soft voiting"]):
            if(label == "KNN DTW"):
                
                1+1
            else: 
                scores = cross_validation.cross_val_score(clf, self.X, self.Y, cv=2)
                print("Accuracy: %0.2f (+/- %0.2f) [%s]" % (scores.mean(), scores.std(), label))

            plot = ConfusionPlot(self.X,self.Y).test(clf,label)
            file = "./images/"+ label+ "_" + self.file + ".png"
            plot.savefig(file)
            




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
  
        outcome = clf.predict(laughingBaby)
        print(outcome[outcome == -1].size)
        print(outcome[outcome == 1].size)
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

            #saveClassifiers[label] = clf 

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
    def loadClassifier(self):
        data = pickle.load( open( "./classifiers.pickle", "rb" ))
        print(data['svm'])
        for i in data['svm']:
            print(data['svm'][i].predict([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]))
    
        