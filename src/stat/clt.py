import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('mikan-all.csv')
weight_array = np.array(df['weight'])

mu = np.mean(weight_array)
print(mu)

start = 10
end = 1001
X = np.arange(start, end, 5)
Y = []

for n in range(start, end, 5):
    sample = np.random.choice(weight_array, n, replace=False) 
    x_bar = np.mean(sample)
    Y.append(x_bar)

plt.hlines(mu, start, end, "black", linestyles='dashed')

plt.plot(X, Y, color='blue')
plt.show()