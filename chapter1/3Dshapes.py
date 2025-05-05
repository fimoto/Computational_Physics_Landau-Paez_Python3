""" From "COMPUTATIONAL PHYSICS: PROBLEM SOLVING with PYTHON"
    3rd Ed. by RH Landau, MJ Paez, and CC Bordeianu, 2015 """
# Updated for Python 3.10.17

# List 1.3 3Dshapes.py: Some 3-D Shapes of VPython

from vpython import *

graph1 = canvas(width=500, height=500, title='VPython 3-D Shapes', range=10)
sphere(pos=vec(0,0,0), radius=1, color=color.green)
sphere(pos=vec(0,1,-3), radius=1.5, color=color.red)
arrow(pos=vec(3,2,2), axis=vec(3,1,1), color=color.cyan)
cylinder(pos=vec(-3,-2,3), axis=vec(6,-1,5), color=color.yellow)
cone(pos=vec(-6,-6,0), axis=vec(-2,1,-0.5), radius=2, color=color.magenta)
helix(pos=vec(-5,5,-2), axis=vec(5,0,0), radius=2, thickness=0.4, color=color.orange)
ring(pos=vec(-6,1,0), axis=vec(1,1,1), radius=2, thickness=0.3, color=vec(0.3,0.4,0.6))
box(pos=vec(5,-2,2), length=5, width=5, height=0.4, color=vec(0.4,0.8,0.2))
pyramid(pos=vec(2,5,2), size=vec(4,3,2), color=vec(0.7,0.7,0.2))
ellipsoid(pos=vec(-1,-7,1), axis=vec(2,1,3), length=4, height=2, width=5, color=vec(0.1,0.9,0.8))
