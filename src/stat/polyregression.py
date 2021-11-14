largeX = []
for i in range(10):
    x=i+1
    largeX.append([1,x,x*x])

print(largeX)

total=[]
total.append(0)
for i in range(4):
    total.append(0)
for i in range(10):
    x=i+1
    for j in range(4):
        y=j+1
        total[y]+=x**y

print(total)

def trans(x):
    nRow = len(x)
    nCol = len(x[0])
    y = []
    for i in range(nCol):
        y.append([])
    for i in range(nRow):
        for j in range(nCol):
            y[j].append(x[i][j])
    return y

print(trans(largeX))

def mult(x,y):
    nRowX = len(x)
    nColX = len(x[0])
    nRowY = len(y)
    nColY = len(y[0])
    res = []
    for i in range(nRowX):
        res.append([])
        for j in range(nColY):
            res[i].append(0)
    for row in range(nRowX):
        for col in range(nColY):
            sum = 0
            for i in range(nColX):
                sum+=x[row][i]*y[i][col]
            res[row][col]=sum
    return res

XX=mult(trans(largeX),largeX)
print(XX)

XXinv=[[83/60,-21/40,1/24],[-21/40,637/2640,-1/48],[1/24,-1/48,1/528]]
print(mult(XXinv,XX))

print(trans(largeX))
z=mult(XXinv,trans(largeX))
print(z)

y=[[1,3,5,8,11,14,18,21,25,28]]
print(trans(y))
print(mult(z,trans(y)))

