from numpy import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as fn
plt.style.use('dark_background')

def f(x):
    return 2**x*sin(x)
def intigrate(a,b,h,n):
    result=(h/2)*(f(a)+f(b))
    for i in range(1,n):
        result+=h*f(a+i*h)
    return result
def romberg(a,b,order=8,n=10):
    order=int(order/2)
    x=ndarray((order,order))
    h=(b-a)/n
    for i in range(order):
        x[:,0]=intigrate(a,b,h,order)
        h/=2
    for j in range(1,order):
        for i in range(j,order):
            x[i,j]=x[i,j-1]+(x[i,j-1]-x[i-1,j-1])/(4**j-1)
    return x[order-1,order-1]
print(romberg(-2,4))
    