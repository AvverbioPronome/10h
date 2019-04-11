import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


plt.rc('font',size=30)


data=np.load('data.npz')


x=data['x']
y=data['y']


y=np.log10(y)


xed=np.linspace(x.min(),0.27,30)
yed=np.linspace(-1.5,3.5,30)



H, xedges, yedges = np.histogram2d(x, y, bins=(xed,yed))
H = H.T 


lst=['magma','brg','seismic','jet','hot','afmhot','gnuplot','gnuplot2','gist_ncar','nipy_spectral','gist_rainbow','inferno']

i=0
for ccc in lst:

	fig=plt.figure(i,figsize=(30,20))
	ax=fig.add_subplot(111)
	im=ax.imshow(H/H.max(axis=0),interpolation='bicubic', origin='low',extent=[xed[0],xed[-1],yed[0],yed[-1]],cmap=ccc,aspect='auto')
	divider = make_axes_locatable(ax)
	cax = divider.append_axes('right', size='5%', pad=0.05)

	ax.set_xlabel(r'$T_{PEAK}\ [GK]$',labelpad=20)
	ax.set_ylabel(r'$[O/H]$',labelpad=30)
	ax.set_title('Density plot',y=1.05)
	fig.colorbar(im, cax=cax, orientation='vertical')
	plt.savefig('%s.png' %(ccc))
	
	i=i+1
