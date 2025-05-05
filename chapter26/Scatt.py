""" From "COMPUTATIONAL PHYSICS: PROBLEM SOLVING with PYTHON"
    3rd Ed. by RH Landau, MJ Paez, and CC Bordeianu, 2015 """
# Updated for Python 3.10.17

# List 26.2 Scatt.py:    Soln p space Lippmann Schwinger for scattering

from vpython import *
import numpy as np
import numpy.linalg as lina                      # Numpy's LinearAlgebra  

def gauss(npts, job, a, b, x, w):
    m  = i = j = t = t1 = pp = p1 = p2 = p3 = 0.
    eps = 3.E-14                    # Accuracy: ******ADJUST THIS*******!
    m = (npts + 1)/2
    for i in np.arange(1, m + 1):
        t = np.cos(np.pi*(float(i) - 0.25)/(float(npts) + 0.5) )
        t1 = 1 
        while( (abs(t - t1) ) >= eps):
            p1 = 1. ;  p2 = 0.  
            for j in range(1, npts + 1):
                p3 = p2;   p2 = p1 
                p1 = ((2.*float(j)-1)*t*p2 - (float(j)-1.)*p3)/(float(j))
            pp = npts*(t*p1 - p2)/(t*t - 1.) 
            t1 = t; t = t1  -  p1/pp     
        x[int(i-1)] = - t;   x[int(npts-i)] = t 
        w[int(i-1)] = 2./( (1. - t*t)*pp*pp) 
        w[int(npts-i)] = w[int(i-1)]  
    if (job == 0):
        for i in range(0, npts):
            x[i] = x[i]*(b - a)/2. + (b + a)/2. 
            w[i] = w[i]*(b - a)/2. 
    if (job == 1):
        for i in range(0, npts):
            xi   = x[i]
            x[i] = a*b*(1. + xi) / (b + a - (b - a)*xi) 
            w[i] = w[i]*2.*a*b*b/( (b + a - (b-a)*xi)*(b + a - (b-a)*xi))
    if (job == 2):
        for i in range(0, npts):
            xi = x[int(i)]
            x[int(i)] = (b*xi +  b + a + a) / (1. - xi) 
            w[int(i)] = w[int(i)]*2.*(a + b)/( (1. - xi)*(1. - xi) )
            
graphscatt = graph(x=0, y=0, xmin=0, xmax=6,ymin=0, ymax=1, width=600, height=400, title='S Wave Cross Section vs E', xtitle='kb', ytitle='[sin(delta)]**2')
sin2plot = gcurve(color=color.red)
M = 27;             b = 10.0;           n = 26
k = np.zeros((M),float);        x = np.zeros((M),float);      w = np.zeros((M),float)
Finv = np.zeros((M,M),float);   F = np.zeros((M,M), float);   D = np.zeros((M),float)
V = np.zeros((M), float);       Vvec = np.zeros((n+1,1),float)
scale = n/2;                 lambd = 1.5

gauss(n, 2, 0., scale, k, w)                        # Set up points & wts
ko = 0.02
for m in range(1,901):	
    k[n] = ko		
    for i in range (0, n):  D[i]=2/np.pi*w[i]*k[i]*k[i]/(k[i]*k[i]-ko*ko) #D
    D[n] = 0. 
    for  j in range(0,n):   D[n]=D[n]+w[j]*ko*ko/(k[j]*k[j]-ko*ko)
    D[n] = D[n]*(-2./pi)    
    for i in range(0,n+1):                               # Set up F &  V
        for j in range(0,n+1):
            pot = -b*b * lambd * np.sin(b*k[i])*np.sin(b*k[j])/(k[i]*b*k[j]*b)
            F[i][j] = pot*D[j]	                                  
            if i==j: F[i][j] = F[i][j] + 1. 
        V[i] = pot                                                
    for  i in range(0,n+1): Vvec[i][0]= V[i]   
    Finv = lina.inv(F)                       # LinearAlgebra for inverse
    R = np.dot(Finv, Vvec)                                 # Matrix multiply
    RN1 = R[n][0]
    shift = np.arctan(-RN1*ko)
    sin2 = (np.sin(shift))**2
    sin2plot.plot(pos = (ko*b,sin2))                 # Plot sin**2(delta)
    ko = ko + 0.2*pi/1000.
print("Done")
