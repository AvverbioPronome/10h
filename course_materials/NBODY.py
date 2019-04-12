#modules needed
import pylab
from matplotlib.pyplot import *
import math
import numpy
from scipy.integrate import odeint



#body_i acceleration :  direction k (being 2D x or y)

def a(i,k,data): #input: i=index of the body,k=direction (x or y), data=array with positions and velocities
	
	
	A=0. #starting with 0
	
	
	xi=data[4*i] #coordinates for body_i (x & y)
	yi=data[4*i+1]	
	arri=numpy.array([xi,yi]) #put coordinates together
	
	
	for j in range(0,len(bod)): #for every other body
	
		if j==i: #if the same index (same body)
			
			A=A+0. #skip
			
		else:  
	
			
			
	
			xj=data[4*bod[j]] #body_j coordinates (x & y)
			yj=data[4*bod[j]+1]
	
			arrj=numpy.array([xj,yj])  #put coordinates together

			diff=arri-arrj #calculate distance ij
			dij=numpy.linalg.norm(diff) #modulus
			
	
			A= A - G*m[j]*(data[4*i+k]-data[4*j+k])/((dij+eps)**3) #and sum 
	
	#at the end we get the total acceleration (along direction k) for the body_i ONLY!
	return A 


def dAdt(data,t): #differential system
	
	
	datadot=numpy.zeros(len(data)) #define the differential system
	
	
	for k in range(0,2): #for each direction (x,y)
	
		for i in range(0,N): #for each body
	
			datadot[4*i+k+2]=a(i,k,data) #vdot_i=acc_i
			datadot[4*i+k]=data[4*i+k+2] #rdot_i=v_i
		
	
	return datadot 

#MAIN

#changing units (A.U.=1, year=1, Msun=1)

Kg=1./(1.988E+30)
m=1./(1.496E11)
s=1./(3.153E+07)
G=(6.674E-11)*(m**3)*(Kg**-1)*(s**-2)
pi=math.pi


#INPUT: NUMBER OF BODIES (TRY 3/4 MAXIMUM!)
N=3
#INPUT: MASSES 
m=[1,3.003E-06,2.447E-06]
#INPUT: INITIAL POSITIONS AND VELOCITIES
data0=[0,0,0,0, 1,0,0,2*pi, 0.723,0,0,1.175957*(2*pi)] #[x1,y1,vx1,vy1,     x2,y2,vx2,vy2,   ....]



#program
bod=numpy.arange(0,N,1) #index for each body (0 -> N-1)


eps=1.E-10 #softening parameter, to avoid divergences


t=numpy.linspace(0.,8.,1000)  #time vector


sol=odeint(dAdt,data0,t)  #odeint solution


pylab.rc('font',size=30) #plot


dx=sol[:,8]-sol[:,4] #x_venus-x_earth
dy=sol[:,9]-sol[:,5] #y_venus-y_earth

plot(dx,dy,color='black',lw=3)

xlabel(r'$\Delta\ x \ [A.U.]$')
ylabel(r'$\Delta\ y \ [A.U.]$')
title('Lissajous curve: Earth-Venus 13:8 resonance',y=1.05)

show()











