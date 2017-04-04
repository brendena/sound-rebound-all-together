from featuresAudio.audioPickleClass import audioPickleClass
from classifyingAudio.BaggedSvmOneClass import BaggedSvmOneClass
from classifyingAudio.SvmStates import SvmStates
from classifyingAudio.SvmSingleState import SvmSingleState
from sklearn.svm import OneClassSVM
import pickle

class TrainerSvmSingleState():
    def __init__(self):
        self._pickleLocation = "./pickles/"

    def trainSVM(self,svmState):
        if(svmState.bagged == True):
            svmState.classifier = BaggedSvmOneClass(svmState.params, svmState.baggedNumber)
        else:
            svmState.classifier = OneClassSVM(**svmState.params)
        dataUnorganized = self.loadPickle(svmState.frame_hopLength[0],svmState.frame_hopLength[1])
        dataOrganized = self.getArrayOfLabelData(dataUnorganized[svmState.typeAudio], dataUnorganized["target"])
        svmState.classifier.fit(dataOrganized["1"])





    def createPickleLocation(self,frameLength, hopLength): 
            return  self._pickleLocation + "FrameLength_" + str(frameLength) + "_HopLength_" + str(hopLength)
        

    def loadPickle(self, frameLength, hopLength):
        pickleLocation = self.createPickleLocation(frameLength, hopLength)
       
        return pickle.load( open( pickleLocation + ".pickle", "rb" ) )

    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    /   returns a dictionary of data 
    /   based off the label
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''' 
    def getArrayOfLabelData(self, X, Y):
        data = {}
        for i in range(0, len(Y)):
            label = str(Y[i])
            if(label not in data):
                data[label] = [X[i]]
            else:
                data[label].append(X[i])
        return data

