import time
import soundfile as sf
import librosa
import multiprocessing
import pickle

from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import OneClassSVM 

class consumer(multiprocessing.Process):
    def __init__(self, getQueue, setQueue  ):
        multiprocessing.Process.__init__(self)
        self.queueGetAudio = getQueue
        self.queueSetNotificationColor = setQueue
        self.loadClassifiers()


    def run(self):           
        while True:
            time.sleep(1.2)
            if (self.queueGetAudio.empty()):
                print("the queue is empty")
                break;
                
            else :
                item = self.queueGetAudio.get()
                self.queueSetNotificationColor.put({'red': "34",'blue':"14", 'green':"5"})

                '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                /  sending over raw information 
                /  so that raspberry pi can do 
                /  so i can do some quick testing.
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
                rf = open('./recording.raw', 'wb')
                rf.write(item)
                rf.close()
                
                data, samplerate = sf.read("./recording.raw", channels=1, samplerate=16000,
                           subtype='FLOAT')
                #data, samplerate = librosa.core.load("./recording.wav",mono=True)
                mfccs = librosa.feature.mfcc(y=data, sr=samplerate,n_mfcc=20,hop_length=16000)
                
                asdf = []
                asdf.extend([x[0] for x in mfccs]) 
                print(asdf)
                for svmName in self.svm:
                    print(self.svm[svmName].predict([asdf]))

                

    def loadClassifiers(self):
        data = pickle.load( open( "./classifiers.pickle", "rb" ))
        self.svm = data['svm']