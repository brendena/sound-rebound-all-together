from classifyingAudio.ClassifyingOneClassSVM import ClassifyingOneClassSVM



OC_SVM = ClassifyingOneClassSVM()
OC_SVM.createPossiblePickles()

OC_SVM.createSVM({
    "params": {
        "kernel": ["linear", "poly", "rbf", "sigmoid", "precomputed"]
    },
    "typeAudio":["mfcc"],
    "frame_hopLength":[[1,1]]
})