# coding: UTF-8

print("こんにちは")

msg = "Hello"
print(msg)

sum = 10 + 45
print(sum)

amari = 10 % 3

if amari != 0:
    print("割り切れませんでした。")
    print("余りは", str(amari), "です")
else:
    print("割り切れました。")


plist = ["山田", "太郎", 12, 31, "男性"]
print ("氏名: " + plist[0] + plist[1])
print ("生年月日: " + str(plist[2]) + "/" + str(plist[3]))
print ("性別: " + plist[4])

tuple = ("A", "B", "C", "D")
print (tuple[1:3])
print (tuple[1:])
print (tuple[:2])

str1 = "ABC"
str2 = "ABC"
print (str1 == str2)
print (str1 is str2)

name1 = "Hello, Yamashita.How are you doing?"
name2 = "Hello, Yamashita.How are you doing?"
print ("name1 == name2", name1 == name2)
print ("name1 is name2", name1 is name2)

dict = {"itou":64, "yamada":75, "endou":82}
print (dict["itou"])
print (dict["yamada"])
print (dict["endou"])
print (dict.fromkeys("endou"))

fr = open("category.txt", "rt", encoding="utf-8")
line = fr.readline() # 1行を文字列として読み込む(改行文字も含まれる)
while line:
    print(line, end='') # printの改行を防ぐにはend=''を追加することで防ぐことができる。
    line = fr.readline()
fr.close
