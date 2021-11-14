import numpy as np
import pylab
import scipy.stats as stats
import matplotlib.pyplot as plt


# measurements = np.random.normal(loc = 20, scale = 5, size=100)
# # stats.probplot(measurements, dist="norm", plot=pylab)
# stats.probplot([.01,.1,.2,.28,.8], dist="unif", plot=pylab)
# pylab.show()



def test():
    nsample = 100
    np.random.seed(7654321)
    x = stats.norm.rvs(loc=0, scale=1.5, size=(nsample//2,2)).ravel()
    res = stats.probplot(x, plot=plt)
    plt.show()