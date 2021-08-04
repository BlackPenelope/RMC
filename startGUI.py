# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 15:31:45 2021

@author: Morita-T1700
"""
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from gui import main_window

#main_window.aaa()

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()