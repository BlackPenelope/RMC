# -*- coding: utf-8 -*-
"""
Created on Mon May 31 14:31:06 2021

@author: H.Morita
"""

import core.rmc_configuration as rmc_cfg
import core.atoms
import numpy as np
import os
import os.path
import sys

class XyzConfiguration(object):
    
    def __init__(self):
        
        self.atoms = None
        self.vectors = None
        
    def convert(self, rmc, elem):
        
        mat = rmc.vectors          # cell matrix
        positions = []   
        elems = []
        
        self.vectors = rmc.vectors * 2.
                
        nmol = 0
        for i in range(rmc.nmol_types):
            for ni in range(rmc.ni[i]):
                n = nmol + ni
                v = rmc.atoms.positions[n]
                pos = np.dot(v, mat)
                #print(pos)
                positions.append(pos)
                elems.append(elem[i])
                
            nmol = nmol + rmc.ni[i]
        
        self.atoms = core.atoms.Atoms(positions, elems)        

    def write(self, path, title, elec):
                        
        with open(path, mode='w') as f:            
        
            f.write("{}\n".format(self.atoms.number))
            f.write(title)
            f.write("{:10.06f}\n".format(elec))
                        
            ni = 0
            for i in range(self.atoms.number):   
                f.write(self.atoms.elements[i].decode('utf-8'))
                pos = self.atoms.positions[i]                
                f.write(" {:8.04f}".format(pos[0]))
                f.write(" {:8.04f}".format(pos[1]))
                f.write(" {:8.04f}\n".format(pos[2]))


if __name__ == '__main__':
    rmc = rmc_cfg.RmcConfiguration()
    rmc.read("../sio2_h2o_md.cfg")
    xyz = XyzConfiguration()
    xyz.convert(rmc, ['Si', 'Si', 'O', 'O'])
    xyz.write('../a.xyz', 'convert', 0.0)