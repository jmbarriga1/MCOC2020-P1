# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 11:35:17 2020

@author: MiguelB
"""

from sympy import *
from legendre_np import legendre

x = S("x")
y = S("y")
z = S("z")
μ = S("μ")
J2 = S("J2") 
J3 = S("J3")
J4 = S("J4") 
J5 = S("J5")
J6 = S("J6") 

R = S("R")

r = sqrt(x**2 + y**2+ z**2)
sinθ = z/r

u = -μ/r *(1+
    J2*legendre(0,2,sinθ) / (r/R)**2 + 
    J3*legendre(0, 3, sinθ) / (r/R)**3 +
    J4*legendre(0,4,sinθ) / (r/R)**4 + 
    J5*legendre(0, 5, sinθ) / (r/R)**5 + 
    J6*legendre(0,6,sinθ) / (r/R)**6) 
    


Fx = u.diff(x)
Fy = u.diff(y)
Fz = u.diff(z)

print (Fx)
print (Fy)
print (Fz)