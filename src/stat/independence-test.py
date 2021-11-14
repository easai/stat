import numpy as np
import scipy.stats as stats
import math
from scipy.stats import chi2

n = np.array([[52, 98, 26],[41, 190, 62]])
n = np.array([[221, 204, 203, 174, 52],[45.4, 46.6, 42.8, 44.4, 42.2]])
n = np.array([[221, 204, 203, 174, 52],[63, 25, 25, 23, 10.3]])
a = np.zeros(len(n))
for i in range(len(n)):
    a[i]=sum(n[i])
b=np.zeros(len(n[0]))
for i in range(len(n[0])):
    for j in range(len(n)):
        b[i]+=n[j,i]
print(f"{a=}")
print(f"{b=}")
total=sum(a)
t=np.zeros((len(n),len(n[0])))
for i in range(len(n)):
    for j in range(len(n[0])):
        t[i,j]=(a[i]*b[j])/total
print(f'{t=}')
d = 0
for i in range(len(n)):
    for j in range(len(n[0])):
        d+=(n[i,j]-t[i,j])*(n[i,j]-t[i,j])/t[i,j]
print(f'{d=}')
c=chi2.ppf(.95, len(n[0])-1)
print(f'{c=}')
