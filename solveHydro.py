# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 16:50:46 2021

@author: Morita-T1700
"""

import numpy as np
import scipy.optimize as opt
import utils.rmc_util as rmc_util
import sys

h2o = np.array([[0.000,0.000,0.000],
                [0.001,-0.774,-0.554],
                [-0.021,0.762,-0.570]])

oh = h2o[1] - h2o[0]
hh = h2o[2] - h2o[1]

hlx = 10.680965
hly = 10.680965
hlz = 10.680965
lx = 2*hlx
ly = 2*hly
lz = 2*hlz
cell = [lx, ly, lz]

o = np.array([ 4.85654934,10.43352976,7.10982708])

si = np.array([[ 4.48096388, 9.12741864, 6.43090222],
               [ 3.49814421,-7.83429557, 7.03538075],
               [ 2.10049721,-9.48614099, 9.21681832],
               [ 2.86527567, 9.82153183, 3.87362285],
               [ 2.50966362, 7.38300344, 8.18407581],
               [ 6.94284087, 7.26418838, 5.55446495],
               [ 3.04507904, 9.19569137,-10.59489223],
               [ 6.26840202,-7.04063578, 5.78190542],
               [ 5.98971428,10.23426568,-9.91013471],
               [ 1.57478012,-8.68096498, 4.66858572],
               [ 5.92752970,-8.03353829,-10.65191278],
               [ 8.70616138, 9.7779535 , 9.88433591],
               [ 9.41191682, 8.58510332, 7.06849174]])

for p in si:
    d = p - o
    if (d[0] > hlx): p[0] = p[0] - lx
    if (d[0] <-hlx): p[0] = p[0] + lx
    if (d[1] > hly): p[1] = p[1] - ly
    if (d[1] <-hly): p[1] = p[1] + ly
    if (d[2] > hlz): p[2] = p[2] - lz
    if (d[2] <-hlz): p[2] = p[2] + lz
    '''
    x = d[0] - lx*int(d[0]/hlx)
    y = d[1] - ly*int(d[1]/hly)
    z = d[2] - lz*int(d[2]/hlz)
    '''
    #print(p)

#sys.exit()

def func(x,o,si):
    
    #global si, o
        
    pot = 0.0
    
    # 0-H potential
    for i in range(2):
        dx = x[3*i]   - o[0]
        dy = x[3*i+1] - o[1]
        dz = x[3*i+2] - o[2]
        
        r = np.linalg.norm([dx,dy,dz])        
        
        # escape zero devide
        if (r < 1.e-8): r = 1.e-8
            
        epsilon = 1.
        sigma_oh = 0.85        
        e6 = (sigma_oh/r)**6
        
        pot = pot + 4.*epsilon*e6*(e6 - 1.)
    
    # H-H potential
    dx = x[0] - x[3]
    dy = x[1] - x[4]
    dz = x[2] - x[5]
    
    r = np.linalg.norm([dx,dy,dz])    
        
    # escape zero devide
    if (r < 1.e-8): r = 1.e-8
    
    epsilon = 1.
    sigma_hh = 1.4
    e6 = (sigma_hh/r)**6
    
    pot = pot + 4.*epsilon*e6*(e6 - 1.)    

    # Si-H potential
    for p in si:        
        for i in range(2):
            dx = x[3*i] - p[0]
            dy = x[3*i+1] - p[1]
            dz = x[3*i+2] - p[2]
            
            r = np.linalg.norm([dx,dy,dz])
            # escape zero devide
            if (r < 1.e-8): r = 1.e-8
            
            epsilon = 1.
            sigma_sih = 1.5
            e12 = (sigma_sih/r)**12
            
            pot = pot + 4.*epsilon*e12
    
    return pot

def lj(x):
    
    #n = int(x.shape[0]/2)
    
    #dx = np.array([0,0])
    dx = x[2]-x[0]
    dy = x[3]-x[1]
    r = np.linalg.norm([dx,dy])

    # escape zero devide
    if (r < 1.e-8): r = 1.e-8
        
    epsilon = 1.
    sigma = 2.    
    e6 = (sigma/r)**6
    
    return 4.*epsilon*e6*(e6 - 1.)    

# x1, y1, x2, y2
a=1.4
b=2.3
for i in range(10):
    
    m = rmc_util.uniform_random_rotate_matrix()
    vec = [h2o[1], h2o[2]]
    
    vec[0] = np.dot(vec[0], m)
    vec[1] = np.dot(vec[1], m)
    
    x = np.array(o+vec)    
    
    result = opt.minimize(func, x, method='BFGS', args=(o,si))

    print(result.fun)
    #print(result.x)


#y = np.linalg.norm(x, ord=2)

#dx = x[2]-x[0]
#dy = x[3]-x[1]

#print(dx, dy, np.sqrt(dx*dx+dy*dy))
#print(y)

#result = opt.minimize(lj, x, method='Nelder-Mead')
#result = opt.minimize(lj, x, method='BFGS')
#result = opt.minimize(func, x, method='BFGS')

#print(result.fun)
#print(result.x)
