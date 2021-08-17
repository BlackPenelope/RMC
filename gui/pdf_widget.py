# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 15:49:38 2021

@author: morita
"""

from PyQt5 import QtCore, QtWidgets

class PDFWidget(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.init_gui()
        
    def init_gui(self):
        pass
        