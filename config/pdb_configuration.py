# -*- coding: utf-8 -*-
"""
Created on Wed May  5 14:52:24 2021

@author: H. Morita
"""

import sys
import os
import numpy as np
import atoms

class PdbConfiguration(object):
    
    def __init__(self):
        
        self.atoms = None
        
    def read(self, path=None):        
        self.path = path

        positions = []
        elems = []
        
        try:
            with open(path.encode("utf-8"), "r") as f:
                line = f.readline()
        
                while not("END" in line): 
                    
                    if 'HETATM' in line:                
                        items = line.split()
                        idx = int(items[1])
                        elem = items[2]
                        x = float(items[3])
                        y = float(items[4])
                        z = float(items[5])
                        
                        elems.append(elem)
                        position = np.array([x, y, z])
                        positions.append(position)
                                
                    line = f.readline()
                
                self.atoms = atoms.Atoms(positions, elems)
                
        except IOError:
            raise
        except Exception as e:
            print(e)
            pass
