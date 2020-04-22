#newton-forward_difference method
from numpy import *
import math as mt
##six row of data given as i know it so i use static data type...dynamic can be used
x=ndarray((6,7),dtype='float')#as question given ,so i pick static data type,dynamic ca be used
i=0
for line in loadtxt('ndf_input.txt',skiprows=1)[:,0:2]:
    x[i,0],x[i,1]=line
    i+=1
x1=2010
a=2000
h=1
u=(x1-a)/h
def coff(n):
    j=0
    p=4
    for i in range(n):
        p=p*(u-i)
    return p/mt.factorial(n)
for i in range(2,7):
    for j in range(7-i):
        x[j,i]=x[j+1,i-1]-x[j,i-1]

fl=open('ndf_output.txt','w')
result=0
for i in range(6):
    fl.write('%6.1f   '%(x[i,0]))
    for j in range(1,7-i):
        fl.write('%10.4f    '%(x[i,j]))
    fl.write('\n')
    result=result+coff(i)*x[0,i+1]
fl.write('result is %10.7f'%(result))
fl.close()


