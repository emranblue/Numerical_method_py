from numpy import *
import matplotlib.pyplot as plt
plt.style.use('dark_background')
plt.axis('off')
data=loadtxt('lagrange-interpolation_input.txt')#read data from text file
n=len(data[:,0])#taking the lenth
A=ndarray((n,n))#creating an matrix array
x,y=data[:,0],data[:,1]#unpack the data and shift the data to x,y variable array
A[:,0]=1
def g(m):#lagrange function
    result=0
    for i in range(n):
        temp=1
        for j in range(n):
            if i==j:
                continue
            temp*=(m-x[j])/(x[i]-x[j])    #lagrange formula
        result+=temp*y[i]    
    return result        
for i in range(n):
    for j in range(1,n):
        A[i,j]=x[i]**j
soln=linalg.solve(A,y)#linalg.solve is numpy function,used to solve system of eqn.when A is matrix and y is vector....Ax=b form....here y is b
def f(q):#polynomial function
    result=0
    for i in range(n):
        result+=soln[i]*q**i#** means raise to power
    return result
plt.plot(x,y,label='Raw_Data',marker='o')
a=linspace(x[0],x[-1],1000)#taking 1000 sample from x[0] to x[-1](-1 means,last element of this array)..this creat an array...
plt.plot(a,f(a),label='polynomial_interpolation',linewidth=5,color='green')#check label
plt.plot(a,g(a),label='lagrange_interpolation',color='red',linewidth=2)#check label
plt.plot([0,0],[144,325],color='white')#ploting y axis
plt.plot([-2,10],[158,158],color='white')#ploting x axis
plt.legend()#show label of graphs
plt.savefig('compare-interpolation.png')#save the figure
plt.show()    ##show the graph
 
