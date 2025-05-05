""" From "COMPUTATIONAL PHYSICS: PROBLEM SOLVING with PYTHON"
    3rd Ed. by RH Landau, MJ Paez, and CC Bordeianu, 2015 """
# Updated for Python 3.10.17

# List 1.1 EasyVisual.py:

import numpy as np
import vpython as vs

Plot1 = vs.gcurve(color = vs.color.red)

for x in np.arange(0., 8.1, 0.1):
    Plot1.plot( pos = (x, 5.*np.cos(2.*x)*np.exp(-0.4*x)) )

graph1 =  vs.graph(width=600, height=450,\
    title='Visual 2-D Plot', xtitle='x', ytitle='f(x)',\
    foreground = vs.color.black, background = vs.color.white)

Plot2 = vs.gdots(color = vs.color.black)

for x in np.arange( -5.,  +5, 0.1 ):
    Plot2.plot(pos = (x, np.cos(x)))
