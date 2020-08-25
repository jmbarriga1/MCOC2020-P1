# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 09:43:20 2020

@author: MiguelB
"""

import scipy as sp
from scipy.integrate import odeint


rho = 1.225  #kg/m**3
cd = 0.47
cm = 0.01
inch = 2.54*cm
D = 8.5*inch
r = D/2
A = sp.pi * r**2
CD = 0.5*rho*cd*A
g = 9.81          #m/s**2
m = 15           #Kg
V = 0
          #velocidad viento m/s
        
names = ["V = 0 m/s.txt","V = 10.0 m/s.txt", "V = 20.0 m/s.txt"]


#  z --> vector de estado
# z = [x, y, vx, vy]
# dz/dt = bala(z, t)

#  dz/dt = [z2, 0, FD/m - g]

# z[0] --> x
# z[1] --> y
# z[2] --> vx
# z[3] --> vy

 
def bala (z, t):
    zp = sp.zeros(4)
    zp[0] = z[2]
    zp[1] = z[3]
    v = z[2:4]
    v[0] = v[0] - V
    v2 = sp.dot(v,v)
    vnorm = sp.sqrt(v2)
    FD = -CD * v2 * (v/vnorm)
    zp[2]= FD[0] / m
    zp[3] = FD[1] / m - g
    
    return zp

import matplotlib.pylab as plt

plt.figure()

V = 0
t = sp.linspace(0, 5.7, 1000)

# Parte en el origen y tiene vx = vy = 10

vi = 100*1000/3600
z0 = sp.array([0, 0, vi, vi])

sol = odeint(bala, z0, t)



x = sol[:, 0]
y = sol[:, 1]

plt.plot(x,y,label= "V = 0 m/s")

V = 10
t = sp.linspace(0, 5.7, 1000)

# Parte en el origen y tiene vx = vy = 10

vi = 100*1000/3600
z0 = sp.array([0, 0, vi, vi])

sol = odeint(bala, z0, t)



x = sol[:, 0]
y = sol[:, 1]

plt.plot(x,y,label= "V = 10 m/s")

V = 20
t = sp.linspace(0, 5.7, 1000)

# Parte en el origen y tiene vx = vy = 10

vi = 100*1000/3600
z0 = sp.array([0, 0, vi, vi])

sol = odeint(bala, z0, t)



x = sol[:, 0]
y = sol[:, 1]

plt.plot(x,y,label= "V = 20 m/s")



plt.ylabel("Y (m)")
plt.xlabel("X (m)")
plt.title("Trayectoria para distintos vientos")
plt.legend()
plt.grid()
plt.plot()
plt.ylim(0,40)
plt.savefig("graphic_balistica.png")
plt.show()
    