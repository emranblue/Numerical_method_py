#fixed point iteration method
from numpy import *
import matplotlib.pyplot as plt
plt.style.use('dark_background')
plt.axis('off')
def f(x):#defining a function
    return -2**-x+x**3-0.5*x**2+x
def g(x):
    return 2**-x-x**3+0.5*x**2
a=linspace(0,1,500)
b=array(g(a))
plt.plot(a,b)
plt.plot(a,a)   

p0=0.5#initial guess given in question
p=g(p0)#defination of fixed point
tol=10**-3#when p=g(p) that p is our answer,here tol is error level
fl=open('a3q2','w')
while abs(g(p)-p)>tol:
    plt.plot([p0,g(p0)],[g(p0),g(p0)],color='red',linewidth=0.3,marker='.')
    plt.plot([g(p0),g(p0)],[g(p0),g(p)],color='red',linewidth=0.3,marker='.')
    fl.write('%10.7f    %10.7f   %10.7f\n'%(p,g(p),f(p)))
    p0=p
    p=g(p0)
plt.savefig('fixed-point.png')
plt.show()    
fl.close()

