from numpy import *
def f(x):#defining a function
    return -2**-x+x**3-0.5*x**2+x
def g(x):
    return 2**-x-x**3+0.5*x**2
p0=0.5#initial guess given in question
p=g(p0)#defination of fixed point
tol=10**-3#when p=g(p) that p is our answer,here tol is error level
fl=open('a3q2','w')
while abs(g(p)-p)>tol:
    fl.write('%10.7f    %10.7f   %10.7f\n'%(p,g(p),f(p)))
    p=g(p)
fl.close()

