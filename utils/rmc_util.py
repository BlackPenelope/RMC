# -*- coding: utf-8 -*-
"""
Created on Mon May 24 16:53:30 2021

@author: H.Morita

"""
import numpy as np
import math

def uniform_random_rotate_matrix():
    '''

    Returns
    -------
    r : matrix
        random rotate matrix

    '''
    x0 = np.random.random()
    y1 = 2*math.pi*np.random.random()
    y2 = 2*math.pi*np.random.random()
    r1 = math.sqrt(1.0-x0)
    r2 = math.sqrt(x0)
    u0 = math.cos(y2)*r2
    u1 = math.sin(y1)*r1
    u2 = math.cos(y1)*r1
    u3 = math.sin(y2)*r2
    coefi = 2.0*u0*u0-1.0
    coefuu = 2.0
    coefe = 2.0*u0
    r = np.zeros(shape=(3, 3))
    r[0, 0] = coefi+coefuu*u1*u1
    r[1, 1] = coefi+coefuu*u2*u2
    r[2, 2] = coefi+coefuu*u3*u3

    r[1, 2] = coefuu*u2*u3-coefe*u1
    r[2, 0] = coefuu*u3*u1-coefe*u2
    r[0, 1] = coefuu*u1*u2-coefe*u3

    r[2, 1] = coefuu*u3*u2+coefe*u1
    r[0, 2] = coefuu*u1*u3+coefe*u2
    r[1, 0] = coefuu*u2*u1+coefe*u3
    
    return r

def uniform_random_rotate_vector(v):
    '''    

    Parameters
    ----------
    v : vector
        rotate axis vector

    Returns
    -------
    TYPE
        random axis vector

    '''
    x0 = np.random.random()
    y1 = 2*math.pi*np.random.random()
    y2 = 2*math.pi*np.random.random()
    r1 = math.sqrt(1.0-x0)
    r2 = math.sqrt(x0)
    u0 = math.cos(y2)*r2
    u1 = math.sin(y1)*r1
    u2 = math.cos(y1)*r1
    u3 = math.sin(y2)*r2
    coefi = 2.0*u0*u0-1.0
    coefuu = 2.0
    coefe = 2.0*u0
    r = np.zeros(shape=(3, 3))
    r[0, 0] = coefi+coefuu*u1*u1
    r[1, 1] = coefi+coefuu*u2*u2
    r[2, 2] = coefi+coefuu*u3*u3

    r[1, 2] = coefuu*u2*u3-coefe*u1
    r[2, 0] = coefuu*u3*u1-coefe*u2
    r[0, 1] = coefuu*u1*u2-coefe*u3

    r[2, 1] = coefuu*u3*u2+coefe*u1
    r[0, 2] = coefuu*u1*u3+coefe*u2
    r[1, 0] = coefuu*u2*u1+coefe*u3

    return np.dot(v, r)

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    #from mpl_toolkits.mplot3d import Axes3D
    from random_rotate import uniform_random_rotate

    uvec = np.array([1,0,0])
    data = []
    for v in range(10000):
        data.append(uniform_random_rotate(uvec))
    data = np.array(data)
    
    fig = plt.figure(figsize=(15, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter3D(data[:,0:1], data[:,1:2], data[:,2:3], s=0.2)
    plt.show()
    