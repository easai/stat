import numpy as np
import matplotlib.pyplot as plt
x = np.random.uniform(0,1,5) # theoretical samples from uniform distribution [0,1]
y = [0.01, 0.1, 0.2, 0.28, 0.8]
plt.figure()
plt.scatter(np.sort(x), np.sort(y))
plt.scatter(np.linspace(0, 1, 100), np.linspace(0, 1, 100), s=1) # y=x
plt.show()