#lagrange-interpolation-method
from numpy import *
x=loadtxt('lagrange-interpolation_input.txt')
a=float(input("interpolating point\n"))
n=len(x[:,0])
result=0
for i in range(n):
    coff=1
    for j in range(n):
        if i==j:
            continue
        coff*=(a-x[j,0])/(x[i,0]-x[j,0])
    result+=coff*x[i,1]
with open('lag_output.txt','w') as fl:
    fl.write('result is %10.7f'%(result))        
