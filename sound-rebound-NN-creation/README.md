# sound-rebound-NN-creation #
This is all the code to construct the neural net more the raspberry pi.  This will most likely converge with [matrix-creator](https://github.com/brendena/sound-rebound-matrix-creator) latter down the road once there more intergrated.  

### Visuals
To build a graph of the neural network using TensorBoard which is a part of tensorflow.

Place this where you defined your model.  tensorboard_verbose= 3 is the highest level of visualization.

```python
model = DNN(network, tensorboard_verbose=3)
```

Run network and then type in terminal

```shell
tensorboard --logdir='/tmp/tflearn_logs'
``` 
Then it will spin up a server with the performace of the neural network.


## Resources and References

### TFLearn
This Nerual Net is going to be using a abstraction library for TensorFlow called [TFLearn](http://tflearn.org/).  It simplifies many neural nets and they have lots of [examples](http://tflearn.org/examples/).  [Place i original found TFLearn](https://pythonprogramming.net/tflearn-machine-learning-tutorial/)

### Great resource on neural nets
[click here](https://pythonprogramming.net/recurrent-neural-network-rnn-lstm-machine-learning-tutorial/)


### Install Nvidia Drivers
[look here](https://github.com/brendena/sound-rebound-matrix-creator)
