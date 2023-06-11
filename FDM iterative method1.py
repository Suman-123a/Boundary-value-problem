#Finite difference method
#y"+y = 1
import matplotlib.pyplot as plt
import numpy as np
x,h=np.linspace(0,np.pi/2,101,retstep=True)
h2=h**2
y=np.zeros(101)
e=10
while e>0.00001:
	yo=y.copy()
	for i in range(1,100):
		y[i]=(y[i+1]+y[i-1]-h2)/(2-h2)
	e=np.linalg.norm(y-yo)
plt.plot(x,y)
plt.show()
print(y)
