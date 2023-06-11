#Finite difference method
#y''=-g
import matplotlib.pyplot as plt
import numpy as np
n=101
x,h=np.linspace(0,10,n,retstep=True)
h2=h**2
y=np.zeros(n)
e=10
y[0],y[100]=0,50
while e>0.00001:
	yo=y.copy()
	for i in range(1,n-1):
		y[i]=(9.8*h2+y[i+1]+y[i-1])/2
	e=np.linalg.norm(y-yo)
plt.plot(x,y)
plt.show()

