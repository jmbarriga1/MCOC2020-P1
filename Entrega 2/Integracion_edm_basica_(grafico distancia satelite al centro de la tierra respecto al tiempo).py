# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 16:15:28 2020

@author: MiguelB
"""

import scipy as sp
from scipy.integrate import odeint
import numpy as np

g = 6.67*(10**-11)  #Nm**2/k**2
m_t = 5.98*(10**24)  #Kg
r = (6371 + 700)*1000 #metros
radio_tierra = 6371*1000
radio_orbita = (6371+80)*1000
t = 12700             
omega = (2*3.14)/(24*3600)   #2*Pi/24 horas en segundos
T = sp.linspace(0,t,1001)




# El satelite se encuentra a cierta distancia del centro del planeta
x = r
y = 0
z = 0


# Las variables de velocidad variaran excepto en el eje z que sera siempre 0

vz = 0      #m/s
vx = 0   #m/s
vy = 7000    #m/s

z_0 =  sp.array([x,y,z,vx,vy,vz])


def satelite (z,T):
    #Matriz de rotación
    R = sp.array([[sp.cos(omega*T), -sp.sin(omega*T), 0], [sp.sin(omega*T), sp.cos(omega*T), 0], [0, 0, 1]])

    #Primera derivada de R
    dR_dt = sp.array([[-sp.sin(omega*T), -sp.cos(omega*T), 0], [sp.cos(omega*T), -sp.sin(omega*T), 0], [0, 0, 0]])*(omega)

    #Segunda derivada de R
    dR_dt2 = sp.array([[-sp.cos(omega*T), sp.sin(omega*T), 0], [-sp.sin(omega*T), -sp.cos(omega*T), 0], [0, 0, 0]])*(omega**2)

    zp = sp.zeros(6)
    zp[0:3] = z[3:6]
    z2 = ((-g*m_t)/(r**3))*z[0:3] - R.T@(dR_dt2@z[0:3] + 2*dR_dt@z[3:6])
    zp[3:6] = z2
    return zp

import matplotlib.pylab as plt

plt.figure()
sol = odeint(satelite,z_0,T)
x = sol[:,0]
y = sol[:,1]
z = sol[:,2]


r_atmosfera = (6371+80)*1000
tetha = np.linspace(0,2*3.14,100)

X = r_atmosfera*np.cos(tetha)
Y = r_atmosfera*np.sin(tetha)

plt.plot(T,x)
plt.hlines(y = radio_tierra, xmin = 0, xmax=14000,color="green")
plt.hlines(y = radio_orbita, xmin = 0, xmax=14000, color="orange")
plt.hlines(y = -radio_tierra, xmin = 0, xmax=14000, color="green")
plt.hlines(y = -radio_orbita, xmin = 0, xmax=14000, color="orange")

plt.title("Distancia satelite, tierra y orbita respecto al tiempo.")


plt.ylabel("Posicion (m)")
plt.xlabel("tiempo (s)")
plt.grid(True)
plt.legend(["r(t)","Radio tierra","Radio orbita"])  
plt.savefig("Distancia satelite, tierra y orbita respecto al tiempo.png")


plt.show()
