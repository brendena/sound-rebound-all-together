import numpy as np
from sklearn.model_selection import KFold

X = ["a", "b", "c", "d","e", "f", "g", "h"]
kf = KFold(n_splits=3)
for train, test in kf.split(X):
    print("%s %s" % (train, test))