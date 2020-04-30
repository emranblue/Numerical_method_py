#newton-rapson methode
from numpy import *
import matplotlib.pyplot as plt
plt.style.use('dark_background')
def f(x):
    return x**2-3*x
def df(x):
    return 2*x-3
a=linspace(1,6,1000)
b=array(f(a))
plt.axis('off')
plt.plot(a,b)
plt.xlim(2,5)
plt.ylim(0,6)
plt.plot([-1,8],[0,0],color='white')
plt.plot([0,0],[-7,7],color='white')     
tol=10**-5
p0=4.5#initial guess
p=p0-f(p0)/df(p0)#newtons method iterative formula
fl=open('newton-rapson_result','w')
while abs(f(p))>tol:
    plt.plot([p,p0],[0,f(p0)],color='red')
    plt.plot([p,p],[0,f(p)],color='blue')
    fl.write('%10.7f    %10.7f    %10.7f\n'%(p0,p,f(p)))
    p0=p
    p=p0-f(p0)/df(p0)
plt.savefig('newton-rapson.png')
plt.show()    
fl.close()
