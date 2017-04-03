from classifyingAudio.ClassifyingOneClassSVM import ClassifyingOneClassSVM
from classifyingAudio.SvmStates import SvmStates
import numpy as np

#'''
OC_SVM = ClassifyingOneClassSVM()
OC_SVM.createPossiblePickles()
OC_SVM.getLabelSize()
#'''
#http://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html
#'''

'''
OC_SVM.createSVM(20,{
    "params": {
        "kernel": ["linear", "rbf", "sigmoid"], #, "poly"
        "degree": [i for i in range(1,10)],
        "nu": [i/10 for i in range(1,9)],
        "shrinking": [1,0],
        "gamma": np.logspace(-9, 3, 13),
        "coef0": np.arange( 0.0, 10.0+0.0, 0.1 )

        
    },
    #"typeAudio":["zcr"],
    #"frame_hopLength":[[2,2]],
    "bagged": [True],
    "baggedNumber": [i for i in range(3,10,2)]
})
#'''

'''
OC_SVM.createSVM(100,{
    "params": {
        "kernel": ["poly"],
        "degree": [i for i in range(1,10)],
        "nu": [i/10 for i in range(1,5)],
        "shrinking": [1],
        "gamma": np.logspace(-9, 3, 13)
        #"coef0"

        
    },
    #"typeAudio":["mfcc","zcr","rms"],
    "frame_hopLength":[[1,1]]
})
#'''



#'''
svm = SvmStates()
svm.load()
svm.getHighestAverage()


#'''


'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
implement wrapper for bagged classes
implement wrapper for soft voting classes

problem
SVM 
    poly - shrinking 1
There a problem with the fit function in bagged svm
Where some items don't get trained.
This is because of the way i break if there is not enough information.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''