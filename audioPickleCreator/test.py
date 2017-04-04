from featuresAudio.audioPickleClass import audioPickleClass
from classifyingAudio.ClassifyingTraining import ClassifyingTraining
from classifyingAudio.ClassifyingSave import ClassifyingSave
import pickle
locationOfPickleAudioClassifier = "./pickles/audioClassifier"
locationOfSVMClassifier = "./pickles/audioSVM"

#'''
dataClassifier = pickle.load( open( "./pickles/FrameLength_10_HopLength_10.pickle", "rb" ) )

#'''

#'''
CC = ClassifyingTraining(dataClassifier["mfcc"], dataClassifier["target"])
#CC.gridSearchCVForest()
CC.trainNerualNet()
CC.testGaussianNB()
#CC.getArrayOfLabelData()
#'''

#'''
#CSave = ClassifyingSave()
#CSave.saveClassifiers()
#CSave.setData(dataSVM["zcr"],dataSVM["target"])
#CSave.saveSVM()
#'''

print("done test 1")