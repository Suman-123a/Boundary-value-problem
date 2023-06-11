#Finite difference method
#Matrix operatios
#y''+y=1
import matplotlib.pyplot as plt
import numpy as np
n=51
x,h=np.linspace(0,np.pi/2,n,retstep=True)
A=np.zeros((n,n))
for i in range(1,n-1):
	A[i][i+1]=1
	A[i][i]=h**2-2
	A[i][i-1]=1
A[0][0]=1
A[-1][-1]=1
b=np.zeros(n)
b[0]=0
b[1:-1]=h**2
b[-1]=0
y=np.linalg.solve(A,b)
plt.plot(x,y)
plt.show()

