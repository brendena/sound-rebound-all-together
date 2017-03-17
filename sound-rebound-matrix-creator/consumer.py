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
            time.sleep(1.5)
            #print(self.managedDict)
            if (self.queueGetAudio.empty()):
                print("the queue is empty")
                break;
                1+1
            else :
                item = self.queueGetAudio.get()
                

                '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                /  wrighting a file and then converting it
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
                #"sox -r 16000 -c 1 -e signed  -b 16 " + file + " " + output
                inputFile = item.decode("utf-8") 
                print(inputFile)
                print("output")
                output = './recording.wav'
                #https://github.com/matrix-io/matrix-creator-quickstart/wiki/Microphone-Array-Recording-Test
                subprocess.call(["sox","-r","16000", "-c","1","-e","signed","-b","16",inputFile,output])
                print("sox -r 16000 -c 1 -e signed -b 16 "+ inputFile + " " +output)


                
                data, samplerate = librosa.core.load(output,mono=True)
                mfccs = librosa.feature.mfcc(y=data, sr=samplerate,n_mfcc=20,hop_length=16000)
                

                #self.queueSetNotificationColor.put({'red': "34",'blue':"14", 'green':"5"})
                self.count = self.count + 1
                asdf = []
                asdf.extend([x[0] for x in mfccs]) 
                #print(asdf)
                for svmName in self.svm:
                    print(self.svm[svmName].predict([asdf]))


                

                

    def loadClassifiers(self):
        data = pickle.load( open( "./classifiers.pickle", "rb" ))
        self.svm = data['svm']

