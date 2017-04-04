from classifyingAudio.softVotingSvm.Composite import Composite
import librosa

'''*************************************************************
/   softVotingSvm allows you to have a voting system that 
/   can have multiple items that can 
*************************************************************'''

class SoftVotingSvm(Composite):
    def __init__(self, listClassifiers):
        self.listClassifiers = listClassifiers
        self.listAudioNeeded = {}
        self.audioFileRate = 16000
        self.getNeededItems()
    
    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    /   This loop through all the 
    /   classifiers and get a list of 
    /   all the values that are getNeeded
    /   so you don't have to calculate
    /   any number twice.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def getNeededItems(self):
        for classifier in self.listClassifiers:
            if(type(classifier) == SoftVotingSvm):
                classifier.getNeededItems()
            else:
                if(classifier.typeAudio not in self.listAudioNeeded):
                    self.listAudioNeeded[classifier.typeAudio] = [classifier.frame_hopLength[1]]
                else:
                    self.listAudioNeeded[classifier.typeAudio].append(classifier.frame_hopLength[1])
    
    def predictData(self,data):
        predictingData = {}
        for audioNeeded in self.listAudioNeeded:
            setAudioNeeded = list(set(self.listAudioNeeded[audioNeeded]))
            #hack for the sack of time
            if(audioNeeded == "mfcc"):
                predictingData[audioNeeded] = {}
                for numberHopes in setAudioNeeded:
                    hopLength = int(self.audioFileRate/numberHopes)
                    mfcc = librosa.feature.mfcc(y=data, sr=self.audioFileRate,hop_length=hopLength,n_mfcc=20)
                    predictingData[audioNeeded][numberHopes] = mfcc

            elif(audioNeeded == "rms"):
                predictingData[audioNeeded] = {}
                for numberHopes in setAudioNeeded:
                    hopLength = int(self.audioFileRate/numberHopes)
                    rms = librosa.feature.rmse(y=data,hop_length=hopLength)
                    predictingData[audioNeeded][numberHopes] = rms

            elif(audioNeeded == "zcr"):
                predictingData[audioNeeded] = {}
                for numberHopes in setAudioNeeded:
                    hopLength = int(self.audioFileRate/numberHopes)
                    zcr = librosa.feature.zero_crossing_rate(y=data,hop_length=hopLength)
                    predictingData[audioNeeded][numberHopes] = zcr

        self.predict(predictingData)
    def predict(self, data):
        for classifier in self.listClassifiers:
            if(type(classifier) == SoftVotingSvm):
                classifier.getNeededItems()
            else:
                #self.listObjects[classifier.typeAudio] = classifier.frame_hopLength
                
                asdf = self.segmentData(data[classifier.typeAudio][classifier.frame_hopLength[1]],classifier.frame_hopLength[0])
                #print(asdf)
                #print(len(asdf))
                print(classifier.classifier.predict(asdf)) 
                print("\n")

    def segmentData(self,data,numHopLengthPerFrame):
        allData = []
        for sectionNum in range(0,int(len(data[0])/numHopLengthPerFrame)):
                newArray = []
                for frame in data:
                    currentFrameNumber = sectionNum*numHopLengthPerFrame
                    newArray.extend((list(frame[currentFrameNumber:(sectionNum+1)*numHopLengthPerFrame])))
                allData.append(newArray)
        return allData