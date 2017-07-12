# -*- coding: utf-8 -*-
## @package Threading
#  @author  Jagoda Sokół
#  @file    main.py 
#  @date    July 12, 2017 
#  @brief   Threading. 
#  @version 1.0.0.0 
#  @details The main file of dummy EA15 instrument Device Server. 
'''
    - Every thread has its own heap (about 1MB)
    - Functions must be called implicitly under definition
'''

import time

def oblicz(x,y):
    print "Method result",
    time.sleep(3)
    print x * y
    return x * y

oblicz(2, 10)
print "Thread"

