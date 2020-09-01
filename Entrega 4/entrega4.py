# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 12:17:40 2020

@author: MiguelB
"""

from scipy.integrate import odeint
import matplotlib.pylab as plt
import numpy as np

f = 1.0         #Hz
m = 1.0         #kg
chi = 0.2       
w = 2 * np.pi * f
k = m * w**2
c = 2 * chi * w * m 

t = np.linspace(0, 4., 100)
x0 = 1.0
xp0 = 1.0
z0 = [x0,xp0]
#Solución analitica

x_t = np.exp(-c*t/2)*np.cos(w*t)

plt.plot(t, x_t, color ="black", linewidth = 2,label = "Solución analitica")

#Solución odeint

def zpunto(z, t):
    zp = np.zeros(2)
    zp[0] = z[1]
    z1 = z[0]
    z2 = z[1]
    zp[1] = -(k*z1+c*z2)/m
    return zp

sol = odeint(zpunto,z0,t)
xpp = sol[:,0]
plt.plot(t,xpp, color = "blue", label = "Solución odeint")

#Solución eulerint

def eulerint(zp, z0, t, Nsubdivisiones=1):
    Nt = len(t)
    Ndim = len(np.array(z0))
    
    z = np.zeros((Nt, Ndim))
    z[0,:] = z0[0]
    
    for i in range (1, Nt):
        t_anterior = t[i-1]
        
        dt = (t[i] - t[i-1])/Nsubdivisiones
        z_temp = z[i-1, :].copy()
        
        for k in range (Nsubdivisiones):
            z_temp += dt * zpunto(z_temp, t_anterior + k*dt)
            
        z[i,:] = z_temp
    return z

zp = sol[:,:]
sol = eulerint(zp ,z0, t, Nsubdivisiones = 1)
e = sol[:,0]
plt.plot(t, e, ":", color="green", label ="Nsub = 1")


zp = sol[:,:]
sol = eulerint(zp ,z0, t, Nsubdivisiones = 10)
e = sol[:,0]
plt.plot(t, e, ":", color="red", label ="Nsub = 10")


zp = sol[:,:]
sol = eulerint(zp ,z0, t, Nsubdivisiones = 100)
e = sol[:,0]
plt.plot(t, e, ":", color="orange", label ="Nsub = 100")

plt.xlabel("tiempo (s)")
plt.ylabel("x (t)")
plt.title("Estudio convergencia Metodo Euler")
plt.legend()
plt.show()

