import pickle
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
singleStates.results[numberLables] =
	[
		[numberofIterations] = [
			valid:
			denied:
			label
		]
	]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

class SvmStates():
    def __init__(self):
        self.states = []
        self.labels = []
        self.largestValue = {}


    def save(self, labels):
        pickle.dump({"states":self.states,"labels":labels},open("./pickles/svm.pickle", "wb+"))

    def load(self):
        data =  pickle.load(open("./pickles/svm.pickle", "rb+" ))
        self.states = data["states"]
        self.labels = data["labels"]

    def getHighestAverage(self):
     
        for singleStates in self.states:
            #print(len(singleStates.results))
            finalResults = {}
            for i in self.labels:
                finalResults[i] = self.caluculateAverage(singleStates.results[i], i )

            singleStates.finalResults = finalResults
        self.findHighestValue()

    def findHighestValue(self):
        #print(self.states[0].finalResults["label"].finalScore)

        for resultsLabel in self.states[0].finalResults:
            self.largestValue[self.states[0].finalResults[resultsLabel]['label']] = self.states[0]

        
        for i in range(0, len(self.states)):
            for label in self.labels:
  
                if(self.largestValue[label].finalResults[label]['finalScore'] < self.states[i].finalResults[label]['finalScore']):
                    self.largestValue[label] = self.states[i]

        for value in self.largestValue:
            print(value)
            print(self.largestValue[value].finalResults[value]['finalScore'])
            print(self.largestValue[value].params)
            print(self.largestValue[value].typeAudio)
            print(self.largestValue[value].frame_hopLength)


    def caluculateAverage(self, results,trainedLabel): 
        valid = 0
        unvalid = 0

        validLabel = 0
        unvalidLabel = 0
        '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        /   looping through each kfold iteration
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
        for i in range(0,len(results)):
            '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            /   looping though each prediction
            /   on each specific labels
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
            for j in range(0,len(results[i])):
                if(trainedLabel == str(results[i][j]['label'])):
                    validLabel = results[i][j]['valid']
                    unvalidLabel = results[i][j]['unvalid']
                else:
                    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                    /   valid becomes un valid because
                    /   they weren't supposed to be
                    /   correct.
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
                    unvalid = unvalid + results[i][j]['valid']
                    valid = valid + results[i][j]["unvalid"]
                
        total = valid + unvalid
        totalLabel = validLabel + unvalidLabel

        valid = valid/total
        unvalid = unvalid/total
        validTrainedLabel = validLabel/totalLabel
        unvalidTrainedLabel = unvalidLabel/totalLabel

        finalScore = (valid  + validTrainedLabel) / 2

        #print("valid " + str(valid))
        #print("unvalid " + str(unvalid))

        #print("validTrainedLabel " + str(validTrainedLabel))
        #print("unvalidTrainedLabel " + str(unvalidTrainedLabel))


        return {
            "valid" : valid,
            "unvalid" : unvalid,
            'validTrainedLabel' :validTrainedLabel,
            'unvalidTrainedLabel' : unvalidTrainedLabel,
            'finalScore' : finalScore,
            'label' : trainedLabel
        }


    		


    