#bisection method
from numpy import *
import matplotlib.pyplot as plt
plt.style.use('dark_background')
plt.axis('off')
def f(x):#defining function and return only
    return (1/16)*x**3-sin(x)
tol=10**-6
a=-1#choosen as we find oposite sign in the function
b=2
p=(a+b)/2
x=linspace(-1,2,1000)
y=array(f(x))
plt.plot(x,y)
plt.plot([-2,2.5],[0,0],color='white')
plt.plot([0,0],[-3,3],color='white')
fl=open('bisection-output','w')
while abs(f(p))>tol:
    fl.write('%10.7f    %10.7f    %10.7f    %10.7f\n'%(a,b,p,f(p)))
    plt.plot([a,a],[0,f(a)],color='blue')
    plt.plot([b,b],[0,f(b)],color='blue')
    plt.scatter(p,0)
    if f(p)*f(a)>0:
        a=p
    else:
        b=p
    p=(a+b)/2
plt.savefig('bisection-method.png')    
plt.show()    
fl.close()
