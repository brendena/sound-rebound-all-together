#! /usr/bin/env python
import multiprocessing
from producer import producer
from consumer import consumer
from multiprocessing import Process, Manager
#from raspberryPiInterface.index import runServer
import os, signal, subprocess, time

'''
this is the final example
of using it with my neural network.
Know all i have to do is 
save values to the class and then we can
get rolling.
'''         

'''
sharing dict
http://stackoverflow.com/questions/6832554/python-multiprocessing-how-do-i-share-a-dict-among-multiple-processes

'''
                
if __name__ == '__main__':
	
	toClassifiers = multiprocessing.Queue()
	toRaspberryPieQueue = multiprocessing.Queue()
	lock = multiprocessing.Lock()
	managedDict = Manager().dict()

	

	#process_server = Process(target=runServer, args=(managedDict,lock))
	process_producer = producer(toClassifiers, toRaspberryPieQueue)
	process_consumer = consumer( toRaspberryPieQueue, toClassifiers, managedDict, lock)

	#process_server.start()
	process_producer.start()
	process_consumer.start()

	process_producer.join()
	process_consumer.join()

	
	



