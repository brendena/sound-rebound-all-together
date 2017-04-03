from classifyingAudio.softVotingSvm.Composite import Composite

'''*************************************************************
/   softVotingSvm allows you to have a voting system that 
/   can have multiple items that can 
*************************************************************'''

class SoftVotingSvm(Composite):
    def __init__(self, listClassifiers):
        self.listClassifiers = listClassifiers
        self.listAudioNeeded
    
    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    /   This loop through all the 
    /   classifiers and get a list of 
    /   all the values that are getNeeded
    /   so you don't have to calculate
    /   any number twice.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def getNeededItems(self):

        for classifier in listClassifiers:
            if(type(classifier) == SoftVotingSvm):
                classifier.getNeededItems()
            else:
                #self.listObjects[classifier.typeAudio] = classifier.frame_hopLength
                print(classifier.frame_hopLength)
        
        
            
    def predict(self, data):
        for classifier in listClassifiers:
            if(type(classifier) == SoftVotingSvm):
                classifier.getNeededItems()
            else:
                #self.listObjects[classifier.typeAudio] = classifier.frame_hopLength
                print(classifier.predcit(classifier.typeAudio))

            