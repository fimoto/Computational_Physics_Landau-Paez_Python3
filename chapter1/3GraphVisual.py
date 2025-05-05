""" From "COMPUTATIONAL PHYSICS: PROBLEM SOLVING with PYTHON"
    3rd Ed. by RH Landau, MJ Paez, and CC Bordeianu, 2015 """
# Updated for Python 3.10.17

# List 1.2 3GraphVisual.py:

import numpy as np
import vpython as vs

string = "blue: sin^2(x), white: cos^2(x), red: sin(x)*cos(x)"
graph1 = vs.graph(title=string, xtitle='x', ytitle='y')
y1 = vs.gcurve(color=vs.color.red)           # Curve
y2 = vs.gvbars(color=vs.color.blue)                     # Vertical bars
y3 = vs.gdots(color=vs.color.red)               # Dots
for x in np.arange(-5, 5, 0.1):                       # arange for floats
    y1.plot( pos=(x, np.sin(x)*np.sin(x)) )
    y2.plot( pos=(x, np.cos(x)*np.cos(x)/3.) )
    y3.plot( pos=(x, np.sin(x)*np.cos(x)) )
