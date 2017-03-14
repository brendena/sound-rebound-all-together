# How this works
So i pulled the threading queue logic from my other repository [here](https://github.com/brendena/sound-rebound-other-stuff/tree/master/thread)

## Communication Raspberry pi to Matrix Creator

#### Simple answer is to just pass it args on the construction 

`process = subprocess.Popen(['./micarray/build/micarray_dump'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)`

This sets up a script to open up a seperate process that launches the matrix creator and launches the Micarray_dump exe file.
So it sets up a pip so i could in theory talk to the Matrix Creator through the pip but that would be really hard so i 
just use the pip for communication from the Matrix Creator to Raspberry Pi

`audio, err = process.communicate()`
Grabs all the stdout values and puts it into audio and
grabs all stderr and pipes that to err

### !important
it pipes these values as buffers.   So you have to decode them to be able to use them.


## Communication Matrix Creator to Raspberry pi

#### Simple answer is stdout Stream

So i use the cout/stdout stream for sending data from the Matrix Creator to Raspberry Pi.  

Example
`std::printf("%f , ", mfcc_result);`
then
`std::cout.flush();`

So you wright to stdout and then you flush it at the end to make sure all the values get outputed.



### inspiration came from
[alexa_demo](https://github.com/matrix-io/matrix-creator-alexa-voice-demo/blob/master)