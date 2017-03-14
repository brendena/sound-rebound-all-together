import multiprocessing
import subprocess
class producer(multiprocessing.Process):
    def __init__(self, getQueue, setQueue):
        multiprocessing.Process.__init__(self)
        self.queueGetNotificationColor = getQueue
        self.queueSetAudio = getQueue = setQueue


        
    def run(self) :

        while(True):
            
            for i in range(2):
                print ("micArray_demp " + str(i))
                if(self.queueGetNotificationColor.empty()):
                    process = subprocess.Popen(
                        ['./micarray/build/micarray_dump', "12", "15", "40"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                else:
                    noifColor = self.queueGetNotificationColor.get()
                    process = subprocess.Popen(
                        ['./micarray/build/micarray_dump', noifColor["red"], noifColor["blue"], noifColor["green"]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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