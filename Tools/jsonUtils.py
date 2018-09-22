#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Json Utility

import json
from collections import namedtuple

class JsonUtils():
    """
    Json Utilities Class
    """

    @staticmethod
    def ToJson(obj):
        """
        JSON文字列に変換する
        obj: objectを継承したclassのインスタンス
        """
        if isinstance(obj, object) == True:
            return json.dumps(obj.__dict__)
        return ""

    @staticmethod
    def ToJsonFile(obj, fileName):
        """
        JSON文字列に変換して指定
        obj: objectを継承したclassのインスタンス
        filename: 保存するファイル名
        """
        if isinstance(obj, object) != True:
            return

        with open(fileName,'w') as fw:
            json.dump(obj.__dict__, fw)
    
    @staticmethod
    def FromJson(obj, jsonStr):
        """
        Json文字列をdictに変換して指定のオブジェクトに設定して返す。
        obj: 対象オブジェクト
        jsonStr: JSON文字列
        Return obj
        """
        d = json.loads(jsonStr)
        for key in obj.__dict__.keys():
            for k in d.keys():
                if key == k:
                    obj.__dict__[key] = d[k]
                    break
        return obj

    @staticmethod
    def FromJsonFile(obj, fileName):
        """
        指定のJsonファイルを読み込み指定のオブジェクトにセットして返す
        obj: 対象オブジェクト
        fileName: Jsonファイル
        Return obj
        """
        if isinstance(obj, object) != True:
            return obj

        with open(fileName,'r') as fr:
            d = json.load(fr)
            for key in obj.__dict__.keys():
                for k in d.keys():
                    if key == k:
                        obj.__dict__[key] = d[k]
                        break
            return obj

