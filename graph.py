#!/usr/bin/env python
# -*- coding: utf-8 -*-
# グラフ表示のサンプル

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.legend()
plt.show()