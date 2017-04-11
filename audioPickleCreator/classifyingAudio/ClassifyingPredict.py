import pickle
#import tflearn



class ClassifyingPredict():
	def __init__(self):
		classifiers = pickle.load(open("./savedClassifier" + ".pickle", "rb+"))
		
		


		n_nodes_hl1 = 300
		n_nodes_hl2 = 300
		n_nodes_hl3 = 300

		n_classes = 5
		batch_size = 20
		hm_epochs = 10

		input_layer = tflearn.input_data(shape=[None, 20, 10], name='input')

		dense1 = tflearn.fully_connected(input_layer, n_nodes_hl1, activation='tanh',
										regularizer='L2', weight_decay=0.001)

		dropout1 = tflearn.dropout(dense1, 0.8)
		dense2 = tflearn.fully_connected(dropout1, n_nodes_hl2, activation='tanh',
		                                 regularizer='L2', weight_decay=0.001)

		dropout2 = tflearn.dropout(dense2, 0.8)
		softmax = tflearn.fully_connected(dropout2, n_classes, activation='softmax')

		# Regression using SGD with learning rate decay and Top-3 accuracy
		sgd = tflearn.SGD(learning_rate=0.1, lr_decay=0.96, decay_step=1000)
		top_k = tflearn.metrics.Top_k(3)
		net = tflearn.regression(softmax, optimizer=sgd, metric=top_k,
		                         loss='categorical_crossentropy')

		model = tflearn.DNN(net)
		classifiers["clf3"]['clf'] = model.load('./TensorFlowModel/my_model.model')

	def predict(data):
		1+1
		