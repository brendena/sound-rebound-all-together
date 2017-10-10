# sound-rebound-all-together

![image of the final device](https://github.com/brendena/sound-rebound-all-together/blob/master/Images/RaspberryPi1.PNG?raw=true)

sound-rebound-all-together is a combination of lots of smaller projects put together.

[sound-rebound-NN-creation](https://github.com/brendena/sound-rebound-NN-creation)

[sound-rebound-matrix-creator](https://github.com/brendena/sound-rebound-matrix-creator)

[sound-rebound-other-stuff](https://github.com/brendena/sound-rebound-other-stuff)

Each part had a destinct function that I grouped together at the end.

## Goal

The goal was to create a system that would listen for specific sounds and alert the user when that sound happend.  I accomplished this using a array of machine learning techniques (see diagram bellow).  I trained a bagged SVM hard voting classifier for each sound and if any of them returned true then i converted the audio to MFCC signal and pushed it to a soft voting ensemble.  If the end result had a high enough probability of being true then i alerted the user.

![diagram of machine learning](https://github.com/brendena/sound-rebound-all-together/blob/master/Images/DesignDiagram.PNG?raw=true)

The project had a front end ui to configure the types of sounds the user wanted to be notified about.  Which was synced with a firebaseDB which would push the setting to the raspberry pi.  The raspberry pi also had its own web ui interface to set up the initial  setup.  The audio was grabbed by a mic array devices called the "Matrix Creator".  It grabbed the audio and pushed it to a Python Pipe ever second.  Every Second another process would check to see if there was information on the pipe and pop it off and analyse it.  If a match was found it would then push the notification to Firebase which would then send a notification to the user.

![How it worked](https://github.com/brendena/sound-rebound-all-together/blob/master/Images/SoundReboundProject.PNG?raw=true)

![image of device](https://github.com/brendena/sound-rebound-all-together/blob/master/Images/RaspberryPi2.PNG?raw=true)



