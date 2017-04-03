from softVotingSvm.SoftVotingSvm import SoftVotingSvm
from SvmSingleState import SvmSingleState

classifier1 = SvmSingleState()
classifier1.params =  {
    "kernel": "rbf", #, "poly"
    "degree": 5
}
classifier1.typeAudio = "zcr"
classifier1.frame_hopLength = [2,2]
classifier1.baggedNumber = 3


classifier2 = SvmSingleState()
classifier2.params =  {
    "kernel": "rbf", #, "poly"
    "degree": 5
}
classifier2.typeAudio = "zcr"
classifier2.frame_hopLength = [1,2]
classifier2.baggedNumber = 3


dataClassifier = pickle.load( open("./pickles/FrameLength_2_HopLength_2.pickle", "rb" ) )
def getArrayOfLabelData(X, Y):
    data = {}
    for i in range(0, len(Y)):
        label = str(Y[i])
        if(label not in data):
            data[label] = [X[i]]
        else:
            data[label].append(X[i])
    return data
data = getArrayOfLabelData(dataClassifier["zcr"],dataClassifier["target"])["1"]




softVotingSvm = SoftVotingSvm([classifier1,classifier2])

def test_getNeededItems():
    softVotingSvm.getNeededItems()
    assert self.listAudioNeeded["zcr"] == [1,2]
    assert self.listAudioNeeded["mfcc"] == [2,2]

def test_predict():
    softVotingSvm.getNeededItems()
    results = softVotingSvm.predict(data)
    assert len(results) == len(softVotingSvm.listClassifiers)