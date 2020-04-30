#newton-forward_difference method
from numpy import *
import matplotlib.pyplot as plt
import math as mt
x=ndarray((19,20),dtype='float')
i=0
for line in loadtxt('ndf_input.txt'):
    x[i,0],x[i,1]=line
    i+=1
x1=27
a=8
h=1
u=(x1-a)/h
def coff(n):
    j=0
    p=1
    for i in range(n):
        p=p*(u-i)
    return p/mt.factorial(n)
for i in range(2,20):
    for j in range(20-i):
        x[j,i]=x[j+1,i-1]-x[j,i-1]

fl=open('ndf_output.txt','w')
result=0
for i in range(19):
    fl.write('%6.1f   '%(x[i,0]))
    for j in range(1,20-i):
        fl.write('%5.2f    '%(x[i,j]))
    fl.write('\n')
    result=result+coff(i)*x[0,i+1]
fl.write('result is %5.2f'%(result))
print(result)
fl.close()
plt.plot(x[:,0],x[:,1])
plt.show()


