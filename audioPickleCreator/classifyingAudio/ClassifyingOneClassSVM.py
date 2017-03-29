from featuresAudio.audioPickleClass import audioPickleClass
from classifyingAudio.BaggedSvmOneClass import BaggedSvmOneClass
from classifyingAudio.SvmStates import SvmStates
from classifyingAudio.SvmSingleState import SvmSingleState
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn import cross_validation
from sklearn.svm import OneClassSVM

import pickle
import random
import time


class ClassifyingOneClassSVM():
    def __init__(self):
        random.seed(time.time())  
        self._maxFrameLength = 1 
        self._maxHopLength = 1
        self._pickleLocation = "./pickles/"
        self.allPossibleCombinations = []
        for FrameL in range(1,self._maxHopLength + 1):
            for HopL in range(1,self._maxFrameLength + 1):
                if(self.acceptibleFrameToHopeLenght(FrameL,HopL)):
                    self.allPossibleCombinations.append([FrameL,HopL])

    def getLabelSize(self):
        data = self.loadPickle(1,1)     
        self.listLabels = self.getListLabelData(data["mfcc"],data["target"])
    
    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    /   i don't want hoplength to be larger
    /   then framelenth because then it will
    /   be longer then a second.  I also dont
    /   want the framlength not to evenly
    /   divisible by hoplength because else
    /   i loose data.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def acceptibleFrameToHopeLenght(self,frameLength, hopLength):
        
        if(hopLength % frameLength != 0 or
           hopLength < frameLength):
            return False
        else:
           return True

    def createPickleLocation(self,frameLength, hopLength): 
        return  self._pickleLocation + "FrameLength_" + str(frameLength) + "_HopLength_" + str(hopLength)
    
    def createPossiblePickles(self):
        APC = audioPickleClass()
        for pairF_H in self.allPossibleCombinations:
            APC.set_HopLength_FrameLength(pairF_H[0],pairF_H[1])
            APC.addLabelsToClassify()
            APC.createPickle(self.createPickleLocation(pairF_H[0],pairF_H[1]))

    def loadPickle(self, frameLength, hopLength):
        pickleLocation = self.createPickleLocation(frameLength, hopLength)
        return pickle.load( open( pickleLocation + ".pickle", "rb" ) )

    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    /   Classifiers:[
    /        classifier: # if prefined then it skips the rest of this stuff
    /        params: 
    /        typeAudio:
    /        FrameLength_HopLength:
    /        Bagged: true or false
    /     ]
    /
    /
    /
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def createSVM(self,numberItterations,classifiers):
        #'''
        #for classifier in classifiers:
        if('typeAudio' not in classifiers  ):
            classifiers["typeAudio"] = ["mfcc","zcr","rms"]

        if('FrameLeng_HopLength' not in classifiers):
            classifiers["frame_hopLength"] = self.allPossibleCombinations
            #if(classifer.Bagged then):
            #    classifer.classifier = False
            #if(classifer.numberOfBages):
        #'''
        '''
            loop through all these params and come up with a random pair
        '''
        svmStates = SvmStates()
        for i in range(0,numberItterations):
            svmState = SvmSingleState()
            self.getRandomSVM(classifiers,svmState)
            if(svmState.bagged == True):
                clf = BaggedSvmOneClass(svmState.params, svmState.baggedNumber)
            else:
                clf = OneClassSVM(**svmState.params)
            fullData = self.loadPickle(svmState.frame_hopLength[0], svmState.frame_hopLength[1])
            


            #get label from pickle data
            for label in self.listLabels:
                kf = KFold(n_splits=11)
                count = 0
                for train_index, test_index in kf.split(fullData[svmState.typeAudio]):
                    #split the data up
                    splitDataX = fullData[svmState.typeAudio][train_index[0]:train_index[-1]]
                    splitDataY = fullData["target"][train_index[0]:train_index[-1]]
                    #then get data divided by labels
                    trainData = self.getArrayOfLabelData(splitDataX, splitDataY)

                    clf.fit(trainData[label])
                    results = []
                    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                    /   for each label predict the best 
                    /   predict the results fro each 
                    /   label 
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
                    for labelPredict in self.listLabels:
                        outcome = clf.predict(trainData[labelPredict])
                        results.append({
                                "label":labelPredict,
                                "unvalid": outcome[outcome == -1].size,
                                "valid": outcome[outcome == 1].size
                            })



                    if( label in svmState.results):
                        svmState.results[label].append(results)
                    else:
                        svmState.results[label] = [results]

                    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                    /   i want to have a high k fold ratio
                    /   but don't want to do that many
                    /   iterations.  So i brake early
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
                    if(count >= 2):
                        break
                    else:  
                        count = count +1
                



            svmStates.states.append(svmState)
            svmStates.save(self.listLabels)
            
    
    def getRandomSVM(self,classifier,svmState):
        returnParams = {}
        for param in classifier["params"]:
            returnParams[param] = random.choice(classifier["params"][param])
        svmState.params = returnParams
        svmState.typeAudio = random.choice(classifier["typeAudio"])
        svmState.frame_hopLength = random.choice(classifier["frame_hopLength"])
        svmState.bagged = random.choice(classifier['bagged'])
        svmState.baggedNumber = random.choice(classifier["baggedNumber"])
        print(returnParams)


        
    def getArrayOfLabelData(self, X, Y):
        data = {}
        for i in range(0, len(Y)):
            label = str(Y[i])
            if(label not in data):
                data[label] = [X[i]]
            else:
                data[label].append(X[i])
        return data

    def getListLabelData(self, X, Y):
        data = []
        for i in range(0, len(Y)):
            label = str(Y[i])
            if(label not in data):
                data.extend(str(Y[i]))
        return data