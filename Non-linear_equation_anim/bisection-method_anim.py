#bisection method
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as fn
plt.style.use('dark_background')
def f(x):
    return (1/16)*x**3-sin(x)
fl=open('bisection-output','w')
fig,ax=plt.subplots()
a=-5
b=6
p=(a+b)/2
def animate(i):
    ax.cla()
    global a,b,p
    x=linspace(-5,6,1000)
    ax.axis('off')
    ax.set_title('Bisection-method')
    ax.plot(x,f(x),color='#904BB4')
    ax.axvline(color='white',linewidth=3)
    ax.axhline(color='white',linewidth=3)
    ax.plot([a,a],[0,f(a)],color='#49B2B6',linewidth=2,label='Negative-functional_value')
    ax.plot([b,b],[0,f(b)],color='#B64D49',linewidth=2,label='Positive-functional_value')
    ax.legend()
    ax.scatter(p,0,color='red')
    ax.scatter(a,f(a),color='#E7BB18',marker='.')
    ax.scatter(b,f(b),color='#E7BB18',marker='.')
    if f(p)*f(a)>0:
        a=p
    else:
        b=p
    p=(a+b)/2
    
manim=fn(fig,animate,frames=arange(8),repeat=False,interval=800)  
manim.save('Animation-bisection_method.mp4',fps=1,writer='ffmpeg')   
plt.show()
