import functools
import operator

def sample_mean(x):
    total = functools.reduce(operator.add,x)
    # this
    # for item in x:
    #     total+=item
    ave = total/len(x)
    return ave


def sample_variance(x):
    ave = sample_mean(x)
    total = 0
    for item in x:
        total += (item-ave)*(item-ave)
    variance = total/len(x)
    return variance


def mat_add(A,B):
    try:
        C=[]
        if len(B)!=len(A):# row # comparison
            raise
        i_row = 0
        for row_A in A:
            row_B = B[i_row]
            if len(row_B)!=len(row_A):# col # comparison
                raise
            C.append(list(map(operator.add, row_A, row_B)))
            i_row += 1
        return C
    except Exception as e:
        return None

def fisher_info(mean, var):
    ele00=1/(var*var)
    ele11=1/(2*var**4)
    # print(f"[[{ele00} 0]")
    # print(f"[0 {ele11}]]")
    return [[ele00, 0],[0, ele11]]


if __name__=="__main__":
    x = [.2, -.1, -1.9, -.4, -1.8]
    # print(sample_mean(x))
    # print(sample_variance(x))
    # fisher_info(0,1)
    # print(mat_add([[1.4, 0],[0, 1.3]],[[1, 0],[0, 1]]))
    import numpy as np
    I=np.array(fisher_info(0,1))
    A=[sample_mean(x), sample_variance(x)-1]
    At=np.transpose(A)
    print(len(x)*At.dot(I).dot(A))
    print(5*(.64+.114*.228))
