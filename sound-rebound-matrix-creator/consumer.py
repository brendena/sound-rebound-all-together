import time
import librosa
import multiprocessing
import pickle
from multiprocessing import Process, Manager
import scipy
import numpy as np
import array
import subprocess

from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import OneClassSVM 

class consumer(multiprocessing.Process):
    def __init__(self, getQueue, setQueue,managedDict,lock):
        multiprocessing.Process.__init__(self)
        self.queueGetAudio = getQueue
        self.queueSetNotificationColor = setQueue
        self.managedDict = managedDict
        self.lock = lock
        self.loadClassifiers()


    def run(self):
        self.count= 0           
        while True:
            time.sleep(1.2)
            #print(self.managedDict)
            if (self.queueGetAudio.empty()):
                print("the queue is empty")
                break
                1+1
            else :
                item = self.queueGetAudio.get()
                

                '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                /  wrighting a file and then converting it
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
                #"sox -r 16000 -c 1 -e signed  -b 16 " + file + " " + output
                inputFile = item.decode("utf-8") 
                output = './recording.wav'
                #https://github.com/matrix-io/matrix-creator-quickstart/wiki/Microphone-Array-Recording-Test
                subprocess.call(["sox","-r","16000", "-c","1","-e","signed","-b","16",inputFile,output])
                #print("sox -r 16000 -c 1 -e signed -b 16 "+ inputFile + " " +output)


                
                data, samplerate = librosa.core.load(output,mono=True)
                mfccs = librosa.feature.mfcc(y=data, sr=samplerate,n_mfcc=20,hop_length=16000)

                hopLength = (int(16000/16))
                zcr = librosa.feature.zero_crossing_rate(y=data,hop_length=hopLength)

                


                final = []
                for dataPoint in zcr:
                    final.extend((x for x in dataPoint))
                    
                self.count = self.count + 1
                mfcc = []
                mfcc.extend([x[0] for x in mfccs])
                
                for i in range(0,len(final),4):
                    #hack
                    if(i == 20):
                        break
                    for svmName in self.svm:
                        prediction = self.svm[svmName].predict([final[i:i+4]])
                        #print(prediction)

                        if(prediction == 1):
                            prediction = self.classifiers.predict([mfcc])
                            print("\n predicting mffc values")
                            print(prediction)
                            self.queueSetNotificationColor.put({'red': "34",'blue':"14", 'green':"5"})
                            break
                


                

                

    def loadClassifiers(self):
        data = pickle.load( open( "../audioPickleCreator/pickles/TrainedSVM.pickle", "rb" ))
        self.svm = data['svm']

        #hack
        
        
        data = pickle.load( open( "../audioPickleCreator/pickles/TrainedClassifiers.pickle", "rb" ))
        self.classifiers = data["Random Forest"]


