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
        self.sb_vwait.setMaximum(100.0)
        self.sb_vwait.setObjectName("sb_vwait")
        self.horizontalLayout_12.addWidget(self.sb_vwait)
        self.label_15 = QtWidgets.QLabel(self.groupBox_14)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_12.addWidget(self.label_15)
        self.horizontalLayout_12.setStretch(0, 2)
        self.verticalLayout_4.addWidget(self.groupBox_14)

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

        self.IVsettings = QtWidgets.QGroupBox(self.centralwidget)
        self.IVsettings.setObjectName("IVsettings")
        self.verticalLayout_4_1 = QtWidgets.QVBoxLayout(self.IVsettings)
        self.verticalLayout_4_1.setObjectName("verticalLayout_4_1")

        self.groupBox_9 = QtWidgets.QGroupBox(self.IVsettings)
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
        self.verticalLayout_4_1.addWidget(self.groupBox_9)

        self.groupBox_10 = QtWidgets.QGroupBox(self.IVsettings)
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
        self.verticalLayout_4_1.addWidget(self.groupBox_10)

        self.groupBox_11 = QtWidgets.QGroupBox(self.IVsettings)
        self.groupBox_11.setObjectName("groupBox_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.sb_vstep = QtWidgets.QDoubleSpinBox(self.groupBox_11)
        self.sb_vstep.setMaximum(1000)
        self.sb_vstep.setObjectName("sb_vstep")
        self.horizontalLayout_11.addWidget(self.sb_vstep)
        self.verticalLayout_4_1.addWidget(self.groupBox_11)

        self.temp_vertical_layout.addWidget(self.settings)
        self.temp_vertical_layout.addWidget(self.IVsettings)


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
        
                
        self.ItSettings = QtWidgets.QGroupBox(self.device)
        self.ItSettings.setObjectName("ItSettings")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.ItSettings)
        self.verticalLayout_5.setObjectName("verticalLayout_5")


        self.groupBox_voltage = QtWidgets.QGroupBox(self.ItSettings)
        self.groupBox_voltage.setObjectName("groupBox_voltage")
        self.horizontalLayout_voltage = QtWidgets.QHBoxLayout(self.groupBox_voltage)
        self.horizontalLayout_voltage.setObjectName("horizontalLayout_voltage")

        self.sb_voltage = QtWidgets.QDoubleSpinBox(self.groupBox_voltage)
        self.sb_voltage.setMinimum(-1100.0)
        self.sb_voltage.setMaximum(1100.0)
        self.sb_voltage.setObjectName("sb_voltage")
        self.horizontalLayout_voltage.addWidget(self.sb_voltage)

        self.label_12 = QtWidgets.QLabel(self.groupBox_voltage)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_voltage.addWidget(self.label_12)

        self.verticalLayout_5.addWidget(self.groupBox_voltage)
        
        self.groupbox_time_step = QtWidgets.QGroupBox(self.ItSettings)
        self.groupbox_time_step.setObjectName("groupbox_time_step")
        self.horizontalLayout_time_step = QtWidgets.QHBoxLayout(self.groupbox_time_step)
        self.horizontalLayout_time_step.setObjectName("horizontalLayout_time_step")

        self.sb_time_step_m = QtWidgets.QDoubleSpinBox(self.groupbox_time_step)
        self.sb_time_step_m.setRange(0,599)
        self.sb_time_step_m.setSingleStep(1)  
        self.sb_time_step_m.setDecimals(0)
        self.sb_time_step_m.setObjectName("sb_time_step_m")
        self.horizontalLayout_time_step.addWidget(self.sb_time_step_m)

        self.label_12_time_step_1 = QtWidgets.QLabel(self.groupbox_time_step)
        self.label_12_time_step_1.setObjectName("label_12_time_step_1")
        self.horizontalLayout_time_step.addWidget(self.label_12_time_step_1)

        self.sb_time_step_s = QtWidgets.QDoubleSpinBox(self.groupbox_time_step)
        self.sb_time_step_s.setRange(0,59)
        self.sb_time_step_s.setObjectName("sb_time_step_s")
        self.horizontalLayout_time_step.addWidget(self.sb_time_step_s)
        
        self.label_12_time_step_2 = QtWidgets.QLabel(self.groupbox_time_step)
        self.label_12_time_step_2.setObjectName("label_12_time_step_2")
        self.horizontalLayout_time_step.addWidget(self.label_12_time_step_2)

        self.verticalLayout_5.addWidget(self.groupbox_time_step)

        self.groupbox_timelimit = QtWidgets.QGroupBox(self.ItSettings)
        self.groupbox_timelimit.setObjectName("groupbox_timelimit")
        self.horizontalLayout_timelimit = QtWidgets.QHBoxLayout(self.groupbox_timelimit)
        self.horizontalLayout_timelimit.setObjectName("horizontalLayout_timelimit")

        self.sb_timelimit_h = QtWidgets.QDoubleSpinBox(self.groupbox_timelimit)
        self.sb_timelimit_h.setRange(0,23)
        self.sb_timelimit_h.setSingleStep(1)  
        self.sb_timelimit_h.setDecimals(0)
        self.sb_timelimit_h.setObjectName("sb_timelimit_h")
        self.horizontalLayout_timelimit.addWidget(self.sb_timelimit_h)

        self.label_12_1 = QtWidgets.QLabel(self.groupbox_timelimit)
        self.label_12_1.setObjectName("label_12_1")
        self.horizontalLayout_timelimit.addWidget(self.label_12_1)

        self.sb_timelimit_m = QtWidgets.QDoubleSpinBox(self.groupbox_timelimit)
        self.sb_timelimit_m.setRange(0,59)
        self.sb_timelimit_m.setObjectName("sb_timelimit_h")
        self.horizontalLayout_timelimit.addWidget(self.sb_timelimit_m)
        
        self.label_12_12 = QtWidgets.QLabel(self.groupbox_timelimit)
        self.label_12_12.setObjectName("label_12_12")
        self.horizontalLayout_timelimit.addWidget(self.label_12_12)

        self.verticalLayout_5.addWidget(self.groupbox_timelimit)

        self.groupBox_history = QtWidgets.QGroupBox(self.ItSettings)
        self.groupBox_history.setObjectName("groupBox_history")
        self.horizontalLayout_history = QtWidgets.QHBoxLayout(self.groupBox_history)
        self.horizontalLayout_history.setObjectName("horizontalLayout_history")

        self.sb_history = QtWidgets.QSpinBox(self.groupBox_history)
        self.sb_history.setMinimum(1)
        self.sb_history.setMaximum(1500)
        self.sb_history.setObjectName("sb_history")
        self.horizontalLayout_history.addWidget(self.sb_history)

        self.label_12_2 = QtWidgets.QLabel(self.groupBox_history)
        self.label_12_2.setObjectName("label_12_2")
        self.horizontalLayout_history.addWidget(self.label_12_2)

        self.verticalLayout_5.addWidget(self.groupBox_history)

        
        
        
        
        self.verticalLayout_7.addWidget(self.ItSettings)
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
       
        
        self.pb_PAD = QtWidgets.QPushButton(self.gb_scans)
        self.pb_PAD.setMinimumSize(QtCore.QSize(0, 50))
        self.pb_PAD.setObjectName("pb_PAD")
        self.gridLayout.addWidget(self.pb_PAD, 1, 0, 2, 2)
        
        
        self.pb_test = QtWidgets.QPushButton(self.gb_scans)
        self.pb_test.setMinimumSize(QtCore.QSize(0, 50)) 
        self.pb_test.setObjectName("pb_test")
        self.gridLayout.addWidget(self.pb_test,3, 0, 2, 2)
        
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

        MainWindow.setWindowTitle(_translate("MainWindow", "IV and It measurement"))
        self.settings.setTitle(_translate("MainWindow", "Global Settings"))
        self.IVsettings.setTitle(_translate("MainWindow", "IV Settings"))
        self.gb_supplies.setTitle(_translate("MainWindow", "Connected power supplies"))
        self.ItSettings.setTitle(_translate("MainWindow", "It Settings"))
        self.groupBox.setTitle(_translate("MainWindow", "Data operations"))
        self.gb_scans.setTitle(_translate("MainWindow", "Run "))
        self.settings.setStyleSheet("QGroupBox#settings { font-weight: bold; }")
        self.IVsettings.setStyleSheet("QGroupBox#IVsettings { font-weight: bold; }")
        self.gb_supplies.setStyleSheet("QGroupBox#gb_supplies { font-weight: bold; }")
        self.ItSettings.setStyleSheet("QGroupBox#ItSettings { font-weight: bold; }")
        self.groupBox.setStyleSheet("QGroupBox#groupBox { font-weight: bold; }")
        self.gb_scans.setStyleSheet("QGroupBox#gb_scans { font-weight: bold; }")
        self.pb_settingsDefault.setText(_translate("MainWindow", "Reset Defaults"))
        self.pb_scanDevices.setText(_translate("MainWindow", "Scan Devices"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Voltage start"))
        self.label_10.setText(_translate("MainWindow", "V"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Voltage stop"))
        self.label_11.setText(_translate("MainWindow", "V"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Voltage step (V)"))
        self.groupBox_14.setTitle(_translate("MainWindow", "Stabilization time"))
        self.label_15.setText(_translate("MainWindow", "s"))
        self.groupBox_17.setTitle(_translate("MainWindow", "Measurements per point"))
        self.groupBox_13.setTitle(_translate("MainWindow", "Ramp up speed"))
        self.label_13.setText(_translate("MainWindow", "V/s"))
        self.groupBox_12.setTitle(_translate("MainWindow", "Ramp down speed"))
        self.label_14.setText(_translate("MainWindow", "V/s"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Compliance"))
        self.label_8.setText(_translate("MainWindow", "uA"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Temperature"))
        self.label_7.setText(_translate("MainWindow", "°C"))
        
        self.groupBox_voltage.setTitle(_translate("MainWindow", "Voltage "))
        self.groupbox_time_step.setTitle(_translate("MainWindow", "Time step "))
        
        self.groupbox_timelimit.setTitle(_translate("MainWindow", "It duration"))
        self.groupBox_history.setTitle(_translate("MainWindow", "Plot visibility"))

        self.label_12.setText(_translate("MainWindow", "V"))
        self.label_12_time_step_1.setText(_translate("MainWindow", "min"))
        self.label_12_time_step_2.setText(_translate("MainWindow", "s"))
        self.label_12_1.setText(_translate("MainWindow", "h"))
        self.label_12_12.setText(_translate("MainWindow", "min"))
        self.label_12_2.setText(_translate("MainWindow", "min"))
        self.pb_test.setText(_translate("MainWindow", "RUN It"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Path"))
        self.pb_browse.setText(_translate("MainWindow", "Browse"))
        self.groupBox_3.setTitle(_translate("MainWindow", "File name"))
        self.label_5.setText(_translate("MainWindow", "TILE"))
        self.label_6.setText(_translate("MainWindow", "_date_time.dat"))
        self.pb_PAD.setText(_translate("MainWindow", "RUN IV"))
        self.pb_stop.setText(_translate("MainWindow", "ABORT"))
        self.label.setText(_translate("MainWindow", "Output "))
        self.outputText.setText(_translate("MainWindow", "OFF"))
        self.voltage_reading.setText(_translate("MainWindow", "nan"))
        self.label_9.setText(_translate("MainWindow", "V"))
        self.current_reading.setText(_translate("MainWindow", "nan"))
        self.label_4.setText(_translate("MainWindow", "uA"))








class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    plotData    = QtCore.pyqtSignal(str, np.ndarray, np.ndarray, bool)
    enableScan  = QtCore.pyqtSignal(bool)
    enableTest  = QtCore.pyqtSignal(bool)
    scan_It  = QtCore.pyqtSignal(bool)
    scan_IV  = QtCore.pyqtSignal(bool)
    

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
        
        self.sb_temperature.setValue(20)
        self.sb_current.setValue(1)
        self.sb_timelimit_h.setValue(0)
        self.sb_timelimit_m.setValue(10)
        self.sb_time_step_m.setValue(0)
        self.sb_time_step_s.setValue(10)
        self.sb_history.setValue(1)
        self.temperature=20
        self.timelimit = 600
        self.timelimit_h=0
        self.timelimit_m=10
        self.time_step=10
        self.time_step_m=0
        self.time_step_s=10
        
        self.configPath = self.resource_path("config.cfg")
        self.initCommands()
        self.scannerCommands()
        
        
        
        self.defaultDevices()

        self.path     = ""
        self.pathSet  = False
        self.setName("")

        self.voltageTesting = 0
        
        self.testing = False
        self.running = False


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
        for i in np.arange(len(self.names)):
            item = self.list_plots.item(i)
            if (item.checkState() == QtCore.Qt.Checked):
                print(" " + str(self.names[i]))
                self.plotsEnabled.append(self.names[i])
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
        
        self.validos=[]
        for dev in self.devicesEnabled:
            self.validos.append(dev.GetName())
        self.plotter.updatePlots(self.validos)

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

        self.sb_v0       .valueChanged.connect(self.setIVStart)
        self.sb_vmax     .valueChanged.connect(self.setIVStop)
        self.sb_vstep    .valueChanged.connect(self.setIVSteps)
        self.sb_vrampup  .valueChanged.connect(self.setIVrampUp)
        self.sb_vrampdown.valueChanged.connect(self.setIVrampDown)
        self.sb_vwait    .valueChanged.connect(self.setIVwait)
        self.sb_vaverage .valueChanged.connect(self.setIVaverage)
        

        self.pb_settingsDefault.pressed.connect(self.defaultDevices)
        self.pb_scanDevices.pressed.connect(lambda: [self.initDevices()]+ [self.selectDevices()]+ [self.clearData()])
        self.list_devices.itemChanged.connect(self.selectDevices)


        self.pb_browse.pressed.connect(self.browsePath)
        self.le_path.textChanged.connect(self.setPath)
        self.le_name.textChanged.connect(self.setName)
        self.enableScan.connect(self.setScanEnabled)
        self.enableTest.connect(self.setTestEnabled)

        
        
        self.pb_PAD.pressed.connect(lambda: [self.clearData(), self.plotter.emptyData()] + [self.selectDevices()] + [self.start_IV(dev.GetName()) for dev in self.devicesEnabled] + [self.update_plot()])



        
        self.pb_stop.pressed.connect(self.Stop)


        self.sb_voltage.valueChanged.connect(self.setTestingVoltage)
        self.sb_time_step_m.valueChanged.connect(self.setTimestep_m)
        self.sb_time_step_s.valueChanged.connect(self.setTimestep_s)
        self.sb_timelimit_h.valueChanged.connect(self.setTimelimit_h)
        self.sb_timelimit_m.valueChanged.connect(self.setTimelimit_m)

        self.sb_temperature.valueChanged.connect(self.setGlobalTemperature)

        self.list_plots.itemChanged.connect(self.selectPlots)

    def scannerCommands(self):
        if self.scanner is not None:
            
            self.signalReconnect(self.pb_test.pressed, (lambda:[self.clearData(), self.plotter.emptyData()] + [self.selectDevices()] + [self.start_It(dev.GetName()) for dev in self.devicesEnabled]+ [self.update_plot()]))
            self.signalReconnect(self.scan_It, self.scanner.testVoltage)

            self.signalReconnect(self.scan_IV, self.scanner.enableScan)

            self.signalReconnect(self.sb_current.valueChanged, self.scanner.setCurrentLimit)
            self.signalReconnect(self.sb_current.valueChanged, self.scanner.setCurrentRange)

            self.signalReconnect(self.scanner.scanDone, self.stopped)

            self.signalReconnect(self.scanner.saveData, self.saveFile)

            self.signalReconnect(self.scanner.text, self.receiveText)
            self.signalReconnect(self.scanner.progress, self.receiveProgress)
            self.signalReconnect(self.scanner.measured, self.receiveData)

            self.signalReconnect(self.scanner.outputOn , lambda: self.setOutputStatus('ON' , QtCore.Qt.green), force=True)
            self.signalReconnect(self.scanner.outputOff, lambda: self.setOutputStatus('OFF', QtCore.Qt.red  ), force=True)

            
    def plotterCommands(self):
        self.signalReconnect(self.sb_history.valueChanged, self.plotter.setHistory)
        self.signalReconnect(self.plotData, self.plotter.receiveData)

    def receiveText(self, text):
        print(text)

    def receiveProgress(self, value):
        self.progressBar.setValue(value)

    def clearData(self, name = None):
        if name is None:
            self.voltage = {name:np.array([[],[]]) for name in self.names}
            self.current = {name:np.array([[],[]]) for name in self.names}
            self.ntc     = {name:np.array([])      for name in self.names}
            self.time    = {name:np.array([[],[]]) for name in self.names}
        if name in self.names:
            self.voltage[name] = np.array([[],[]])
            self.current[name] = np.array([[],[]])
            self.ntc[name]     = np.array([])
            self.time[name]    = np.array([[],[]])

        self.dummy = np.array([]) 
        self.timeStart = datetime.datetime.now()

    def addData(self, voltage, current, name):
        if self.voltage[name].size == 0 or self.current[name].size == 0:
            self.voltage[name] = voltage.reshape((2,1))
            self.current[name] = current.reshape((2,1))
            self.dummy         = 0
            self.ntc[name]     = self.temperature
            self.time[name]    = np.array([datetime.datetime.now(), 0]).reshape((2,1))
        else:
            self.voltage[name] = np.append(self.voltage[name], voltage.reshape((2,1)), axis=1 )
            self.current[name] = np.append(self.current[name], current.reshape((2,1)), axis=1 )
            self.dummy         = np.append(self.dummy             , 0               )
            self.ntc[name]     = np.append(self.ntc[name]    , self.temperature)
            self.time[name]    = np.append(self.time[name]   , np.array([datetime.datetime.now(), 0]).reshape((2,1)), axis=1 )

    def setTestingVoltage(self, voltage):
        print('Continous voltage: ' + str(voltage))
        self.voltageTesting = voltage
        
    def setTimestep_m(self, time):
        self.time_step_m=time
        self.act_time_step()
    
    def setTimestep_s(self,time):
        self.time_step_s=time
        self.act_time_step()
        
    def act_time_step(self):
        self.time_step=60*self.time_step_m+self.time_step_s
        print('It time step: '+str(self.time_step_m)+ ' min '+ str(self.time_step_s)+ ' s')       
    
        
    def setTimelimit_h(self, time):
        self.timelimit_h = time
        self.act_timelimit()
    
    def setTimelimit_m(self, time):
        self.timelimit_m = time  
        self.act_timelimit()
        
    def act_timelimit(self):
        self.timelimit=3600*self.timelimit_h+60*self.timelimit_m
        print('It timelimit: '+str(self.timelimit_h)+ ' h '+ str(self.timelimit_m)+ ' min')
              


    def setGlobalTemperature(self, temperature):
        print('Global temperature set: ' + str(temperature))
        self.temperature = temperature

    def setIVStart(self, voltage):
        self.config[1]['v0'] = voltage
        self.startDevices()

    def setIVStop(self, voltage):
        self.config[1]['vmax'] = voltage
        self.startDevices()

    def setIVSteps(self, steps):
        self.config[1]['vsteps'] = steps
        self.startDevices()

    def setIVrampUp(self, rampSpeed):
        self.config[1]['vrampup'] = rampSpeed
        self.startDevices()

    def setIVrampDown(self, rampSpeed):
        self.config[1]['vrampdown'] = rampSpeed
        self.startDevices()

    def setIVwait(self, vwait):
        self.config[1]['vwait'] = vwait
        self.startDevices()

    def setIVaverage(self, average):
        self.config[1]['vaverage'] = average
        self.startDevices()

    def setOutputStatus(self, text, color):
        print("Setting new output status")
        self.setColor(self.outputColor, color)
        self.outputText.setText(text)

    def receiveData(self, voltage, current, name, tipo):
        
        
    
        if tipo:
            self.addData(voltage, current, name)
            print("Sendig plot data for: "  + ', '.join(self.validos))
            self.plotData.emit(name, self.voltage[name], np.array([self.current[name][0], self.current[name][1], self.voltage[name][0], self.voltage[name][1]]), tipo)  
        else:
            self.addData(voltage, current, name)
            print("Sendig plot data for: " + ', '.join(self.validos) )
                
            self.plotData.emit(name, self.time[name], np.array([self.current[name][0], self.current[name][1], self.voltage[name][0], self.voltage[name][1]]), tipo)
        
        self.monitor()


    def monitor(self, voltage = None, current = None):
        if voltage is None and current is None:
            try:
                curr_list=[]
                for dev in self.devicesEnabled:
                    curr_list.append(self.current[dev.GetName()][0][-1])
                voltage = self.voltage[dev.GetName()][0][-1]
                current = max(curr_list, key=abs)
            except:
                voltage = 0
                current = 0
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

    def start_IV(self, tile):
        self.settings.setEnabled(False)
        self.control.setEnabled(False)
        self.device.setEnabled(False)
        self.IVsettings.setEnabled(False)
        self.ItSettings.setEnabled(False)
        self.setColor(self.pb_stop, QtCore.Qt.red)
        print('Starting run for: ' + tile)
        self.plotter.setCVLim(self.sb_v0.value(), self.sb_vmax.value())
        self.clearData(tile)
        self.scan_IV.emit(True)
        
        if self.scanner is not None:
            self.scanner.start()
            
    def start_It(self, tile):
        self.settings.setEnabled(False)
        self.control.setEnabled(False)
        self.IVsettings.setEnabled(False)
        self.gb_supplies.setEnabled(False)
       
        for i in range(self.ItSettings.layout().count()):
            widget = self.ItSettings.layout().itemAt(i).widget()
            
            if isinstance(widget, QtWidgets.QGroupBox) and widget != self.groupBox_history:
                # Desactiva todos los widgets dentro de cada QGroupBox que no sea groupBox_history
                for j in range(widget.layout().count()):
                    subwidget = widget.layout().itemAt(j).widget()
                    if subwidget is not None:
                        subwidget.setEnabled(False)

        # Asegúrate de que groupBox_history y sus widgets estén habilitados
        self.groupBox_history.setEnabled(True)
        for i in range(self.groupBox_history.layout().count()):
            widget = self.groupBox_history.layout().itemAt(i).widget()
            if widget is not None:
                widget.setEnabled(True)
                
        self.setColor(self.pb_stop, QtCore.Qt.red)
        
        self.applyTestVoltage()
        self.applyTimeLimit()
        self.applyTime_step()
        print('Starting run for: ' + tile)
        
        self.clearData(tile)
        self.scan_It.emit(True)
        
        if self.scanner is not None:
            self.scanner.start()
            
    def update_plot(self):
        self.validos=[]
        for dev in self.devicesEnabled:
            self.validos.append(dev.GetName())
        self.plotter.updatePlots(self.validos)
        
        
    def Stop(self):
        self.setColor(self.outputColor, QtCore.Qt.yellow)
        self.running=False
        self.testing=False
        if self.scanner is not None:
            self.scanner.killScan()
    
    def applyTimeLimit(self):
        self.scanner.timelimit_It(self.timelimit)
        
    def applyTime_step(self):
        self.scanner.time_step_It(self.time_step)

    def applyTestVoltage(self):
        self.scanner.rampVoltage(self.voltageTesting)

    def setColor(self, object, color = None):
        palette = object.palette()
        if color is not None:
            palette.setColor(object.backgroundRole(), color)
            palette.setColor(object.foregroundRole(), color)
            object.setPalette(palette)
        else:
            object.setPalette(QtWidgets.QApplication.style().standardPalette())

    def stopped(self):
        self.device.setEnabled(True)


        self.settings.setEnabled(True)
        self.control.setEnabled(True)
        self.IVsettings.setEnabled(True)
        self.gb_supplies.setEnabled(True)
        self.ItSettings.setEnabled(True)


        for i in range(self.ItSettings.layout().count()):
            widget = self.ItSettings.layout().itemAt(i).widget()
            
            if widget is not None:
  
                widget.setEnabled(True)
                for j in range(widget.layout().count()):
                    subwidget = widget.layout().itemAt(j).widget()
                    if subwidget is not None:
                        subwidget.setEnabled(True)


        self.groupBox_history.setEnabled(True)
        for i in range(self.groupBox_history.layout().count()):
            widget = self.groupBox_history.layout().itemAt(i).widget()
            if widget is not None:
                widget.setEnabled(True)
                
        self.setColor(self.pb_stop)
        self.setColor(self.pb_test)
        self.pb_test.setText("RUN It")
        self.testing = False
        self.running = False
        
        print('Stopping run for: ' + ', '.join(self.validos))      
              
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


    def saveFile(self, tipo):
        
        if tipo:
            pre='_IV_'
        else:
            pre='_It_'
            
        filename = self.path + '/' + self.fileName + pre + str(datetime.datetime.now().strftime('_%d_%m_%Y_%H_%M_%S')) + '.dat'
        print('Saving: ' + filename)
        
        timestamp = np.array([t.timestamp() for t in self.time[str(self.devicesEnabled[0].GetName())][0]]).T

        dev_conected=len(self.devicesEnabled)
        
        if dev_conected == 2 and tipo:
            tam=[len(self.voltage[str(self.devicesEnabled[0].GetName())][0]), len(self.current[str(self.devicesEnabled[0].GetName())][1]), len(timestamp)]
            mintam=min(tam)
            res = np.array([self.voltage[str(self.devicesEnabled[0].GetName())][0][:mintam], 
                            self.current[str(self.devicesEnabled[0].GetName())][0][:mintam],
                            self.current[str(self.devicesEnabled[0].GetName())][1][:mintam], 
                            self.voltage[str(self.devicesEnabled[1].GetName())][0][:mintam],
                            self.current[str(self.devicesEnabled[1].GetName())][0][:mintam],
                            self.current[str(self.devicesEnabled[1].GetName())][1][:mintam],
                            timestamp[:mintam]])

            np.savetxt(filename
                    ,res.T
                    ,header=str(pre+
                                str(datetime.datetime.now().strftime("%a %b %d %H:%M:%S Hora estándar romance %Y"))+'\n'+
                                    'Start voltage: '+str(self.sb_v0.value())+' V\n'+
                                    'Stop voltage: '+str(self.sb_vmax.value())+' V\n'+
                                    'Step voltage: '+ str(self.sb_vstep.value())+ ' V\n'+
                                    'Init wait time: '+ str(self.sb_vwait.value())+ 's\n'+
                                    'Temperature: '+str(self.temperature)+' ºC\n'+
                                    'Measurements per point: '+str(self.sb_vaverage.value())+'\n'
                                    'Voltage ('+str(self.names[0])+') (V),Current ('+str(self.names[0])+') (A),Current ('+str(self.names[0])+') standard deviation (A),Voltage ('+str(self.names[1])+') (V),Current ('+str(self.names[1])+') (A),Current ('+str(self.names[1])+') standard deviation (A),Timestamp')
                    ,delimiter=','
                    )
           
        elif dev_conected == 2 and not tipo:
            tam=[len(self.voltage[str(self.devicesEnabled[0].GetName())][0]), len(self.current[str(self.devicesEnabled[0].GetName())][1]), len(timestamp)]
            mintam=min(tam)
            res = np.array([self.voltage[str(self.devicesEnabled[0].GetName())][0][:mintam], 
                            self.current[str(self.devicesEnabled[0].GetName())][0][:mintam],
                            self.current[str(self.devicesEnabled[0].GetName())][1][:mintam], 
                            self.voltage[str(self.devicesEnabled[1].GetName())][0][:mintam],
                            self.current[str(self.devicesEnabled[1].GetName())][0][:mintam],
                            self.current[str(self.devicesEnabled[1].GetName())][1][:mintam], 
                            timestamp[:mintam]])

            np.savetxt(filename
                    ,res.T
                    ,header=str(pre+
                                str(datetime.datetime.now().strftime("%a %b %d %H:%M:%S Hora estándar romance %Y"))+'\n'+
                                    'Time step'+ str(self.time_step)+' s\n'
                                    'Temperature: '+str(self.temperature)+' ºC\n'+
                                    'Measurements per point: '+str(self.sb_vaverage.value())+'\n'
                                    'Voltage ('+str(self.names[0])+') (V),Current ('+str(self.names[0])+') (A),Current ('+str(self.names[0])+') standard deviation (A),Voltage ('+str(self.names[1])+') (V),Current ('+str(self.names[1])+') (A),Current ('+str(self.names[1])+') standard deviation (A),Timestamp')
                    ,delimiter=','
                    )
            
        elif dev_conected == 1 and tipo:
            res = np.array([self.voltage[str(self.devicesEnabled[0].GetName())][0],
                            self.current[str(self.devicesEnabled[0].GetName())][0],
                            self.current[str(self.devicesEnabled[0].GetName())][1],
                            timestamp])
            
            np.savetxt(filename
                    ,res.T
                    ,header=str(pre+
                                str(datetime.datetime.now().strftime("%a %b %d %H:%M:%S Hora estándar romance %Y"))+'\n'+
                                'Start voltage: '+str(self.sb_v0)+' V\n'+
                                'Stop voltage: '+str(self.sb_vmax)+' V\n'+
                                'Step voltage: '+ str(self.sb_vstep)+ ' V\n'+
                                'Init wait time: '+ str(self.sb_vwait)+ 's\n'+
                                'Temperature: '+str(self.temperature)+' ºC\n'+
                                'Voltage ('+str(self.devicesEnabled[0].GetName())+') (V),Current ('+str(self.devicesEnabled[0].GetName())+') (A),Current ('+str(self.devicesEnabled[0].GetName())+') standard deviation (A),Timestamp')
                    ,delimiter=','
                    )
        elif dev_conected == 1 and not tipo:
            res = np.array([self.voltage[str(self.devicesEnabled[0].GetName())][0],
                            self.current[str(self.devicesEnabled[0].GetName())][0],
                            self.current[str(self.devicesEnabled[0].GetName())][0],
                            timestamp])
            
            np.savetxt(filename
                    ,res.T
                    ,header=str(pre+
                                str(datetime.datetime.now().strftime("%a %b %d %H:%M:%S Hora estándar romance %Y"))+'\n'+
                                'Time start'+
                                'Temperature: '+str(self.temperature)+' ºC\n'+
                                'Voltage ('+str(self.devicesEnabled[0].GetName())+') (V),Current ('+str(self.devicesEnabled[0].GetName())+') (A),Current ('+str(self.devicesEnabled[0].GetName())+') standard deviation (A),Timestamp')
                    ,delimiter=','
                    )














class Plotter(FigureCanvas):
    def __init__(self, plots, parent=None, width=5, height=4, dpi=100, **kwargs):
        self._fig, self._axes = plt.subplots(
            figsize=(width, height),
            dpi=dpi,
            nrows=1,
            ncols=1,
            constrained_layout=True
        )
        # Eje twin (compartido) para el gráfico doble
        self._axes_twin = self._axes.twinx()

        self._history = 60
        FigureCanvas.__init__(self, self._fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self._plots = plots.copy()
        self._visiblePlots = [plots.copy(), plots.copy()]
        
        self._dataX = {plot: [[], []] for plot in self._plots}
        self._dataY = {plot: [[], [], [], []] for plot in self._plots}

        self._xAxis = kwargs.get('xscale', 'linear')
        self._yAxis = kwargs.get('yscale', 'linear')
        self._xLabel = kwargs.get('xlabel', ['Voltage [V]', 'Time'])
        self._yLabel = kwargs.get('ylabel', ['Current [A]', 'Voltage [V]'])
        self._xlim1 = -50
        self._xlim2 = 0
        self.emptyData()
        self.replot(True)

    def setVisiblePlots(self, plots):
        self.emptyData()
        self._visiblePlots[0] = plots.copy()
        self.updateVisibility()

    def emptyData(self):
        for plot in self._plots:
            self._dataX[plot] = [[], []]
            self._dataY[plot] = [[], [], [], []]

    def receiveData(self, plot, dataX, dataY, tipo):
        self._dataX[plot] = dataX
        self._dataY[plot] = dataY
        self.replot(tipo)

    def replot(self, tipo):
        try:
            if tipo:
                self._replot_single_subplot()
            else:
                self._replot_twin_subplot()
        except Exception as e:
            print(f"Error during plotting: {e}")

        self.draw()

    def _replot_single_subplot(self):
        self._clear_axes()
        self._set_axes_visibility(single=True)

        for plot in self._visiblePlots[0]:
            self._axes.errorbar(
                self._dataX[plot][0],
                self._dataY[plot][0],
                xerr=self._dataX[plot][1],
                yerr=self._dataY[plot][1],
                fmt='x-', label=plot
            )

        self._axes.legend()
        self._axes.set_xlim(self._xlim1, self._xlim2)
        self._axes.set_xlabel(self._xLabel[0])
        self._axes.set_ylabel(self._yLabel[0])

    def _replot_twin_subplot(self):
        self._clear_axes()
        self._set_axes_visibility(single=False)

        for plot in self._visiblePlots[1]:
            # Gráfico primario en el primer eje
            self._axes.errorbar(
                self._dataX[plot][0],
                self._dataY[plot][0],
                yerr=self._dataY[plot][1],
                fmt='x-', label=f"{plot} current"
            )

            # Gráfico secundario en el eje twin
            
            # Configuraciones de los ejes
            self._axes.set_xlabel(self._xLabel[1])
            self._axes.set_ylabel(self._yLabel[0])
            self._axes_twin.set_ylabel(self._yLabel[1], color='black')
            self._axes_twin.yaxis.set_label_position('right')
            self._axes_twin.yaxis.tick_right()

            try:
                last = self._dataX[plot][0][-1]
                previous = datetime.datetime.fromtimestamp(last.timestamp() - self._history)
                self._axes.set_xlim(left=previous, right=last)
                self._axes_twin.set_xlim(left=previous, right=last)
            except Exception as e:
                print(f"Error setting x-axis limits: {e}")
        self._axes_twin.plot(
                self._dataX[plot][0],
                self._dataY[plot][2],
                '-', label=f"Voltage", color='black'
            )

        self._axes.legend(loc='upper left')
        self._axes_twin.legend(loc='upper right')

    def _clear_axes(self):
        self._axes.clear()
        self._axes_twin.clear()

    def _set_axes_visibility(self, single):
        if single:
            self._axes.set_visible(True)
            self._axes_twin.set_visible(False)
        else:
            self._axes.set_visible(True)
            self._axes_twin.set_visible(True)

    def setHistory(self, value):
        self._history = value * 60
        self.replot(False)

    def updateVisibility(self):
        self._set_axes_visibility(single=bool(self._visiblePlots[0]))

    def updatePlots(self, new_plots):
        self._plots = new_plots.copy()
        self._visiblePlots[0] = new_plots.copy()
        self._dataX = {plot: [[], []] for plot in self._plots}
        self._dataY = {plot: [[], [], [], []] for plot in self._plots}
        self.emptyData()
        self.replot(True)

    def setCVLim(self, voltage1, voltage2):
        self._xlim1 = min([voltage1, voltage2])
        self._xlim2 = max([voltage1, voltage2])

        
        
        
        
        
        
        
        
        
class Scanner(QtCore.QThread):
    outputOn  = QtCore.pyqtSignal()
    outputOff = QtCore.pyqtSignal()

    stepDone = QtCore.pyqtSignal()
    scanDone = QtCore.pyqtSignal()

    saveData = QtCore.pyqtSignal(bool)

    rampUp   = QtCore.pyqtSignal()
    rampDown = QtCore.pyqtSignal()

    measured = QtCore.pyqtSignal(np.ndarray, np.ndarray, str, bool)

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

        self.initCommands()
        
    def setDevices(self, devices):
        self.devices  = devices
        
    def setSettings(self, settings):
        self.settings = settings
        self.reloadState()

    def reloadState(self):
        self.testing  = False
        self.running  = False
        self.finished = False
        self.counter  = 0
        
        if self.settings['vmax']<self.settings['v0']:
            sign=-1
        else:
            sign=1
        
        self.dV       = self.settings['vsteps']*sign

        self.text.emit("Preparing IV scan from " + str(self.settings['v0']) + "V to " + str(self.settings['vmax']) + "V in " + str(self.settings['vsteps']) + " steps")
        self.text.emit(".. waiting " + str(self.settings['vwait']) + " sec each averaging for " + str(self.settings['vaverage']) + " measurements")
        self.text.emit(".. ramping up by " + str(self.settings['vrampup'])+"V/s, ramping down by " + str(self.settings['vrampdown']) + "V/s")        

    def initCommands(self):
        self.rampUp.connect(lambda: self.newIV(True))
        self.rampDown.connect(lambda: self.newIV(False))

    def prepare(self):
        self.text.emit("Preparing devices for run")
        self.outputOn.emit()
        # set voltage to all devices without reading out (as they are turned off)
        self.setVoltage(self.settings['v0'])
        for dev in self.devices:
            dev.Start()

        self.counter  = 0
        self.finished = False
        
        
    def prepareTest(self):
        self.text.emit('Prepare devices for It')
        self.outputOn.emit()
        self.setVoltage(0)
        self.counter = 0
        for dev in self.devices:
            dev.Start()
            
        self.finished = False
            
    def finish(self):
        self.text.emit("Stopping devices after run")
        self.outputOff.emit()
        self.testing=False
        self.running=False
        for dev in self.devices:
            dev.Stop()

    def killScan(self):
        self.running = False
        self.testing = False
        self.text.emit('Kill scan initialized.')
        
    def enableScan(self, enabled = True):
        self.running = enabled

    def runScan(self):
        self.prepare()

        self.text.emit("Starting IV run")
        while self.running:

            self.measure(True)
            if self.counter < abs((self.settings['vmax']-self.settings['v0'])/self.settings['vsteps']):
                self.newIV(True)
            else:
                self.newIV(False)

        if not self.finished:
            self.newIV(False)

        self.finish()
        self.scanDone.emit()
        
    def runTest(self):
        self.prepareTest()
        self.text.emit("Starting It run")
        
        self.ramping(self.newVoltage, self.voltage, self.voltage, self.newVoltage, self.settings['vrampup'])
        time_start=time.time()
        
        self.measure(False, True)
        
        while self.testing and (time.time()-time_start)<self.timelimit:
            self.counter +=1
            self.measure(False)
            
        if self.voltage != 0:
            self.newVoltage = self.voltage
            self.ramping(0, self.voltage, 0, self.voltage, self.settings['vrampdown'])
        
        self.saveData.emit(False)
        self.finish()
        self.scanDone.emit()

    def run(self):
        self.text.emit('Starting run thread ...')
        if self.running:
            self.text.emit('.. scan IV')
            self.runScan()
        elif self.testing:
            self.text.emit('.. test It')
            self.runTest()

    def measure(self, tipo, primera=False):
        if tipo or primera:
            wait=self.settings['vwait']
        else:
            wait= self.time_step
        
        
        timeStart = time.time()
        
        while (time.time() - timeStart) < wait and (self.testing or self.running):
            time.sleep(0.05)
            
        
                    
        for dev in self.devices:
            average = self.settings['vaverage']
            Vaverage = np.zeros(average)
            Iaverage = np.zeros(average)
            for taverage in np.arange(average):
                Vaverage[taverage], Iaverage[taverage] = dev.ReadVoltCurrent()

            vMeas = np.array([np.mean(Vaverage), np.std(Vaverage)])
            iMeas = np.array([np.mean(Iaverage), np.std(Iaverage)])

            if self.testing:
                self.measured.emit(vMeas, iMeas, dev.GetName(), False)
                self.progress.emit(int(self.counter*wait*100/self.timelimit))
            elif self.running:
                self.measured.emit(vMeas, iMeas, dev.GetName(), True)


    def newIV(self, up = True):
        
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
            self.running  = False
            self.testing  = False
            self.finished = True
            newvoltage=0
            self.saveData.emit(True)
            
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

        for i in range(1,5):
            try:
                ramp=rampLen*i/4
                timeStart = time.time()
                new = oldvoltage + (sign * ramp)
                iMeas = np.NaN
                for dev in self.devices:
                    vMeas, iMeas = self.setVoltage(new, dev)

                    if abs(iMeas) >= self.currentLimit:
                        self.finish()
                        self.scanDone.emit()
                        self.running = False
                        self.testing = False
                        self.text.emit("Reached maximal enabled current.")
                        raise ValueError("Reached maximal enabled current.")
               
                    self.progress.emit(int(100 * (vMeas - v0) / (vmax - v0)) )
                
                while (time.time() - timeStart) < rampLen/(4*rampSpeed):
                    time.sleep(0.01)
            except:
                break
        

    def timelimit_It(self, timelimit):
        self.timelimit= timelimit
        self.text.emit("Selecting new timelimit for It measurement: "+ str(self.timelimit))
        
    def time_step_It(self, time_step):
        self.time_step=time_step
        self.text.emit("Selecting new time step for It measurement: "+ str(self.time_step))
        
            
    def rampVoltage(self, voltage):
        self.newVoltage = voltage
        self.text.emit("Selecting new test voltage value: " + str(self.newVoltage))


    def setVoltage(self, voltage, device = None):
        self.voltage = voltage
        if device is None:
            self.text.emit("Applied testing voltage in devices: " + str(voltage) + "V")
            for dev in self.devices:
                dev.SetVoltage(voltage)
        else:
            device.SetVoltage(voltage)
            return device.ReadVoltCurrent()

    def testVoltage(self, enable):
        self.testing = enable
        

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

    def setOutputSide(self, side):
        self.text.emit("Setting output side as: " + str(side))
        for dev in self.devices:
            dev.OutputSide(side)





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
        
        self.running = False

        self.Init()
		
    def Init(self):
        if self.Version>2470:
            self.instr.write('*RST')
            self.instr.write(':SENS:FUNC "CURR"')
            self.instr.write(':SOUR:FUNC VOLT ')
            
        elif self.Version > 2000:
            self.instr.write('*RST')
        elif self.Version > 400:
            self.instr.write('*CLS')
            self.instr.write('O0X')
            self.instr.write('V0,1X') # repeated twice as sometimes device gets stuck after IDN or some command
            self.instr.write('V0,1X')
        elif self.Version < 0: # This is for debugging only
            print("DUMMY: initialized")
                
    
    def GetName(self):
        if self.GPIB == 24 and self.Version>0:
            return "PAD"
        elif self.GPIB == 25 and self.Version>0:
            return "RING"
        else:
            if self.Version > 0:
                return 'DEVICE' + str(self.Version) + ' GPIB=' + str(self.GPIB)
            else:
                return 'DUMMY' + str(self.Version) + ' GPIB=' + str(self.GPIB)
          
            
    def Start(self):
        self.Stop()
        self.OutputOn()
            
    def OutputOn(self):
        print("Enabling output.")
        self.running = True
        if self.Version > 2000:
            self.instr.write(':OUTP:STAT ON')      #turn output on
        elif self.Version > 400:
            self.instr.write('O1X')
        elif self.Version < 0: # This is for debugging only
            print("DUMMY: output on")

    def Stop(self):
        print("Disabling output")
        self.running = False
        if self.Version > 2000:
            self.instr.write(':OUTP:STAT OFF')
        elif self.Version > 400:
            self.instr.write('O0X')
        elif self.Version < 0: # This is for debugging only
            print("DUMMY: output off")
            
    def OutputSide(self, side):
        print("Changing output side to: " + str(side))
        if self.Version > 2000:
            if "REAR" in side.upper() or "BACK" in side.upper():
                self.instr.write(':ROUT:TERM REAR')
            else:
                self.instr.write(':ROUT:TERM FRON')
        elif self.Version < 0: # This is for debugging only
            print("DUMMY: side changed")
            
            
    def SetCurrentRangeAuto(self):
        if self.Version > 2000:
            self.instr.write(':SENS:CURR:RANG:AUTO ON')
            print('Current range set AUTO')
        
    def SetCurrentRange(self, current):
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
        if self.Version > 2450:
            self.instr.write('SOUR:VOLT '+str(volt))
        elif self.Version > 2000:
            self.instr.write(':SOUR:VOLT '+str(volt))
        elif self.Version > 400:
            self.instr.write('V'+str(volt)+'X') # just set voltage without changing ranges
        elif self.Version <= 300 and self.Version > 0:
            #self.instr.query('F0,0X')
            #self.instr.write('H0X')
            retval = self.instr.query('B'+str(volt)+',0,0X')
        elif self.Version < 0: # This is for debugging only
            pass

    def ReadVoltCurrent(self):
        if self.running:
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
                        return self.voltage, self.voltage/5e8+np.random.randn()/1e9
                    else:
                        return self.voltage, self.voltage/3e8+np.random.randn()/1e9
            else:
                # return zeros in case the device is not on
                return self.voltage, 0
        else:
            return self.voltage,0
            
    def SetCompliance(self, limit):
        if self.Version >2450:
            self.instr.write(':SOUR:VOLT:ILIM '+str(limit))
        elif self.Version > 2000:
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

    ######### Read config options for IV scan #######
    Section='IV scan'
    if config.has_section(Section):
        data['ivscan'   ] = config.getboolean(Section,'DoIVscan'   )
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
                for i in range(2):
                    if i==0:
                        board_adress=''
                    else:
                        board_adress=str(i)
                    address = 'GPIB'+board_adress+'::'+str(config.getint(Section,'GPIB'))+'::INSTR'
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



    
    
    


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec_())
    