# -*- coding: utf-8 -*-
"""
Created on Tue May  4 12:04:13 2021

@author: H.Morita
"""

import core.rmc_configuration as rmc_cfg
import core.pdb_configuration as pdb_cfg
from utils.rmc_util import rmc_util
import numpy as np
from tools.rmc2xyz import rmc2xyz


rmc = rmc_cfg.RmcConfiguration()
rmc.read('./sio2_h2o_md.cfg')

#rmc2xyz(rmc, ["Si", "Si", "O", "O"], "./sio2.xyz", "SiO2", 0.0)
#rmc2xyz(rmc, ["Si", "Si", "O", "S"], "./sios.xyz", "SiO2", 0.0)

mat = rmc.vectors          # cell matrix
imat = np.linalg.inv(mat)  # cell matrix inverse

add_nmol_types = 4

pdb_path = './H2O.pdb'
pdb = pdb_cfg.PdbConfiguration()
pdb.read(pdb_path)
center_idx = 0  # add center index in pdb molecule

c = pdb.atoms.positions[center_idx]

add_vec = []
for i in range(1, pdb.atoms.number): # only H
    v = pdb.atoms.positions[i] - c
    add_vec.append(v)

add_atoms = []
ni = 0
for i in range(rmc.nmol_types):
    for n in range(ni, ni+rmc.ni[i]):
        v = rmc.atoms.positions[n]        
        
        # add atom rmc index
        if i == add_nmol_types-1:
            m = rmc_util.uniform_random_rotate_matrix()
            pos = np.dot(v, mat)  # Oxygen position
            
            for j in range(len(add_vec)):
                
                add_pos = pos + np.dot(add_vec[j], m)  # new H2O position                
                add_atoms.append(add_pos)
                
    ni = ni + rmc.ni[i]

# update nmol, ni, nsite, nmol_types, sites
# rmc.atoms.number, positions

add_number = len(add_atoms)
rmc.nmol = rmc.nmol + add_number
rmc.ni.append(add_number)
rmc.nsites.append(1)
rmc.nmol_types = rmc.nmol_types + 1

#a = np.array([0.,1.,2.,3,4,5]).reshape(2,3)
#b = np.append(a, [[6,7,8]], axis=0)
#c = np.array([[6,7,8]])
#print(c.shape) #(1,3)

for i in range(add_number):
    pos = np.dot(add_atoms[i], imat)
    position = np.array([pos])
    rmc.atoms.positions = np.append(rmc.atoms.positions, position, axis=0)

rmc.atoms.number = rmc.atoms.number + rmc.atoms.positions.shape[0]
rmc.sites.append([np.array([0., 0., 0.])])

rmc.write("./sio2_add_h2o_md.cfg")

rmc2xyz(rmc, ["Si", "Si", "O", "O", "H"], "./sio2_h2o.xyz", "SiO2H", 0.0)
