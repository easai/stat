import functools
import scipy.stats as stats
import scipy.special as comb

def reducetest():
    x=[9,4,16,13,5,13]
    np=10

    n = functools.reduce(lambda a,b:a+b,x)

    T = functools.reduce(lambda b,a:a+(b-np)*(b-np)/np,x)
    print(T)

    sum = 0
    np = [10]*n
    for i, item in enumerate(x):
        sum+=(item-np[i])*(item-np[i])/np[i]
    print(sum)


def chitest():
    x=[6,4,2]
    n = functools.reduce(lambda a,b:a+b, x)
    sum = 0
    np = [4]*n
    for i, item in enumerate(x):
        sum+=(item-np[i])*(item-np[i])/np[i]
    print(sum)

    f=len(x)-1
    q=stats.chi2.ppf(.95, df=f)
    print(q)

    p=1-stats.chi2.cdf(sum,df=f)
    print(p)


def die():
    x=[3,1,1,2,2,6]
    n=functools.reduce(lambda a,b:a+b, x)
    print(f"{n=}")
    Tn = 0
    np = [n/6] * n
    for i, item in enumerate(x):
        Tn += (item - np[i]) * (item - np[i]) / np[i]
    print(f"{Tn=}")
    f=len(x)-1
    print(f"{f=}")
    C = stats.chi2.ppf(.95, df=f)
    print(f"{C=}")
    p_value = 1 - stats.chi2.cdf(Tn, df=f)
    print(f"{p_value=}")


def planet():
    x=[20,30,50]
    n=functools.reduce(lambda a,b:a+b, x)
    print(f"{n=}")
    Tn = 0
    np = [10,40,50]
    for i, item in enumerate(x):
        Tn += (item - np[i]) * (item - np[i]) / np[i]
    print(f"{Tn=}")
    f=len(x)-1
    print(f"{f=}")
    C = stats.chi2.ppf(.95, df=f)
    print(f"{C=}")
    p_value = 1 - stats.chi2.cdf(Tn, df=f)
    print(f"{p_value=}")


def f_hat(theta, j, K):
    return comb.comb(K,j)*(theta**j)*((1-theta)**(K-j))


def thousand():
    x=[339,455,180,26]
    K=len(x)-1
    n=functools.reduce(lambda a,b:a+b, x)
    print(f"{n=}")
    Xn = 0
    for i, item in enumerate(x):
        Xn += (item*i)
    Tn = 0
    theta_hat = Xn/(n*K)
    print(f"{Xn=}")
    print(f"{theta_hat=}")
    for i, item in enumerate(x):
        f=f_hat(theta_hat, i, K)
        print(f"{i=} {f=}")
        Tn += ((item/n-f)*(item/n-f)/f)
    Tn *= n
    print(f"{Tn=}")
    print(f"{K=}")
    C = stats.chi2.ppf(.95, df=K-1)
    print(f"{C=}")
    p_value = 1 - stats.chi2.cdf(Tn, df=K-1)
    print(f"{p_value=}")


def ratio():
    x=[205,26,25,19]
    n=functools.reduce(lambda a,b:a+b, x)
    print(f"{n=}")
    Tn = 0
    np = [.72,.07,.12,.09]
    for i, item in enumerate(x):
        Tn += (item/n - np[i]) * (item/n - np[i]) / np[i]
    Tn *= n
    print(f"{Tn=}")
    f=len(x)-1
    print(f"{f=}")
    C = stats.chi2.ppf(.95, df=f)
    print(f"{C=}")
    p_value = 1 - stats.chi2.cdf(Tn, df=f)
    print(f"{p_value=}")

# TODO create a class for ChiSq
die()