
from audioPickleClass import audioPickleClass
from classifyingClass import ClassifyingClass
import pickle
'''
APC = audioPickleClass(1,2)
#print(APC.getListAudioFileWithLabels())
APC.addLabels()
APC.shuffle()
APC.createPickle("test")
#'''




data = pickle.load( open( "./test.pickle", "rb" ) )


#'''

final = []
for dataPoint in data["mfcc"]:
	asdf = []
	for i in dataPoint:
		#asdf.extend((x for sublist in i for x in sublist))
		asdf.extend((x for x in i))	
	final.append(asdf)

		

#print(len(final))
#print(len(final[0]))
#print(final[0][0])
#'''

#'''
CC = ClassifyingClass()
#CC.setData(final, data["target"])
#CC.one_class_svm()
#CC.cross_val()
#CC.getArrayOfLabelData()
CC.saveClassifier()
#CC.loadClassifier()
#'''
