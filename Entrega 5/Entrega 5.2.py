# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 20:09:49 2020

@author: MiguelB
"""

from scipy.integrate import odeint
import numpy as np
from leer_eof import leer_eof,utc2time
import matplotlib.pylab as plt

g = 6.6740831*(10**-11)  #Nm**2/k**2
m_t = 5.98*(10**24)  #Kg masa tierra
r_atmosfera = (6371 + 80)*1000 #metros
km = 1000
R_tierra = 6371.*km

hr = 3600             #2 dias en segundos
omega = (2*np.pi)/(24*3600)   #2*Pi/24 horas en segundos



def satelite(z,t):
     
    #Matriz de rotación
    R = np.array([[np.cos(omega*t), -np.sin(omega*t), 0], [np.sin(omega*t), np.cos(omega*t), 0], [0, 0, 1]])

    #Primera derivada de R
    dR_dt = np.array([[-np.sin(omega*t), -np.cos(omega*t), 0], [np.cos(omega*t), -np.sin(omega*t), 0], [0, 0, 0]])*(omega)

    #Segunda derivada de R
    dR_dt2 = np.array([[-np.cos(omega*t), np.sin(omega*t), 0], [-np.sin(omega*t), -np.cos(omega*t), 0], [0, 0, 0]])*(omega**2)
    
    z1 = z[0:3]
    r2 = np.dot(z1,z1)
    r = np.sqrt(r2)
    
    J2 = 1.75553*(10**10)*1000**5
    
    X_J2 = J2*(z[0]/r**7)* (6*z[2]**2-3/2*(z[0]**2+z[1]**2))
    Y_J2 = J2*(z[1]/r**7)* (6*z[2]**2-3/2*(z[0]**2+z[1]**2))
    Z_J2 = J2*(z[2]/r**7)* (3*z[2]**2-9/2*(z[0]**2+z[1]**2))
    J_2 = np.array([X_J2,Y_J2,Z_J2])
    
    J3 = -2.61913*(10**11)*1000**6
    
    X_J3 = J3*z[0]*z[2]/r**9* (10*z[2]**2-15/2*(z[0]**2+z[1]**2))
    Y_J3 = J3*z[1]*z[2]/r**9* (10*z[2]**2-15/2*(z[0]**2+z[1]**2))
    Z_J3 = J3/r**9* (4*z[2]**2*(z[2]**2-3*(z[0]**2+z[1]**2))+3/2*(z[0]**2 + z[1]**2)**2)
    J_3 = np.array([X_J3,Y_J3,Z_J3])
    
    zp = np.zeros(6)
    zp[0:3] = z[3:6]
    z2 = ((-g*m_t)/(r**3))*z[0:3] - R.T@(dR_dt2@z[0:3] + 2*dR_dt@z[3:6]) + J_2[0:3] + J_3[0:3]
    zp[3:6] = z2
    return zp

t, x, y, z, vx, vy, vz = leer_eof("S1B_OPER_AUX_POEORB_OPOD_20200827T111142_V20200806T225942_20200808T005942.EOF")

z0 = np.array([x[0],y[0],z[0],vx[0],vy[0],vz[0]])

sol = odeint(satelite,z0,t)
x_s = sol[:,0]
y_s = sol[:,1]
z_s = sol[:,2]


y_1=[-5e6,0,5e6]
eje_y=["-5000","0","5000"]
x_1=[0,18000,36000,54000,72000,90000]
eje_x=["0","5","10","15","20","25"]

plt.figure()

plt.subplot(3,1,1)
plt.title("Posición")
plt.ylabel("X (KM)")

plt.plot(t,x)
plt.plot(t,x_s)
plt.yticks(y_1,eje_y)
plt.xticks(x_1,eje_x)


plt.subplot(3,1,2)
plt.ylabel("Y (KM)")
plt.plot(t,y)
plt.plot(t,y_s)
plt.yticks(y_1,eje_y)
plt.xticks(x_1,eje_x)

plt.subplot(3,1,3)
plt.ylabel("Z (KM)")
plt.xlabel("Tiempo, t(horas)")
plt.plot(t,z)
plt.plot(t,z_s)
plt.yticks(y_1,eje_y)
plt.xticks(x_1,eje_x)
plt.tight_layout()


plt.savefig("graphic_5.2.png")