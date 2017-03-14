'''
import librosa
y, sr = librosa.load("./labels/fireAlarm/fireAlarm.wav",offset=10,duration=1, mono=True)
audio = librosa.feature.zero_crossing_rate(y=y,hop_length=(int(44100/2)))
print(audio)


y, sr = librosa.load("./labels/fingerSnapping/fingerSnapping.wav",offset=10,duration=1, mono=True)
audio = librosa.feature.zero_crossing_rate(y=y,hop_length=(int(44100/2)))
print(audio)

y, sr = librosa.load("./labels/babyLaughing/babyLaughing.wav",offset=10,duration=1, mono=True)
audio = librosa.feature.zero_crossing_rate(y=y,hop_length=(int(44100/2)))
print(audio)


y, sr = librosa.load("./labels/babyCrying/babyCrying.wav",offset=10,duration=1, mono=True)
audio = librosa.feature.zero_crossing_rate(y=y,hop_length=(int(44100/2)))
print(audio)
#'''
mfccs = [[0],[0],[0],[0],[0]]
asdf = []
asdf.extend((x[0] for x in mfccs)) 
print(asdf)