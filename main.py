# -*
# - coding: utf-8 -*-
## @package Threading
#  @author  Jagoda Sokół
#  @file    main.py
#  @date    October 08, 2018
#  @brief   Threading.
#  @version 1.0.0.1
#  @details Simple class presenting Threads. 
'''
    - Every thread has its own heap (about 1MB)
    - Functions must be called implicitly under definition
'''

import time
import threading
from threading import Thread

class CalculateInBackground(Thread):

    progress = 0

    def doInBackground(self):     # run
        print "Start thread", threading.current_thread()
        self.progress = 1
        print " -> Doing"
        time.sleep(1)
        self.progress+=1
        print " -> some long"
        time.sleep(1)
        self.progress+=1
        print " -> lasting task"
        time.sleep(1)
        self.progress+=1
        print " -> and finishing"
        time.sleep(1)
        self.progress+=1
        print " -> the current"
        time.sleep(3)
        self.progress+=1
        print " -> job FINISHED."
        self.stopped = True

    def longLastingFunc(self):
        if hasattr(self,"thread"):
            if self.thread.is_alive():
                return
        self.stopped = threading.Event()
        self.thread  = threading.Thread(target=self.doInBackground)
        self.thread.deamon = True
        self.thread.start()


class CalculateData():

    x = 0
    y = 0

    ThreadBackgroundTask = None

    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
        self.ThreadBackgroundTask = CalculateInBackground()
        

    def multiply(self):
        print "Multiplying numbers",
        #time.sleep(3)
        print "RESULT", self.x * self.y
        return self.x * self.y

    def prepareData(self):
        self.ThreadBackgroundTask.longLastingFunc()

    def get_internal_progress(self):
        return self.ThreadBackgroundTask.progress

print "-"*15
print " " * 2, "threading"
print "-"*15
print "Threads:{}".format(threading.active_count())

firstData = CalculateData(10,2)
firstData.multiply()
firstData.prepareData()

time.sleep(0.1)
print "Threads:{}".format(threading.active_count())

print "Doing another work", firstData.get_internal_progress()
time.sleep(2)
print "Doing another work", firstData.get_internal_progress()
time.sleep(2)
print "Doing another work", firstData.get_internal_progress()
time.sleep(2)
print "Doing another work", firstData.get_internal_progress()

while firstData.get_internal_progress() != 6:
    print ".",
    time.sleep(1)

print "Finished", firstData.get_internal_progress()
