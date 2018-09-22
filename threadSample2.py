#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Threadライブラリをそのまま使う場合の確認
# ＊　現時点では、C#やJavaのように無名関数でインラインするのはできないように思われる。

import threading
import time

def func():
    count = 0
    while count<10:
        time.sleep(1)
        print("count {}".format(count))
        count+=1

if __name__ == '__main__':
    count = 0
    t1 = threading.Thread(target=func())
    t1.start()
    t1.join()
    print ("end")
