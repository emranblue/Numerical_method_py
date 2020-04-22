#newton-rapson methode
from numpy import *
def f(x):
    return 0.5+0.25*x**2-x*sin(x)-0.5*cos(2*x)
def df(x):
    return 0.5*x-sin(x)-x*cos(x)+sin(2*x) 
tol=10**-5
p0=10*pi#initial guess
p=p0-f(p0)/df(p0)#newtons method iterative formula
fl=open('newton-rapson_result','w')
while abs(f(p))>tol:
    fl.write('%10.7f    %10.7f    %10.7f\n'%(p0,p,f(p)))
    p0=p
    p=p0-f(p0)/df(p0)
fl.close()
