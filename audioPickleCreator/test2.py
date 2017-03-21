from audioPickleClass import audioPickleClass
from classifyingClass import ClassifyingClass
import pandas as pd
import pickle

types = ['zcr','rms','mfcc','mel']
numberFramePerSection = [i for i in range(1,16)]
hopLength = [i for i in range(2,18,2)]
print(hopLength)


'''
So it will output all the information 
to a cvs file
I also what the confusion matrixes
that would be really cool


Maby try differnt combinations
'''

for nFrames in numberFramePerSection:
	for hLength in hopLength:
		if nFrames % hLength !=0:
			break
		#'''
		APC = audioPickleClass(nFrames,hLength)
		#print(APC.getListAudioFileWithLabels())
		APC.addLabels()
		APC.shuffle()
		APC.createPickle("test")
		#'''




		data = pickle.load( open( "./test.pickle", "rb" ) )

		for typeAudio in types:


			
			final = []
			for dataPoint in data[typeAudio]:
				asdf = []
				for i in dataPoint:
					#asdf.extend((x for sublist in i for x in sublist))
					asdf.extend((x for x in i))	
				final.append(asdf)

					

			print(len(final))
			print(len(final[0]))
			print(final[0][0])
			#'''
			fileString = typeAudio+"_"+str(nFrames)+"nFrames_"+str(hLength)+"hLength"
			
			CC = ClassifyingClass(file=fileString)
			CC.setData(final, data["target"])
			#CC.one_class_svm()
			CC.cross_val()

			'''
			put multiple files on pdf

			I've got to change the knn learn to make sure 
			it works properly
			'''
			
