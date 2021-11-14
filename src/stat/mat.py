import numpy as np
"""
x = np.array([1,2,3])
print(np.outer(x,x))

a=np.array([8,4,7])
b=np.array([2,8,1])
c=np.array([3,1,1])
d=np.array([9,7,4])
ave = (a+b+c+d)/4
print(ave)
sum = np.outer(a,a)-np.outer(ave,ave)
sum += np.outer(b,b)-np.outer(ave,ave)
sum += np.outer(c,c)-np.outer(ave,ave)
sum += np.outer(d,d)-np.outer(ave,ave)
print(sum/4)
sum = 8*8-5.5*5.5
sum += 2*2-5.5*5.5
sum += 3*3-5.5*5.5
sum += 9*9-5.5*5.5
print(sum/4)
sum = 8*4-5.5*5
sum += 2*8-5.5*5
sum += 3*1-5.5*5
sum += 9*7-5.5*5
print(sum/4)
"""

x=np.array([1,1,1])
y=np.outer(x,x)
z=np.array([2,-1,-2])
z=np.transpose(z)

a=np.identity(3)*3-y
print(np.matmul(a,z))
print(np.matmul(np.matmul(a,a),z))
print(np.matmul(np.matmul(a,a),z)/3)

a=a
print(a)
print(np.matmul(a,a))

u=np.array([1,2])
x=np.array([1,2])
proj = np.inner(u,x)*u
print(proj)
print(proj/5)
x=np.array([3,4])
proj = np.inner(u,x)*u
print(proj)
print(proj/5)
x=np.array([-1,0])
proj = np.inner(u,x)*u
print(proj)
print(proj/5)

x=np.array([1,1,1])
y=np.outer(x,x)
a=np.identity(3)-y/3
x=np.matrix('1 2;3 4;-1 0')
print(x)
z=np.matmul(np.transpose(x),a)
z=np.matmul(z,x)
print(z)
print(z/3)


