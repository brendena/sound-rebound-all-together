import time
import librosa
import multiprocessing
import pickle
import scipy
import numpy as np
import array
import subprocess

from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import OneClassSVM 
import os



class consumer(multiprocessing.Process):
    def __init__(self, getQueue, setQueue,accountPickle):
        multiprocessing.Process.__init__(self)
        self.queueGetAudio = getQueue
        self.queueSetNotificationColor = setQueue
        self.accountPickle = accountPickle
        #self.loadClassifiers()
        self.hopLength = (int(16000/16))
        self._cached_stamp = 0


    def run(self):
        self.count= 0
        print("!!!!!!!!!!!!runnning!!!!!!!!!!!!!!1")           
             if (self.queueGetAudio.empty()):
                print("the queue is empty")
                break;
                1+1
            else :
                self.loadAccountDetails()
                item = self.queueGetAudio.get()
                
                data, samplerate = self.convertAudio(item)
                

                if(svmCheck(data))
                    classifierRun(data)


                #final = []
                #for dataPoint in zcr:
                #    final.extend((x for x in dataPoint))
                    
                #self.count = self.count + 1
                #mfcc = []
                #mfcc.extend([x[0] for x in mfccs])
                
                

    def classifierRun(self):
        1+1

    def loadAccountDetails(self):
        if(self._cached_stamp != os.stat(self.accountPickle).st_mtime ):
            self._cached_stamp = os.stat(self.accountPickle).st_mtime
            self.accountDetails = pickle.load(open(self.accountPickle, "rb+"))

                

    def loadClassifiers(self):
        #hack
        data = pickle.load( open( "../audioPickleCreator/pickles/TrainedSVM.pickle", "rb" ))
        self.svm = data['svm']
        
        data = pickle.load( open( "../audioPickleCreator/pickles/TrainedClassifiers.pickle", "rb" ))
        self.classifiers = data["Random Forest"]

    def svmCheck(self, data):

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

    def convertAudio(self, item):
        '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        /  wrighting a file and then converting it
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
        #"sox -r 16000 -c 1 -e signed  -b 16 " + file + " " + output
        inputFile = item.decode("utf-8") 
        output = './recording.wav'
        #https://github.com/matrix-io/matrix-creator-quickstart/wiki/Microphone-Array-Recording-Test
        subprocess.call(["sox","-r","16000", "-c","1","-e","signed","-b","16",inputFile,output])
        #print("sox -r 16000 -c 1 -e signed -b 16 "+ inputFile + " " +output)
        return librosa.core.load(output,mono=True)