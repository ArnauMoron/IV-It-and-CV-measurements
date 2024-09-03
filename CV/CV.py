# This Python file uses the following encoding: utf-8
import sys, time, os
import numpy as np
import datetime

import logging

from PyQt5 import QtCore, QtGui, QtWidgets

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import configparser as ConfigParser

import pyvisa as visa



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1177, 1040)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.temp_vertical_layout = QtWidgets.QVBoxLayout()
        self.temp_vertical_layout.setObjectName("temp_vertical_layout")
        self.settings = QtWidgets.QGroupBox(self.centralwidget)
        self.settings.setObjectName("settings")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.settings)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_3 = QtWidgets.QWidget(self.settings)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pb_settingsDefault = QtWidgets.QPushButton(self.widget_3)
        self.pb_settingsDefault.setObjectName("pb_settingsDefault")
        self.verticalLayout_10.addWidget(self.pb_settingsDefault)
        self.pb_scanDevices = QtWidgets.QPushButton(self.widget_3)
        self.pb_scanDevices.setObjectName("pb_scanDevices")
        self.verticalLayout_10.addWidget(self.pb_scanDevices)
        self.verticalLayout_4.addWidget(self.widget_3)

        self.groupBox_14 = QtWidgets.QGroupBox(self.settings)
        self.groupBox_14.setObjectName("groupBox_14")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.groupBox_14)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.sb_vwait = QtWidgets.QDoubleSpinBox(self.groupBox_14)
        self.sb_vwait.setDecimals(1)
        self.sb_vwait.setMinimum(0.1)
        self.sb_vwait.setMaximum(100.0)
        self.sb_vwait.setObjectName("sb_vwait")
        self.horizontalLayout_12.addWidget(self.sb_vwait)
        self.label_15 = QtWidgets.QLabel(self.groupBox_14)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_12.addWidget(self.label_15)
        self.horizontalLayout_12.setStretch(0, 2)
        self.verticalLayout_4.addWidget(self.groupBox_14)

        self.groupBox_14_1 = QtWidgets.QGroupBox(self.settings)
        self.groupBox_14_1.setObjectName("groupBox_14_1")
        self.horizontalLayout_12_1 = QtWidgets.QHBoxLayout(self.groupBox_14_1)
        self.horizontalLayout_12_1.setObjectName("horizontalLayout_12_1")
        self.sb_osc = QtWidgets.QSpinBox(self.groupBox_14)
        self.sb_osc.setMaximum(42000)
        self.sb_osc.setObjectName("sb_osc")
        self.horizontalLayout_12_1.addWidget(self.sb_osc)
        self.label_15_1 = QtWidgets.QLabel(self.groupBox_14_1)
        self.label_15_1.setObjectName("label_15_1")
        self.horizontalLayout_12_1.addWidget(self.label_15_1)
        self.horizontalLayout_12_1.setStretch(0, 2)
        self.verticalLayout_4.addWidget(self.groupBox_14_1)
        


        self.CVsettings = QtWidgets.QGroupBox(self.centralwidget)
        self.CVsettings.setObjectName("CVsettings")
        self.verticalLayout_4_1 = QtWidgets.QVBoxLayout(self.CVsettings)
        self.verticalLayout_4_1.setObjectName("verticalLayout_4_1")
        
        self.groupBox_9_1 = QtWidgets.QGroupBox(self.CVsettings)
        self.groupBox_9_1.setObjectName("groupBox_9_1")
        self.horizontalLayout_5_1 = QtWidgets.QHBoxLayout(self.groupBox_9_1)
        self.horizontalLayout_5_1.setObjectName("horizontalLayout_5_1")
        self.sb_simpleCV = QtWidgets.QDoubleSpinBox(self.groupBox_9_1)
        self.sb_simpleCV.setMinimum(0.01)
        self.sb_simpleCV.setMaximum(1000.0)
        self.sb_simpleCV.setObjectName("sb_simpleCV")
        self.horizontalLayout_5_1.addWidget(self.sb_simpleCV)
        self.label_10_1 = QtWidgets.QLabel(self.groupBox_9_1)
        self.label_10_1.setObjectName("label_10_1")
        self.horizontalLayout_5_1.addWidget(self.label_10_1)
        self.horizontalLayout_5_1.setStretch(0, 2)
        self.verticalLayout_4_1.addWidget(self.groupBox_9_1)

        self.groupBox_9 = QtWidgets.QGroupBox(self.CVsettings)
        self.groupBox_9.setObjectName("groupBox_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.sb_v0 = QtWidgets.QDoubleSpinBox(self.groupBox_9)
        self.sb_v0.setMinimum(-1100.0)
        self.sb_v0.setMaximum(1100.0)
        self.sb_v0.setObjectName("sb_v0")
        self.horizontalLayout_5.addWidget(self.sb_v0)
        self.label_10 = QtWidgets.QLabel(self.groupBox_9)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.horizontalLayout_5.setStretch(0, 2)
        self.verticalLayout_4.addWidget(self.groupBox_9)

        self.groupBox_10 = QtWidgets.QGroupBox(self.CVsettings)
        self.groupBox_10.setObjectName("groupBox_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.sb_vmax = QtWidgets.QDoubleSpinBox(self.groupBox_10)
        self.sb_vmax.setMinimum(-1100.0)
        self.sb_vmax.setMaximum(1100.0)
        self.sb_vmax.setObjectName("sb_vmax")
        self.horizontalLayout_8.addWidget(self.sb_vmax)
        self.label_11 = QtWidgets.QLabel(self.groupBox_10)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        self.horizontalLayout_8.setStretch(0, 2)
        self.verticalLayout_4.addWidget(self.groupBox_10)

        self.groupBox_11 = QtWidgets.QGroupBox(self.CVsettings)
        self.groupBox_11.setObjectName("groupBox_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.sb_vstep = QtWidgets.QDoubleSpinBox(self.groupBox_11)
        self.sb_vstep.setMaximum(1000)
        self.sb_vstep.setObjectName("sb_vstep")
        self.horizontalLayout_11.addWidget(self.sb_vstep)
        self.verticalLayout_4.addWidget(self.groupBox_11)
        
        
        
        self.groupBox_17 = QtWidgets.QGroupBox(self.settings)
        self.groupBox_17.setObjectName("groupBox_17")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.groupBox_17)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.sb_vaverage = QtWidgets.QSpinBox(self.groupBox_17)
        self.sb_vaverage.setMaximum(100)
        self.sb_vaverage.setObjectName("sb_vaverage")
        self.horizontalLayout_14.addWidget(self.sb_vaverage)
        self.verticalLayout_4.addWidget(self.groupBox_17)

        self.groupBox_13 = QtWidgets.QGroupBox(self.settings)
        self.groupBox_13.setObjectName("groupBox_13")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBox_13)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.sb_vrampup = QtWidgets.QDoubleSpinBox(self.groupBox_13)
        self.sb_vrampup.setMaximum(100.0)
        self.sb_vrampup.setObjectName("sb_vrampup")
        self.horizontalLayout_9.addWidget(self.sb_vrampup)
        self.label_13 = QtWidgets.QLabel(self.groupBox_13)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_9.addWidget(self.label_13)
        self.horizontalLayout_9.setStretch(0, 2)
        self.verticalLayout_4.addWidget(self.groupBox_13)

        self.groupBox_12 = QtWidgets.QGroupBox(self.settings)
        self.groupBox_12.setObjectName("groupBox_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.sb_vrampdown = QtWidgets.QDoubleSpinBox(self.groupBox_12)
        self.sb_vrampdown.setMaximum(100.0)
        self.sb_vrampdown.setObjectName("sb_vrampdown")
        self.horizontalLayout_10.addWidget(self.sb_vrampdown)
        self.label_14 = QtWidgets.QLabel(self.groupBox_12)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_10.addWidget(self.label_14)
        self.horizontalLayout_10.setStretch(0, 2)
        self.verticalLayout_4.addWidget(self.groupBox_12)

        self.groupBox_8 = QtWidgets.QGroupBox(self.settings)
        self.groupBox_8.setObjectName("groupBox_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.sb_current = QtWidgets.QDoubleSpinBox(self.groupBox_8)
        self.sb_current.setMaximum(1000000)
        self.sb_current.setObjectName("sb_current")
        self.horizontalLayout_7.addWidget(self.sb_current)
        self.label_8 = QtWidgets.QLabel(self.groupBox_8)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.horizontalLayout_7.setStretch(0, 2)
        self.verticalLayout_4.addWidget(self.groupBox_8)

        self.groupBox_7 = QtWidgets.QGroupBox(self.settings)
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.sb_temperature = QtWidgets.QDoubleSpinBox(self.groupBox_7)
        self.sb_temperature.setMinimum(-100.0)
        self.sb_temperature.setMaximum(100.0)
        self.sb_temperature.setProperty("value", 0.0)
        self.sb_temperature.setObjectName("sb_temperature")
        self.horizontalLayout_6.addWidget(self.sb_temperature)
        self.label_7 = QtWidgets.QLabel(self.groupBox_7)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.horizontalLayout_6.setStretch(0, 2)
        self.verticalLayout_4.addWidget(self.groupBox_7)
        self.temp_vertical_layout.addWidget(self.settings)
        self.temp_vertical_layout.addWidget(self.CVsettings)
        self.horizontalLayout.addLayout(self.temp_vertical_layout)       
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.device = QtWidgets.QWidget(self.widget)
        self.device.setObjectName("device")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.device)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gb_supplies = QtWidgets.QGroupBox(self.device)
        self.gb_supplies.setObjectName("gb_supplies")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.gb_supplies)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.list_devices = QtWidgets.QListWidget(self.gb_supplies)
        self.list_devices.setObjectName("list_devices")
        self.verticalLayout_8.addWidget(self.list_devices)
        self.verticalLayout_7.addWidget(self.gb_supplies)               
        self.CVswipeSettings = QtWidgets.QGroupBox(self.device)
        self.CVswipeSettings.setObjectName("CVswipeSettings")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.CVswipeSettings)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupbox_f0 = QtWidgets.QGroupBox(self.CVswipeSettings)
        self.groupbox_f0.setObjectName("groupbox_f0")
        self.horizontalLayout_f0 = QtWidgets.QHBoxLayout(self.groupbox_f0)
        self.horizontalLayout_f0.setObjectName("horizontalLayout_f0")
        self.sb_f0 = QtWidgets.QDoubleSpinBox(self.groupbox_f0)
        self.sb_f0.setRange(0.01,1000)
        self.sb_f0.setObjectName("sb_f0")
        self.horizontalLayout_f0.addWidget(self.sb_f0)
        self.label_12_1 = QtWidgets.QLabel(self.groupbox_f0)
        self.label_12_1.setObjectName("label_12_1")
        self.horizontalLayout_f0.addWidget(self.label_12_1)
        self.verticalLayout_5.addWidget(self.groupbox_f0)
        self.groupbox_f1 = QtWidgets.QGroupBox(self.CVswipeSettings)
        self.groupbox_f1.setObjectName("groupbox_f1")
        self.horizontalLayout_f1 = QtWidgets.QHBoxLayout(self.groupbox_f1)
        self.horizontalLayout_f1.setObjectName("horizontalLayout_f1")
        self.sb_f1 = QtWidgets.QDoubleSpinBox(self.groupbox_f1)
        self.sb_f1.setMinimum(0.01)
        self.sb_f1.setMaximum(1000)
        self.sb_f1.setObjectName("sb_f1")
        self.horizontalLayout_f1.addWidget(self.sb_f1)
        self.label_12 = QtWidgets.QLabel(self.groupbox_f1)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_f1.addWidget(self.label_12)
        self.verticalLayout_5.addWidget(self.groupbox_f1)
        self.groupbox_freq_step = QtWidgets.QGroupBox(self.CVswipeSettings)
        self.groupbox_freq_step.setObjectName("groupbox_freq_step")
        self.horizontalLayout_freq_step = QtWidgets.QHBoxLayout(self.groupbox_freq_step)
        self.horizontalLayout_freq_step.setObjectName("horizontalLayout_freq_step")
        self.sb_freq_step = QtWidgets.QDoubleSpinBox(self.groupbox_freq_step)
        self.sb_freq_step.setRange(0,100)
        self.sb_freq_step.setSingleStep(1)  
        self.sb_freq_step.setObjectName("sb_freq_step")
        self.horizontalLayout_freq_step.addWidget(self.sb_freq_step)
        self.label_12_freq_step = QtWidgets.QLabel(self.groupbox_freq_step)
        self.label_12_freq_step.setObjectName("label_12_freq_step")
        self.horizontalLayout_freq_step.addWidget(self.label_12_freq_step)
        self.verticalLayout_5.addWidget(self.groupbox_freq_step)
        self.verticalLayout_7.addWidget(self.CVswipeSettings)
        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 1)
        self.verticalLayout_2.addWidget(self.device)
        self.control = QtWidgets.QWidget(self.widget)
        self.control.setObjectName("control")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.control)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox = QtWidgets.QGroupBox(self.control)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.le_path = QtWidgets.QLineEdit(self.groupBox_2)
        self.le_path.setObjectName("le_path")
        self.horizontalLayout_3.addWidget(self.le_path)
        self.pb_browse = QtWidgets.QPushButton(self.groupBox_2)
        self.pb_browse.setObjectName("pb_browse")
        self.horizontalLayout_3.addWidget(self.pb_browse)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.le_name = QtWidgets.QLineEdit(self.groupBox_3)
        self.le_name.setObjectName("le_name")
        self.horizontalLayout_4.addWidget(self.le_name)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.verticalLayout_6.addWidget(self.groupBox)
        self.gb_scans = QtWidgets.QGroupBox(self.control)
        self.gb_scans.setObjectName("gb_scans")
        self.gridLayout = QtWidgets.QGridLayout(self.gb_scans)
        self.gridLayout.setObjectName("gridLayout")
        self.pb_swipe = QtWidgets.QPushButton(self.gb_scans)
        self.pb_swipe.setMinimumSize(QtCore.QSize(0, 50))
        self.pb_swipe.setObjectName("pb_swipe")
        self.gridLayout.addWidget(self.pb_swipe, 1, 0, 2, 2)
        self.pb_simpleCV = QtWidgets.QPushButton(self.gb_scans)
        self.pb_simpleCV.setMinimumSize(QtCore.QSize(0, 50)) 
        self.pb_simpleCV.setObjectName("pb_simpleCV")
        self.gridLayout.addWidget(self.pb_simpleCV,3, 0, 2, 2)    
        self.verticalLayout_6.addWidget(self.gb_scans)
        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 1)
        self.verticalLayout_2.addWidget(self.control)
        self.pb_stop = QtWidgets.QPushButton(self.widget)
        self.pb_stop.setMinimumSize(QtCore.QSize(0, 55))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pb_stop.setFont(font)
        self.pb_stop.setAutoFillBackground(True)
        self.pb_stop.setObjectName("pb_stop")
        self.verticalLayout_2.addWidget(self.pb_stop)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 1)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_6 = QtWidgets.QWidget(self.widget_2)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout.addWidget(self.widget_6)
        self.widget_6.hide()
        self.graphics_frame = QtWidgets.QWidget(self.widget_2)
        self.graphics_frame.setObjectName("graphics_frame")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.graphics_frame)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.graphics = QtWidgets.QWidget(self.graphics_frame)
        self.graphics.setObjectName("graphics")
        self.horizontalLayout_21.addWidget(self.graphics)
        self.list_plots = QtWidgets.QListWidget(self.graphics_frame)
        self.list_plots.setObjectName("list_plots")
        self.list_plots.hide()
        self.verticalLayout.addWidget(self.graphics_frame)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.outputColor = QtWidgets.QLabel(self.widget_4)
        self.outputColor.setMinimumSize(QtCore.QSize(10, 0))
        self.outputColor.setMaximumSize(QtCore.QSize(16777215, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.outputColor.setPalette(palette)
        self.outputColor.setAutoFillBackground(True)
        self.outputColor.setText("")
        self.outputColor.setObjectName("outputColor")
        self.horizontalLayout_2.addWidget(self.outputColor)
        self.label = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.outputText = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.outputText.setFont(font)
        self.outputText.setObjectName("outputText")
        self.horizontalLayout_2.addWidget(self.outputText)
        self.voltage_reading = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.voltage_reading.setFont(font)
        self.voltage_reading.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.voltage_reading.setObjectName("voltage_reading")
        self.horizontalLayout_2.addWidget(self.voltage_reading)
        self.label_9 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.current_reading = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.current_reading.setFont(font)
        self.current_reading.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.current_reading.setObjectName("current_reading")
        self.horizontalLayout_2.addWidget(self.current_reading)
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 2)
        self.horizontalLayout_2.setStretch(4, 1)
        self.horizontalLayout_2.setStretch(5, 2)
        self.horizontalLayout_2.setStretch(6, 1)
        self.verticalLayout.addWidget(self.widget_4)
        self.progressBar = QtWidgets.QProgressBar(self.widget_2)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget_2)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.plainTextEdit.hide() #to show all the prints that appear in the code just delete hide()
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 2)
        self.horizontalLayout.addWidget(self.widget_2)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1177, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "CV and CVswipe measurement"))
        self.settings.setTitle(_translate("MainWindow", "Global Settings"))
        self.CVsettings.setTitle(_translate("MainWindow", "CV Settings"))
        self.gb_supplies.setTitle(_translate("MainWindow", "Connected power supplies"))
        self.CVswipeSettings.setTitle(_translate("MainWindow", "CV swipe Settings"))
        self.groupBox.setTitle(_translate("MainWindow", "Data operations"))
        self.gb_scans.setTitle(_translate("MainWindow", "Run "))
        self.settings.setStyleSheet("QGroupBox#settings { font-weight: bold; }")
        self.CVsettings.setStyleSheet("QGroupBox#CVsettings { font-weight: bold; }")
        self.gb_supplies.setStyleSheet("QGroupBox#gb_supplies { font-weight: bold; }")
        self.CVswipeSettings.setStyleSheet("QGroupBox#CVswipeSettings { font-weight: bold; }")
        self.groupBox.setStyleSheet("QGroupBox#groupBox { font-weight: bold; }")
        self.gb_scans.setStyleSheet("QGroupBox#gb_scans { font-weight: bold; }")
        self.pb_settingsDefault.setText(_translate("MainWindow", "Reset Defaults"))
        self.pb_scanDevices.setText(_translate("MainWindow", "Scan Devices"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Voltage start"))
        self.groupBox_9_1.setTitle(_translate("MainWindow", "Frequency"))
        self.label_10_1.setText(_translate("MainWindow", "kHz"))
        self.label_10.setText(_translate("MainWindow", "V"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Voltage stop"))
        self.label_11.setText(_translate("MainWindow", "V"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Voltage step (V)"))
        self.groupBox_14.setTitle(_translate("MainWindow", "Stabilization time"))
        self.groupBox_14_1.setTitle(_translate("MainWindow", "Oscilation level"))
        self.label_15.setText(_translate("MainWindow", "s"))
        self.label_15_1.setText(_translate("MainWindow", "mV"))
        self.groupBox_17.setTitle(_translate("MainWindow", "Measurements per point"))
        self.groupBox_13.setTitle(_translate("MainWindow", "Ramp up speed"))
        self.label_13.setText(_translate("MainWindow", "V/s"))
        self.groupBox_12.setTitle(_translate("MainWindow", "Ramp down speed"))
        self.label_14.setText(_translate("MainWindow", "V/s"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Compliance"))
        self.label_8.setText(_translate("MainWindow", "uA"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Temperature"))
        self.label_7.setText(_translate("MainWindow", "°C"))
        self.groupbox_f1.setTitle(_translate("MainWindow", "CV swipe END "))
        self.groupbox_freq_step.setTitle(_translate("MainWindow", "Frequency step "))
        self.groupbox_f0.setTitle(_translate("MainWindow", "CV swipe START"))
        self.label_12.setText(_translate("MainWindow", "kHz"))
        self.label_12_freq_step.setText(_translate("MainWindow", "kHz"))
        self.label_12_1.setText(_translate("MainWindow", "kHz"))
        self.pb_simpleCV.setText(_translate("MainWindow", "RUN CV"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Path"))
        self.pb_browse.setText(_translate("MainWindow", "Browse"))
        self.groupBox_3.setTitle(_translate("MainWindow", "File name"))
        self.label_5.setText(_translate("MainWindow", ""))
        self.label_6.setText(_translate("MainWindow", "_FREQ_kHz_CV_date_time.dat"))
        self.pb_swipe.setText(_translate("MainWindow", "RUN CV swipe"))
        self.pb_stop.setText(_translate("MainWindow", "ABORT"))
        self.label.setText(_translate("MainWindow", "Output "))
        self.outputText.setText(_translate("MainWindow", "OFF"))
        self.voltage_reading.setText(_translate("MainWindow", "nan"))
        self.label_9.setText(_translate("MainWindow", "V"))
        self.current_reading.setText(_translate("MainWindow", "nan"))
        self.label_4.setText(_translate("MainWindow", "uA"))




class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    plotData    = QtCore.pyqtSignal(str, np.ndarray, np.ndarray)
    enableScan  = QtCore.pyqtSignal(bool)
    enableTest  = QtCore.pyqtSignal(bool)
    scan_CV  = QtCore.pyqtSignal()
    scan_CVswipe = QtCore.pyqtSignal()

    

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent=parent)
        self.setupUi(self)
        self.scanner = None
        self.devices = []
        self.devicesEnabled = []
        self.lastPlot = datetime.datetime.now().timestamp()

        self.initialize()

    def initialize(self):
        self.setupLogger()
        self.device.setEnabled(True)   
        self.gb_supplies.setEnabled(False)
        
        self.CVswipeSettings.setEnabled(True) 
        self.CVsettings.setEnabled(True)
        
        self.sb_temperature.setValue(20)
        self.sb_osc.setValue(500)
        self.temperature=20
        self.sb_vwait.setValue(0.2)
        
        self.sb_current.setValue(10)
        
        
        
        self.sb_freq_step.setValue(20)
        self.sb_f0.setValue(40)
        self.sb_f1.setValue(100)
        self.f0=20
        self.f1=100       
        self.freq_step=10
        
        self.sb_simpleCV.setValue(20)
        self.simpleCV=20
        
        
        
        self.configPath = self.resource_path("config.cfg")
        self.initCommands()
        self.scannerCommands()
        
        
        
        self.defaultDevices()

        self.path     = ""
        self.pathSet  = False
        self.setName("")

        self.running_CV = False
        self.running_swipe = False


        self.enableScan.emit(False)
        self.enableTest.emit(False)
        
    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS 
        except AttributeError:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)



    def defaultPlotter(self):
        print("Setting default plotter")
        self.initPlotter()
        self.selectPlots()

    def initPlotter(self):
        self.layoutPlot = QtWidgets.QVBoxLayout()
        self.scales = {'lin':'linear', 'log':'symlog'}
        self.startPlotter()
        self.plotterCommands()

        self.list_plots.clear()
        
        for i in np.arange(len(self.names)):
            item = QtWidgets.QListWidgetItem(self.names[i])
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Checked)
            self.list_plots.addItem(item)

    def selectPlots(self):
        print("Reinitializing selected plots")
        self.plotsEnabled = []
        print("List of visible plots: ")
            
        self.plotter.visiblePlots = self.plotsEnabled

       
    def startPlotter(self):
        self.plotter = Plotter(plots = self.names, parent = self.graphics)
        self.layoutPlot.addWidget(self.plotter)
        self.graphics.setLayout(self.layoutPlot)

    def defaultDevices(self):
        print("Setting default devices")
        self.initSettings()
        self.initDevices()
        self.selectDevices()
        self.clearData()
        self.defaultPlotter()

    def initSettings(self):
        self.config  = ParseConfig(self.configPath)

        self.sb_v0       .setValue(self.config[1]['v0'])
        self.sb_vmax     .setValue(self.config[1]['vmax'])
        self.sb_vstep    .setValue(self.config[1]['vsteps'])
        self.sb_vrampup  .setValue(self.config[1]['vrampup'])
        self.sb_vrampdown.setValue(self.config[1]['vrampdown'])
        self.sb_vwait    .setValue(self.config[1]['vwait'])
        self.sb_vaverage .setValue(self.config[1]['vaverage'])

    def initDevices(self):
        config  = ParseConfig(self.configPath)

        self.list_devices.clear()
        self.devices = ListDevices(config[0])
        self.names=[]
        for i in np.arange(len(self.devices)):
            name = self.devices[i].GetName()
            self.names.append(name)
            item = QtWidgets.QListWidgetItem(name)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Checked)
            self.list_devices.addItem(item)
        

    def selectDevices(self):
        print("Reinitializing selected supplies")
        self.devicesEnabled = []
        print("List of used supplies: ")
        for i in np.arange(len(self.devices)):
            item = self.list_devices.item(i)
            if (item.checkState() == QtCore.Qt.Checked):
                print(" " + str(self.devices[i].GetName()))
                self.devicesEnabled.append(self.devices[i])
        self.startDevices()
        self.scannerCommands()

    def startDevices(self):
        try:
            if self.scanner is None:
                print("Creating new scanner instance")
                self.scanner = Scanner(self.devicesEnabled, settings=self.config[1], parent=self)
            else:
                self.scanner.setDevices(self.devicesEnabled)
                self.scanner.setSettings(self.config[1])
            
            self.scanner.setCurrentLimit(self.sb_current.value())
            self.scanner.setCurrentRange()
        except:
            print('error')
            self.scanner = None

    def signalReconnect(self, signal, newhandler=None, oldhandler=None, force=False):
        while True:
            try:
                if force:
                    signal.disconnect()

                if oldhandler is not None:
                    signal.disconnect(oldhandler)
                elif newhandler is not None:
                    signal.disconnect(newhandler)
            except TypeError:
                break
        if newhandler is not None:
            signal.connect(newhandler)

    def initCommands(self):
        TextStream.stdout().textWritten.connect( self.appendText )

        self.sb_v0       .valueChanged.connect(self.setCVStart)
        self.sb_vmax     .valueChanged.connect(self.setCVStop)
        self.sb_vstep    .valueChanged.connect(self.setCVSteps)
        self.sb_vrampup  .valueChanged.connect(self.setCVrampUp)
        self.sb_vrampdown.valueChanged.connect(self.setCVrampDown)
        self.sb_vwait    .valueChanged.connect(self.setCVwait)
        self.sb_vaverage .valueChanged.connect(self.setCVaverage)
        
        
        self.pb_simpleCV.pressed.connect(lambda: self.startCV())
        
        self.pb_swipe.pressed.connect(lambda:self.start_swipe())


        self.pb_settingsDefault.pressed.connect(self.defaultDevices)
        self.pb_scanDevices.pressed.connect(lambda:[self.initSettings()] + [self.initDevices()]+ [self.selectDevices()]+ [self.clearData()])
        self.list_devices.itemChanged.connect(self.selectDevices)


        self.pb_browse.pressed.connect(self.browsePath)
        self.le_path.textChanged.connect(self.setPath)
        self.le_name.textChanged.connect(self.setName)
        self.enableScan.connect(self.setScanEnabled)
        self.enableTest.connect(self.setTestEnabled)

        
        
       


        
        self.pb_stop.pressed.connect(self.Stop)


        self.sb_f1.valueChanged.connect(self.setf1)
        
        self.sb_freq_step.valueChanged.connect(self.setfreq_step)
        
        self.sb_f0.valueChanged.connect(self.setf0)
        self.sb_osc.valueChanged.connect(self.set_osc)
        

        self.sb_simpleCV.valueChanged.connect(self.setFreq)
        
        self.sb_temperature.valueChanged.connect(self.setGlobalTemperature)

        self.list_plots.itemChanged.connect(self.selectPlots)

    def scannerCommands(self):
        if self.scanner is not None:
            
            
            self.signalReconnect(self.scan_CV, self.scanner.simple_CV)
            self.signalReconnect(self.scan_CVswipe, self.scanner.swipe)

       

            self.signalReconnect(self.sb_current.valueChanged, self.scanner.setCurrentLimit)
            self.signalReconnect(self.sb_current.valueChanged, self.scanner.setCurrentRange)

            self.signalReconnect(self.scanner.scanDone, self.stopped)
            self.signalReconnect(self.scanner.realfreq, self.applyFreq)

            self.signalReconnect(self.scanner.saveData, self.saveFile)

            self.signalReconnect(self.scanner.text, self.receiveText)
            self.signalReconnect(self.scanner.progress, self.receiveProgress)
            self.signalReconnect(self.scanner.measured, self.receiveData)
            
            self.signalReconnect(self.scanner.reset, self.reset)
            self.signalReconnect(self.scanner.updateplots, self.updateplots)
            

            self.signalReconnect(self.scanner.outputOn , lambda: self.setOutputStatus('ON' , QtCore.Qt.green), force=True)
            self.signalReconnect(self.scanner.outputOff, lambda: self.setOutputStatus('OFF', QtCore.Qt.red  ), force=True)

            
    def plotterCommands(self):
        self.signalReconnect(self.plotData, self.plotter.receiveData)

    def receiveText(self, text):
        print(text)

    def receiveProgress(self, value):
        self.progressBar.setValue(value)

    def clearData(self, name = None):
        if name is None:
            self.voltage = {str(name):np.array([[],[]]) for name in self.names}
            self.current = {str(name):np.array([[],[],[],[]]) for name in self.names}
            self.ntc     = {str(name):np.array([])      for name in self.names}
            self.time    = {str(name):np.array([[],[]]) for name in self.names}
            self.capacitance = {str(name):np.array([[],[]]) for name in self.names}
            self.conductance ={str(name):np.array([[],[]]) for name in self.names}
        if name in self.names:
            self.voltage[name] = np.array([[],[]])
            self.current[name] = np.array([[],[],[],[]])
            self.ntc[name]     = np.array([])
            self.time[name]    = np.array([[],[]])
            self.capacitance[name]=np.array([[],[]])
            self.conductance[name]=np.array([[],[]])

        self.dummy = np.array([]) 
        self.timeStart = datetime.datetime.now()


    def addData(self, voltage, current, capacitance, conductance, name):
        if self.voltage[name].size == 0 or self.current[name].size == 0:
            self.voltage[name] = voltage.reshape((2,1))
            self.current[name] = current.reshape((4,1))
            self.capacitance[name] = capacitance.reshape((2,1))
            self.conductance[name] = conductance.reshape((2,1))
            self.dummy         = 0
            self.ntc[name]     = self.temperature
            self.time[name]    = np.array([datetime.datetime.now(), 0]).reshape((2,1))
            
        else:
            self.voltage[name] = np.append(self.voltage[name], voltage.reshape((2,1)), axis=1 )
            self.current[name] = np.append(self.current[name], current.reshape((4,1)), axis=1 )
            self.capacitance[name] = np.append(self.capacitance[name], capacitance.reshape((2,1)), axis=1)
            self.conductance[name] = np.append(self.conductance[name], conductance.reshape((2,1)), axis=1)
            self.dummy         = np.append(self.dummy             , 0               )
            self.ntc[name]     = np.append(self.ntc[name]    , self.temperature)
            self.time[name]    = np.append(self.time[name]   , np.array([datetime.datetime.now(), 0]).reshape((2,1)), axis=1 )

        
    def setFreq(self, freq):
        print('CV frequency: ' + str(freq)+ ' kHz')
        self.freq = freq
        
    def setfreq_step(self, freq):
        self.freq_step=freq
        self.scanner.setfreq_step(freq)
        print('Frequency swipe step: '+str(freq)+ ' kHz')
        
    def setf0(self, freq):
        self.f0 = freq
        self.scanner.setf0(freq)
        print('Frequency swipe start set: '+str(freq)+ ' kHz')   
    
    def set_osc(self, volt):
        self.osc=volt
        self.scanner.set_osc(volt)
        print('Oscilation level set to: '+ str(volt)+ ' mV')
        
    
    def setf1(self, freq):
        self.f1 = freq
        self.scanner.setf1(freq)
        print('Frequency swipe end set: '+str(freq)+ ' kHz')
                    

    def setGlobalTemperature(self, temperature):
        print('Global temperature set: ' + str(temperature))
        self.temperature = temperature

    def setCVStart(self, voltage):
        self.config[1]['v0'] = voltage
        self.startDevices()

    def setCVStop(self, voltage):
        self.config[1]['vmax'] = voltage
        self.startDevices()

    def setCVSteps(self, steps):
        self.config[1]['vsteps'] = steps
        self.startDevices()

    def setCVrampUp(self, rampSpeed):
        self.config[1]['vrampup'] = rampSpeed
        self.startDevices()

    def setCVrampDown(self, rampSpeed):
        self.config[1]['vrampdown'] = rampSpeed
        self.startDevices()

    def setCVwait(self, vwait):
        self.config[1]['vwait'] = vwait
        self.startDevices()

    def setCVaverage(self, average):
        self.config[1]['vaverage'] = average
        self.startDevices()

    def setOutputStatus(self, text, color):
        print("Setting new output status")
        self.setColor(self.outputColor, color)
        self.outputText.setText(text)

    def receiveData(self, voltage, current, capacitance, conductance, name):
        
        maxcurrent = max(current, key=abs)
        self.monitor(voltage[0], maxcurrent)
        self.addData(voltage, current, capacitance, conductance, name)
        
        print("Sendig plot data for: " + self.realFreq + ' kHz' )
        self.plotData.emit(name, self.voltage[name], np.array([self.capacitance[name][0], self.capacitance[name][1], self.current[name][0], self.current[name][1], self.current[name][2], self.current[name][3]]))  
        



    def monitor(self, voltage, current):
        vText = "%0.3f" % voltage
        cText = "%0.3f" % (current*1e6)  
        self.voltage_reading.setText(vText)
        self.current_reading.setText(cText)

    def setupLogger(self):
        handler = LoggingHandler(self)
        logging.getLogger().addHandler(handler)
        logging.getLogger().setLevel(logging.WARN)

    def appendText(self, text):
        self.plainTextEdit.appendPlainText(str(datetime.datetime.now().strftime("%H:%M:%S")) + " - " +  text.replace('\n', ''))
        
    def applyFreq(self, freq):
        self.scanner.setFreqs(freq)
        self.realFreq = self.scanner.readFreq()
        
        if self.realFreq.endswith('\n'):
            self.realFreq= self.realFreq.replace('\n','')
        self.realFreq = str(float(self.realFreq)/1000)
        
        print('Real frequency measured: '+str(self.realFreq)+ ' kHz')


    def reset(self):
        self.clearData()
        self.plotter.emptyData()
        
        
    def start_swipe(self):
        self.running_swipe = True
        self.plotter.setCVLim(self.sb_v0.value(), self.sb_vmax.value())
        self.plotter.setCVwaittime(self.sb_vwait.value())
       
        self.setf0(self.sb_f0.value())
        self.setf1(self.sb_f1.value())
        self.setfreq_step(self.sb_freq_step.value())
        
       
        
        self.names=np.arange(self.sb_f0.value(), self.sb_f1.value()+self.sb_freq_step.value(), self.sb_freq_step.value())
        
        self.reset()
        
        self.set_osc(self.sb_osc.value())
        
        self.scan_CVswipe.emit()       
        
        self.settings.setEnabled(False)
        self.control.setEnabled(False)
        self.device.setEnabled(False)
        self.CVsettings.setEnabled(False)
        
        self.setColor(self.pb_stop, QtCore.Qt.red)
        
        print('Starting CV swipe from: '+str(self.sb_f0.value())+' kHz to '+str(self.sb_f1.value())+' kHz at every '+str(self.sb_freq_step.value())+' kHz')
        
        if self.scanner is not None:
            self.scanner.start()
            
       
        
       
    def updateplots(self, plots):
        self.plotter.updatePlots(plots)
        self.freq=(plots[0])
           
    def startCV(self):
        self.setFreq(self.sb_simpleCV.value())
        self.plotter.setCVLim(self.sb_v0.value(), self.sb_vmax.value())
        self.plotter.setCVwaittime(self.sb_vwait.value())
        
        self.reset()
        self.clearData()
        
       
        
        self.names=[str(self.freq)]
        self.clearData(self.names[0])
        self.plotter.updatePlots(self.names)
        
        self.applyFreq(self.sb_simpleCV.value())
        self.set_osc(self.sb_osc.value())
        
        self.scan_CV.emit() 
              
        
        self.settings.setEnabled(False)
        self.control.setEnabled(False)
        self.device.setEnabled(False)
        self.CVsettings.setEnabled(False)
        
        self.setColor(self.pb_stop, QtCore.Qt.red)
        
        print('Starting CV for: '+str(self.freq)+' kHz')
        
        if self.scanner is not None:
            self.scanner.start()
        


    def Stop(self):
        self.setColor(self.outputColor, QtCore.Qt.yellow)
        self.running_CV=False
        self.running_swipe=False
        if self.scanner is not None:
            self.scanner.killScan()
    


    def setColor(self, object, color = None):
        palette = object.palette()
        if color is not None:
            palette.setColor(object.backgroundRole(), color)
            palette.setColor(object.foregroundRole(), color)
            object.setPalette(palette)
        else:
            object.setPalette(QtWidgets.QApplication.style().standardPalette())

    def stopped(self):
        if not self.scanner.running_swipe:
            self.settings.setEnabled(True)
            self.control.setEnabled(True)
            self.device.setEnabled(True)
            self.CVswipeSettings.setEnabled(True)
            self.CVsettings.setEnabled(True)
            self.setColor(self.pb_stop)
            
        self.setColor(self.pb_simpleCV)
        self.pb_simpleCV.setText("RUN CV")
        
        self.running_CV = False
        
        print('Stopping run for: ')
        
        self.monitor(0,0)
        self.receiveProgress(0)
        
        

    def setScanEnabled(self, enabled):
        self.gb_scans.setEnabled(enabled)
        self.le_path.setEnabled(enabled)

    def setTestEnabled(self, enabled):
        self.pb_stop.setEnabled(enabled)
        self.le_path.setEnabled(enabled)

    
            
    def browsePath(self):
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        
        dialog = QtWidgets.QFileDialog(self, 'Select save path', desktop_path)
        dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.le_path.setText(dialog.selectedFiles()[0])

    def setPath(self, path):
        self.path    = path
        self.pathSet = True
        self.enableScan.emit(True)
        self.enableTest.emit(True)
        print('New path set: ' + self.path)

    def setName(self, name):
        self.fileName = name


    def saveFile(self, name):
        

        filename = self.path + '/' + self.fileName +'_'+str(self.realFreq)+'_KHz_CV_'+str(datetime.datetime.now().strftime('_%d_%m_%Y_%H_%M_%S')) + '.dat'
        print('Saving: ' + filename)
        
        timestamp = np.array([t.timestamp() for t in self.time[str(name)][0]]).T

        
       
        res = np.array([self.voltage[str(name)][0], 
                        self.current[str(name)][0],
                        self.current[str(name)][1], 
                        self.voltage[str(name)][1],
                        self.current[str(name)][2],
                        self.current[str(name)][3], 
                        self.capacitance[str(name)][0],
                        self.capacitance[str(name)][1],
                        self.conductance[str(name)][0],
                        self.conductance[str(name)][1],
                        timestamp])

        np.savetxt(filename
                    ,res.T
                    ,header=str(str(datetime.datetime.now().strftime("%a %b %d %H:%M:%S Hora estándar romance %Y"))+'\n'+
                                    'Frequency: '+str(self.realFreq)+ ' KHz\n'+
                                    'Oscilation level: '+str(self.sb_osc.value())+' mV\n'+
                                    'Start voltage: '+str(self.sb_v0.value())+' V\n'+
                                    'Stop voltage: '+str(self.sb_vmax.value())+' V\n'+
                                    'Step voltage: '+ str(self.sb_vstep.value())+ ' V\n'+
                                    'Init wait time: '+ str(self.sb_vwait.value())+ 's\n'+
                                    'Temperature: '+str(self.temperature)+' ºC\n'+
                                    'Measurements per point: '+str(self.sb_vaverage.value())+'\n'
                                    'Voltage ('+str(self.devicesEnabled[0].GetName())+') (V),Current ('+str(self.devicesEnabled[0].GetName())+') (A),Current ('+str(self.devicesEnabled[0].GetName())+') standard deviation (A),Voltage ('+str(self.devicesEnabled[1].GetName())+') (V),Current ('+str(self.devicesEnabled[1].GetName())+') (A),Current ('+str(self.devicesEnabled[1].GetName())+') standard devication (A),Capacitance(F),Capacitance standard deviation (F),Conductance(S),Conductance standard deviation(S),Timestamp')
                    ,delimiter=','
                    )
           






















class Logger:
    def __init__(self, log=True):
        self.save = log
        self.filename = 'Logfile_'+datetime.datetime.now().strftime("%y-%m-%d_%H-%M")+'.log'
        if self.save:
            open(self.filename,'w').write('Logfile date: '+datetime.datetime.now().ctime()+'\n\n')
    def AddLogEntry(self, devicenum, time, voltage, current):
        line=str(devicenum)+','+str(time)+','+str(voltage)+','+str(current)
        if self.save:
            open(self.filename,'a').write(line+'\n')
        print(line)
        
        
        
        


class Device:
    def __init__(self,INSTR, devicenum, gpibnum,ver,timeout=5000):
        if INSTR is not None:
            INSTR.timeout = timeout
        self.instr   = INSTR
        self.GPIB    = gpibnum
        self.Version = ver      
        self.devnum  = devicenum
        self.timeout = timeout
        self.voltage = 0
        
        self.running_CV = False

        self.Init()
		
    def Init(self):
        if self.GPIB != 17:
            if self.Version > 2000:
                self.instr.write('*RST')
            elif self.Version > 400:
                self.instr.write('*CLS')
                self.instr.write('O0X')
                self.instr.write('V0,1X') # repeated twice as sometimes device gets stuck after IDN or some command
                self.instr.write('V0,1X')
            elif self.Version < 0: # This is for debugging only
                print("DUMMY: initialized")
        else:
            if self.Version>0:
                self.instr.write('*RST;*CLS')
                self.instr.write("DISP:PAGE MEAS")    
                self.instr.write("FORMAT:DATA ASCII") 
                self.instr.write("APER MED")
                self.instr.write("TRIG:SOUR EXT")
                self.instr.write("FUNC:IMP:TYPE CPG")
                self.instr.write("FUNC:IMP:RANGE:AUTO ON")
                self.instr.write("BIAS:STATE OFF")
                   
            elif self.Version<0:
                print('DUMMY: initialized')
                    
    
    def GetName(self):
        if self.GPIB == 24 and self.Version>0:
            return "PAD"
        elif self.GPIB == 25 and self.Version>0:
            return "RING"
        elif self.GPIB == 17 and self.Version>0:
            return "Capacitance"
        else:
            if self.Version > 0:
                return 'DEVICE' + str(self.Version) + ' GPIB=' + str(self.GPIB)
            else:
                return 'DUMMY' + str(self.Version) + ' GPIB=' + str(self.GPIB)
        
            
    def GetGPIB(self):
        return self.GPIB
           
    def Start(self):
        self.Stop()
        self.OutputOn()
            
    def OutputOn(self):
        print("Enabling output.")
        self.running_CV = True
        if self.GPIB != 17:
            if self.Version > 2000:
                self.instr.write(':OUTP:STAT ON')      #turn output on
            elif self.Version > 400:
                self.instr.write('O1X')
            elif self.Version < 0: # This is for debugging only
                print("DUMMY: output on")

    def Stop(self):
        print("Disabling output")
        self.running_CV = False
        if self.GPIB != 17:
            if self.Version > 2000:
                self.instr.write(':OUTP:STAT OFF')
            elif self.Version > 400:
                self.instr.write('O0X')
            elif self.Version < 0: # This is for debugging only
                print("DUMMY: output off")
                   
            
    def SetCurrentRangeAuto(self):
        if self.GPIB != 17:
            if self.Version > 2000:
                self.instr.write(':SENS:CURR:RANG:AUTO ON')
                print('Current range set AUTO')
        
    def SetCurrentRange(self, current):
        if self.GPIB != 17:
            if self.Version > 2000:
                self.instr.write(':SOUR:CURR:RANG ' + str(current))  #:RANGe <n>|UP|DOWN|
                print("Current range set: " + str(current) + "A")
            elif self.Version > 400:
                command = 0
                # values specified from documentation
                for index in np.arange(6):
                    if np.abs(current) > (2 * 1e-9 * np.power(10, index)):
                        command = index + 2 # +2 because command indices are from 1 to 8 and we need to set range one larger than that
                self.instr.write('R' + str(command) + 'X')
                print("Current range set: " + str(current) + "A (R" + str(command)+")")
            elif self.Version < 0: # This is for debugging only
                print("DUMMY: range set")
            
    def SetVoltage(self, volt):
        self.voltage = volt
        if self.GPIB != 17:
            if self.Version > 2450:
                self.instr.write('SOUR:VOLT '+str(volt))
            if self.Version > 2000:
                self.instr.write(':SOUR:VOLT '+str(volt))
            elif self.Version > 400:
                self.instr.write('V'+str(volt)+'X') # just set voltage without changing ranges
            elif self.Version <= 300 and self.Version > 0:
                #self.instr.query('F0,0X')
                #self.instr.write('H0X')
                retval = self.instr.query('B'+str(volt)+',0,0X')
            elif self.Version < 0: # This is for debugging only
                pass
        
        
            
    def SetFreq(self, freq):
        self.freq=freq
        if self.GPIB == 17:
            if self.Version>0:
                self.instr.write(':FREQ '+str(freq)+' KHZ')
                time.sleep(0.2)
                
            elif self.Version<0:
                print('DUMMY: frequency set')
    
    def readFreq(self):
        if self.GPIB == 17:
            if self.Version>0:
                real_freq=self.instr.query('FREQ?')
                
                return real_freq
            else:
                return str(self.freq*1000) 
        
    
    def Set_osc(self, volt):
        self.osc = volt
        if self.GPIB == 17:
            if self.Version>0:
                self.instr.write('VOLT '+str(volt)+' MV')
            elif self.Version<0:
                print('DUMMY: oscilation level set')
            
        
    def ReadVoltCurrent(self):
        if self.GPIB != 17:
            if self.running_CV:
                if self.Version>2450:
                    MeasI = float(self.instr.query(':READ?').strip())
                    return self.voltage, MeasI
                if self.Version>2000: # only tested with ke2410
                    Measure = self.instr.query(':READ?')
                    MeasV   = (float(Measure.split(',')[0]))
                    MeasI   = (float(Measure.split(',')[1]))
                    return MeasV, MeasI
                elif self.Version > 400:
                    Measure = self.instr.query('B0X')
                    MeasI   = (float(Measure.replace('NDCI','')))
                    return self.voltage, MeasI
                elif self.Version <= 300 and self.Version > 0: # only tested with ke237
                    Measure = self.instr.query('G15,0,0X')
                    MeasV   = (float(Measure.split(',')[0].replace('NSDCV','')))
                    MeasI   = (float(Measure.split(',')[2].replace('NMDCI','')))
                    return MeasV, MeasI
                elif self.Version < 0: # This is for debugging only
                    if self.GPIB==24:
                        return self.voltage, self.voltage/5e7+np.random.randn()/1e8
                    else:
                        return self.voltage, self.voltage/3e7+np.random.randn()/1e8
            else:
                # return zeros in case the device is not on
                return self.voltage, 0
        else:
            return self.voltage,0
    
    def Read_Capacitance_Conductance(self):
        if self.GPIB == 17:
            if self.running_CV:
                if self.Version > 0:
                    self.instr.write("TRIGGER:IMM")
                    Measure = self.instr.query("FETCH?")
                    Measure = list(map(float, Measure.split(',')))
                    
                    Capacitance = Measure[0]
                    Conductance = Measure[1]
                    
                    return Capacitance, Conductance
                elif self.Version < 0:
                    return (self.voltage)**3/100+np.random.randn(), self.voltage**2/100+np.random.randn()
            else:
                return 0, 0
            
    def SetCompliance(self, limit):
        if self.GPIB != 17:
            if self.Version >2450:
                self.instr.write(':SOUR:VOLT:ILIM '+str(limit))
            if self.Version > 2000:
                self.instr.write(':CURR:PROT '+str(limit))
            elif self.Version<=300 and self.Version>0: # only tested with ke237
                retVal = self.instr.query('L'+("%.0E" %limit)+',0X')
            elif self.Version < 0: # This is for debugging only
                print("DUMMY: compliance set")



def ParseConfig(cfgfile):
    config = ConfigParser.ConfigParser()
    config.read(cfgfile)
    data = dict() # initialize empty dictionary

    ######### Read config IP options ########## 
    if config.has_section('Config'):
        data['sendip']   = config.get('Config','sendtoip')
        data['sendport'] = config.getint('Config','sendtoport')
    else:
        data['sendip']   = '<broadcast>' #'localhost'
        data['sendport'] = 5005

    ######### Read config options for CV scan #######
    Section='CV scan'
    if config.has_section(Section):
        data['ivscan'   ] = config.getboolean(Section,'DoCVscan'   )
        data['v0'       ] = config.getfloat  (Section,'V0'         )
        data['vmax'     ] = config.getfloat  (Section,'VMax'       )
        data['vsteps'   ] = config.getint    (Section,'VStep'     )
        data['vrampup'  ] = config.getfloat  (Section,'VRampUp'    )
        data['vrampdown'] = config.getfloat  (Section,'VRampDown'  )
        data['vwait'    ] = config.getfloat  (Section,'TimePerStep')
        data['vaverage' ] = config.getint    (Section,'AverageMeas')
        data['ndecay'   ] = config.getint    (Section,'NDecayMeas' )
        data['tdecay'   ] = config.getfloat  (Section,'TimePerDecayMeas')

    else:
        data['ivscan'   ] = False
        data['v0'       ] = 0
        data['vmax'     ] =-100
        data['vsteps'   ] = 20
        data['vrampup'  ] = 2
        data['vrampdown'] = 10
        data['vwait'    ] = 10
        data['vaverage' ] = 10
        data['ndecay'   ] = 1
        data['tdecay'   ] = 1
    return config, data
   
    
def ListDevices(config):
    rm = visa.ResourceManager()
    print(rm.list_resources('?*'))
    
    #### Fill list of devices #### 
    devices = []
    for idev in range(10):
        Section= 'Device '+str(idev)
        if config.has_section(Section):
            if config.getboolean(Section,'Include'):
                keithleyver = config.getint(Section,'KeithleyVer')
                for i in range(2): #there should be at max 2 different boards but in case it detects diferent drivers should work
                    if i==0:
                        board_adress=''
                    else:
                        board_adress=str(i)
                    address     = 'GPIB'+board_adress+'::'+str(config.getint(Section,'GPIB'))+'::INSTR'
                    try:
                        instr = rm.open_resource(address)
                        instr.write('*RST')
                        break
                    except:
                        instr = None
                        keithleyver = -np.abs(keithleyver)
                    
                    
                devices.append(Device(INSTR=instr,
                                      devicenum=idev,
                                      gpibnum=config.getint(Section,'GPIB'),
                                      ver=keithleyver))
            else:
                print("Ignoring "+Section)
        else:
            print(Section+" not in .cfg")
    return devices







class TextStream(QtCore.QObject):
    _stdout = None
    _stderr = None
    textWritten = QtCore.pyqtSignal(str)
    def flush( self ):
        pass
    def fileno( self ):
        return -1
    def write(self, text):
        if ( len(text)>1 ):
            self.textWritten.emit(str(text))
    @staticmethod
    def stdout():
        if ( not TextStream._stdout ):
            TextStream._stdout = TextStream()
            sys.stdout = TextStream._stdout
        return TextStream._stdout
    @staticmethod
    def stderr():
        if ( not TextStream._stderr ):
            TextStream._stderr = TextStream()
            sys.stderr = TextStream._stderr
        return TextStream._stderr

class LoggingHandler(QtCore.QObject, logging.Handler):
    def __init__(self, parent):
        super().__init__(parent)
        super(logging.Handler).__init__()
        formatter = Formatter('%(levelname)s: %(message)s')
        self.setFormatter(formatter)

    def emit(self, record):
        msg = self.format(record)
        TextStream.stdout().write(str(msg))

class Formatter(logging.Formatter):
    def formatException(self, ei):
        result = super(Formatter, self).formatException(ei)
        return result

    def format(self, record):
        s = super(Formatter, self).format(record)
        if record.exc_text:
            s = s.replace('\n', '')
        return s








class Scanner(QtCore.QThread):
    outputOn  = QtCore.pyqtSignal()
    outputOff = QtCore.pyqtSignal()

    stepDone = QtCore.pyqtSignal()
    scanDone = QtCore.pyqtSignal()
    realfreq = QtCore.pyqtSignal(int)
    saveData = QtCore.pyqtSignal(str)

    measured = QtCore.pyqtSignal(np.ndarray, np.ndarray, np.ndarray, np.ndarray, str)
    
    reset = QtCore.pyqtSignal()
    updateplots = QtCore.pyqtSignal(list)

    progress = QtCore.pyqtSignal(int)
    text     = QtCore.pyqtSignal(str)

    def __init__(self, devices, settings, parent =None):
        super(self.__class__, self).__init__(parent=parent)
        self.setDevices(devices)
        self.setSettings(settings)

        self.voltage = 0
        self.newVoltage = 0

        self.read = False
        self.ramp = False
        
    def setDevices(self, devices):
        self.devices  = devices
        
    def setSettings(self, settings):
        self.settings = settings
        self.reloadState()

    def reloadState(self):
        self.running_CV  = False
        self.running_swipe = False
        self.finished = False
        self.counter  = 0
        
        if self.settings['vmax']<self.settings['v0']:
            sign=-1
        else:
            sign=1
        
        self.dV       = self.settings['vsteps']*sign

        self.text.emit("Preparing CV scan from " + str(self.settings['v0']) + "V to " + str(self.settings['vmax']) + "V in " + str(self.settings['vsteps']) + " steps")
        self.text.emit(" waiting " + str(self.settings['vwait']) + " sec each averaging for " + str(self.settings['vaverage']) + " measurements")
        self.text.emit(" ramping up by " + str(self.settings['vrampup'])+"V/s, ramping down by " + str(self.settings['vrampdown']) + "V/s")        

   

    def prepare(self):
        self.text.emit("Preparing devices for run")
        self.outputOn.emit()
        self.running_CV = True
        # set voltage to all devices without reading out (as they are turned off)
        self.setVoltage(self.settings['v0'])
        for dev in self.devices:
            dev.Start()

        self.counter  = 0
        self.finished = False

    def finish(self):
        self.text.emit("Stopping devices after run")
        self.outputOff.emit()
        self.running_CV=False
        
        for dev in self.devices:
            dev.Stop()

    def killScan(self):
        self.running_CV = False
        self.running_swipe = False
        self.text.emit('Kill scan initialized.')
        
    def enableScan(self, enabled = True):
        self.running_CV = enabled

    def run_CV(self):
        self.prepare()
        
        self.text.emit("Starting CV run")
        while self.running_CV:
            
            self.measure()
            if self.counter < abs((self.settings['vmax']-self.settings['v0'])/self.settings['vsteps']):
                self.newCV(True)
            else:
                self.newCV(False)

        if not self.finished:
            self.newCV(False)

        self.finish()
        self.scanDone.emit()
     

    def run(self):
        self.text.emit('Starting run thread ...')
        if self.running_CV and not self.running_swipe:
            self.text.emit('.. scan CV')
            self.run_CV()
            
        elif self.running_swipe:
            self.running_CV=True
            self.text.emit('Start CV swipe')
            
            
            for freq in np.arange(self.f0, self.f1 + self.f_step, self.f_step):
                if self.running_swipe == False:
                    break
                self.frequency = freq
                self.realfreq.emit(freq)
                time.sleep(0.5)
                self.setFreqs(freq)
                self.updateplots.emit([str(self.frequency)])
                self.run_CV()
                    
                while not self.finished:
                    time.sleep(0.1)   
                                       
                self.reset.emit()
                
            self.running_swipe =False
            
    def measure(self):
        
        wait=self.settings['vwait']
        
        
        timeStart = time.time()
        
        while (time.time() - timeStart) < wait and self.running_CV:
            time.sleep(0.05)
                    
                    
        for dev in self.devices:
            
            average = self.settings['vaverage']
            Vaverage1 = np.zeros(average)
            Iaverage1 = np.zeros(average)
            Vaverage2 = np.zeros(average)
            Iaverage2 = np.zeros(average)
            Caverage = np.zeros(average)
            Gaverage = np.zeros(average)
              
                
            if dev.GetGPIB()==24:
                for taverage in np.arange(average):
                    Vaverage1[taverage], Iaverage1[taverage] = dev.ReadVoltCurrent()
                    time.sleep
                vMeas1 = np.array([np.mean(Vaverage1), np.std(Vaverage1)])
                iMeas1 = np.array([np.mean(Iaverage1), np.std(Iaverage1)])
            elif dev.GetGPIB()==25:
                for taverage in np.arange(average):
                    Vaverage2[taverage], Iaverage2[taverage] = dev.ReadVoltCurrent()
                vMeas2 = np.array([np.mean(Vaverage2), np.std(Vaverage2)])
                iMeas2 = np.array([np.mean(Iaverage2), np.std(Iaverage2)])            
            elif dev.GetGPIB()==17:
                for taverage in np.arange(average):
                    Caverage[taverage], Gaverage[taverage] = dev.Read_Capacitance_Conductance()
                cMeas=np.array([np.mean(Caverage), np.std(Caverage)])     
                gMeas=np.array([np.mean(Gaverage), np.std(Gaverage)])
                
        vMeas=np.array([vMeas1[0], vMeas2[0]])
        iMeas=np.array([iMeas1[0], iMeas1[1], iMeas2[0], iMeas2[1]])
       
        
        
       
        self.measured.emit(vMeas, iMeas, cMeas, gMeas, str(self.frequency))           
            

    def newCV(self, up = True):
        
        oldvoltage = self.settings['v0'] + ((self.counter) * self.dV)
        newvoltage = self.settings['v0']
        
        if (up):
            sign=1
            direction = " up "
            newvoltage   += ((self.counter + 1) * self.dV)
            rampValue     = self.settings['vrampup']
        else:
            sign=-1
            direction = " down "
            rampValue     = self.settings['vrampdown']
            self.running_CV  = False
            self.finished = True
            newvoltage=0
            
            self.saveData.emit(str(self.frequency))     
            
        self.counter += 1
        
        
        
        self.ramping(newvoltage, oldvoltage, self.settings['v0'], self.settings['vmax'], rampValue)

        self.text.emit("Ramping" + direction + "by " + str(rampValue) + "V/s from " + str(oldvoltage) + " to " + str(newvoltage))
        
        
        
        

    def ramping(self, newvoltage, oldvoltage, v0, vmax, rampSpeed):
        rampLen = np.abs(newvoltage-oldvoltage)
        if newvoltage == oldvoltage:
            return
        elif (newvoltage-oldvoltage < 0):
            sign = -1
        else:
            sign = 1

        for i in range(1,4):
            try:
                ramp=rampLen*i/3
                timeStart = time.time()
                new = oldvoltage + (sign * ramp)
                iMeas = np.NaN
                for dev in self.devices:
                    vMeas, iMeas = self.setVoltage(new, dev)

                    if abs(iMeas) >= self.currentLimit:
                        self.running_CV = False
                        self.text.emit("Reached maximal enabled current.")
                        raise ValueError("Reached maximal enabled current.")
                    
                
                self.progress.emit(int(100 * (vMeas - v0) / (vmax - v0)) )
                
                while (time.time() - timeStart) < rampLen/(3*rampSpeed):
                    time.sleep(0.01)
            except:
                break
        



    def setVoltage(self, voltage, device = None):
        self.voltage = voltage
        if device is None:
            self.text.emit("Applied testing voltage in devices: " + str(voltage) + "V")
            for dev in self.devices:    
                dev.SetVoltage(voltage)
        else:
            device.SetVoltage(voltage)
            return device.ReadVoltCurrent()
                      

                    
    def setFreqs(self,freq, device = None):
        self.frequency= freq
        if device is None:
            self.text.emit("Applied current frequency: " + str(freq) + " kHz")
            for dev in self.devices:
                if dev.GetGPIB()==17:
                    dev.SetFreq(freq)
                    time.sleep(0.5)
        else:
            self.text.emit("Applied current frequency: " + str(freq) + " kHz")
            if device.GetGPIB() ==17:
                    device.SetFreq(freq)
                    time.sleep(0.5)
                    
       
    def readFreq(self, device = None):
        if device is None:
            for dev in self.devices:
                if dev.GetGPIB()==17:
                    return dev.readFreq()
        else:
            if device.GetGPIB()==17:
                return device.readFreq()
            
                   
    def setf0(self, freq):
        self.f0=freq
        
    def set_osc(self, volt, device = None):
        self.osc=volt
        
        if device is None:
            self.text.emit("Applied oscilation level: " + str(volt) + " mV")
            for dev in self.devices:
                if dev.GetGPIB()==17:
                    dev.Set_osc(volt)
                    time.sleep(0.3)            
        else:
            self.text.emit("Applied oscilation level: " + str(volt) + " mV")
            if device.GetGPIB()==17:
                device.Set_osc(volt)
                time.sleep(0.3)
  
    
    def setf1(self, freq):
        self.f1=freq
        
    def setfreq_step(self, freq):
        self.f_step=freq
         
            
    def simple_CV(self):
        self.running_CV = True
        self.running_swipe = False
        
    def swipe(self):
        self.running_swipe = True
        self.running_CV = True
        

    def setCurrentLimit(self, current):
        self.text.emit("Setting current limit in devices: " + str(current) + "mA")
        self.currentLimit = current * 1e-6
        for dev in self.devices:
            dev.SetCompliance(self.currentLimit) # convert to A

    def setCurrentRange(self, current = None):
        if current == None:
            self.text.emit('Setting current Range Auto on')
            for dev in self.devices:
                dev.SetCurrentRangeAuto()                
            
        else:
            self.text.emit("Setting current range in devices: " + str(current) + "uA")
            self.currentRange = current * 1e-6
            for dev in self.devices:
                dev.SetCurrentRange(self.currentRange) # convert to A





class Plotter(FigureCanvas):
    def __init__(self, plots, parent=None, width=5, height=4, dpi=100, **kwargs):
        self._fig, self._axes = plt.subplots(
            figsize=(width, height),
            dpi=dpi,
            nrows=1, 
            ncols=1,
            constrained_layout=True
        )
        self._axes = [self._axes, self._axes.twinx()]
        FigureCanvas.__init__(self, self._fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self._plots = plots.copy()
        self._visiblePlots = plots.copy()

        self._dataX = {plot: [[],[]] for plot in self._plots}
        self._dataY = {plot: [[], [], [], [], [], []] for plot in self._plots}

        self._xLabel = kwargs.get('xlabel', 'Voltage [V]')
        self._yLabelLeft = kwargs.get('ylabel_left', 'Capacitance [F]')
        self._yLabelRight = kwargs.get('ylabel_right', 'Current [A]')

        self.emptyData()
        
        # Prepare for blitting
        self._background = None
        self._need_redraw = False
        
        # Timer for updating
        self.wait=200
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self.updatePlot)
        self._timer.start(self.wait)  

    def emptyData(self):
        for plot in self._plots:
            self._dataX[plot] = [[],[]]
            self._dataY[plot] = [[], [], [], [], [], []]

    def receiveData(self, plot, dataX, dataY):
        self._dataX[plot] = dataX
        self._dataY[plot] = dataY
        self._need_redraw = True

    def updatePlot(self):
        if self._need_redraw:
            self.replot()
            self._need_redraw = False
    def replot(self):
        try:
            if self._background is None:
                # Capturar el fondo para blitting (solo una vez)
                self.draw()
                self._background = self.copy_from_bbox(self._fig.bbox)
            else:
                # Restaurar el fondo capturado
                self.restore_region(self._background)

            # Limpiar solo los datos en los ejes, sin borrar el fondo
            for ax in self._axes:
                ax.clear()  # Esto sigue borrando los ejes, pero sin afectar el fondo

            # Plot data
            for plot in self._visiblePlots:
                x_common = self._dataX[plot][0]  # Eje X común (voltage)

                # Graficar en el primer eje
                line1 = self._axes[0].errorbar(
                    x_common,
                    self._dataY[plot][0],  # Capacitancia
                    yerr=self._dataY[plot][1],  # Errores de Capacitancia
                    fmt='x-', label=f"{plot} kHz, Capacitance", color='black'
                )
                self._axes[0].set_xlabel(self._xLabel)
                self._axes[0].set_ylabel(self._yLabelLeft)

                # Graficar en el segundo eje
                line2 = self._axes[1].errorbar(
                    x_common,
                    self._dataY[plot][2],  # Intensidad 1
                    yerr=self._dataY[plot][3],  # Errores de Intensidad 1
                    fmt='o--', label=f"{plot} kHz, Intensity PAD", ms=1
                )
                line3 = self._axes[1].errorbar(
                    x_common,
                    self._dataY[plot][4],  # Intensidad 2
                    yerr=self._dataY[plot][5],  # Errores de Intensidad 2
                    fmt='s--', label=f"{plot} kHz, Intensity RING", ms=1
                )
                self._axes[1].set_ylabel(self._yLabelRight)
                self._axes[1].tick_params(axis='y', labelcolor='black')
                self._axes[1].yaxis.set_label_position('right')
                self._axes[1].yaxis.tick_right()

                # Añadir leyendas
                legend1 = self._axes[0].legend(loc='upper left')
                legend2 = self._axes[1].legend(loc='upper right')

            # Establece los límites del eje X para ambos ejes
            self._axes[0].set_xlim(self._xlim1, self._xlim2)
            self._axes[1].set_xlim(self._xlim1, self._xlim2)

            # Redibujar todo para asegurar que las etiquetas no se recorten
            self._fig.canvas.draw_idle()  # Actualización eficiente
            self.blit(self._fig.bbox)

        except Exception as e:
            print(f"Error during plotting: {e}")


    def updatePlots(self, new_plots):
        self._plots = new_plots.copy()
        self._visiblePlots = new_plots.copy()

        self._dataX = {plot: [[],[]] for plot in self._plots}
        self._dataY = {plot: [[], [], [], [], [], []] for plot in self._plots}
        
        self.emptyData()
        self._need_redraw = True

    def setCVLim(self, voltage1, voltage2):
        self._xlim1 = min([voltage1, voltage2])
        self._xlim2 = max([voltage1, voltage2])
        
    def setCVwaittime(self, time):
        self.wait=time
        

    


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec_())