#regula-falsi method
from numpy import *
import matplotlib.pyplot as plt
plt.style.use('dark_background')
def f(x):
    return x**2-3*x
exct=log(7/3)/(log(27/25))
a=1
b=5
p=b-((b-a)*f(b))/(f(b)-f(a))
tol=10**-4
d=linspace(1,5,1000)
e=array(f(d))
plt.xlim(-1,5)
plt.ylim(-5,15)
plt.plot([-1,5],[0,0],color='white')
plt.plot([0,0],[-5,15],color='white')
plt.axis('off')
plt.plot(d,e)
fl=open('regula-falsi','w')
while abs(f(p))>tol:
    plt.plot([a,b],[f(a),f(b)],color='red')
    plt.plot([p,p],[0,f(p)],color='blue')
    fl.write('%10.7f    %10.7f    %10.7f    %10.7f\n'%(a,b,p,f(p)))
    if f(p)*f(a)>0:
        a=p
    else:
        b=p
    p=b-((b-a)*f(b))/(f(b)-f(a))
plt.savefig('regula-falsi.png')
plt.show()    
fl.close()











