# -*- coding: utf-8 -*-
"""
Created on Mon May 24 16:56:30 2021

@author: morita
"""

import rmc_configuration as rmc_cfg
import rmc_io

rmc = rmc_cfg.RmcConfiguration()
rmc.read('./cfg/rsn100.cfg')
rmc_io.writePDB(rmc, './pdb/rsn100.pdb', ['Na', 'Si', 'O'])

rmc = rmc_cfg.RmcConfiguration()
rmc.read('./cfg/rsk100.cfg')
rmc_io.writePDB(rmc, './pdb/rsk100.pdb', ['K', 'Si', 'O'])

rmc = rmc_cfg.RmcConfiguration()
rmc.read('./cfg/rsn50k50.cfg')
rmc_io.writePDB(rmc, './pdb/rsn50k50.pdb', ['Na', 'K', 'Si', 'O'])
