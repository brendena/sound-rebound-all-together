from sklearn.svm import OneClassSVM
from sklearn.model_selection import KFold
import numpy as np

class BaggedSvmOneClass():

    def __init__(self, params, numberBagged):
        self.numberBagged = numberBagged
        self.listSvmClasses = []
        for i in range(0, numberBagged):
            self.listSvmClasses.append(OneClassSVM(**params))


    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    /  Definition fit:
    /   this splits up all the data by the
    /   the self.numberBagged and trains
    /    a list of svm based on the above self.params 
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def fit(self, data):
        kf = KFold(self.numberBagged)
        splitAmount = int(len(data)/self.numberBagged)
        count = 0
        if(splitAmount  == 0):
            raise NameError('not enough data to bag - NumberBags ' + str(self.numberBagged) + " size Data set - " + str(len(data)))

        for train_index in range(0,len(data),splitAmount):
            if(count == self.numberBagged):
                break
            else:
                self.listSvmClasses[count].fit(data[train_index: train_index + splitAmount])
            count = count + 1

        if(count != len(self.listSvmClasses)):
            raise NameError('broke to early, not all data is fit')
    
    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    /   probability = false
    /        return [1,-1,1,-1,1]
    /   probability = True
    /       return [-.23,  .7, 1, -1, ]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

    def predict(self, data, probability=False):
        sumList = []
        for svm in self.listSvmClasses:
            value = svm.predict(data)
            if(sumList == []):
                sumList = value 
            else:
                sumList = [x + y for x, y in zip(sumList, value)]
                sumList = np.array(sumList)

        if(probability == False):
            for i in range(0, len(sumList)):
                if(sumList[i] <= 0 ):
                    sumList[i] = -1
                else:
                    sumList[i] = 1 
        else:
            for i in range(0, len(sumList)):
                sumList[i] = sumList[i]/len(sumList)
        #print("denied " + str(sumList[sumList <= 0].size))
        #print("valid " + str(sumList[sumList > 0].size))
        return sumList

