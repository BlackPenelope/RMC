# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 12:22:53 2021

@author: morita
"""

import numpy as np

from PyQt5.QtCore import QSize
try:
    from PyQt5.QtWidgets import QOpenGLWidget
    has_qopenglwidget = True
except:
    print('Opengl not import')
    has_qopenglwidget = False

#import OpenGL.GL as gl

class GLWidget(QOpenGLWidget):
    """
    OpenGL widget to show the 3D-scene
    """
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def minimumSizeHint(self):
        return QSize(50, 50)
    
    def sizeHint(self):
        return QSize(400, 400)
    
    def initializeGL(self):
        print('initialize GL')
        
    def paintGL(self):
        pass
        #gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    
    