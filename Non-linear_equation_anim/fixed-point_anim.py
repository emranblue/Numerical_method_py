#fixed point iteration method
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as fn
plt.style.use('dark_background')
def f(x):#defining a function
    return -2**-x+x**3-0.5*x**2+x
def g(x):
    return 2**-x-x**3+0.5*x**2
fig,ax=plt.subplots() 
p0=0.9
p=g(p0)
def inti():
    ax.cla()
    a=linspace(0,1,500)
    ax.axis('off')
    ax.set_title('Fixed-point-method')
    ax.plot(a,g(a))
    ax.plot(a,a)
    ax.scatter(p0,p,color='red',label='Intitial-approximation')
    ax.axvline(color='white',linewidth=3)
    ax.axhline(color='white',linewidth=3)
    
def animate(i):
    global p0,p
    ax.plot([p0,g(p0)],[g(p0),g(p0)],color='#AE40Bf',linewidth=0.8,label='p0')
    ax.plot([g(p0),g(p0)],[g(p0),g(p)],color='#6A18E7',linewidth=0.8,label='g(p0)')
    if i==0:
        ax.legend()
    p0=p
    p=g(p0)
manim=fn(fig,animate,frames=arange(50),interval=1000,repeat=False,init_func=inti)    
manim.save('Animation-fixed_point-method.mp4',fps=2,writer='ffmpeg')
plt.show()    

