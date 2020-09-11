# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 14:16:10 2020

@author: MiguelB
"""

from scipy.integrate import odeint
from leer_eof import leer_eof
import numpy as np
from sys import argv

#from sys import argv
#eofname=argv[1]


eofname="S1B_OPER_AUX_POEORB_OPOD_20200827T111142_V20200806T225942_20200808T005942.EOF"


sat_t,sat_x,sat_y,sat_z,sat_vx,sat_vy,sat_vz=leer_eof(eofname)

eof_out=eofname.replace('.EOF','.PRED')
print(f'Archivo de entrada: {eofname}')
print(f'Archivo de salida: {eof_out}')


z0=np.array([sat_x[0],sat_y[0],sat_z[0],sat_vx[0],sat_vy[0],sat_vz[0]])

zf=np.array([sat_x[-1],sat_y[-1],sat_z[-1],sat_vx[-1],sat_vy[-1],sat_vz[-1]])

g = 6.6740831*(10**-11)  #Nm**2/k**2
m_t = 5.98*(10**24)  #Kg masa tierra
r_atmosfera = (6371 + 80)*1000 #metros
km = 1000
R_tierra = 6371.*km

hr = 3600             
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


sol=odeint(satelite,z0,sat_t) 
sol_ode=sol[:,:]
t=sat_t
x=sol_ode[:,0]
y=sol_ode[:,1]
z=sol_ode[:,2]
vx=sol_ode[:,3]
vy=sol_ode[:,4]
vz=sol_ode[:,5]


with open(eof_out,'w') as fout:
    fout.write('<?xml version="1.0" ?>\n'
'<Earth_Explorer_File>\n'
'  <Earth_Explorer_Header>\n'
'    <Fixed_Header>\n'
'      <File_Name>S1B_OPER_AUX_POEORB_OPOD_20200827T111142_V20200806T225942_20200808T005942</File_Name>\n'
'      <File_Description>Precise Orbit Ephemerides (POE) Orbit File</File_Description>\n'
'      <Notes></Notes>\n'
'      <Mission>Sentinel-1B</Mission>\n'
'      <File_Class>OPER</File_Class>\n'
'      <File_Type>AUX_POEORB</File_Type>\n'
'      <Validity_Period>\n'
'        <Validity_Start>UTC=2020-08-06T22:59:42</Validity_Start>\n'
'        <Validity_Stop>UTC=2020-08-08T00:59:42</Validity_Stop>\n'
'      </Validity_Period>\n'
'      <File_Version>0001</File_Version>\n'
'      <Source>\n'
'        <System>OPOD</System>\n'
'        <Creator>OPOD</Creator>\n'
'        <Creator_Version>0.0</Creator_Version>\n'
'        <Creation_Date>UTC=2020-08-27T11:11:42</Creation_Date>\n'
'      </Source>\n'
'    </Fixed_Header>\n'
'    <Variable_Header>\n'
'      <Ref_Frame>EARTH_FIXED</Ref_Frame>\n'
'      <Time_Reference>UTC</Time_Reference>\n'
'    </Variable_Header>\n'
'  </Earth_Explorer_Header>\n'
'<Data_Block type="xml">\n'
'  <List_of_OSVs count="9361">\n')
    Nt=len(t) 
    for i in range(Nt):
        fout.write('    <OSV>\n'
f'      <TAI>TAI=2020-08-06T23:00:19.000000</TAI>\n'
f'      <UTC>UTC=2020-08-06T22:59:42.000000</UTC>\n'
f'      <UT1>UT1=2020-08-06T22:59:41.796580</UT1>\n'
f'      <Absolute_Orbit>+22663</Absolute_Orbit>\n'
f'      <X unit="m">{x[i]}</X>\n'
f'      <Y unit="m">{y[i]}</Y>\n'
f'      <Z unit="m">{z[i]}</Z>\n'
f'      <VX unit="m/s">{vx[i]}</VX>\n'
f'      <VY unit="m/s">{vy[i]}</VY>\n'
f'      <VZ unit="m/s">{vz[i]}</VZ>\n'
'      <Quality>NOMINAL</Quality>\n'
'    </OSV>\n')
    fout.write('  </List_of_OSVs>\n'
'</Data_Block>\n'
'</Earth_Explorer_File>\n')


