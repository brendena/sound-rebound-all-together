from classifyingAudio.ClassifyingOneClassSVM import ClassifyingOneClassSVM
from classifyingAudio.SvmStates import SvmStates

#'''
OC_SVM = ClassifyingOneClassSVM()
OC_SVM.createPossiblePickles()

OC_SVM.createSVM(3,{
    "params": {
        "kernel": ["linear", "poly", "rbf", "sigmoid"]
    },
    #"typeAudio":["mfcc","zcr","rms"],
    #"frame_hopLength":[[1,1]]
})
#'''


#'''Z
svm = SvmStates()
svm.load()
svm.getHighestAverage()


#'''


'''
implement wrapper for bagged classes
implement wrapper for soft voting classes
'''