#!/usr/bin/env python
# -*- coding: utf-8 -*-
# jsonライブラリを使用し、tupleで参照するようにした例
# この場合、データ扱いで汎用オブジェクトの扱いにならないので注意が必要。

import json
import pprint
from collections import namedtuple

s = r'{"C": "\u3042", "A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}]}'

print(s)
# {"C": "\u3042", "A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}]}

x = json.loads(s, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
print(x.C, x.A.i, x.B[1].X)
