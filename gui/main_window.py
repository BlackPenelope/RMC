# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 15:34:21 2021

@author: Morita-T1700
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.gl_stack import GLStack

class MainWindow(QtWidgets.QMainWindow):
    """
    Main Window Class
    
    Attributes
    ----------
    center : CentralWidget
        Central Widget
    fruit_name : str
        果物名。
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.center = CentralWidget(self)
        
        self.setCentralWidget(self.center)
                
        self.statusBar().showMessage('RMC')
        
        self.setWindowTitle('Statusbar')
        
        self.show()
        
        
class CentralWidget(QtWidgets.QWidget):
    """
    Central Widget at Main Window
    
    Attributes
    ----------
    gl_stack : GLStack
        OpenGL Graphics Widget
    
    """
    def __init__(self, parent):
        super().__init__(parent)
        
        self.init_gui()
        
    def init_gui(self):
                
        self.gl_stack = GLStack(self)
        self.combo = QtWidgets.QComboBox()
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.gl_stack)
        layout.addWidget(self.combo)

        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setLayout(layout)