from numpy import *
import matplotlib.pyplot as plt
plt.style.use('dark_background')
data=loadtxt('lagrange-interpolation_input.txt')
n=len(data[:,0])
A=ndarray((n,n))
x,y=data[:,0],data[:,1]
A[:,0]=1
def g(m):
    result=0
    for i in range(n):
        temp=1
        for j in range(n):
            if i==j:
                continue
            temp*=(m-x[j])/(x[i]-x[j])    
        result+=temp*y[i]    
    return result        
for i in range(n):
    for j in range(1,n):
        A[i,j]=x[i]**j
soln=linalg.solve(A,y)
def f(q):
    result=0
    for i in range(n):
        result+=soln[i]*q**i
    return result
fig,(ax1,ax2)=plt.subplots(nrows=1,ncols=2)    
ax1.plot(x,y,label='Raw_Data',marker='o')
ax2.plot(x,y,label='Raw_Data',marker='o')
a=linspace(x[0],x[-1],1000)
ax1.plot(a,f(a),label='polynomial_interpolation',linewidth=2,color='green')
ax2.plot(a,g(a),label='lagrange_interpolation',color='red',linewidth=2)
ax1.plot([0,0],[144,325],color='white')
ax1.plot([-2,10],[158,158],color='white')
ax2.plot([0,0],[144,325],color='white')
ax2.plot([-2,10],[158,158],color='white')
ax2.axis('off')
ax1.legend()
ax2.legend()
ax1.set_title('Polynomial')
ax2.set_title('Lagrange')
ax1.axis('off')
plt.savefig('compare-interpolation.png')
plt.show()    
 
