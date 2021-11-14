import math

from moment import Moment

import numpy as np

from scipy.stats import norm


def kstest(x):
    x.sort()
    n=len(x)
    y=[]
    for i, val in enumerate(x):
        lower=abs((i)/n-val)
        upper=abs((i+1)/n-val)
        print(f"{lower=}, {upper=}")
        y.append(max(lower,upper))

    print(f"{max(y)=}")
    Tn=math.sqrt(n)*max(y)
    print(f"{Tn=}")


def lillie(x):
    unbiased_var = np.array(x).var(ddof=1)
    unbiased_var = np.array(x).var()
    mean = Moment.moment(x, 1)
    x.sort()
    n=len(x)
    y=[]
    for i, t in enumerate(x):
        p = norm.cdf(t, loc=np.mean(x), scale=math.sqrt(np.var(x)))
        lower=abs((i)/n-p)
        upper=abs((i+1)/n-p)
        print(f"{lower=}, {upper=}")
        y.append(max(lower,upper))
        y.append(lower)

    print(f"{max(y)=}")
    Tn=math.sqrt(n)*max(y)
    print(f"{Tn=}")


if __name__ == '__main__':
    x = [.8, .7, .4, .7, .2]
    x = [.28, .2, .01, .8, .1]
    lillie(x)
    # n = len(x)
    # for i in range(1,7):
    #     moment = Moment.moment(x, i)
    #     sum = moment * n
    #     print(f"{i=} {moment=} {sum=}")
    # x=np.array(x)
    # var = x.var()
    # print(f"{var=}")
    # unbiased_var = x.var(ddof=1)
    # print(f"{unbiased_var=}")
