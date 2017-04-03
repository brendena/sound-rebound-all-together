from featuresAudio.audioPickleClass import audioPickleClass
from classifyingAudio.ClassifyingTraining import ClassifyingTraining
from classifyingAudio.ClassifyingSave import ClassifyingSave
import pickle
locationOfPickleAudioClassifier = "./pickles/audioClassifier"
locationOfSVMClassifier = "./pickles/audioSVM"

APC = audioPickleClass(4,2)

'''
APC.set_HopLength_FrameLength(2,2)
APC.addLabelsToClassify()
APC.createPickle("./pickles/testing")
#'''

'''
APC.set_HopLength_FrameLength(4,16)
APC.addLabelsToClassify()
APC.createPickle(locationOfSVMClassifier)
#'''



#'''
dataClassifier = pickle.load( open( "./pickles/FrameLength_2_HopLength_2.pickle", "rb" ) )
#dataSVM = pickle.load( open(locationOfSVMClassifier + ".pickle", "rb" ) )
print(dataClassifier["mfcc"][1])
for i in dataClassifier["mfcc"]:
    print(len(i))

#'''

'''
CC = ClassifyingTraining(dataClassifier["mfcc"], dataClassifier["target"])
#CC.gridSearchCVForest()
#CC.trainNerualNet()
#CC.getArrayOfLabelData()
CC.setData(dataSVM["rms"],dataSVM["target"])
#CC.one_class_svm()
CC.bagginSVM()
#CC.testSVM()
#'''

#'''
#CSave = ClassifyingSave(dataClassifier["mfcc"], dataClassifier["target"])
#CSave.saveClassifiers()
#CSave.setData(dataSVM["zcr"],dataSVM["target"])
#CSave.saveSVM()
#'''

print("done test 1")