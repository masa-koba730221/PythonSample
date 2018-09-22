#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1分待ち

import datetime
import threading
import time

class TestThread(threading.Thread):
    '''
    テスト用クラス
    '''
    def __init__(self, expect):
        """ コンストラクタ 'expect'終了時間
        'expect'の時間になったらスレッドは終了する
        """
        self.__expect__ = expect
        threading.Thread.__init__(self)
 
    def run(self):
        """ run (Override)
        Thread Run
        """
        while datetime.datetime.now()<self.__expect__:
            time.sleep(1)
            print ("sub thread : " + str(datetime.datetime.now()))
 
if __name__ == '__main__':
    now = datetime.datetime.now()
    expect = now + datetime.timedelta(minutes=1)
    t1 = TestThread(expect)
    t1.start() # Threadスタート
    t1.join() # Thread終了待ち
    print ("end")







