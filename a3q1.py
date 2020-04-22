from numpy import *
def f(x):#defining function and return only
    return (1/16)*x**3-sin(x)
tol=10**-6
a=-1#choosen as we find oposite sign in the function
b=2
p=(a+b)/2
fl=open('a3q1','w')
while abs(f(p))>tol:
    fl.write('%10.7f    %10.7f    %10.7f    %10.7f\n'%(a,b,p,f(p)))
    if f(p)*f(a)>0:
        a=p
    else:
        b=p
    p=(a+b)/2
fl.close()
