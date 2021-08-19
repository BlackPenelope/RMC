# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 13:48:54 2021

@author: Morita-T1700
"""
import os
import sys
import numpy as np
from core.rmc_configuration import RmcConfiguration
import utils.ncoeff as ncoeff
from utils.grsq import calc_gr
import six

dr = 0.05
qmin = 0.05
dq = 0.05
qmax = 15.0
in_file  = './example/sio.cfg'
out_file = './gr.dat'

cfg = RmcConfiguration()
cfg.read(in_file)

ntypes = cfg.nmol_types
npar = int(ntypes*(ntypes+1)/2)

symbol = ['Si', 'O']
frac = [0.333, 0.667]
norm = True
coeff = ncoeff.calc_ncoeff(symbol, frac)
print(coeff)

r, gr, gr_tot = calc_gr(cfg, dr, coeff)

fw = open(out_file, 'w')

fw.write(' Partial g(r)\'s\n')
fw.write('  r, g(r)\n')
fw.write(' PLOTS\n')
fw.write('%12d,%12d\n' % (len(r), npar))
for i in range(gr.shape[0]):
    fw.write("%16.6f" % r[i])
    for j in range(npar):
        fw.write("%16.6F" % gr[i][j])
    fw.write("\n")
fw.write(' ENDGROUP\n')

fw.close()
