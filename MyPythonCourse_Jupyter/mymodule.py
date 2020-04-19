# mymodule.py

import time

def say_hello(name):
    print('hello', name)

def multiprocessing_with_busy_wait(n, queue=None):
    start_time = time.perf_counter()
    count = 1
    for i in range(1, n):
        for j in range(1, n):
            count = i + j          # pointless busy work for CPU to chew on
    end_time = time.perf_counter()
    if queue is not None:
        ret = queue.get()
        ret['delta_time'] = end_time - start_time
        queue.put(ret)

def mysquare(x):
    return x*x

def average(row):
    sum = 0
    for n in row:
        sum += n
    return sum/len(row)

class QueueMessageObject(object):
    def __init__(self, value):
        self.value = value
    def display(self):
        print(self.value)
        
def worker_process(queue):
    queue.put(QueueMessageObject('This is a message sent from worker_process.'))
