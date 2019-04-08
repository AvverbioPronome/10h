import matplotlib.pyplot as plt
import scipy
import pandas
import numpy as np 



def func1(x,y):
	
	return (0.,0.16*y)

def func2(x,y):
	
	return (0.85*x+0.04*y, -0.04*x+0.85*y+1.6)


def func3(x,y):

	return (0.2*x-0.26*y, 0.23*x+0.22*y+1.6)

def func4(x,y):

	return (-0.15*x+0.28*y, 0.26*x+0.24*y+0.44)




F=[func1,func2,func3,func4]
prob=[0.01,0.85,0.07,0.07]

points=100000


x,y=0.,0.


X=[]
Y=[]


fig=plt.figure(1,figsize=(30,20))
ax=fig.add_subplot(111)


for i in range(points):


	ff=np.random.choice(F,p=prob)
	x,y=ff(x,y)



	X.append(x)
	Y.append(y)



ax.set_title('Barnsley fern fractal')
ax.scatter(X,Y,color='green',marker='s',s=10)
#plt.show()
plt.savefig("fern.png")




