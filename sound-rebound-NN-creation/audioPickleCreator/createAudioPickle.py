import sys

from audioPickleClass import audioPickleClass


'''
set the file name and
stops the program if it is not set
'''
FilePickle = ""
try:
    if(len(sys.argv) >= 2):
        FilePickle = sys.argv[1]
    else:
        raise
except : 
    print("Please specifiy the file name")
    sys.exit(2)



APC = audioPickleClass()
#APC.addMusic("./babyCrying.wav", 0)
#APC.addMusic("./babylaughing.wav", 1)
#APC.shuffle()
APC.addMusic("./babyCrying2.wav", 1)
print("making pickle \n") 
APC.createPickle(FilePickle)





