""" Fibonacci math module """
import math

def fib(a):
    """ Calculates/Prints fibonacci series """
    if a==0:
        return 1
    else:
        if a==1:
            return 1
        else:
            return fib(a-1)+fib(a-2)


def fastfib(a):
    p = (1+math.sqrt(5))*.5
    n = (1-math.sqrt(5))*.5
    res = p**a-n**a+p**(a-1)-n**(a-1)
    return res/math.sqrt(5)


if __name__=="__main__":        
    print (fib(10))
    print (fastfib(10))
