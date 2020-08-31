import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


a=np.loadtxt('14rns.dat' , delimiter=',')
b=np.loadtxt('14lorene.dat' , delimiter=',')
c=np.loadtxt('14sly4.dat' , delimiter=',')
x=a[:,0]
q=a[:,1]
xprima=b[:,0]
qprima=b[:,1]
xdprima=c[:,0]
qdprima=c[:,1]

#parabolic fit

z=np.polyfit(x,q,2)
zprima=np.polyfit(xprima,qprima,2)
zdprima=np.polyfit(xdprima,qdprima,2)

print(z)




#quadratic fit
	
def quadratic(x,a):
	return a*x**2

def quadraticprima(xprima,aprima):
	return aprima*xprima**2
def quadraticdprima(xdprima,adprima):
	return adprima*xdprima**2
	

	
a,cov=curve_fit(quadratic,x,q)
aprima,covprima=curve_fit(quadraticprima,xprima,qprima)
adprima,covdprima=curve_fit(quadraticdprima,xdprima,qdprima)


t=np.linspace(min(xdprima)-0.01,max(x),200)

#plots

#plt.plot(x,q, 'or', label='fps-rns')
plt.plot(xdprima,qdprima, 'oy', label='sly4-lorene')
plt.plot(xprima,qprima, 'ob', label='fps-Lorene')
#plt.plot(t,a*t**2, '-r', label='rns fit')
plt.plot(t,aprima*t**2, '-b', label='fps-lorene fit')
plt.plot(t,adprima*t**2, '-y', label='sly4-lorene fit')

plt.title(r'$M=1.4 M_{\odot}$')
plt.ylabel(r'$q$')
plt.xlabel(r'$\chi$')
plt.grid(True)
plt.legend(loc='lower left')
plt.show(True)

arns=(a+z[0])/2
alorene=(aprima+zprima[0])/2
alorenesly4=(adprima+zdprima[0])/2


chi2fps_rns=np.sum((quadratic(x,a)-q)**2)
chi2fps_lorene=np.sum((quadratic(xprima,aprima)-qprima)**2)
chi2sly4_lorene=np.sum((quadratic(xdprima,adprima)-qdprima)**2)

print("chi2(rns)=", chi2fps_rns)
print("chi2(fps,lorene)=", chi2fps_lorene)
print("chi2(sly4,lorene)=", chi2sly4_lorene)

print(arns)
print (alorene)
print (alorenesly4)


