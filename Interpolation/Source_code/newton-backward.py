#newton-backward_difference_formula
from numpy import *
import math as mt
import matplotlib.pyplot as plt
plt.style.use('dark_background')
plt.axis('off')
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
plt.plot(x,y,marker='o')
plt.plot([-3,3],[0,0],color='white',linewidth=3)
plt.plot([0,0],[-1,1],color='white',linewidth=3)
plt.xlim(-3,3)
plt.ylim(-1,1.5)
a=2.0000
h=0.4000
def coff(n,xn):
    u=(xn-a)/h
    p=1
    for i in range(n):
        p=p*(u+i)
    return p/mt.factorial(n)
fl=open('nbf_2.txt','w')
def f(xn):
    result=0
    for i in range(11):
        fl.write('%10.6f    '%(x[i]))
        for j in range(i+1):
            fl.write('%10.6f     '%(xp[i,j]))
        fl.write('\n')    
        result=result+coff(i,xn)*xp[10,i]
    return result    
q=linspace(x[0],x[-1],1000)
w=array(f(q))
plt.plot(q,w)
fl.write('result is: %10.7f'%(w[-1]))
plt.savefig('newton-backward.png')
plt.show()
fl.close()    


