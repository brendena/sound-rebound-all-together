from BaggedSvmOneClass import BaggedSvmOneClass
import pickle

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

def test_attributes():
    bagged = BaggedSvmOneClass({},5)

    assert hasattr(bagged, 'fit')
    assert hasattr(bagged, 'predict')
    assert hasattr(bagged, '__init__')


def test_predict_no_probability():
    bagged = BaggedSvmOneClass({},2)
    bagged.fit(data)
    results = bagged.predict(data)
    for i in results:
        assert i == -1 or i == 1
    
    assert len(data) == len(results)
    

def test_predict_has_probability():
    bagged = BaggedSvmOneClass({},2)
    bagged.fit(data)
    results = bagged.predict(data,probability=True)
    for i in results:
        assert i >= -1 and i <= 1
        
    assert len(data) == len(results)

test_predict_has_probability()