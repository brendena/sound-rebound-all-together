from sklearn.svm import OneClassSVM
from sklearn.model_selection import KFold
import numpy as np

class BaggedSvmOneClass():

    def __init__(self, params, numberBagged):
        self.numberBagged = numberBagged
        self.listSvmClasses = []
        for i in range(0, numberBagged):
            self.listSvmClasses.append(OneClassSVM(**params))

    def fit(self, data):
        kf = KFold(self.numberBagged)
        splitAmount = int(len(data)/self.numberBagged)
        count = 0
        for train_index in range(splitAmount,len(data),splitAmount):
            if(count == self.numberBagged -1):
                self.listSvmClasses[count].fit(data[train_index:-1])
                break
            else:
                self.listSvmClasses[count].fit(data[train_index: train_index + splitAmount])
            count = count + 1
        

    def predict(self, data):
        sumList = []
        for svm in self.listSvmClasses:
            value = svm.predict(data)
            if(sumList == []):
                sumList = value 
            else:
                sumList = [x + y for x, y in zip(sumList, value)]
                sumList = np.array(sumList)

        for i in range(0, len(sumList)):
            if(sumList[i] <= 0 ):
                sumList[i] = -1
            else:
                sumList[i] = 1 

        #print("denied " + str(sumList[sumList <= 0].size))
        #print("valid " + str(sumList[sumList > 0].size))
        return sumList

