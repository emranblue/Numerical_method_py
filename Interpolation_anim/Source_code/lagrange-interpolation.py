#lagrange-interpolation-method
from matplotlib.animation import FuncAnimation
from numpy import *
import matplotlib.pyplot as plt
plt.style.use('dark_background')
x=loadtxt('ndf_input.txt')
def f(a):
    result=0
    n=len(x[:,0])
    for i in range(n):
        coff=1
        for j in range(n):
            if i==j:
                continue
            coff*=(a-x[j,0])/(x[i,0]-x[j,0])
        result+=coff*x[i,1]
    return result    
a=linspace(x[0,0],x[-1,0],1000)
plt.xlim(10,20)
plt.ylim(0,800)
b=array(f(a))
plt.title('Lagrange-interpolation')
plt.xlabel('Days in April')
plt.ylabel('Number of infected per day')
plt.plot(a,b,label='interpolated data',linewidth=4,marker='.')
plt.plot(x[:,0],x[:,1],marker='o',label='Original data of Bangladesh',linewidth=3,color='red')
plt.legend()
plt.savefig('lagrange-interpolation.png')
plt.show()











    





