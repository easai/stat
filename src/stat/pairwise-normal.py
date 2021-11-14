import numpy as np
import scipy.stats as stats
import math

x = np.array([45, 32, 56, 49, 45, 38, 47, 51, 42, 38])
y = np.array([47, 34, 52, 51, 48, 44, 45, 56, 46, 44])
d = y - x
print(f"{d=}")
print(f"{np.mean(d)=}")
m=np.mean(d)
n = 10
v = np.var(d,ddof=1)
print(f"{math.sqrt(v)=}")
t =  m/ math.sqrt(v/n)
print(f"{t=}")
