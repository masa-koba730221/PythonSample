#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 日付の出力サンプル

import datetime

# 現在時間
d = datetime.datetime.now()

# フォーマット
s = d.strftime("%Y/%m/%d %a %H:%M:%S.%f")

# 年を2桁
m = d.strftime("%y/%m/%d %a %H:%M:%S.%f")

# 0埋めなし
l = d.strftime('%Y/%-m/%-d %-H:%-M')

print(d)
print(s)
print(m)
print(l)
