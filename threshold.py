# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 14:15:52 2021

@author: Morita-T1700
"""

import numpy as np
from pyevtk.hl import gridToVTK
import core.rmc_configuration as rmc_cfg
from tools.rmc2xyz import rmc2xyz

rmc = rmc_cfg.RmcConfiguration()
rmc.read('./sample/rsn100.cfg')

rmc2xyz(rmc, ["Na", "Si", "O"], "./na2o-sio2.xyz", "22.7Na2O-77.3SiO2", 0.0)



'''
ix = 128
jx = 128
kx = 128

xmin = 0.
xmax = 1.
ymin = 0.
ymax = 1.
zmin = 0.
zmax = 1.

dx = (xmax-xmin)/ix
dy = (ymax-ymin)/jx
dz = (zmax-zmin)/kx

x = xmin + 0.5*dx + np.arange(ix)*dx
y = ymin + 0.5*dy + np.arange(jx)*dy
z = zmin + 0.5*dz + np.arange(kx)*dz

xx,yy,zz = np.meshgrid(x,y,z)

ds = 0.1

x0 = (xmax+xmin)/2.
y0 = (ymax+ymin)/2.
z0 = (zmax+zmin)/2.

amp = 1.0

rr = (xx-x0)**2+(yy-y0)**2+(zz-z0)**2
#qq = amp*np.exp(-rr/(2.*ds**2))
qq = amp*np.exp(-rr/(2.*ds*2))

gridToVTK('./test',x,y,z,pointData={'quantity':qq})
'''