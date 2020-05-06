#regula-falsi method
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as fn
plt.style.use('dark_background')
def f(x):
    return x**2-3*x
fig,ax=plt.subplots()
exct=log(7/3)/(log(27/25))
a=1
b=5
p=b-((b-a)*f(b))/(f(b)-f(a))
def animate(i):
    global a,b,p
    ax.cla()
    d=linspace(1,5,1000)
    ax.axis('off')
    ax.set_title('Regula-falsi-method')
    ax.axhline(color='white',linewidth=3)
    ax.axvline(color='white',linewidth=3)
    ax.plot(d,f(d))
    ax.scatter(a,f(a),marker='.',color='#E7183F')
    ax.scatter(b,f(b),marker='.',color='#E7183F')
    ax.scatter(p,0,marker='o',color='#18E7C0')
    ax.plot([a,b],[f(a),f(b)],color='red',label='approximate')
    ax.plot([p,p],[0,f(p)],color='blue')
    ax.plot([p,b],[f(p),f(b)],color='#95E718',label='next-approximate')
    ax.legend()
    if f(p)*f(a)>0:
        a=p
    else:
        b=p
    p=b-((b-a)*f(b))/(f(b)-f(a))
manim=fn(fig,animate,frames=arange(10),repeat=False,interval=500)
manim.save('Animation-regula_falsi-method.mp4',fps=2,writer='ffmpeg')
plt.show()











