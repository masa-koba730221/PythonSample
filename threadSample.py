#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Threadクラスを継承した場合の確認

import threading
import time

class TestThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
 
    def run(self):
        for i in range(5):
            time.sleep(1)
            print ("sub thread : " + str(i))
 
if __name__ == '__main__':
    t1 = TestThread()
    t1.start()
    t1.join()
    print ("end")
