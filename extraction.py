import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from matplotlib.backends.backend_pdf import PdfPages
data=fits.open('NGC1366.fits')
dat=data[0].data
#print(data[0].header)



dat=dat[:,:580,:580]
print(np.shape(dat))
#np.savetxt('signal.txt', np.column_stack([dat]),fmt=b'%10.6f')


# To check if the array contains any NaN values
#if(np.isnan(dat).any()):
#    print("The Array contain NaN values")
#else:
#    print("The Array does not contain NaN values")

N=3272
#Noise=np.zeros((580,580),float)
#Signal=np.zeros((580,580),float)
	


fout = open('S.txt','w')
for i in range(580):
	for j in range(580):
#		Noi=0.0
#		Sig=0.0
		dm=np.mean(dat[:,i,j]) # For H-alpha line, we take 1419:1427
		Noise=np.sum((dat[:,i,j]-dm)**2)
		Noise=np.sqrt(Noise/N)
#		Noise=np.std(dat[:,i,j])
		Signal=np.sqrt(np.sum(np.square(dat[1419:1427,i,j])))
#		Noise[i,j]=np.sqrt(Noi/N)
		if Noise==0: Noise=10	
#		Signal[i,j]=np.sqrt(Sig/N)
		if Signal==0: Signal=1
#		print(Noise[i,j],Signal[i,j])
		SNR= Signal/Noise
		print(i,j,Signal,Noise,SNR,file=fout)
#		np.savetxt('extract.txt', (Noise[i,j], Signal[i,j]),newline='\n')
#np.savetxt('noise.txt', np.column_stack([Noise]),fmt=b'%10.6f')
#np.savetxt('signal.txt', np.column_stack([Signal]),fmt=b'%10.6f')
fout.close()
print(np.amax(Signal),np.amin(Signal))
print(np.amax(Noise),np.amin(Noise))


"""

dm=np.mean(d)

for i in range(len(d)):
	if d[i]==np.nan:
		d[i]=dm
	Noi+=(d[i]-dm)**2
	Sig+=d[i]**2
Noise=np.sqrt(Noi/N)
Signal=np.sqrt(Sig/N)
print(Noise,Signal)
#np.savetxt('extract.txt', np.column_stack([d]),'%10.6f')
"""

