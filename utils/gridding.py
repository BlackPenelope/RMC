# -*- coding: utf-8 -*-
"""
Created on Sat May  8 13:34:31 2021

@author: H.Morita
"""

import core.rmc_configuration as rmc_cfg
import numpy as np

class Gridding(object):
    
    """
    Gridding for RMC Configuration
    """
    def __init__(self, rmc):
        self.rmc = rmc
        self.grid = None
        self.no = None
        self.gridco = None
        self.GRID_SIZE = 60
        self.MAX_NO = 200
        self.cell_width = 0.0
        
    def make_grid(self):
        
        """
        make grid table
        """
        grid_size = self.GRID_SIZE
        maxno = self.MAX_NO
        
        self.grid = np.zeros((grid_size, grid_size, grid_size, maxno), dtype=np.int)
        self.no = np.zeros((grid_size, grid_size, grid_size), dtype=np.int)
        self.gridco = np.zeros((self.rmc.nmol, 3), dtype=np.int)
        
        centres = self.rmc.atoms.positions
        vectors = self.rmc.vectors
        
        for i in range(self.rmc.nmol):
            # calculate index at grid
            ix = int((centres[i][0]+1.)*float(grid_size)/2.)+1
            iy = int((centres[i][1]+1.)*float(grid_size)/2.)+1
            iz = int((centres[i][2]+1.)*float(grid_size)/2.)+1
            ix = min(ix, grid_size)-1
            iy = min(iy, grid_size)-1
            iz = min(iz, grid_size)-1
            
            try:
                self.grid[ix,iy,iz,self.no[ix,iy,iz]] = i
                self.no[ix,iy,iz] = self.no[ix,iy,iz] + 1
                self.gridco[i,0] = ix
                self.gridco[i,1] = iy
                self.gridco[i,2] = iz
            except IndexError:
                print('Gridding error: Too many particles in grid box ({0},{1},{2})'.format(ix,iy,iz))
                raise
        
        '''
        Find shortest distance from centre of cell to a face
        '''
        triprod = vectors[0,0]*vectors[1,1]*vectors[2,2] \
                + vectors[1,0]*vectors[2,1]*vectors[0,2] \
                + vectors[2,0]*vectors[0,1]*vectors[1,2] \
                - vectors[2,0]*vectors[1,1]*vectors[0,2] \
                - vectors[1,0]*vectors[0,1]*vectors[2,2] \
                - vectors[0,0]*vectors[2,1]*vectors[1,2]
        
        axb1 = vectors[1,0]*vectors[2,1]-vectors[2,0]*vectors[1,1]
        axb2 = vectors[2,0]*vectors[0,1]-vectors[0,0]*vectors[2,1]
        axb3 = vectors[0,0]*vectors[1,1]-vectors[1,0]*vectors[0,1]
        bxc1 = vectors[1,1]*vectors[2,2]-vectors[2,1]*vectors[1,2]
        bxc2 = vectors[2,1]*vectors[0,2]-vectors[0,1]*vectors[2,2]
        bxc3 = vectors[0,1]*vectors[1,2]-vectors[1,1]*vectors[0,2]
        cxa1 = vectors[1,2]*vectors[2,0]-vectors[2,2]*vectors[1,0]
        cxa2 = vectors[2,2]*vectors[0,0]-vectors[0,2]*vectors[2,0]
        cxa3 = vectors[0,2]*vectors[1,0]-vectors[1,2]*vectors[0,0]
        
        d1 = triprod/np.sqrt(axb1**2+axb2**2+axb3**2)
        d2 = triprod/np.sqrt(bxc1**2+bxc2**2+bxc3**2)
        d3 = triprod/np.sqrt(cxa1**2+cxa2**2+cxa3**2)
        dmax = min(d1,d2,d3)
        
        if self.rmc.truncated == True:
            d1 = 1.5*triprod/np.sqrt( \
                (axb1+bxc1+cxa1)**2+(axb2+bxc2+cxa2)**2+(axb3+bxc3+cxa3)**2)
            d2 = 1.5*triprod/np.sqrt( \
                (axb1-bxc1+cxa1)**2+(axb2-bxc2+cxa2)**2+(axb3-bxc3+cxa3)**2)
            d3 = 1.5*triprod/np.sqrt( \
                (axb1+bxc1-cxa1)**2+(axb2+bxc2-cxa2)**2+(axb3+bxc3-cxa3)**2)
            d4 = 1.5*triprod/np.sqrt( \
                (axb1-bxc1-cxa1)**2+(axb2-bxc2-cxa2)**2+(axb3-bxc3-cxa3)**2)
            dmax = min(dmax,d1,d2,d3,d4)
            
        self.cell_width = 2.*dmax/float(grid_size)
        

    def neighbours(self,ic,rmax,n1,n2):
        
        """
        Finds neighbours. Returns coords in terms of unit cell vectors
        and d (distance) in real units.
        """
        
        neigh = 0
        
        try:
            ng = int(rmax/self.cell_width)+1
        except ZeroDivisionError:
            print("cell width is not calculated. execute make_grid function")
            return
        
        grid_size = self.GRID_SIZE
        centres = self.rmc.atoms.positions
        metric = self.rmc.metric
        
        gridx = self.gridco[ic,0]
        gridy = self.gridco[ic,1]
        gridz = self.gridco[ic,2]
        
        in_idx = []
        d = []
        coords = []
                
        for ix in range(gridx-ng, gridx+ng+1):
            iix = ix
            if iix < 0: iix = iix + grid_size
            if iix >= grid_size: iix = iix - grid_size

            for iy in range(gridy-ng, gridy+ng+1):
                iiy = iy
                if iiy < 0: iiy = iiy + grid_size
                if iiy >= grid_size: iiy = iiy - grid_size

                for iz in range(gridz-ng, gridz+ng+1):
                    iiz = iz
                    if iiz < 0: iiz = iiz + grid_size
                    if iiz >= grid_size: iiz = iiz - grid_size

                    for ino in range(self.no[iix,iiy,iiz]):
                        ig = self.grid[iix,iiy,iiz,ino]
                        
                        if ig >= n1 and ig <= n2 and ig != ic:
                            x = centres[ig,0] - centres[ic,0] + 3.
                            y = centres[ig,1] - centres[ic,1] + 3.
                            z = centres[ig,2] - centres[ic,2] + 3.

                            x = 2.*(x/2.-int(x/2.))-1.
                            y = 2.*(y/2.-int(y/2.))-1.
                            z = 2.*(z/2.-int(z/2.))-1.
                            
                            if self.rmc.truncated and \
                               np.abs(x)+np.abs(y)+np.abs(z) > 1.5:
                                x = x - np.sign(x)
                                y = y - np.sign(y)
                                z = z - np.sign(z)
                                
                            dd = metric[0,0]*x*x+metric[1,1]*y*y+metric[2,2]*z*z \
                               + 2.*(metric[0,1]*x*y+metric[0,2]*x*z+metric[1,2]*y*z)
                            dd = np.sqrt(dd)
                            
                            if dd < rmax:
                                neigh = neigh + 1
                                in_idx.append(ig)
                                coords.append(np.array([x,y,z]))
                                d.append(dd)
                                
        # Now sort into order
        for i in range(neigh):
            imin = i
            for j in range(i+1, neigh):
                if d[j] < d[imin]: imin = j
            
            ini = in_idx[imin]
            xd = coords[imin][0]
            yd = coords[imin][1]
            zd = coords[imin][2]
            dd = d[imin]
            in_idx[imin] = in_idx[i]
            coords[imin][0] = coords[i][0]
            coords[imin][1] = coords[i][1]
            coords[imin][2] = coords[i][2]
            d[imin] = d[i]
            in_idx[i] = ini
            coords[i][0] = xd
            coords[i][0] = yd
            coords[i][0] = zd
            d[i] = dd
        
        return neigh, in_idx, coords, d
        
if __name__ == '__main__':
    
    rmc = rmc_cfg.RmcConfiguration()
    rmc.read('./sio2.cfg')
    grid = Gridding(rmc)
    grid.make_grid()
    neigh, in_idx, coords, d = grid.neighbours(0, 2.0, 999, 2999)
    
    print(in_idx)