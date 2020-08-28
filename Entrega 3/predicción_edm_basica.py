# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 16:15:28 2020

@author: MiguelB
"""


from scipy.integrate import odeint
import numpy as np



g = 6.6740831*(10**-11)  #Nm**2/k**2
m_t = 5.98*(10**24)  #Kg masa tierra
r = (6371 + 700)*1000 #metros
km = 1000
R = 6371.*km
H0 = 7071000
hr = 3600             #2 dias en segundos
omega = (2*np.pi)/(24*3600)   #2*Pi/24 horas en segundos

Fgmax = g*m_t/(R**2)




def satelite (z,T):
    #Matriz de rotación
    R = np.array([[np.cos(omega*T), -np.sin(omega*T), 0], [np.sin(omega*T), np.cos(omega*T), 0], [0, 0, 1]])

    #Primera derivada de R
    dR_dt = np.array([[-np.sin(omega*T), -np.cos(omega*T), 0], [np.cos(omega*T), -np.sin(omega*T), 0], [0, 0, 0]])*(omega)

    #Segunda derivada de R
    dR_dt2 = np.array([[-np.cos(omega*T), np.sin(omega*T), 0], [-np.sin(omega*T), -np.cos(omega*T), 0], [0, 0, 0]])*(omega**2)

    zp = np.zeros(6)
    zp[0:3] = z[3:6]
    z2 = ((-g*m_t)/(r**3))*z[0:3] - R.T@(dR_dt2@z[0:3] + 2*dR_dt@z[3:6])
    zp[3:6] = z2
    return zp

from datetime import datetime
ti = "2020-08-06T22:59:42.000000"
ti = ti.split("T")
ti = "{} {}".format(ti[0], ti[1])
ti = datetime.strptime(ti, '%Y-%m-%d %H:%M:%S.%f')

tf = "2020-08-08T00:59:42.000000"
tf = tf.split("T")
tf = "{} {}".format(tf[0], tf[1])
tf = datetime.strptime(tf, '%Y-%m-%d %H:%M:%S.%f')

deltaT = (tf - ti).total_seconds()


x_i = -392986.308753
y_i = -2227879.832739
z_i = 6694197.438184

vx_i = -2344.327333
vy_i = 6884.951903
vz_i = 2149.055260


x_f = -1817591.100957
y_f = -6839034.484849
z_f = 67373.395040

vx_f = -1509.882651
vy_f = 483.865973
vz_f = 7430.088041



T = np.linspace(0, deltaT, 9361)



vt = 6810

z0 =  np.array([x_i,y_i,z_i,vx_i,vy_i,vz_i])

sol = odeint(satelite,z0,T)

x = sol[:, :]

pos_final = np.array([x_f,y_f,z_f,vx_f,vy_f,vz_f])- sol[-1]


norma_error = (pos_final[0]**2 + pos_final[1]**2 + pos_final[2]**2)**(1/2.0)
print(norma_error)

H = (x[:, 0]**2 + x[:, 1]**2 + x[:, 2]**2)**(1/2) - R


#for i in range(3):
 #   plt.subplot(3, 1, 1+i)
  #  plt.grid(True)
   # plt.plot(T / hr, x[:, i])

#plt.figure()
#plt.grid(True)
#plt.plot(T / hr, H / km)
#plt.axhline(80., linestyle="--", color = "blue")
#plt.axhline(0.,linestyle="--", color="black", linewidth=2)
#plt.figure()
#plt.grid(True)
#plt.plot(x[:, 0], x[:,1])

#th = sp.linspace(0, 2*3.14, 400)
#plt.plot(R*sp.cos(th), R*sp.sin(th), color="green", linewidth=2)

#plt.axis("equal")




