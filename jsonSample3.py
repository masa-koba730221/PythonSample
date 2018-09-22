#!/usr/bin/env python
# -*- coding: utf-8 -*-
# jsonライブラリを使用して、ObjectをJsonに変換する確認

import json
import pprint
from collections import namedtuple

class Test():
    def __init__(self):
        self.name = "あ"
        self.id = 1

a = Test()

json = json.dumps(a.__dict__)

print(json)
