from scipy import stats
import numpy as np
from matplotlib import pyplot as plt

# doing 1000 times every moneth = not

# if you anre not doing, then you blond wisconsin shit

# weekly in MO for half a year = no mention

# mark shit losing D supporter = good D

x = np.linspace(-5, 5, 100)
pdf_norm1 = stats.norm.cdf(x, loc=0, scale=1)
plt.plot(x, pdf_norm1, 'r')
plt.show()