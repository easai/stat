import numpy as np
from statistics import mean, median,variance,stdev

x=[]
x.append([-5,-10])
x.append([0,3])
x.append([2,11])
x.append([3,14])
xrow=[y[0] for y in x]
var = np.var(x, axis=0)
print(f"{var=}")
var = np.var(xrow)
print(f"{var=}")
var=variance(xrow)
print(f"{var=}")
var = np.array(xrow).var()
print(f"{var=}")
var = np.array(xrow).var()
print(f"{var=}")
xrow=np.array(xrow)
var = mean(abs(xrow - xrow.mean())**2)
cov=np.cov(x,bias=0)
print(f"{cov=}")

totalX=0
totalY=0
totalXY=0
n=len(x)
for item in x:
    totalX+=item[0]
    totalY+=item[1]
    totalXY+=item[0]*item[1]
meanX = totalX/n
meanY=totalY/n
meanXY=totalXY/n
print(f"{meanX=}")
print(f"{meanY=}")
print(f"{meanXY=}")
print(f"cov = {meanXY-meanX*meanY}")
print(np.mean(x, axis=1))
diffX=0
diffY=0
diffXY=0
for item in x:
    diffX+=(item[0]-meanX)*(item[0]-meanX)
    diffY+=(item[1]-meanY)*(item[1]-meanY)
    diffXY+=(item[0]-meanX)*(item[1]-meanY)
varX=diffX/n
varY=diffY/n
cov=diffXY/n
print(f"{varX=}")
print(f"{varY=}")
print(f"{cov=}")

a=meanY-(meanXY-meanX*meanY)/(varX)*meanX
b=(meanXY-meanX*meanY)/(varX)
print(f"{a=}")
print(f"{b=}")

import pandas as pd
df = pd.DataFrame(x)
print(df)
print(df.describe())
print(df.cov())