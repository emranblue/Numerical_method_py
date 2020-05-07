#newton-rapson methode
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as fn
plt.style.use('dark_background')
def f(x):
    return x**2-3*x
def df(x):
    return 2*x-3
fig,ax=plt.subplots()
p0=10
p=p0-f(p0)/df(p0)
def animate(i):
    global p0,p
    ax.cla()
    a=linspace(1,6,1000)
    ax.axis('off')
    ax.set_title('Newton-Rapson')
    ax.plot(a,f(a))
    ax.axhline(color='white',linewidth=3)
    ax.axvline(color='white',linewidth=3)
    ax.plot([p,p0],[0,f(p0)],color='red',label='tangent-line')
    ax.scatter(p0,f(p0),color='#E7BB18')
    ax.plot([p,p],[0,f(p)],color='#18E794')
    ax.legend()
    p0=p
    p=p0-f(p0)/df(p0)
manim=fn(fig,animate,frames=arange(6),repeat=False,interval=500)    
manim.save('Animation-newton_rapson-method.mp4',fps=1,writer='ffmpeg')
plt.show()