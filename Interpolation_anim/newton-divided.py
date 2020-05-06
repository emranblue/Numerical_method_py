#newton-divided-difference
from numpy import *
import math as mt
x0=loadtxt('lagrange-interpolation_input.txt')
y=ndarray((6,6))
y[:,0]=x0[:,1]
x=float(input("interpolating point\n"))
for i in range(1,6):
    for j in range(6-i):
        y[j,i]=(y[j+1,i-1]-y[j,i-1])/(x0[i+j,0]-x0[j,0])
def coff(n):
    p=1
    for i in range(n):
        p*=(x-x0[i,0])
    return p
f=open('ndf_ot.txt','w')  
result=0  
for i in range(6):
    f.write('%6.3f   '%(x0[i,0]))
    for j in range(6-i):
        f.write('%7.5f    '%(y[i,j]))
    f.write('\n')
    result+=coff(i)*y[0,i]
f.write('result is: %10.7f'%(result))
f.close()        
        
        
        
                    
