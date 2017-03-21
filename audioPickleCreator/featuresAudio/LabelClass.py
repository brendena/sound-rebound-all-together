import os
from os import listdir
import json

class LabelClass:

	def __init__(self):
		print("created LabelClass")


	'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''
	#~~~~~~~~~~~~~~~definition~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	#	grabs the elements from labelLocations
	#   and create a dictionary, out of them.
	#   This is usefull because you give this
	#   the parents directory of a audio file
	#   and it will give you a cordisponding
	#   label for it. 
	'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''
	def _getLabelLocations(self):
		labelLocationFile =  "./audioLocation.json"

		data = []
		with open(labelLocationFile) as f:
		    data = json.load(f)

		return data['labelLocation'] 


	def getCurrentDirectory(self):
		return os.path.dirname(os.path.abspath(__file__))  + "/.."


	'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''
	#~~~~~~~~~~~~~~~definition~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	#	loop through all file in the labels and is going to
	#   look for all the wave files with a corisponding
	#   label file.
	#	ex.
	#		[
	#			{"dir": "babyCrying",
	#			 "fileName": "babyCrying2" --stripped of file extensions
	#			}
	#		]
	'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''
	def getListAudioFileWithLabels(self):
		'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
		get home directoy and then labels
		directory.  Then grabs all the directores
		from it.
		%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''
		mypath = self.getCurrentDirectory()
		mypath = mypath + "/labels"

		audioFilesWithExtensions = []
		labelsDir = listdir(mypath)
		for labelDir in labelsDir:
			listFilesDir = listdir(mypath + "/" + labelDir)
			
			'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
			get the files that have a unique file name.
			By file name i mean the file name with
			a extension
			%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''
			uniqueFileName = []

			def append_IfNotIn(value, array):
				a = os.path.splitext(value)[0]

				if(a not in array):
					array.append(a)
			[append_IfNotIn(x, uniqueFileName) for x in listFilesDir]

			'''%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
			Append all the files with both
			a label and a wav files.
			%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''
			
			for fNameWE in uniqueFileName:
				if(fNameWE + ".txt" in listFilesDir):
					if(fNameWE + ".wav" in listFilesDir):
						audioFilesWithExtensions.append({"dir":labelDir, "fileName":fNameWE })
		return audioFilesWithExtensions



		