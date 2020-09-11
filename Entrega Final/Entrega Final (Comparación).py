# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 04:30:22 2020

@author: MiguelB
"""

from leer_eof import leer_eof
from numpy import sqrt
#from sys import argv

#eof_1 = argv[1]
#eof_2 = argv[2]

eof_1 = "S1B_OPER_AUX_POEORB_OPOD_20200827T111142_V20200806T225942_20200808T005942.EOF"
eof_2 = "S1B_OPER_AUX_POEORB_OPOD_20200827T111142_V20200806T225942_20200808T005942.PRED"


t1, x1, y1, z1, vx1, vy1, vz1 = leer_eof(eof_1)
t2, x2, y2, z2, vx2, vy2, vz2 = leer_eof(eof_2)

delta = sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)

print(delta[-1]/1000)