#y"-y'-2y=0
import matplotlib.pyplot as plt
import numpy as np
x,h=np.linspace(0,np.log(2),101,retstep=True)
h2=h**2
y=np.zeros(101)
y[0],y[100]=0,1
e=10
while e>0.00001:
	yo=y.copy()
	for i in range(1,100):
		y[i]=((1-h)*y[i+1]+y[i-1])/(2-h+2*h**2)
	e=np.linalg.norm(y-yo)
plt.plot(x,y)
plt.grid()
plt.show()

