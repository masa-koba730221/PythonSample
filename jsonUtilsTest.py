#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JsonUtils classのテスト

import json
import pprint
from Tools.jsonUtils import JsonUtils

class Test():
    def __init__(self):
        self.name = "A"
        self.id = 1

s = r'{"name": "abc", "id": 3}'
testObj = Test()

obj = JsonUtils.FromJson(Test(), s)

print("Json Str1 = {}".format(JsonUtils.ToJson(testObj)))

print("id:{} name:{}".format(obj.id, obj.name))

print("Json Str2 = {}".format(JsonUtils.ToJson(obj)))

JsonUtils.ToJsonFile(obj, "result.json")

obj2 = JsonUtils.FromJsonFile(Test(), "result.json")
print("Json Str3 = {}".format(JsonUtils.ToJson(obj2)))
