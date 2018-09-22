#!/usr/bin/env python
# -*- coding: utf-8 -*-
# リスト表示のサンプル

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("population.csv", encoding="utf-8")
# 増減を調べる --- (*1)
df['増減'] = df["平成28年"] - df["平成12年"]
# 並び替え --- (*2)
df = df.sort_values(by=["増減"], ascending=False)
# 上位10位を得る --- (*3)
top10 = df[0:10]
# グラフで描画 --- (*4)
top10.plot.bar(y="増減", x="都道府県")
print(top10)
plt.show()
