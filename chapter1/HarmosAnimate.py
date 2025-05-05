""" From "COMPUTATIONAL PHYSICS: PROBLEM SOLVING with PYTHON"
    3rd Ed. by RH Landau, MJ Paez, and CC Bordeianu, 2015 """
# Updated for Python 3.10.17

# HarmonsAnimate: Solve t-dependent Sch Eqt for HO wi animation

#from vpython import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#import matplotlib
#matplotlib.interactive(False)


# Initialize wave function, probability, potential
dx = 0.02;   dx2 = dx*dx;   k0 = 3.0*np.pi;  dt = dx2/4.0;  
xmax = 6.0;  beta = dt/dx2
xs = np.arange(-xmax,xmax+dx/2,dx)                    # Array x values
# Initial wave packet
nmax=np.size(xs)
R=np.zeros((nmax,2),float)
I=np.zeros((nmax,2),float)
v=np.zeros((nmax),float)

#print(nmax)
#print(v[nmax])

R[:,0] = np.exp(-0.5*(xs/0.5)**2) * np.cos(k0*xs)             # Array Re I
I[:,0] = np.exp(-0.5*(xs/0.5)**2) * np.sin(k0*xs)             # Array Im I
v[:]   = 5.0*xs**2                                     # The potential

fig = plt.figure()
# select axis; 111: only one plot, x,y, scales given\n",
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-xmax,xmax), ylim=(0, 1.1))
ax.grid()
plt.title("Harmonic Oscillator")
line, = ax.plot(xs, R[:,0]**2+I[:,0]**2, lw=2)             # x axis, y values, linewidth=2\n",
def animate(dum):
   R[1:-1,1] = R[1:-1,0] - (dt)*(I[2:,0]+I[:-2,0]-2*I[1:-1,0])/dx2 +dt*v[1:-1]*I[1:-1,0]
   I[1:-1,1] = I[1:-1,0] + (dt)*(R[2:,1]+R[:-2,1]-2*R[1:-1,1])/dx2 -dt*v[1:-1]*R[1:-1,1]
   line.set_data(xs, R[:,0]**2+I[:,0]**2)
   for i in range(0,nmax-1):
      R[i,0]=R[i,1]
      I[i,0]=I[i,1]
   return line,

ani = animation.FuncAnimation(fig, animate,frames=1000,interval=1)
#ani.save("HarmosAnimate.gif")
