from featuresAudio.audioPickleClass import audioPickleClass
from classifyingAudio.ClassifyingTraining import ClassifyingTraining
from classifyingAudio.ClassifyingSave import ClassifyingSave
import pickle
locationOfPickleAudioClassifier = "./pickles/audioClassifier"
locationOfSVMClassifier = "./pickles/audioSVM"

APC = audioPickleClass(4,2)

'''
APC.set_HopLength_FrameLength(1,1)
APC.addLabelsToClassify()
APC.createPickle(locationOfPickleAudioClassifier)
#'''

'''
APC.set_HopLength_FrameLength(4,16)
APC.addLabelsToClassify()
APC.createPickle(locationOfSVMClassifier)
#'''



#'''
dataClassifier = pickle.load( open( locationOfPickleAudioClassifier + ".pickle", "rb" ) )
dataSVM = pickle.load( open(locationOfSVMClassifier + ".pickle", "rb" ) )
#'''

#'''
#CC = ClassifyingTraining(dataClassifier["mfcc"], dataClassifier["target"])
#CC.gridSearchCVForest()
#CC.trainNerualNet()
#CC.getArrayOfLabelData()
#CC.saveClassifier()
#CC.testSVM()
#'''

#'''
CSave = ClassifyingSave(dataClassifier["mfcc"], dataClassifier["target"])
CSave.saveClassifiers()
#CSave.setData(dataSVM["zcr"],dataSVM["target"])
#CSave.saveSVM()
#'''

print("done test 1")