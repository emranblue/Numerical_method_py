from numpy import *
from matplotlib.animation import FuncAnimation as fn
import matplotlib.pyplot as plt
plt.style.use('dark_background')
def f(x):
    return 2**x*sin(x)
def df(x,h):
    return (f(x+h)-f(x-h))/(2*h)
def derivat(a,h=0.2,n=4):
    x=ndarray((n,n))
    for i in range(n):
        x[i,0]=df(a,h)
        h/=2
    for j in range(1,n):
        for i in range(j,n):
            x[i,j]=x[i,j-1]+(x[i,j-1]-x[i-1,j-1])/(4**j-1)
    return x[n-1,n-1]           
fig,ax=plt.subplots()

def animate(i):
    b=linspace(-2,4,(i+1))
    ax.cla()
    ax.axis('off')
    a=linspace(-2,4,1000)
    ax.axis('off')
    ax.axhline(color='white',linewidth=3)
    ax.axvline(color='white',linewidth=3)
    ax.plot(a,f(a),color='red')
    ax.bar(b,f(b),width=7/(i+1),alpha=0.7,color='#57A897')
anim=fn(fig,animate,frames=arange(1,300),interval=500)
anim.save('approx.mp4',fps=30,writer='ffmpeg')
plt.show()