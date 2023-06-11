#Shooting Method(BVP)
#y"= -y+2(y')**2/y
import matplotlib.pyplot as plt
import numpy as np
def f(x,y,z):
	return (2*z**2)/y-y
def D(xi,xf,y,z,n):
	xx,yy=[],[]
	h=(xf-xi)/(n-1)
	for i in range(n):
		x=xi+i*h
		xx.append(x)
		ya=y
		y=y+h*z
		z=z+h*f(x,ya,z)
		yy.append(y)
	return xx,yy
z1,z2=0.1,0.3
g1,w1=D(-1,1,0.324,z1,201)
g2,w2=D(-1,1,0.324,z2,201)

e=0.00001
while abs(w2[-1]-w1[-1])>e:
	z3=z2+(z2-z1)*(0.324-w2[-1])/(w2[-1]-w1[-1])
	t1,t2=D(-1,1,0.324,z3,201)
	w1[-1]=w2[-1]
	w2[-1]=t2[-1]
	z1=z2
	z2=z3
a1,a2=D(-1,1,0.324,z3,201)
print(a2[-1])
plt.plot(a1,a2,"o")
plt.plot(g1,w1)
plt.plot(g2,w2)
plt.show()


	