import numpy as np
import pandas as pd

data = pd.read_csv('data1.csv', header=None).to_numpy()

x = data[0]
y = data[1]
arg = np.polyfit(x, y, 3)
print(arg)
s = 0
for i in range(3, -1, -1):
    s += arg[3 - i] * (x[5] ** i)
print(s)
