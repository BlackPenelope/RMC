# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 15:34:21 2021

@author: Morita-T1700
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    """
    Main Window Class
    
    Attributes
    ----------
    fruit_id : int
        対象の果物のマスタID。
    fruit_name : str
        果物名。
    """
    def __init__(self):
        super().__init__()
        
        #self.center = CentralWidget(self)
        # 2
        #self.setCentralWidget(self.center)
                
        self.statusBar().showMessage('RMC')
        
        self.setWindowTitle('Statusbar')
        
        self.show()
        
        
class CentralWidget(QtWidgets.QWidget):
    """
    Central Widget at Main Window
    
    Attributes
    ----------
    
    """
    def __init__(self):
        super().__init__()
        
