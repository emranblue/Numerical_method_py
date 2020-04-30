#newton-rapson methode
from numpy import *
import matplotlib.pyplot as plt
plt.style.use('dark_background')
def f(x):
    return 0.5+0.25*x**2-x*sin(x)-0.5*cos(2*x)
def df(x):
    return 0.5*x-sin(x)-x*cos(x)+sin(2*x)
a=linspace(-5,10*pi,10000)
b=array(f(a))
plt.axis('off')
plt.plot(a,b)
plt.xlim(-5,10*pi)
plt.ylim(f(-5)-10,f(10*pi)+10)
plt.plot([-5,10*pi],[0,0],color='white')
plt.plot([0,0],[-2,20],color='white')     
tol=10**-5
p0=10*pi#initial guess
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
