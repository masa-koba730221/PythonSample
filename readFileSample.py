#!/usr/bin/env python
# -*- coding: utf-8 -*-
# テキストファイルを行単位で読みだし表示するサンプル

def read1():
    print("Read File Type1")
    fr = open("category.txt", "rt", encoding="utf-8")
    line = fr.readline() # 1行を文字列として読み込む(改行文字も含まれる)
    while line:
        print(line, end='') # printの改行を防ぐにはend=''を追加することで防ぐことができる。
        line = fr.readline()
    fr.close()
    print("")


def read2():
    """
    close処理は自動でしてくれる。
    """
    print("Read File Type2")
    with open("category.txt", "rt", encoding="utf-8") as fr:
        line = fr.readline() # 1行を文字列として読み込む(改行文字も含まれる)
        while line:
            print(line, end='') # printの改行を防ぐにはend=''を追加することで防ぐことができる。
            line = fr.readline()


if __name__ == '__main__':
    read1()
    read2()
