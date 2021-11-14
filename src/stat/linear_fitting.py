import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

x=[45, 51, 39, 41, 52, 48, 49, 46, 43, 47]
y=[171, 178, 157, 163, 183, 172, 183, 172, 175, 173]


cov_mat=np.cov(x,y)
beta_1 =cov_mat[0,1]/cov_mat[0,0]
print(beta_1)
beta_0 = np.mean(y)-beta_1*np.mean(x)
print(beta_0)

z=[beta_0+beta_1*a for a in x]

plt.plot(x,z)
plt.scatter(x,y)
plt.show()
