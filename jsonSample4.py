#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Josnファイルから読み出して、dict化する確認

import json
import pprint
from collections import namedtuple

with open('jsonSample.json') as f:
    df = json.load(f, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

print(json)
print("id:{} name:{}".format(df.id, df.name))
