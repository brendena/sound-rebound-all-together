import librosa
import pickle
from random import shuffle
import pandas as pd
import LabelClass
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#
#
#
#
#
#
#
#  Globals
#		- listAudioObject:
#			A audio Object is all the MFCC values,  
#			MelSpectrogram and audio data.
#			Its also the object that will 
#			be pickle for the classificatoin
#			alogrithms.
#		-labelLocations:
#			directly corisponds with the labelLocation.txt
#			its used to turn a directory into 
#			a labelNumber.
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class audioPickleClass:

	def __init__(self,numberFramePerSection=1,hopLengthPerSecond=16):
		self.listAudioObject = []
		'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''
		#   It works because of
		#	http://stackoverflow.com/questions/5514573/python-error-typeerror-module-object-is-not-callable-for-headfirst-python-co
		'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''
		self.labelClass = LabelClass.LabelClass()
		self.labelLocations = self.labelClass._getLabelLocations()
		self.numberFramePerSection = numberFramePerSection
		self.hopLengthPerSecond = hopLengthPerSecond
	


	'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''
	#~~~~~~~~~~~~~~~definition~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	#	This function allows you to add the types of 
	#   labels you want to add to listAudioObject.  for pickle
	#   latter on.
	'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''
	def addLabels(self,labels=[]):
		fileLocationsWithLabels = self.labelClass.getListAudioFileWithLabels()
		if(len(labels) != 0 ):
			for label in range(len(fileLocationsWithLabels)-1,-1,-1):
				if(fileLocationsWithLabels[i]["dir"] not in self.labelLocations):
					del fileLocationWithLabs[i]


		

		print(fileLocationsWithLabels)
		
		
		for fileLocation in fileLocationsWithLabels:
			splittingPoints = self.getLabelTextData("labels/" + fileLocation["dir"] + "/" + fileLocation["fileName"] + ".txt")
			audioFile = "labels/" + fileLocation["dir"] + "/" + fileLocation["fileName"] + ".wav"
			self.addMusic(audioFile, splittingPoints,self.labelLocations[fileLocation["dir"]])


	'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	get the label text data and convert
	it into a list of list like this
	ex.
		[
			[0.11111, 8.0000], - clipping 1
			[20.62311, 45.3434] - clippint 2
		]
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''
	def getLabelTextData(self,labelText):
		f = open(  labelText, 'r')
		splittingPoints = []

		for line in f:
				#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
				#this create a list divided by \t and then
				#converts then to ints by the map(int and
				#then converts it back to a list
				#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
				splittingPoints.append( list(map(float, line.split("\t")[0:2] )))
		f.close()
		return splittingPoints



	def addMusic(self,audioFile, labelsArray, target):
		#limit = 100 , duration=limit
		y0, sr0 = librosa.core.load(audioFile,44100, mono=True)#converts to singal to mono


		'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		/	Section - is the data point
		/	
		/	Frame - is the amount of 
		/				hopLenght you want to take
		/
		/	hopLength - is the length of 
		/					time for each mesurment.
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
		numberFramePerSection = self.numberFramePerSection
		hopLength = (int(44100/self.hopLengthPerSecond))
		print(len(y0))
		print(len(y0)/ sr0)
		for label in labelsArray:

			#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			#labels can be less then zero which will break
			# this program.this forces it to be at least zero
			#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			if(label[0] < 0):
				label[0] = 0
				



			start = round(label[0] * sr0)
			end = round(label[1] * sr0)

			
			ySample = y0[start: end]
			#data = ySample
			mfccs = librosa.feature.mfcc(y=ySample, sr=sr0,hop_length=hopLength,n_mfcc=20)
			melSpec  = librosa.feature.melspectrogram(y=ySample, sr=sr0,hop_length=hopLength,n_mels=128)
			rms = librosa.feature.rmse(y=ySample,hop_length=hopLength)
			zcr = librosa.feature.zero_crossing_rate(y=ySample,hop_length=hopLength)

			
			'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			/	numberSections forces it to only chuck up the data
			/	to the point where you have a full set.  that 
			/   whats what the int() for.
			~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
			numberSections = int(len(mfccs[0]) / numberFramePerSection)

			mfccs = self.segmentData3d(mfccs,numberFramePerSection,numberSections)
			melSpec = self.segmentData3d(melSpec,numberFramePerSection,numberSections)
			rms = self.segmentData3d(rms,numberFramePerSection,numberSections)
			zcr = self.segmentData3d(zcr,numberFramePerSection,numberSections)
			
			for i in range(0, numberSections):
				#'''
				data= []
				self.listAudioObject.append({
					'mfcc' : mfccs[i],
					'mel': melSpec[i],
					'data': data,
					'rms' : rms[i],
					'zcr' : zcr[i],
					'target': target
				})
				#'''



	'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	/	dataStartAs
	/	2d array
	/	mfccs[numberOfMFCCS] = 
	/					array[len(ySample) / hopLength]
	/
	/	DataEnds
	/	3d array
	/	allData[numberSections] = 
	/					mfccs[numberOfMFCCS] = 
	/							array[hopLength * numberFramePerSection]
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
	def segmentData3d(self,data,numberFramePerSection,numberSections):
		allData = []
		for sectionNum in range(0,numberSections):
				newArray = []
				for frame in data:
					currentFrameNumber = sectionNum*numberFramePerSection
					newArray.append((list(frame[currentFrameNumber:(sectionNum+1)*numberFramePerSection])))
				allData.append(newArray)
		#print(len(allData))
		return allData

	def segmentData2d(self,data, numberFramePerSection,numberSections):
		allData = []
		for sectionNum in range(0,numberSections):
			allData.append(list(data[sectionNum*numberFramePerSection:(sectionNum+1)*numberFramePerSection]))

		#print(len(allData))
		return allData

	def shuffle(self):
		shuffle(self.listAudioObject)

	def createPickle(self, FilePickle):
		tmpArray = {
			'mfcc' : [],
			'mel': [],
			'data': [],
			'zcr': [],
			'rms': [],
			'target': []
		}
		print("lens of list Audio Object")
		print(len(self.listAudioObject))
		for x in range(0, len(self.listAudioObject)):
			tmp = self.listAudioObject[x]
			tmpArray["mfcc"].append(tmp["mfcc"])
			tmpArray["mel"].append(tmp["mel"])
			tmpArray["data"].append(tmp["data"])
			tmpArray["zcr"].append(tmp["zcr"])
			tmpArray["rms"].append(tmp["rms"])
			tmpArray["target"].append(tmp["target"])
		pickle.dump(tmpArray, open(FilePickle + ".pickle", "wb"))
