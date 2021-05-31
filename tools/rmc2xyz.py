# -*- coding: utf-8 -*-
"""
Created on Mon May 31 14:01:17 2021

@author: H.Morita
"""

import core.rmc_configuration as rmc_cfg
import numpy as np

def rmc2xyz(rmc, atoms, path, title, elec):
    ''' Create XYZ file format from RMC Configuration format

    Parameters
    ----------
    rmc : RmcConfiguration class Object
        RMC Configuration
    atoms : list 
        atoms labels list
    path : string
        output file path
    title : string
        title in output file 
    elec : float
        total electron

    Returns
    -------
    None.

    '''
    with open(path, mode='w') as f:
        
        f.write("{}\n".format(rmc.nmol))
        f.write(title)
        f.write("{:10.06f}\n".format(elec))
        
        ni = 0
        for i in range(rmc.nmol_types):
            for n in range(ni, ni + rmc.ni[i]):
                f.write(atoms[i])
                v = rmc.atoms.positions[n]
                pos = np.dot(v, rmc.vectors)
                f.write(" {:8.04f}".format(pos[0]))
                f.write(" {:8.04f}".format(pos[1]))
                f.write(" {:8.04f}\n".format(pos[2]))
                    
            ni = ni + rmc.ni[i]
            
if __name__ == '__main__':
    rmc = rmc_cfg.RmcConfiguration()
    rmc.read('./sio2_h2o_md.cfg')
    rmc2xyz(rmc, ["Si", "Si", "O", "O"], "./sio2.xyz", "SiO2", 0.0)