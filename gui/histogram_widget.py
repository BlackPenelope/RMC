# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 15:24:06 2021

@author: morita
"""

from PyQt5 import QtCore, QtWidgets

class HistogramWidget(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.init_gui()

    def init_gui(self):
        
        vbox = QtWidgets.QVBoxLayout()
        grid = QtWidgets.QGridLayout()
        
        
        self.datasetlabel = QtWidgets.QLabel("No data loaded.", self)
        self.datasetlabel.setAlignment(QtCore.Qt.AlignHCenter)

        selectbox = QtWidgets.QHBoxLayout()
        self.cavity_type_box = QtWidgets.QComboBox(self)
        self.cavity_type_box.setMinimumWidth(180)
        selectbox.addWidget(self.cavity_type_box)
        selectbuttongroup = QtWidgets.QButtonGroup(self)
        self.volumebutton = QtWidgets.QRadioButton("Cavity Volume", self)
        selectbox.addWidget(self.volumebutton)
        selectbuttongroup.addButton(self.volumebutton)
        self.areabutton = QtWidgets.QRadioButton("Surface Area", self)
        selectbox.addWidget(self.areabutton)
        selectbuttongroup.addButton(self.areabutton)
        self.volumebutton.setChecked(True)
        grid.addLayout(selectbox, 0, 0)

        self.weightbutton = QtWidgets.QCheckBox("Weighted Histogram", self)
        self.weightbutton.setChecked(True)
        grid.addWidget(self.weightbutton, 0, 1)

        binbox = QtWidgets.QHBoxLayout()
        binbox.addWidget(QtWidgets.QLabel("Number of Bins:", self), 0)
        self.nbins = QtWidgets.QLineEdit(self)
        self.nbins.setMinimumWidth(50)
        binbox.addWidget(self.nbins, 0, QtCore.Qt.AlignLeft)
        grid.addLayout(binbox, 0, 2)

        buttonbox = QtWidgets.QHBoxLayout()

        self.plotbutton = QtWidgets.QPushButton("Plot", self)
        buttonbox.addWidget(self.plotbutton)
        #self.plotbutton.clicked.connect(self.draw)

        self.export_image_button = QtWidgets.QPushButton("Save Image", self)
        buttonbox.addWidget(self.export_image_button)
        #self.export_image_button.clicked.connect(self.export_image)

        self.export_data_button = QtWidgets.QPushButton("Export Data", self)
        buttonbox.addWidget(self.export_data_button)
        #self.export_data_button.clicked.connect(self.export_data)
        grid.addLayout(buttonbox, 1, 0, 1, 3)

        #vbox.addWidget(self.gr_widget, stretch=1)
        vbox.addWidget(self.datasetlabel, stretch=0)
        vbox.addLayout(grid)
        self.setLayout(vbox)
        self.show()
    
    def sizeHint(self):
        return QtCore.QSize(1000, 1000)