from scipy import stats
import numpy as np
from matplotlib import pyplot as plt

data = stats.norm.rvs(size=500)
pv = stats.kstest(data, "norm")[1]
print('p-value:' + str(pv))

mu = 5
sigma2 = 3
data = stats.norm.rvs(size=500) * sigma2 + mu
pv = stats.kstest(data, stats.norm(loc=mu, scale=sigma2).cdf)[1]
print('p-value:' + str(pv))

pv = stats.kstest(data, stats.norm(loc=mu + 1, scale=sigma2).cdf)[1]
print('p-value:' + str(pv))

x = np.linspace(-5, 15, 100)
pdf_norm1 = stats.norm.pdf(x, loc=mu, scale=sigma2)
pdf_norm2 = stats.norm.pdf(x, loc=mu + 1, scale=sigma2)
plt.hist(data)
plt.plot(x, pdf_norm1, 'r')
plt.plot(x, pdf_norm2, 'k')
plt.show()