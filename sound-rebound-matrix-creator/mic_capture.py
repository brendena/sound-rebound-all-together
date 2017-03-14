#! /usr/bin/env python


import multiprocessing
from producer import producer
from consumer import consumer


'''
this is the final example
of using it with my neural network.
Know all i have to do is 
save values to the class and then we can
get rolling.
'''         


                
if __name__ == '__main__':
    toClassifiers = multiprocessing.Queue()
    toRaspberryPieQueue = multiprocessing.Queue()
    process_producer = producer(toClassifiers, toRaspberryPieQueue)
    process_consumer = consumer( toRaspberryPieQueue, toClassifiers)
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    process_consumer.join()

