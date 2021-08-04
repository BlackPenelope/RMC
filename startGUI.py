# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 15:31:45 2021

@author: Morita-T1700
"""
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from gui import main_window

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = main_window.MainWindow()    
    #w = QtWidgets.QWidget()
    #w.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()