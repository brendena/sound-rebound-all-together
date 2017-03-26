from featuresAudio.audioPickleClass import audioPickleClass
from sklearn.model_selection import cross_val_score



class ClassifyingOneClassSVM():
    def __init__(self):
        self._maxHopLength = 16
        self._maxFrameLength = 16
        self._pickleLocation = "./pickles/"
        self.allPossibleCombinations = []
        for FrameL in range(1,self._maxHopLength + 1):
            for HopL in range(1,self._maxFrameLength + 1):
                if(self.acceptibleFrameToHopeLenght(FrameL,HopL)):
                    self.allPossibleCombinations.append([FrameL,HopL])
        
    
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
        return  self._pickleLocation + "FrameLength_" + str(frameLength) + "_HopLength_" + str(hopLength) + ".pickle"
    
    def createPossiblePickles(self):
        APC = audioPickleClass()
        for pairF_H in self.allPossibleCombinations:
            APC.set_HopLength_FrameLength(pairF_H[0],pairF_H[1])
            APC.addLabelsToClassify()
            APC.createPickle(self.createPickleLocation(pairF_H[0],pairF_H[1]))

    def loadPickle(self, frameLength, hopLength):
        pickleLocation = self.createPickleLocation(frameLength, hopLength)
        return pickle.load( open( locationOfpickleLocationPickleAudioClassifier, "rb" ) )

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
    def createSVM(self,classifiers):
        '''
        for classifier in classifiers:
            if(clasifier.typeAudio != )
                typeAudio = 

            if(classifier.FrameLeng_HopLength):
                FrameLEngth_HopLength = self.allPossibleCombinations
            if(classifer.Bagged then):
                classifer.classifier =
        '''
        '''
            loop through all these params and come up with a random pair
        '''
        
        
       
        for i in range(0,1):
            params = getRandomSVM(classifiers)
            clf = OneClassSVM(params.params)
            data = loadPickle(params.frame_hopLength[0], params.frame_hopLength[1])
            data2 = self.getArrayOfLabelData(data[params.typeAudio])
            clf.train(data2["1"])




        '''
        i think i'm going to have to use kfold because i can
        use this kind of method becaseu
        '''
        #scores = cross_val_score(clf, data, iris.target, cv=5)
    
    def getRandomSVM(classifier):
        returnParams = {}
        for param in classifier.params:
            returnParams[param] = random.choice(classifier.params[param])

        return{
            "params": returnParams,
            "typeAudio": random.choice(classifier.typeAudio),
            "frame_hopLength": random.choice(classifier.frame_hopLength)   
        }

        
    def getArrayOfLabelData(self):
        data = {}
        for i in range(0, len(self.Y)):
            label = str(self.Y[i])
            if(label not in data):
                print(label)
                data[label] = [self.X[i]]
            else:
                data[label].append(self.X[i])
        return data