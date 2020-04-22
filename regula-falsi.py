#regula-falsi method
from numpy import *
def f(x):
    return 3**(3*x+1)-7*(5**2*x)
exct=log(7/3)/(log(27/25))
a=0
b=1#why i pick a,b values 0,1...beacuse i find this using another program. i calculate it
p=b-((b-a)*f(b))/(f(b)-f(a))
tol=10**-4
fl=open('regula-falsi','w')
while abs(f(p))>tol:
    fl.write('%10.7f    %10.7f    %10.7f    %10.7f\n'%(a,b,p,f(p)))
    if f(p)*f(a)>0:
        a=p
    else:
        b=p
    p=b-((b-a)*f(b))/(f(b)-f(a))
fl.close()

