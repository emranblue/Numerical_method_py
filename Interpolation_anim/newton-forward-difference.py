#newton-forward_difference method
from numpy import *
import math as mt
import matplotlib.pyplot as plt
plt.style.use('dark_background')
x=ndarray((19,20),dtype='float')
i=0
for line in loadtxt('ndf_input.txt'):
    x[i,0],x[i,1]=line
    i+=1
a=8
h=1
def coff(n,x1):
    u=(x1-a)/h
    p=1
    for i in range(n):
        p=p*(u-i)
    return p/mt.factorial(n)
for i in range(2,20):
    for j in range(20-i):
        x[j,i]=x[j+1,i-1]-x[j,i-1]

fl=open('ndf_output.txt','w')
def f(x1):
    result=0
    for i in range(19):
        fl.write('%6.1f   '%(x[i,0]))
        for j in range(1,20-i):
            fl.write('%5.2f    '%(x[i,j]))
        fl.write('\n')
        result=result+coff(i,x1)*x[0,i+1]
    return result    
plt.plot(x[:,0],x[:,1],label='raw-data',linewidth=2,marker='o')
q=linspace(10,20,1000)
w=array(f(q))
plt.xlim(9,20)
plt.ylim(0,800)
plt.plot(q,w,label='interpolated',linewidth=2)
plt.title('Newton-divided_formula')
plt.legend()
plt.savefig('newton-forward.png')
plt.show()
fl.write('result is %5.2f'%(w[-1]))
fl.close()

