#!/usr/bin/env python
# -*- coding: utf-8 -*-
# jsonライブラリを使用し、dicとして使用する場合の確認

import json
import pprint

s = r'{"C": "\u3042", "A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}]}'

print(s)
# {"C": "\u3042", "A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}]}

d = json.loads(s)

pprint.pprint(d, width=40)
# {'A': {'i': 1, 'j': 2},
#  'B': [{'X': 1, 'Y': 10},
#        {'X': 2, 'Y': 20}],
#  'C': 'あ'}

print(type(d))
# <class 'dict'>

print(d["C"])
print("B[0].X = {}".format(d["B"][0]["X"]))