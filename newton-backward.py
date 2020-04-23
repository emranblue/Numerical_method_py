#newton-backward_difference_formula
from numpy import *
import math as mt
x=linspace(-2,2,11)
y=cos(exp(x))
with open('nbf_1.txt','w') as fl:
    for i in range(len(x)):
        fl.write('%8.4f      %8.4f\n'%(x[i],y[i]))
xp=ndarray((11,11))
xp[:,0]=y[:]
for i in range(1,11):
    for j in range(1,i+1):
        xp[i,j]=xp[i,j-1]-xp[i-1,j-1]
a=2.0000
h=0.4000
xn=int(input("point where to interpolate\n"))
u=(xn-a)/h
result=0
def coff(n):
    p=1
    for i in range(n):
        p=p*(u+i)
    return p/mt.factorial(n)
fl=open('nbf_2.txt','w')
for i in range(11):
    fl.write('%10.6f    '%(x[i]))
    for j in range(i+1):
        fl.write('%10.6f     '%(xp[i,j]))
    fl.write('\n')    
    result=result+coff(i)*xp[10,i]
fl.write('result is: %10.7f'%(result))
fl.close()    


