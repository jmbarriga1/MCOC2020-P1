# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 11:39:44 2020

@author: MiguelB
"""
from sympy import sqrt
from legendre_np import legendre

μ = 398600441500000.000000
R = 6378136.3 
J2 = 1.75553*(10**10)*1000**5
J3 = -2.61913*(10**11)*1000**6
J4 = -0.16193312050719E-05/((R**4)*μ)
J5 = -0.22771610163688E-06/((R**5)*μ)
J6 = 0.53964849049834E-06/((R**6)*μ)


def Fg(x,y,z):
    r2 = x**2 + y**2 + z**2
    Fx = x*μ*(J2*R**2*(3*z**2/(2*(r2)) - 0.5)/(r2) + J3*R**3*(5*z**3/(2*(r2)**(3/2)) - 3*z/(2*sqrt(r2)))/(r2)**(3/2) + J4*R**4*(35*z**4/(8*(r2)**2) - 15*z**2/(4*(r2)) + 0.375)/(r2)**2 + J5*R**5*(63*z**5/(8*(r2)**(5/2)) - 35*z**3/(4*(r2)**(3/2)) + 15*z/(8*sqrt(r2)))/(r2)**(5/2) + J6*R**6*(231*z**6/(16*(r2)**3) - 315*z**4/(16*(r2)**2) + 105*z**2/(16*(r2)) - 0.3125)/(r2)**3 + 1)/(r2)**(3/2) - μ*(-3*J2*R**2*x*z**2/(r2)**3 - 2*J2*R**2*x*(3*z**2/(2*(r2)) - 0.5)/(r2)**2 - 3*J3*R**3*x*(5*z**3/(2*(r2)**(3/2)) - 3*z/(2*sqrt(r2)))/(r2)**(5/2) + J3*R**3*(-15*x*z**3/(2*(r2)**(5/2)) + 3*x*z/(2*(r2)**(3/2)))/(r2)**(3/2) - 4*J4*R**4*x*(35*z**4/(8*(r2)**2) - 15*z**2/(4*(r2)) + 0.375)/(r2)**3 + J4*R**4*(-35*x*z**4/(2*(r2)**3) + 15*x*z**2/(2*(r2)**2))/(r2)**2 - 5*J5*R**5*x*(63*z**5/(8*(r2)**(5/2)) - 35*z**3/(4*(r2)**(3/2)) + 15*z/(8*sqrt(r2)))/(r2)**(7/2) + J5*R**5*(-315*x*z**5/(8*(r2)**(7/2)) + 105*x*z**3/(4*(r2)**(5/2)) - 15*x*z/(8*(r2)**(3/2)))/(r2)**(5/2) - 6*J6*R**6*x*(231*z**6/(16*(r2)**3) - 315*z**4/(16*(r2)**2) + 105*z**2/(16*(r2)) - 0.3125)/(r2)**4 + J6*R**6*(-693*x*z**6/(8*(r2)**4) + 315*x*z**4/(4*(r2)**3) - 105*x*z**2/(8*(r2)**2))/(r2)**3)/sqrt(r2)
    Fy = y*μ*(J2*R**2*(3*z**2/(2*(r2)) - 0.5)/(r2) + J3*R**3*(5*z**3/(2*(r2)**(3/2)) - 3*z/(2*sqrt(r2)))/(r2)**(3/2) + J4*R**4*(35*z**4/(8*(r2)**2) - 15*z**2/(4*(r2)) + 0.375)/(r2)**2 + J5*R**5*(63*z**5/(8*(r2)**(5/2)) - 35*z**3/(4*(r2)**(3/2)) + 15*z/(8*sqrt(r2)))/(r2)**(5/2) + J6*R**6*(231*z**6/(16*(r2)**3) - 315*z**4/(16*(r2)**2) + 105*z**2/(16*(r2)) - 0.3125)/(r2)**3 + 1)/(r2)**(3/2) - μ*(-3*J2*R**2*y*z**2/(r2)**3 - 2*J2*R**2*y*(3*z**2/(2*(r2)) - 0.5)/(r2)**2 - 3*J3*R**3*y*(5*z**3/(2*(r2)**(3/2)) - 3*z/(2*sqrt(r2)))/(r2)**(5/2) + J3*R**3*(-15*y*z**3/(2*(r2)**(5/2)) + 3*y*z/(2*(r2)**(3/2)))/(r2)**(3/2) - 4*J4*R**4*y*(35*z**4/(8*(r2)**2) - 15*z**2/(4*(r2)) + 0.375)/(r2)**3 + J4*R**4*(-35*y*z**4/(2*(r2)**3) + 15*y*z**2/(2*(r2)**2))/(r2)**2 - 5*J5*R**5*y*(63*z**5/(8*(r2)**(5/2)) - 35*z**3/(4*(r2)**(3/2)) + 15*z/(8*sqrt(r2)))/(r2)**(7/2) + J5*R**5*(-315*y*z**5/(8*(r2)**(7/2)) + 105*y*z**3/(4*(r2)**(5/2)) - 15*y*z/(8*(r2)**(3/2)))/(r2)**(5/2) - 6*J6*R**6*y*(231*z**6/(16*(r2)**3) - 315*z**4/(16*(r2)**2) + 105*z**2/(16*(r2)) - 0.3125)/(r2)**4 + J6*R**6*(-693*y*z**6/(8*(r2)**4) + 315*y*z**4/(4*(r2)**3) - 105*y*z**2/(8*(r2)**2))/(r2)**3)/sqrt(r2)
    Fz = z*μ*(J2*R**2*(3*z**2/(2*(r2)) - 0.5)/(r2) + J3*R**3*(5*z**3/(2*(r2)**(3/2)) - 3*z/(2*sqrt(r2)))/(r2)**(3/2) + J4*R**4*(35*z**4/(8*(r2)**2) - 15*z**2/(4*(r2)) + 0.375)/(r2)**2 + J5*R**5*(63*z**5/(8*(r2)**(5/2)) - 35*z**3/(4*(r2)**(3/2)) + 15*z/(8*sqrt(r2)))/(r2)**(5/2) + J6*R**6*(231*z**6/(16*(r2)**3) - 315*z**4/(16*(r2)**2) + 105*z**2/(16*(r2)) - 0.3125)/(r2)**3 + 1)/(r2)**(3/2) - μ*(-2*J2*R**2*z*(3*z**2/(2*(r2)) - 0.5)/(r2)**2 + J2*R**2*(-3*z**3/(r2)**2 + 3*z/(r2))/(r2) - 3*J3*R**3*z*(5*z**3/(2*(r2)**(3/2)) - 3*z/(2*sqrt(r2)))/(r2)**(5/2) + J3*R**3*(-15*z**4/(2*(r2)**(5/2)) + 9*z**2/(r2)**(3/2) - 3/(2*sqrt(r2)))/(r2)**(3/2) - 4*J4*R**4*z*(35*z**4/(8*(r2)**2) - 15*z**2/(4*(r2)) + 0.375)/(r2)**3 + J4*R**4*(-35*z**5/(2*(r2)**3) + 25*z**3/(r2)**2 - 15*z/(2*(r2)))/(r2)**2 - 5*J5*R**5*z*(63*z**5/(8*(r2)**(5/2)) - 35*z**3/(4*(r2)**(3/2)) + 15*z/(8*sqrt(r2)))/(r2)**(7/2) + J5*R**5*(-315*z**6/(8*(r2)**(7/2)) + 525*z**4/(8*(r2)**(5/2)) - 225*z**2/(8*(r2)**(3/2)) + 15/(8*sqrt(r2)))/(r2)**(5/2) - 6*J6*R**6*z*(231*z**6/(16*(r2)**3) - 315*z**4/(16*(r2)**2) + 105*z**2/(16*(r2)) - 0.3125)/(r2)**4 + J6*R**6*(-693*z**7/(8*(r2)**4) + 1323*z**5/(8*(r2)**3) - 735*z**3/(8*(r2)**2) + 105*z/(8*(r2)))/(r2)**3)/sqrt(r2)
 
    return Fx, Fy, Fz
