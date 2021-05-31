# -*- coding: utf-8 -*-
"""
Created on Mon May 24 16:53:30 2021

@author: H.Morita
"""

import rmc_configuration as rmc_cfg
import numpy as np

def writePDB(rmc_cfg, path, atoms):
    '''
    RMC Configuration file format -> PDB file format

    Parameters
    ----------
    rmc_cfg : RmcConfiguration class object
        RMC Configuration class object
    path : string
        .pdb file path name
    atoms : list
        atoms list

    Returns
    -------
    None.

    '''
    
    
    with open(path, mode='w') as f:
        
        mol_type = 0
        mol = rmc_cfg.ni[mol_type]
        
        for n in range(rmc_cfg.nmol):                
            if n >= mol:
                mol_type = mol_type + 1
                mol = mol + rmc_cfg.ni[mol_type]            
                
            v = rmc_cfg.atoms.positions[n]
            pos = np.dot(v, rmc_cfg.vectors)
            
            f.write("HETATM")            
            f.write("{:>5d}".format(n + 1))
            f.write("  ")
            f.write("{:<7s}".format(atoms[mol_type]))
            f.write("          ")
            f.write('{:8.03f}'.format(pos[0]))
            f.write('{:8.03f}'.format(pos[1]))
            f.write('{:8.03f}'.format(pos[2]))            
            f.write("\n")
            
        f.write("END\n")

        
        
    
    