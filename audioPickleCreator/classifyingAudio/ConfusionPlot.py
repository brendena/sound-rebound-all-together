from sklearn.metrics import confusion_matrix
from sklearn import cross_validation
import matplotlib.pyplot as plt
import numpy as np
import itertools



class ConfusionPlot:
	def __init__(self,x,y):
		self.X = x
		self.Y = y

	def test(self,classifier,label):
		print(len(self.Y))
		kf = cross_validation.KFold(len(self.Y), n_folds=2)
		for train_index, test_index in kf:

			if(label == "KNN DTW"):
				#not perfect un even data
				print("!!!!!!!!!!!!!!!!!!!!!!!!!")
				X_train, X_test, y_train, y_test = \
				cross_validation.train_test_split(self.X, self.Y, test_size=.2)

			else:
				X_train, X_test = self.X[train_index[0]:train_index[-1]], self.X[test_index[0]:test_index[-1]]
				y_train, y_test = self.Y[train_index[0]:train_index[-1]], self.Y[test_index[0]:test_index[-1]]

			classifier.fit(X_train, y_train)
			cf = confusion_matrix(y_test, classifier.predict(X_test))
			alist = ["cryingBaby","laughingBaby", "fingerSnapping","fireAlarm"]
			plt.figure()
			self.plot_confusion_matrix(cf,alist,title=label)
			return plt



	def plot_confusion_matrix(self,cm, classes, 
								normalize=False,
								title='Confusion matrix',
								cmap=plt.cm.Blues):
		"""
		This function prints and plots the confusion matrix.
		Normalization can be applied by setting `normalize=True`.
		"""
		plt.imshow(cm, interpolation='nearest', cmap=cmap)
		plt.title(title)
		plt.colorbar()
		tick_marks = np.arange(len(classes))
		plt.xticks(tick_marks, classes, rotation=45)
		plt.yticks(tick_marks, classes)

		if normalize:
			cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
			print("Normalized confusion matrix")
		else:
			print('Confusion matrix, without normalization')

		print(cm)

		thresh = cm.max() / 2.
		for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
			plt.text(j, i, cm[i, j],
			horizontalalignment="center",
			color="white" if cm[i, j] > thresh else "black")

		plt.tight_layout()
		plt.ylabel('True label')
		plt.xlabel('Predicted label')

	