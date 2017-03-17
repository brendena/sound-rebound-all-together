import numpy as np
import pandas as pd
import pickle


def to1hot(row):
    one_hot = np.zeros(2)
    one_hot[row]=1.0
    return one_hot







class MusicData:
	def __init__(self):

		#data = pickle.load( open( "./audioForNeuralNetwork.pickle", "rb" ) )
		dataPickle = pickle.load( open( "./test.pickle", "rb" ) )

		data = pd.DataFrame({
			'mfcc': dataPickle['mfcc'],
			'target': dataPickle['target']
		})

		data["one_hot_encoding"] = data.target.apply(to1hot)

		data["mfcc_flatten"] = data.mfcc.apply(lambda mfcc: mfcc.flatten())



		length = len(data["mfcc_flatten"])
		trainingSection = length * .20
		train_data = data[0:int(length - trainingSection)]
		test_data = data[int(length - trainingSection):]

		X = np.vstack(train_data.mfcc_flatten).reshape(train_data.shape[0],20, 87).astype(np.float32)
		Y = np.vstack(train_data["one_hot_encoding"])

		testX = np.vstack(test_data.mfcc_flatten).reshape(test_data.shape[0],20, 87).astype(np.float32)
		testY = np.vstack(test_data["one_hot_encoding"])




		self.X = X
		self.Y = Y
		self.testX = testX
		self.testY = testY
		self.myShape = [None, 20, 87] 


