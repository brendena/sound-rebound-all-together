from classifyingAudio.softVotingSvm.SoftVotingSvm import SoftVotingSvm
from classifyingAudio.softVotingSvm.SoftVotingCollection import SoftVotingCollection
from classifyingAudio.SvmSingleState import SvmSingleState
from classifyingAudio.TrainerSvmSingleState import TrainerSvmSingleState
import librosa

Svm1 = SvmSingleState()
Svm2 = SvmSingleState()

Svm1.params = {}
Svm1.typeAudio = "mfcc"
Svm1.frame_hopLength = [2,4]
Svm1.bagged = True
Svm1.baggedNumber = 9
Svm1.label = "1"

Svm2.params = {}
Svm2.typeAudio = "zcr"
Svm2.frame_hopLength = [1,8]
Svm2.bagged = True
Svm2.baggedNumber = 9
Svm2.label = "1"

trainer = TrainerSvmSingleState()
trainer.trainSVM(Svm1)
trainer.trainSVM(Svm2)

sVoting = SoftVotingSvm([Svm1, Svm2])

sVoting = SoftVotingSvm([Svm1, Svm2])

extremeSVoting = SoftVotingCollection([sVoting,sVoting])


y0, s0 = librosa.core.load("./labels/babyCrying/babyCrying.wav",16000, mono=True,duration=1)
print(len(y0))
print(extremeSVoting.predict(y0))

