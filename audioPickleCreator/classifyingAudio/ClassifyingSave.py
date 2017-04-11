from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.svm import OneClassSVM
from classifyingAudio.softVotingSvm.SoftVotingSvm import SoftVotingSvm
from classifyingAudio.softVotingSvm.SoftVotingCollection import SoftVotingCollection
from classifyingAudio.SvmSingleState import SvmSingleState
from classifyingAudio.TrainerSvmSingleState import TrainerSvmSingleState
import librosa
import pickle
import numpy as np
#import tensorflow as tf

from classifyingAudio.ClassifyingBase import ClassifyingBase

class ClassifyingSave(ClassifyingBase):
    def __init__(self):
        ClassifyingBase.__init__(self)
        np.random.seed(123)

    def saveClassifiers(self):
        
        self.clf1 = {
            "frameLength": 3,
            "hopLength": 6,
            "clf": "",
            "typeClf": "Random Forest",
            "dataNeeded": "mfcc"
        }
        
        dataClassifier = pickle.load( open( "./pickles/FrameLength_"+ str(self.clf1["frameLength"]) +
                                                       "_HopLength_"+ str(self.clf1["hopLength"]) +".pickle", "rb" ) )
        
        self.clf1["clf"] = RandomForestClassifier(n_estimators=151, criterion="gini")
        self.clf1["clf"].fit(dataClassifier["mfcc"],dataClassifier["target"])


        self.clf2 = {
            "frameLength": 10,
            "hopLength": 10,
            "clf": "",
            "typeClf": "Naiye Bayes",
            "dataNeeded": "mfcc"
        }
        dataClassifier = pickle.load( open( "./pickles/FrameLength_"+ str(self.clf2["frameLength"])+
                                                       "_HopLength_"+ str(self.clf2["hopLength"])+".pickle", "rb" ) )
        self.clf2["clf"] = GaussianNB()
        self.clf2["clf"].fit(dataClassifier["mfcc"],dataClassifier["target"])

        self.clf3 = {
            "frameLength": 10,
            "hopLength": 10,
            "clf": "",
            "typeClf": "neural net",
            "dataNeeded": "mfcc"
        }

        pickle.dump({"clf1": self.clf1,
                     "clf2": self.clf2,
                     "clf3": self.clf3},
                      open("./savedClassifier" + ".pickle", "wb+"))

    def saveSVM(self):
        Svm1_1 = SvmSingleState()
        Svm1_2 = SvmSingleState()
        Svm2_1 = SvmSingleState()
        Svm2_2 = SvmSingleState()
        Svm3_1 = SvmSingleState()
        Svm3_2 = SvmSingleState()
        Svm4_1 = SvmSingleState()
        Svm4_2 = SvmSingleState()

        Svm1_1.params = {'shrinking': 1, 'coef0': 3.2000000000000002, 'degree': 7, 'gamma': 9.9999999999999995e-08, 'kernel': 'rbf', 'nu': 0.5}
        Svm1_1.typeAudio = "zcr"
        Svm1_1.frame_hopLength = [6, 12]
        Svm1_1.bagged = True
        Svm1_1.baggedNumber = 3
        Svm1_1.label = "1"

        Svm1_2.params = {'shrinking': 0, 'coef0': 4.6000000000000005, 'degree': 9, 'gamma': 9.9999999999999995e-07, 'kernel': 'sigmoid', 'nu': 0.5}
        Svm1_2.typeAudio = "rms"
        Svm1_2.frame_hopLength = [10, 10]
        Svm1_2.bagged = True
        Svm1_2.baggedNumber = 9
        Svm1_2.label = "1"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Svm2_1.params = {'shrinking': 1, 'coef0': 3.2000000000000002, 'degree': 7, 'gamma': 9.9999999999999995e-08, 'kernel': 'rbf', 'nu': 0.5}
        Svm2_1.typeAudio = "zcr"
        Svm2_1.frame_hopLength = [2, 10]
        Svm2_1.bagged = True
        Svm2_1.baggedNumber = 3
        Svm2_1.label = "2"

        Svm2_2.params = {'shrinking': 1, 'coef0': 9.5, 'degree': 4, 'gamma': 9.9999999999999995e-07, 'kernel': 'rbf', 'nu': 0.7}
        Svm2_2.typeAudio = "rms"
        Svm2_2.frame_hopLength = [7, 7]
        Svm2_2.bagged = True
        Svm2_2.baggedNumber = 7
        Svm2_2.label = "2"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Svm3_1.params = {'shrinking': 0, 'coef0': 2.0, 'degree': 2, 'gamma': 0.0001, 'kernel': 'sigmoid', 'nu': 0.1}
        Svm3_1.typeAudio = "zcr"
        Svm3_1.frame_hopLength = [4, 8]
        Svm3_1.bagged = True
        Svm3_1.baggedNumber = 5
        Svm3_1.label = "3"

        Svm3_2.params = {'shrinking': 1, 'coef0': 3.3000000000000003, 'degree': 9, 'gamma': 100.0, 'kernel': 'rbf', 'nu': 0.2}
        Svm3_2.typeAudio = "rms"
        Svm3_2.frame_hopLength = [1, 3]
        Svm3_2.bagged = True
        Svm3_2.baggedNumber = 3
        Svm3_2.label = "3"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Svm4_1.params = {'shrinking': 1, 'coef0': 3.3000000000000003, 'degree': 4, 'gamma': 0.0001, 'kernel': 'rbf', 'nu': 0.5}
        Svm4_1.typeAudio = "zcr"
        Svm4_1.frame_hopLength = [4, 8]
        Svm4_1.bagged = True
        Svm4_1.baggedNumber = 3
        Svm4_1.label = "4"

        Svm4_2.params = {'shrinking': 0, 'coef0': 6.9000000000000004, 'degree': 6, 'gamma': 1e-08, 'kernel': 'rbf', 'nu': 0.6}
        Svm4_2.typeAudio = "rms"
        Svm4_2.frame_hopLength = [3, 9]
        Svm4_2.bagged = True
        Svm4_2.baggedNumber = 3
        Svm4_2.label = "4"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


        trainer = TrainerSvmSingleState()
        trainer.trainSVM(Svm1_1)
        trainer.trainSVM(Svm1_2)
        trainer.trainSVM(Svm2_1)
        trainer.trainSVM(Svm2_2)
        trainer.trainSVM(Svm3_1)
        trainer.trainSVM(Svm3_2)
        trainer.trainSVM(Svm4_1)
        trainer.trainSVM(Svm4_2)


        sVoting1 = SoftVotingSvm([Svm1_1, Svm1_2])
        sVoting2 = SoftVotingSvm([Svm2_1, Svm2_2])
        sVoting3 = SoftVotingSvm([Svm3_1, Svm3_2])
        sVoting4 = SoftVotingSvm([Svm4_1, Svm4_2])


        extremeSVoting = SoftVotingCollection([sVoting1,sVoting2,sVoting3,sVoting4])


        y0, s0 = librosa.core.load("./labels/babyCrying/babyCrying.wav",16000, mono=True,duration=1)
        
        print(len(y0))
        print(extremeSVoting.predict(y0))

        pickle.dump({"oneClassSVM": extremeSVoting},
                      open("./savedOneClassSVM" + ".pickle", "wb+"))







