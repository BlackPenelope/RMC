# -*- coding: utf-8 -*-
"""
Created on Wed May  5 14:54:58 2021

@author: morita
"""

import numpy as np

class Atoms(object):
    """
    This class represents a list of atoms and their properties: 
    """
    def __init__(self, *args):
        positions = args[0]
        elements = args[1]
        
        self.positions = np.array(positions, dtype=np.float, copy=False)
        self.number = self.positions.shape[0]
        self.elements = np.array(elements, dtype="|S4", copy=False)
