# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 08:07:25 2021

@author: morita
"""

from PyQt5 import QtWidgets
from gui.gl_widget import GLWidget
from gui.histogram_widget import HistogramWidget

class GLStack(QtWidgets.QStackedWidget):
    """
    """
    def __init__(self, parent):
        super().__init__(parent)
        
        self.histogram_widget = HistogramWidget(self)
        
        self.addWidget(self.histogram_widget)
        
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        
        self.show()