import multiprocessing
import subprocess
class producer(multiprocessing.Process):
    def __init__(self, getQueue, setQueue):
        multiprocessing.Process.__init__(self)
        self.queueGetNotificationColor = getQueue
        self.queueSetAudio = getQueue = setQueue


        
    def run(self) :

        while(True):
            numberOfSeconds = 1
            for itteration in range(10):
                #print ("micArray_demp " + str(itteration))
                if(self.queueGetNotificationColor.empty()):
                    process = subprocess.Popen(
                        ['./micarray/build/micarray_dump',str(itteration), str(numberOfSeconds), "0", "0", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                else:
                    notifyColors = self.queueGetNotificationColor.get()
                    print(notifyColors)
                    process = subprocess.Popen(
                        ['./micarray/build/micarray_dump', str(itteration), str(numberOfSeconds), notifyColors["red"], notifyColors["blue"], notifyColors["green"]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                audio, err = process.communicate()
                
                '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                / converts the string of mfcc 
                / values to a list of mfcc values
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

                
                #print(audio)
                #convert = audio.decode("utf-8") 
                #convert = eval(''.join(['[',   convert, ']']))
                self.queueSetAudio.put(audio)
            break;