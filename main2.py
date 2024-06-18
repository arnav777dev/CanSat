

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cProfile
import subprocess
import time
from time import sleep
import matplotlib.ticker as ticker

import io
import folium  # pip install folium
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QMdiArea, QMdiSubWindow, QTextEdit
import random
from PyQt5 import uic
from PyQt5.QtWebEngineWidgets import QWebEngineView  # pip install PyQtWebEngine
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
# import pyqtgraph as pg
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, QDateTime,QTime
# from pyqtgraph import PlotWidget, plot
# import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import matplotlib
import pandas as pd
import csv
import time
from itertools import count
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from PyQt5.QtWidgets import QFileDialog
import threading
from matplotlib.figure import Figure
import tkinter
from numpy import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import serial
# import serial.tools.list_ports``
import threading
import multiprocessing
import serial
import serial.tools.list_ports
from datetime import datetime
from matplotlib.ticker import FuncFormatter
global vel,prevalt
prevalt=0
counterx=0
memory=['0', '00:00:00', '0', '0', '0', '0', '0', '00:00:00', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 
'0\n']
initial=['0', '00:00:00', '0', '0', '0', '0', '0', '00:00:00', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 
'0\n']
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # self.ser=serial.Serial('COM13', 9600)
        if os.path.exists(r'C:\Users\DELL\OneDrive\Desktop\cansat\pfrcsv.csv'):
            with open(r'C:\Users\DELL\OneDrive\Desktop\cansat\pfrcsv.csv', 'r') as file:
                
                reader = csv.reader(file)
                last_row = None
                for row in reader:
                    last_row = row
                    
            if last_row is not None:
                last_row_values = last_row
                global initial
                global memory
                for i in range(len(initial)):
                    if i < len(last_row_values):
                        initial[i] = last_row_values[i]
                        memory[i] = last_row_values[i]
                        print(initial[i])

        else:
            initial=['0', '00:00:00', '0', '0', '0', '0', '0', '00:00:00', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 
'0\n']
            

        # self.ser = serial.Serial('COM13', 9600)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1855, 1107)
        MainWindow.setStyleSheet("background-color:#303030")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color:#303030;\n"
                                 "border-radius:10px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(10, 30))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 15))
        self.frame_2.setStyleSheet("\n"
                                   "\n"
                                   "background-color:orange;\n"
                                   "")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 117))
        self.frame_3.setStyleSheet("background-color:#595959;\n"
                                   "padding: 1px;\n"
                                   "border-radius:5px;\n"
                                   "\n"
                                   "")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.NameSymbol = QtWidgets.QFrame(self.frame_3)
        self.NameSymbol.setMinimumSize(QtCore.QSize(237, 66))
        self.NameSymbol.setStyleSheet("background-color:rgb(89, 89, 89);")
        self.NameSymbol.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.NameSymbol.setFrameShadow(QtWidgets.QFrame.Raised)
        self.NameSymbol.setObjectName("NameSymbol")
        self.label_7 = QtWidgets.QLabel(self.NameSymbol)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 57, 49))
        self.label_7.setMinimumSize(QtCore.QSize(10, 0))
        self.label_7.setMaximumSize(QtCore.QSize(57, 49))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("icons/space-shuttle.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.label_7.setObjectName("label_7")
        self.Commands = QtWidgets.QFrame(self.NameSymbol)
        self.Commands.setGeometry(QtCore.QRect(350, -10, 931, 119))
        self.Commands.setMinimumSize(QtCore.QSize(900, 90))
        self.Commands.setStyleSheet("background-color:rgb(89, 89, 89)")
        self.Commands.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Commands.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Commands.setObjectName("Commands")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.Commands)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_31 = QtWidgets.QFrame(self.Commands)
        self.frame_31.setMinimumSize(QtCore.QSize(46, 95))
        self.frame_31.setSizeIncrement(QtCore.QSize(0, 3))
        self.frame_31.setStyleSheet("background-color:rgb(89, 89, 89);\n"
                                    "border: solid grey;\n"
                                    "border-width: 0px 3px 0px 3px\n"
                                    "")
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_31)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_31)
        self.pushButton_17.setMinimumSize(QtCore.QSize(49, 41))
        self.pushButton_17.setBaseSize(QtCore.QSize(9, 0))
        self.pushButton_17.setStyleSheet("\n"
                                         "QPushButton{\n"
                                         "    border: 6px solid white;\n"
                                         "    border-radius:12px;\n"
                                         "\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "    border: 6px solid orange;\n"
                                         "\n"
                                         "    change-cursor: cursor(\'PointingHand\');\n"
                                         "    transition:2s;\n"
                                         "}\n"
                                         "QPushButton:after{\n"
                                         "    border: 6px solid #ff9933;;\n"
                                         "}\n"
                                         "")
        self.pushButton_17.setText("")
        self.pushButton_17.setIconSize(QtCore.QSize(32, 25))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_17.clicked.connect(lambda: self.send_string('s'))
        self.verticalLayout_19.addWidget(
            self.pushButton_17, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_16 = QtWidgets.QLabel(self.frame_31)
        self.label_16.setMinimumSize(QtCore.QSize(0, 12))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("border:none")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_19.addWidget(
            self.label_16, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_6.addWidget(self.frame_31)
        self.frame_30 = QtWidgets.QFrame(self.Commands)
        self.frame_30.setMinimumSize(QtCore.QSize(46, 95))
        self.frame_30.setSizeIncrement(QtCore.QSize(0, 3))
        self.frame_30.setStyleSheet("background-color:rgb(89, 89, 89);\n"
                                    "border: solid grey;\n"
                                    "border-width: 0px 3px 0px 0px")
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_30)
        self.pushButton_16.setGeometry(QtCore.QRect(40, 12, 49, 41))
        self.pushButton_16.setMinimumSize(QtCore.QSize(49, 41))
        self.pushButton_16.setBaseSize(QtCore.QSize(9, 0))
        self.pushButton_16.setStyleSheet("\n"
                                         "QPushButton{\n"
                                         "    border: 6px solid white;\n"
                                         "    border-radius:12px;\n"
                                         "\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "    border: 6px solid #ff9933;\n"
                                         "    change-cursor: cursor(\'PointingHand\');\n"
                                         "    transition:2s;\n"
                                         "}\n"
                                         "QPushButton:after{\n"
                                         "    border: 6px solid #ff9933;;\n"
                                         "}\n"
                                         "")
        self.pushButton_16.setText("")
        self.pushButton_16.setIconSize(QtCore.QSize(32, 25))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.clicked.connect(lambda: self.send_string('c'))
        self.label_15 = QtWidgets.QLabel(self.frame_30)
        self.label_15.setGeometry(QtCore.QRect(27, 65, 75, 18))
        self.label_15.setMinimumSize(QtCore.QSize(0, 12))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("border:none")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_6.addWidget(self.frame_30)
        self.frame_26 = QtWidgets.QFrame(self.Commands)
        self.frame_26.setMinimumSize(QtCore.QSize(46, 95))
        self.frame_26.setSizeIncrement(QtCore.QSize(0, 3))
        self.frame_26.setStyleSheet("background-color:rgb(89, 89, 89);\n"
                                    "border: solid grey;\n"
                                    "border-width: 0px 3px 0px 0px")
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_26)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_26)
        self.pushButton_11.setMinimumSize(QtCore.QSize(49, 41))
        self.pushButton_11.setBaseSize(QtCore.QSize(9, 0))
        self.pushButton_11.setStyleSheet("\n"
                                         "QPushButton{\n"
                                         "    border: 6px solid white;\n"
                                         "    border-radius:12px;\n"
                                         "\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "    border: 6px solid #ff9933;\n"
                                         "    change-cursor: cursor(\'PointingHand\');\n"
                                         "    transition:2s;\n"
                                         "}\n"
                                         "QPushButton:after{\n"
                                         "    border: 6px solid #ff9933;;\n"
                                         "}\n"
                                         "")
        self.pushButton_11.setText("")
        self.pushButton_11.setIconSize(QtCore.QSize(32, 25))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(lambda: self.send_string('e'))
        self.verticalLayout_14.addWidget(
            self.pushButton_11, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_11 = QtWidgets.QLabel(self.frame_26)
        self.label_11.setMinimumSize(QtCore.QSize(0, 12))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border:none")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_14.addWidget(
            self.label_11, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
        self.horizontalLayout_6.addWidget(self.frame_26)
        self.frame_27 = QtWidgets.QFrame(self.Commands)
        self.frame_27.setMinimumSize(QtCore.QSize(46, 95))
        self.frame_27.setSizeIncrement(QtCore.QSize(0, 3))
        self.frame_27.setStyleSheet("background-color:rgb(89, 89, 89);\n"
                                    "border: solid grey;\n"
                                    "border-width: 0px 3px 0px 0px")
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_27)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_27)
        self.pushButton_13.setMinimumSize(QtCore.QSize(49, 41))
        self.pushButton_13.setBaseSize(QtCore.QSize(9, 0))
        self.pushButton_13.setStyleSheet("\n"
                                         "QPushButton{\n"
                                         "    border: 6px solid white;\n"
                                         "    border-radius:12px;\n"
                                         "\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "    border: 6px solid #ff9933;\n"
                                         "    change-cursor: cursor(\'PointingHand\');\n"
                                         "    transition:2s;\n"
                                         "}\n"
                                         "QPushButton:after{\n"
                                         "    border: 6px solid #ff9933;;\n"
                                         "}\n"
                                         "")
        self.pushButton_13.setText("")
        self.pushButton_13.setIconSize(QtCore.QSize(32, 25))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(lambda: self.send_string_dis('d'))
        self.verticalLayout_15.addWidget(
            self.pushButton_13, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_12 = QtWidgets.QLabel(self.frame_27)
        self.label_12.setMinimumSize(QtCore.QSize(0, 12))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("border:none")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_15.addWidget(
            self.label_12, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_6.addWidget(self.frame_27)
        self.frame_29 = QtWidgets.QFrame(self.Commands)
        self.frame_29.setMinimumSize(QtCore.QSize(46, 95))
        self.frame_29.setSizeIncrement(QtCore.QSize(0, 3))
        self.frame_29.setStyleSheet("background-color:rgb(89, 89, 89);\n"
                                    "border: solid grey;\n"
                                    "border-width: 0px 3px 0px 0px")
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_29)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_29)
        self.pushButton_15.setMinimumSize(QtCore.QSize(49, 41))
        self.pushButton_15.setBaseSize(QtCore.QSize(9, 0))
        self.pushButton_15.setStyleSheet("\n"
                                         "QPushButton{\n"
                                         "    border: 6px solid white;\n"
                                         "    border-radius:12px;\n"
                                         "\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "    border: 6px solid #ff9933;\n"
                                         "    change-cursor: cursor(\'PointingHand\');\n"
                                         "    transition:2s;\n"
                                         "}\n"
                                         "QPushButton:after{\n"
                                         "    border: 6px solid #ff9933;;\n"
                                         "}\n"
                                         "")
        self.pushButton_15.setText("")
        self.pushButton_15.setIconSize(QtCore.QSize(32, 25))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.clicked.connect(lambda: self.graph('a'))
        self.verticalLayout_17.addWidget(
            self.pushButton_15, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_14 = QtWidgets.QLabel(self.frame_29)
        self.label_14.setMinimumSize(QtCore.QSize(0, 12))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("border:none")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_17.addWidget(
            self.label_14, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_6.addWidget(self.frame_29)
        self.frame_28 = QtWidgets.QFrame(self.Commands)
        # self.frame_28.setGeometry(QtCore.QRect(1220, 0, 145, 95))
        self.frame_28.setMinimumSize(QtCore.QSize(46, 95))
        self.frame_28.setSizeIncrement(QtCore.QSize(0, 3))
        self.frame_28.setStyleSheet("background-color:rgb(89, 89, 89);\n"
                                    "border: solid grey;\n"
                                    "border-width: 0px 3px 0px 0px")
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_28)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_28)
        self.pushButton_14.setMinimumSize(QtCore.QSize(49, 41))
        self.pushButton_14.setBaseSize(QtCore.QSize(9, 0))
        self.pushButton_14.setStyleSheet("\n"
                                         "QPushButton{\n"
                                         "    border: 6px solid white;\n"
                                         "    border-radius:12px;\n"
                                         "\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "    border: 6px solid #ff9933;\n"
                                         "    change-cursor: cursor(\'PointingHand\');\n"
                                         "    transition:2s;\n"
                                         "}\n"
                                         "QPushButton:after{\n"
                                         "    border: 6px solid #ff9933;;\n"
                                         "}\n"
                                         "")
        self.pushButton_14.setText("")
        self.pushButton_14.setIconSize(QtCore.QSize(32, 25))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.clicked.connect(lambda: self.send_string('x'))
        
        self.verticalLayout_16.addWidget(
            self.pushButton_14, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_13 = QtWidgets.QLabel(self.frame_28)
        self.label_13.setMinimumSize(QtCore.QSize(0, 12))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("border:none")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_16.addWidget(
            self.label_13, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_6.addWidget(self.frame_28)
        self.frame_32 = QtWidgets.QFrame(self.NameSymbol)
        self.frame_32.setGeometry(QtCore.QRect(1270, 2, 145, 95))
        self.frame_32.setMinimumSize(QtCore.QSize(46, 95))
        self.frame_32.setSizeIncrement(QtCore.QSize(0, 3))
        self.frame_32.setStyleSheet("background-color:rgb(89, 89, 89);\n"
                                    "border: solid grey;\n"
                                    "border-width: 0px 3px 0px 0px")
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.frame_mtime = QtWidgets.QFrame(self.NameSymbol)
        self.frame_mtime.setGeometry(QtCore.QRect(1500, 2, 245, 91))
        self.frame_mtime.setStyleSheet(
            "background-color:#1d1f1f;border: 2px solid green")
        self.frame_mtime.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_mtime.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_mtime.setObjectName("frame_mtime")
        self.verticalLayout_mtime = QtWidgets.QVBoxLayout(self.frame_mtime)
        self.verticalLayout_mtime.setObjectName("verticalLayout_mtime")
        self.label_mtime_title = QtWidgets.QLabel(self.frame_mtime)
        self.label_mtime_title.setObjectName("label_mtime_title")
        self.label_mtime_title.setStyleSheet(
            "border: none;")
        self.verticalLayout_mtime.addWidget(self.label_mtime_title)
        self.label_mtime_val = QtWidgets.QLabel(self.frame_mtime)
        # self.label_mtime_val.setStyleSheet("font-size:20px;")
        self.label_mtime_val.setObjectName("label_mtime_val")
        self.label_mtime_val.setStyleSheet(
            "font-size:20px; border: none;")
        self.verticalLayout_mtime.addWidget(self.label_mtime_val)
        # self.timer_mtime = QTimer()
        # self.timer_mtime.timeout.connect(self.update_label_values)
        # self.timer_mtime.start(1)
        # self.current_time = 0
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_32)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_32)
        self.pushButton_18.setMinimumSize(QtCore.QSize(49, 41))
        self.pushButton_18.setBaseSize(QtCore.QSize(9, 0))
        self.pushButton_18.setStyleSheet("\n"
                                         "QPushButton{\n"
                                         "    border: 6px solid white;\n"
                                         "    border-radius:12px;\n"
                                         "\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "    border: 6px solid #ff9933;\n"
                                         "    change-cursor: cursor(\'PointingHand\');\n"
                                         "    transition:2s;\n"
                                         "}\n"
                                         "QPushButton:after{\n"
                                         "    border: 6px solid #ff9933;;\n"
                                         "}\n"
                                         "")
        self.pushButton_18.setText("")
        self.pushButton_18.setIconSize(QtCore.QSize(32, 25))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_18.clicked.connect(lambda: self.graph('r'))
        # self.pushButton_18.clicked.connect(lambda: self.graph(1))
        self.verticalLayout_18.addWidget(
            self.pushButton_18, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_19 = QtWidgets.QLabel(self.frame_32)
        self.label_19.setMinimumSize(QtCore.QSize(0, 12))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("border:none")
        self.label_19.setObjectName("label_19")
        self.verticalLayout_18.addWidget(
            self.label_19, 0, QtCore.Qt.AlignBottom)
        self.label_6 = QtWidgets.QLabel(self.NameSymbol)
        self.label_6.setGeometry(QtCore.QRect(130, 50, 181, 20))
        self.label_6.setStyleSheet("border:none;\n"
                                   "")
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.NameSymbol)
        self.label_5.setGeometry(QtCore.QRect(130, 20, 121, 20))
        self.label_5.setStyleSheet("\n"
                                   "\n"
                                   "Qlabel{\n"
                                   "        border:none;\n"
                                   "    \n"
                                   "}\n"
                                   "Qlabel:hover{\n"
                                   "color:#FF9933\n"
                                   "    \n"
                                   "}\n"
                                   "\n"
                                   "")
        self.label_5.setObjectName("label_5")
        self.label_img = QtWidgets.QLabel(self.NameSymbol)
        self.label_img.setGeometry(QtCore.QRect(20, -5, 110, 100))
        self.pixmap_img = QtGui.QPixmap('./kalpana.png')
        self.label_img.setPixmap(self.pixmap_img)
        self.horizontalLayout_5.addWidget(self.NameSymbol)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("\n"
                                   "         background-color:#2A2A2A")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 800))
        self.scrollArea.setStyleSheet("border-radius:10px")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(
            QtCore.QRect(0, -789, 1768, 1589))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setStyleSheet("background-color:#2A2A2A;\n"
                                                    "         border-radius:10px")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.part1 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.part1.setMinimumSize(QtCore.QSize(0, 780))
        self.part1.setStyleSheet("\n"
                                 "         QPushButton{\n"
                                 "               border-radius:0;\n"
                                 "               color:white;\n"
                                 "               background-color:#1d1f1f;\n"
                                 "               font-size:14px;\n"
                                 "               font-weight:400;\n"
                                 "\n"
                                 "         }\n"
                                 "         QPushButton:hover{\n"
                                 "               background-color:#595959;\n"
                                 "               change-cursor: cursor(\'PointingHand\');\n"
                                 "               transition:2s;\n"
                                 "         }\n"
                                 "         QPushButton:pressed{\n"
                                 "               background-color:#595959;\n"
                                 "         }\n"
                                 "         \n"
                                 "         ")
        self.part1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.part1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.part1.setObjectName("part1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.part1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_9 = QtWidgets.QFrame(self.part1)
        self.frame_9.setMaximumSize(QtCore.QSize(350, 670))
        self.frame_9.setStyleSheet("background-color:#595959;\n"
                                   "         border-radius:10px")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_15 = QtWidgets.QFrame(self.frame_9)
        self.frame_15.setMinimumSize(QtCore.QSize(277, 303))
        self.frame_15.setStyleSheet(
            "background-color:#2A2A2A;border 1px solid orange")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.label_61 = QtWidgets.QLabel(self.frame_15)
        self.label_61.setGeometry(QtCore.QRect(20, 20, 291, 41))
        self.label_61.setStyleSheet("color:white;\n"
                                    "         background:#595959;\n"
                                    "         font-size:15px;\n"
                                    "         font-weight:600;")
        self.label_61.setObjectName("label_61")
        self.frame_16 = QtWidgets.QFrame(self.frame_15)
        self.frame_16.setGeometry(QtCore.QRect(20, 100, 291, 81))
        self.frame_16.setStyleSheet("border-radius:0;\n"
                                    "               color:white;\n"
                                    "               background-color:#1d1f1f;\n"
                                    "               font-size:14px;\n"
                                    "               font-weight:500;")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_71 = QtWidgets.QLabel(self.frame_16)
        self.label_71.setObjectName("label_71")
        self.verticalLayout_23.addWidget(self.label_71)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.frame_16)
        self.label_8.setStyleSheet("font-size:20px;\n"
                                   "border: 1 px solid #FF9933;")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.frame_16)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.verticalLayout_23.addLayout(self.horizontalLayout_8)
        self.frame_24 = QtWidgets.QFrame(self.frame_15)
        self.frame_24.setGeometry(QtCore.QRect(20, 320, 291, 81))
        self.frame_24.setStyleSheet("border-radius:0;\n"
                                    "               color:white;\n"
                                    "               background-color:#1d1f1f;\n"
                                    "               font-size:14px;\n"
                                    "               font-weight:500;")
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.frame_24)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_10 = QtWidgets.QLabel(self.frame_24)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_24.addWidget(self.label_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_17 = QtWidgets.QLabel(self.frame_24)
        self.label_17.setStyleSheet("font-size:20px;")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_9.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.frame_24)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_9.addWidget(self.label_18)
        self.verticalLayout_24.addLayout(self.horizontalLayout_9)
        self.frame_25 = QtWidgets.QFrame(self.frame_15)
        self.frame_25.setGeometry(QtCore.QRect(20, 210, 291, 81))
        self.frame_25.setStyleSheet("border-radius:0;\n"
                                    "               color:white;\n"
                                    "               background-color:#1d1f1f;\n"
                                    "               font-size:14px;\n"
                                    "               font-weight:500;")
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_25)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.label_22 = QtWidgets.QLabel(self.frame_25)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_25.addWidget(self.label_22)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_23 = QtWidgets.QLabel(self.frame_25)
        self.label_23.setStyleSheet("font-size:20px;")
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_10.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.frame_25)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_10.addWidget(self.label_24)
        self.verticalLayout_25.addLayout(self.horizontalLayout_10)
        self.frame_36 = QtWidgets.QFrame(self.frame_15)
        self.frame_36.setGeometry(QtCore.QRect(20, 541, 291, 81))
        self.frame_36.setStyleSheet("border-radius:0;\n"
                                    "               color:white;\n"
                                    "               background-color:#1d1f1f;\n"
                                    "               font-size:14px;\n"
                                    "               font-weight:500;")
        self.frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.frame_36)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.label_34 = QtWidgets.QLabel(self.frame_36)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_26.addWidget(self.label_34)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label = QtWidgets.QLabel(self.frame_36)
        self.label.setStyleSheet("font-size:20px;")
        self.label.setObjectName("label")
        self.horizontalLayout_11.addWidget(self.label)
        self.label_36 = QtWidgets.QLabel(self.frame_36)
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_11.addWidget(self.label_36)
        self.verticalLayout_26.addLayout(self.horizontalLayout_11)
        self.frame_37 = QtWidgets.QFrame(self.frame_15)
        self.frame_37.setGeometry(QtCore.QRect(20, 430, 291, 81))
        self.frame_37.setStyleSheet("border-radius:0;\n"
                                    "               color:white;\n"
                                    "               background-color:#1d1f1f;\n"
                                    "               font-size:14px;\n"
                                    "               font-weight:500;")
        self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.frame_37)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.label_37 = QtWidgets.QLabel(self.frame_37)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_27.addWidget(self.label_37)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_38 = QtWidgets.QLabel(self.frame_37)
        self.label_38.setStyleSheet("font-size:20px;")
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_12.addWidget(self.label_38)
        self.label_39 = QtWidgets.QLabel(self.frame_37)
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_12.addWidget(self.label_39)
        self.verticalLayout_27.addLayout(self.horizontalLayout_12)
        self.verticalLayout_7.addWidget(self.frame_15)
        self.horizontalLayout.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.part1)
        self.frame_10.setMaximumSize(QtCore.QSize(1016, 16777215))
        self.frame_10.setStyleSheet("background-color:#595959;\n"
                                    "         border-radius:10px")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.frame_12 = QtWidgets.QFrame(self.frame_10)
        self.frame_12.setGeometry(QtCore.QRect(30, 29, 951, 701))
        self.frame_12.setStyleSheet(
            "background-color:#2A2A2A;border: 2px solid orange")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_graph = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_graph.setObjectName('horizontalLayout_graph')
        # canvas

        self.horizontalLayout.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.part1)
        self.frame_11.setMaximumSize(QtCore.QSize(350, 670))
        self.frame_11.setStyleSheet("background-color:#595959;\n"
                                    "         border-radius:10px")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_22 = QtWidgets.QFrame(self.frame_11)
        self.frame_22.setMinimumSize(QtCore.QSize(324, 643))
        self.frame_22.setStyleSheet(
            "background-color:#2A2A2A;border 1px solid orange")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.frame_35 = QtWidgets.QFrame(self.frame_22)
        self.frame_35.setGeometry(QtCore.QRect(11, 59, 302, 573))
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_35)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 170, 281, 47))
        self.pushButton_6.setMinimumSize(QtCore.QSize(241, 47))
        self.pushButton_6.setStyleSheet("\n"
                                        "         QPushButton{\n"
                                        "               border-radius:0;\n"
                                        "               color:white;\n"
                                        "               background-color:#1d1f1f;\n"
                                        "               font-size:14px;\n"
                                        "               font-weight:400;\n"
                                        "\n"
                                        "\n"
                                        "         }\n"
                                        "         QPushButton:hover{\n"
                                        "               background-color:#595959;\n"
                                        "               change-cursor: cursor(\'PointingHand\');\n"
                                        "               transition:2s;\n"
                                        "\n"
                                        "         }\n"
                                        "         QPushButton:pressed{\n"
                                        "               background-color:#595959;\n"
                                        "         }\n"
                                        "         \n"
                                        "         ")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_35)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 240, 281, 47))
        self.pushButton_5.setMinimumSize(QtCore.QSize(241, 47))
        self.pushButton_5.setStyleSheet("\n"
                                        "         QPushButton{\n"
                                        "               border-radius:0;\n"
                                        "               color:white;\n"
                                        "               background-color:#1d1f1f;\n"
                                        "               font-size:14px;\n"
                                        "               font-weight:400;\n"
                                        "\n"
                                        "         }\n"
                                        "         QPushButton:hover{\n"
                                        "               background-color:#595959;\n"
                                        "               change-cursor: cursor(\'PointingHand\');\n"
                                        "               transition:2s;\n"
                                        "         }\n"
                                        "         QPushButton:pressed{\n"
                                        "               background-color:#595959;\n"
                                        "         }\n"
                                        "         \n"
                                        "         ")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_35)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 310, 281, 47))
        self.pushButton_4.setMinimumSize(QtCore.QSize(241, 47))
        self.pushButton_4.setStyleSheet("\n"
                                        "         QPushButton{\n"
                                        "               border-radius:0;\n"
                                        "               color:white;\n"
                                        "               background-color:#1d1f1f;\n"
                                        "               font-size:14px;\n"
                                        "               font-weight:400;\n"
                                        "\n"
                                        "         }\n"
                                        "         QPushButton:hover{\n"
                                        "               background-color:#595959;\n"
                                        "               change-cursor: cursor(\'PointingHand\');\n"
                                        "               transition:2s;\n"
                                        "         }\n"
                                        "         QPushButton:pressed{\n"
                                        "               background-color:#595959;\n"
                                        "         }\n"
                                        "         \n"
                                        "         ")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_35)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 380, 281, 47))
        self.pushButton_3.setMinimumSize(QtCore.QSize(241, 47))
        self.pushButton_3.setStyleSheet("\n"
                                        "         QPushButton{\n"
                                        "               border-radius:0;\n"
                                        "               color:white;\n"
                                        "               background-color:#1d1f1f;\n"
                                        "               font-size:14px;\n"
                                        "               font-weight:400;\n"
                                        "\n"
                                        "         }\n"
                                        "         QPushButton:hover{\n"
                                        "               background-color:#595959;\n"
                                        "               change-cursor: cursor(\'PointingHand\');\n"
                                        "               transition:2s;\n"
                                        "         }\n"
                                        "         QPushButton:pressed{\n"
                                        "               background-color:#595959;\n"
                                        "         }\n"
                                        "         \n"
                                        "         ")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_35)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 450, 281, 47))
        self.pushButton_2.setMinimumSize(QtCore.QSize(241, 47))
        self.pushButton_2.setStyleSheet("\n"
                                        "         QPushButton{\n"
                                        "               border-radius:0;\n"
                                        "               color:white;\n"
                                        "               background-color:#1d1f1f;\n"
                                        "               font-size:14px;\n"
                                        "               font-weight:400;\n"
                                        "\n"
                                        "         }\n"
                                        "         QPushButton:hover{\n"
                                        "               background-color:#595959;\n"
                                        "               change-cursor: cursor(\'PointingHand\');\n"
                                        "               transition:2s;\n"
                                        "         }\n"
                                        "         QPushButton:pressed{\n"
                                        "               background-color:#595959;\n"
                                        "         }\n"
                                        "         \n"
                                        "         ")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.send_string('l'))
        self.pushButton = QtWidgets.QPushButton(self.frame_35)
        self.pushButton.setGeometry(QtCore.QRect(10, 100, 281, 47))
        self.pushButton.setMinimumSize(QtCore.QSize(241, 47))
        self.pushButton.setStyleSheet("\n"
                                      "         QPushButton{\n"
                                      "               border-radius:0;\n"
                                      "               color:white;\n"
                                      "               background-color:#1d1f1f;\n"
                                      "               font-size:14px;\n"
                                      "               font-weight:400;\n"
                                      "\n"
                                      "         }\n"
                                      "         QPushButton:hover{\n"
                                      "               background-color:#595959;\n"
                                      "               change-cursor: cursor(\'PointingHand\');\n"
                                      "               transition:2s;\n"
                                      "         }\n"
                                      "         QPushButton:pressed{\n"
                                      "               background-color:#595959;\n"
                                      "         }\n"
                                      "         \n"
                                      "         ")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_35)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 520, 281, 47))
        self.pushButton_7.setMinimumSize(QtCore.QSize(241, 47))
        self.pushButton_7.setStyleSheet("\n"
                                        "         QPushButton{\n"
                                        "               border-radius:0;\n"
                                        "               color:white;\n"
                                        "               background-color:#1d1f1f;\n"
                                        "               font-size:14px;\n"
                                        "               font-weight:400;\n"
                                        "\n"
                                        "         }\n"
                                        "         QPushButton:hover{\n"
                                        "               background-color:#595959;\n"
                                        "               change-cursor: cursor(\'PointingHand\');\n"
                                        "               transition:2s;\n"
                                        "         }\n"
                                        "         QPushButton:pressed{\n"
                                        "               background-color:#595959;\n"
                                        "         }\n"
                                        "         \n"
                                        "         ")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(lambda: self.send_string('u'))
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_35)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 30, 281, 47))
        self.pushButton_9.setMinimumSize(QtCore.QSize(241, 47))
        self.pushButton_9.setStyleSheet("\n"
                                        "         QPushButton{\n"
                                        "               border-radius:0;\n"
                                        "               color:white;\n"
                                        "               background-color:#1d1f1f;\n"
                                        "               font-size:14px;\n"
                                        "               font-weight:400;\n"
                                       
                                        "\n"
                                        "         }\n"
                                        "         QPushButton:hover{\n"
                                        "               background-color:#595959;\n"
                                        "               change-cursor: cursor(\'PointingHand\');\n"
                                        "               transition:2s;\n"
                                        "\n"
                                        "         }\n"
                                        "         QPushButton:pressed{\n"
                                        "               background-color:#595959;\n"
                                        "         }\n"
                                        "         \n"
                                        "         ")    
        
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(lambda: self.send_string('r'))
        self.label_2 = QtWidgets.QLabel(self.frame_22)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 281, 41))
        self.label_2.setStyleSheet("color:white;\n"
                                   "         background:#595959;\n"
                                   "         font-size:15px;\n"
                                   "         font-weight:600;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_10.addWidget(
            self.frame_22, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.frame_11)
        self.verticalLayout_4.addWidget(self.part1)
        self.part2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.part2.setMinimumSize(QtCore.QSize(0, 780))
        self.part2.setStyleSheet("background-color:#2A2A2A")
        self.part2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.part2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.part2.setObjectName("part2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.part2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.part2)
        self.frame_5.setStyleSheet("background-color:#2A2A2A")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_13 = QtWidgets.QFrame(self.frame_5)
        self.frame_13.setMinimumSize(QtCore.QSize(792, 678))
        self.frame_13.setStyleSheet("background-color:rgb(89, 89, 89)")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.frame_56 = QtWidgets.QFrame(self.frame_13)
        self.frame_56.setGeometry(QtCore.QRect(30, 30, 731, 611))
        self.frame_56.setStyleSheet("background-color:#1d1f1f;")
        self.frame_56.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_56.setObjectName("frame_56")
        self.pushButton_21 = QtWidgets.QPushButton(self.frame_56)
        self.pushButton_21.setGeometry(QtCore.QRect(90, 430, 551, 47))
        self.pushButton_21.setMinimumSize(QtCore.QSize(241, 47))
        self.pushButton_21.setStyleSheet("\n"
                                         "         QPushButton{\n"
                                         "               border-radius:0;\n"
                                         "               color:white;\n"
                                         "               background-color:#1d1f1f;\n"
                                         "               font-size:14px;\n"
                                         "               font-weight:500;\n"
                                         "border: 2px solid orange;\n"
                                         "         }\n"
                                         "         QPushButton:hover{\n"
                                         "               background-color:#595959;\n"
                                         "               change-cursor: cursor(\'PointingHand\');\n"
                                         "               transition:2s;\n"
                                         "         }\n"
                                         "         QPushButton:pressed{\n"
                                         "               background-color:#595959;\n"
                                         "         }\n"
                                         "         \n"
                                         "         ")
        self.pushButton_21.setObjectName("pushButton_21")

        self.pushButton_csv = QtWidgets.QPushButton(self.frame_56)
        self.pushButton_csv.setGeometry(QtCore.QRect(90, 550, 551, 47))
        self.pushButton_csv.setMinimumSize(QtCore.QSize(241, 47))
        self.pushButton_csv.setStyleSheet("\n"
                                         "         QPushButton{\n"
                                         "               border-radius:0;\n"
                                         "               color:white;\n"
                                         "               background-color:#1d1f1f;\n"
                                         "               font-size:14px;\n"
                                         "               font-weight:500;\n"
                                         "border: 2px solid orange;\n"
                                         "         }\n"
                                         "         QPushButton:hover{\n"
                                         "               background-color:#595959;\n"
                                         "               change-cursor: cursor(\'PointingHand\');\n"
                                         "               transition:2s;\n"
                                         "         }\n"
                                         "         QPushButton:pressed{\n"
                                         "               background-color:#595959;\n"
                                         "         }\n"
                                         "         \n"
                                         "         ")
        self.pushButton_csv.setObjectName("pushButton_csv")

        self.pushButton_pfr = QtWidgets.QPushButton(self.frame_56)
        self.pushButton_pfr.setGeometry(QtCore.QRect(90, 490, 551, 47))
        self.pushButton_pfr.setMinimumSize(QtCore.QSize(241, 47))
        self.pushButton_pfr.setStyleSheet("\n"
                                         "         QPushButton{\n"
                                         "               border-radius:0;\n"
                                         "               color:white;\n"
                                         "               background-color:#1d1f1f;\n"
                                         "               font-size:14px;\n"
                                         "               font-weight:500;\n"
                                         "border: 2px solid orange;\n"
                                         "         }\n"
                                         "         QPushButton:hover{\n"
                                         "               background-color:#595959;\n"
                                         "               change-cursor: cursor(\'PointingHand\');\n"
                                         "               transition:2s;\n"
                                         "         }\n"
                                         "         QPushButton:pressed{\n"
                                         "               background-color:#595959;\n"
                                         "         }\n"
                                         "         \n"
                                         "         ")
        self.pushButton_pfr.setObjectName("pushButton_pfr")
        
        self.pushButton_21.clicked.connect(self.live_location)
        self.pushButton_csv.clicked.connect(self.gen_csv)
        self.pushButton_pfr.clicked.connect(self.gen_pfr)
        self.frame_14 = QtWidgets.QFrame(self.frame_56)
        self.frame_14.setGeometry(QtCore.QRect(110, 50, 511, 371))
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
       
        self.verticalLayout_6.addWidget(
            self.frame_13, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.part2)
        self.frame_6.setStyleSheet("background-color:#2A2A2A")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setMinimumSize(QtCore.QSize(5, 0))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 326))
        self.frame_7.setStyleSheet("background-color:rgb(89, 89, 89)\n"
                                   "         ")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.frame_33 = QtWidgets.QFrame(self.frame_7)
        self.frame_33.setMinimumSize(QtCore.QSize(100, 100))
        self.frame_33.setMaximumSize(QtCore.QSize(805, 16777215))
        self.frame_33.setStyleSheet("border-radius:0;\n"
                                    "               color:white;\n"
                                    "               background-color:#1d1f1f;\n"
                                    "               font-size:14px;\n"
                                    "               font-weight:500;")
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_33)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_25 = QtWidgets.QLabel(self.frame_33)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_20.addWidget(self.label_25)
        self.label_27 = QtWidgets.QLabel(self.frame_33)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_20.addWidget(self.label_27)
        self.label_28 = QtWidgets.QLabel(self.frame_33)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_20.addWidget(self.label_28)
        self.label_30 = QtWidgets.QLabel(self.frame_33)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_20.addWidget(self.label_30)
        self.label_29 = QtWidgets.QLabel(self.frame_33)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_20.addWidget(self.label_29)
        self.label_26 = QtWidgets.QLabel(self.frame_33)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_20.addWidget(self.label_26)
        self.horizontalLayout_13.addWidget(self.frame_33)
        self.verticalLayout_5.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 315))
        self.frame_8.setStyleSheet("background-color:rgb(89, 89, 89)")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.frame_55 = QtWidgets.QFrame(self.frame_8)
        self.frame_55.setMinimumSize(QtCore.QSize(100, 100))
        self.frame_55.setMaximumSize(QtCore.QSize(805, 16777215))
        self.frame_55.setStyleSheet("border-radius:0;\n"
                                    "               color:white;\n"
                                    "               background-color:#1d1f1f;\n"
                                    "               font-size:14px;\n"
                                    "               font-weight:500;")
        self.frame_55.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_55.setObjectName("frame_55")
        self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.frame_55)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.label_51 = QtWidgets.QLabel(self.frame_55)
        self.label_51.setObjectName("label_51")
        self.verticalLayout_37.addWidget(self.label_51)
        self.label_52 = QtWidgets.QLabel(self.frame_55)
        self.label_52.setObjectName("label_52")
        self.verticalLayout_37.addWidget(self.label_52)
        self.label_53 = QtWidgets.QLabel(self.frame_55)
        self.label_53.setObjectName("label_53")
        self.verticalLayout_37.addWidget(self.label_53)
        self.label_54 = QtWidgets.QLabel(self.frame_55)
        self.label_54.setObjectName("label_54")
        self.verticalLayout_37.addWidget(self.label_54)
        self.label_55 = QtWidgets.QLabel(self.frame_55)
        self.label_55.setObjectName("label_55")
        self.verticalLayout_37.addWidget(self.label_55)
        self.label_56 = QtWidgets.QLabel(self.frame_55)
        self.label_56.setObjectName("label_56")
        self.verticalLayout_37.addWidget(self.label_56)
        self.horizontalLayout_20.addWidget(self.frame_55)
        self.verticalLayout_5.addWidget(self.frame_8)
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.verticalLayout_4.addWidget(self.part2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_3.raise_()
        self.frame_2.raise_()
        self.frame_4.raise_()
        self.verticalLayout.addWidget(self.frame)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.stop_thread = threading.Event()
        thread = threading.Thread(target=self.read_serial_data)
        thread.start()

    def gen_csv(self):
        filename=r"C:\Users\DELL\OneDrive\Desktop\cansat\pfrcsv.csv"
        with open(filename, 'a', newline='') as csvfile:
            subprocess.Popen([filename], shell=True)
        
    def gen_pfr(self):
        filename=r"C:\Users\DELL\OneDrive\Desktop\cansat\pfrcsv.csv"
        
        self.figure_graph = plt.figure()
        self.canvas_graph = FigureCanvas(self.figure_graph)
                # self.canvas.setStyleSheet("background-color:transparent")
                # canvas end
                # adding canvas
        self.horizontalLayout_graph.addWidget(self.canvas_graph)

        # Create a figure with two subplots
        self.ax1 = self.figure_graph.add_subplot(3, 2, 1)
        self.ax2 = self.figure_graph.add_subplot(3, 2, 2)
        self.ax3 = self.figure_graph.add_subplot(3, 2, 3)
        self.ax4 = self.figure_graph.add_subplot(3, 2, 4)
        self.ax5 = self.figure_graph.add_subplot(3, 2, 5)
        self.ax6 = self.figure_graph.add_subplot(3, 2, 6)

        alt = []
        press = []
        volt = []
        gr = []
        gp = []
        gy = []
        ar = []
        ap =[]
        ay = []
        vel =[]
        packet_counts = []
        c=0
        plt.subplots_adjust(top=0.93, bottom=0.07, hspace=0.45, wspace=0.3)
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if(c==0):
                    c=1
                    continue
                # Append altitude and packet count values to the respective lists
                if len(packet_counts)==0:
                    alt.append(float(row['ALTITUDE']))
                    press.append(float(row['PRESSURE']))
                    volt.append(float(row['VOLTAGE']))
                    gr.append(float(row['GYRO_R']))
                    gp.append(float(row['GYRO_P']))
                    gy.append(float(row['GYRO_Y']))
                    ar.append(float(row['ACC_R']))
                    ap.append(float(row['ACC_P']))
                    ay.append(float(row['ACC_Y']))
                    packet_counts.append(1)
                    print(row)
                else:
                    alt.append(float(row['ALTITUDE']))
                    press.append(float(row['PRESSURE']))
                    volt.append(float(row['VOLTAGE']))
                    gr.append(float(row['GYRO_R']))
                    gp.append(float(row['GYRO_P']))
                    gy.append(float(row['GYRO_Y']))
                    ar.append(float(row['ACC_R']))
                    ap.append(float(row['ACC_P']))
                    ay.append(float(row['ACC_Y']))
                    packet_counts.append(int(packet_counts[-1])+1)
                    print(row)
            for i in range(len(alt)):
                if i == 0:
                    vel.append(alt[i] - 0)  # For the first value, subtract from 0
                else:
                    vel.append(alt[i] - alt[i - 1])

        self.ax1.plot(packet_counts, alt, color='#FF5733')
        self.ax2.plot(packet_counts, press, color='#FF5733')
        self.ax3.plot(packet_counts, volt, color='#FF5733')
        # self.ax3.yaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))

        self.ax4.plot(packet_counts, gr, color='#FF5733', label='Roll', linestyle='-')  # Solid line
        self.ax4.plot(packet_counts, gp, color='#00FF00', label='Pitch', linestyle='--') # Dotted line
        self.ax4.plot(packet_counts, gy, color='#03c2fc', label='Yaw', linestyle='-.') # Dash-dot line
        self.ax4.legend(loc='upper left', frameon=False, bbox_to_anchor=(0.0, 1.0), facecolor='white', edgecolor='black', framealpha=1.0)

        self.ax5.plot(packet_counts, ar, color='#FF5733',label='Roll')
                # self.ax4.stackplot(rollSeq,color='orange',alpha=0.1)
        self.ax5.plot(packet_counts, ap, color='#00FF00',label='Pitch')
                # self.ax5.stackplot(rollSeq,color='orange',alpha=0.1)
        self.ax5.plot(packet_counts, ay, color='#03c2fc',label='Yaw')
                # self.ax6.stackplot(rollSeq,color='orange',alpha=0.1)
        self.ax5.legend(loc='upper left', frameon=False, bbox_to_anchor=(0.0, 1.0), facecolor='white', edgecolor='black', framealpha=1.0)
        self.ax6.plot(packet_counts, vel, color='#FF5733')

        self.ax1.set_title("Altitude(m) vs Time(s)",
                        fontsize=14)
        self.ax2.set_title("Pressure(Pa) vs Time(s)",
                        fontsize=14)
        self.ax3.set_title("Voltage(V) vs Time(s)",
                        fontsize=14)
        self.ax4.set_title("Gyro(°/s) vs Time(s)",
                        fontsize=14)
        self.ax5.set_title("Accel(m/s²) vs Time(s)",
                        fontsize=14)
        self.ax6.set_title("Velocity(m/s) vs Time(s)",
                        fontsize=14)


        
    def read_serial_data(self):
        packet = self.ser.read(1)
        csvreader=packet.decode('utf-8')
        if(csvreader=='y'):
            self.pushButton_16.setStyleSheet("\n"
                                         "QPushButton{\n"
                                         "    border: 6px solid blue;\n"
                                         "    border-radius:12px;\n"
                                         "\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "    border: 6px solid #ff9933;\n"
                                         "    change-cursor: cursor(\'PointingHand\');\n"
                                         "    transition:2s;\n"
                                         "}\n"
                                         "QPushButton:after{\n"
                                         "    border: 6px solid #ff9933;;\n"
                                         "}\n"
                                         "")
    
        self.destroyed.connect(self.stop_thread.set)
            

    def load(self):
        pass

    # def update_label_values(self):
    #     self.current_time += 1
    #     minutes = self.current_time // 60000
    #     seconds = (self.current_time // 1000) % 60
    #     milliseconds = (self.current_time // 10) % 100
    #     time_str = f"{minutes:02d}:{seconds:02d}:{milliseconds:02d}"
    #     self.label_mtime_val.setText(
    #         f"<html><head/><body ><p align=\"center\"><span style=\" color:white;\">{time_str}</span></p></body></html>")
        
    
    def send_string(self,command):
        time.sleep(1)
        # print(command)
        global counterx
        if command == 'r':
            self.ser.write(command.encode())
            self.ser.flushInput()
            global command_act
            command_act=command
            self.pushButton_16.setStyleSheet("\n"
                                        "QPushButton{\n"
                                        "    border: 6px solid #34eb61;\n"
                                        "    border-radius:12px;\n"
                                        "\n"
                                        "}\n"
                                        "")
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
            self.label_15.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#b6b6b6;\">Callibrated</span></p></body></html>"))
            
        else:
            print(command)
            self.ser.write(command.encode())
            self.ser.flushInput()
        if command=='c':
            packet = self.ser.read(1)
            csvreader=packet.decode('utf-8')
            if csvreader=='z':
                self.pushButton_16.setStyleSheet("\n"
                                            "QPushButton{\n"
                                            "    border: 6px solid #34eb61;\n"
                                            "    border-radius:12px;\n"
                                            "\n"
                                            "}\n"
                                            "")
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label_15.setText(_translate(
                "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#b6b6b6;\">Callibrated</span></p></body></html>"))

        if command=='x':
            counterx+=1
            if counterx%2!=0:
                self.pushButton_14.setStyleSheet("\n"
                                            "QPushButton{\n"
                                            "    border: 6px solid #34eb61;\n"
                                            "    border-radius:12px;\n"
                                            "\n"
                                            "}\n"
                                            "")
                
            
            else:
                self.ser.reset_input_buffer()
                self.ser.reset_output_buffer()
                
                self.figure_graph.clf()
                self.canvas_graph.close()
                self.pushButton_14.setStyleSheet("\n"
                                            "QPushButton{\n"
                                            "    border: 6px solid red;\n"
                                            "    border-radius:12px;\n"
                                            "\n"
                                            "}\n"
                                            "")  

        if command=='e':
            self.pushButton_11.setStyleSheet("\n"
                                         "QPushButton{\n"
                                         "    border: 6px solid #34eb61;\n"
                                         "    border-radius:12px;\n"
                                         "\n"
                                         "}\n"
                                         )
            
       
            
        

    def send_string_dis(self,command):
        global command_act
        command_act=command
        self.pushButton.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
        self.pushButton_11.setStyleSheet("\n"
                                         "QPushButton{\n"
                                         "    border: 6px solid red;\n"
                                         "    border-radius:12px;\n"
                                         "\n"
                                         "}\n"
                                         )
        self.pushButton_15.setStyleSheet("\n"
                                         "QPushButton{\n"
                                         "    border: 6px solid red;\n"
                                         "    border-radius:12px;\n"
                                         "\n"
                                         "}\n"
                                         )

        
        # plt.close(self.figure_graph)
            
    def animate(self, i):
        _translate = QtCore.QCoreApplication.translate
        # start_time = time.time()
        global memory
        global vel,prevalt
        global command_act,row
        import time
        # if(command_act=='r'):
        #     time.sleep(1)
        #     self.ser.write(command_act.encode())
        #     time.sleep(1)
        #     command_act=0
        if(command_act=='d'):
            time.sleep(1)
            self.ser.write(command_act.encode())
            time.sleep(1)
            self.figure_graph.clf()
            self.canvas_graph.close()
            # command_act=0

        if command_act=='a':
            # time.sleep(1)
            self.pushButton_15.setStyleSheet("\n"
                                         "QPushButton{\n"
                                         "    border: 6px solid #34eb61;\n"
                                         "    border-radius:12px;\n"
                                         "\n"
                                         "}\n"
                                         )
            with open("./bookfinal.csv", 'r') as file:
                csvreader_act = csv.reader(file)
                row_counter = 0
                for row in csvreader_act:
                    global pointer_act
                    if row_counter == pointer_act:
                        pressure=row[0]
                        pointer_act += 1
                        break
                    row_counter += 1

                pres=pressure
                # if pressure[0]=='ï':
                #     pres=pressure[3:]

                print(("<"+str(pres)+">"))
                self.ser.write(("<"+str(pres)+">").encode())
                

        global pointer,packet,csvreader
        if self.ser.in_waiting>1:
            packet = self.ser.readline()
            print(packet)
            csvreader = packet.decode('utf-8', errors='ignore').split(",")
            row = csvreader
        else:
            row=memory
       
        
        if len(row)!=21:
            row=memory
        else:
            memory=row

        for i in range(len(row)):
            if row[i]=='':
                row[i]='0'    

        lt_index = row[0].find('<') 

        if lt_index != -1:
            row[0] = row[0][lt_index + 1:].strip()
        else:
            row[0] = row[0].strip()    

        gt_index = row[-1].find('>') 

        if gt_index != -1:
            row[-1] = row[-1][:gt_index].strip()
        else:
            row[-1] = row[-1].strip()
        csv_file = 'Flight_2022ASI-049.csv'
        if(command_act!='a'):
            if os.path.exists(csv_file):
                with open(csv_file, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(row) 
                file.close()
            else:
                header_string=["TEAM_ID","TIME_STAMPING","PACKET_COUNT","ALTITUDE","PRESSURE","TEMP","VOLTAGE","GNSS_TIME","GNSS_LATITUDE","GNSS_LONGITUDE","GNSS_ALTITUDE","GNSS_SATS","ACC_R","ACC_P","ACC_Y","GYRO_R","GYRO_P","GYRO_Y","FLIGHT_SOFTWARE_STATE"]
                with open(csv_file, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(header_string) 
                file.close()
        

        print(row)
        time_stamp = row[1]

        packet = row[2]
        press = row[4]
        volt = row[6]
        temp = row[5]
        ar = row[12]
        ap = row[13]
        ay = row[14]
        gr = row[15]
        gp = row[16]
        gy = row[17]
        alt=row[3]
        tvoc=int(row[19])
        # co2=int(row[20])

        vel=float(alt)-float(prevalt)
        prevalt=alt
        gnssalt = row[10]
        long = row[9]
        lat = row[8]
        sats = row[11]
        time = row[7]
        softstate = int(row[18])

        
        
        if(tvoc<=50):
            self.frame_mtime.setStyleSheet(
            "background-color:#1d1f1f;border: 2px solid green")
        elif(tvoc<=100):
            self.frame_mtime.setStyleSheet(
            "background-color:#1d1f1f;border: 2px solid yellow")
        elif(tvoc<=150):
            self.frame_mtime.setStyleSheet(
            "background-color:#1d1f1f;border: 2px solid orange")
        else:
            self.frame_mtime.setStyleSheet(
            "background-color:#1d1f1f;border: 2px solid red")
        
        self.label_mtime_val.setText(
            f"<html><head/><body ><p align=\"center\"><span style=\" color:white;\">{tvoc}</span></p></body></html>")

        self.label_8.setText(
            f"<html><head/><body><p align=\"right\">{gnssalt}</p></body></html>")
        self.label_23.setText(f"            {long}°")
        self.label_17.setText(f"            {lat}°")
        self.label_38.setText(f"                {sats}")
        self.label.setText(f"            {time}")
        self.label_25.setText(
            f"                   TIME STAMPING            :                       {time_stamp}                         ")
        self.label_27.setText(
            f"                    PACKET COUNT           :                       {packet}                    ")
        self.label_28.setText(
            f"                    ALTITUDE                   :                       {alt} meters              ")
        self.label_30.setText(
            f"                    PRESSURE                  :                       {press} Pa                    ")
        self.label_29.setText(
            f"                    VOLTAGE                    :                       {volt} V                  ")
        self.label_26.setText(
            f"                    TEMPERATURE            :                       {temp} ℃                          ")
        self.label_51.setText(
            f"                    ACCEL_R                    :                       {ar} m/s²                      ")
        self.label_52.setText(
            f"                    ACCEL_P                    :                       {ap} m/s²                       ")
        self.label_53.setText(
            f"                    ACCEL_Y                    :                       {ay} m/s²                ")
        self.label_54.setText(
            f"                    GYRO_R                     :                       {gr} rad/s                       ")
        self.label_55.setText(
            f"                    GYRO_P                     :                       {gp} rad/s                    ")
        self.label_56.setText(
            f"                    GYRO_Y                     :                       {gy} rad/s                            ")
                
        if softstate==1:
            self.pushButton.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "border: 3px solid orange;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            
            self.pushButton_9.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_7.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_6.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_5.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_4.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_3.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_2.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")

            
        elif softstate==2:

            self.pushButton_6.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "border: 3px solid orange;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_9.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_7.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_5.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_4.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_3.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_2.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")

        elif softstate==3:
            self.pushButton_5.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "border: 3px solid orange;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            
            self.pushButton_9.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_7.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_6.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_4.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_3.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_2.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")

        elif softstate==4:

            self.pushButton_4.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "border: 3px solid orange;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            
            self.pushButton_9.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_7.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_6.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_5.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_3.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_2.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")

        elif softstate==5:

            self.pushButton_3.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "border: 3px solid orange;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_9.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_7.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_6.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_5.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_4.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_2.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")

        elif softstate==6:

            self.pushButton_2.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "border: 3px solid orange;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            
            self.pushButton_9.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_7.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_6.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_5.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_4.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_3.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
        elif softstate==7:

            self.pushButton_7.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "border: 3px solid orange;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_9.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_6.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_5.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_4.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_3.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_2.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
        elif softstate==0:

            self.pushButton_9.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "border: 3px solid orange;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            
            self.pushButton.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_7.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_6.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_5.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_4.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_3.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")
            self.pushButton_2.setStyleSheet("\n"
                                                    "         QPushButton{\n"
                                                    "               border-radius:0;\n"
                                                    "               color:white;\n"
                                                    "               background-color:#1d1f1f;\n"
                                                    "               font-size:14px;\n"
                                                    "               font-weight:400;\n"
                                                    "\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:hover{\n"
                                                    "               background-color:#595959;\n"
                                                    "               change-cursor: cursor(\'PointingHand\');\n"
                                                    "               transition:2s;\n"
                                                    "\n"
                                                    "         }\n"
                                                    "         QPushButton:pressed{\n"
                                                    "               background-color:#595959;\n"
                                                    "         }\n"
                                                    "         \n"
                                                    "         ")

                      
        loop = QtCore.QEventLoop()
        QTimer.singleShot(600, loop.quit)
        loop.exec_()
        currentRoll1 = alt
        currentRoll2 = press
        currentRoll3 = volt
        currentRoll4 = gr
        currentRoll5 = gp
        currentRoll6 = gy
        currentRoll7 = ar
        currentRoll8 = ap
        currentRoll9 = ay
        currentRoll10 = vel
        pointer += 1  
        currentRoll1 = float(currentRoll1)
        rollTotals1.append(next(index1))
        rollSeq1.append(currentRoll1)
        currentRoll2 = float(currentRoll2)
        rollTotals2.append(next(index2))
        rollSeq2.append(float(currentRoll2))
        currentRoll3 = float(currentRoll3)
        rollTotals3.append(next(index3))
        rollSeq3.append(round(currentRoll3,4))
        currentRoll4 = float(currentRoll4)
        rollTotals4.append(next(index4))
        rollSeq4.append(currentRoll4)
        currentRoll5 = float(currentRoll5)
        rollTotals5.append(next(index5))
        rollSeq5.append(currentRoll5)
        currentRoll6 = float(currentRoll6)
        rollTotals6.append(next(index6))
        rollSeq6.append(currentRoll6)
        currentRoll7 = float(currentRoll7)
        rollTotals7.append(next(index7))
        rollSeq7.append(currentRoll7)
        currentRoll8 = float(currentRoll8)
        rollTotals8.append(next(index8))
        rollSeq8.append(currentRoll8)
        currentRoll9 = float(currentRoll9)
        rollTotals9.append(next(index9))
        rollSeq9.append(currentRoll9)
        currentRoll10 = float(currentRoll10)
        rollTotals10.append(next(index10))
        rollSeq10.append(currentRoll10)
            # Set subplot data
                # plt.plot(x3,y3,color='#FF5733',)
                #         plt.stackplot(x3,y3,colors='orange',alpha=0.1)

        self.ax2.clear()
        self.ax2.plot(rollTotals2, rollSeq2, color='#FF5733')
                # self.ax2.fill_between(rollSeq,0,color='orange',alpha=0.1)
        xlim = len(rollSeq2)
        self.ax2.set_xlim(xlim - 30, xlim)
        self.ax1.clear()
        self.ax1.plot(rollTotals1, rollSeq1, color='#FF5733')
                # self.ax1.stackplot(rollSeq,color='orange',alpha=0.1)
        xlim = len(rollSeq1)
        self.ax1.set_xlim(xlim - 30, xlim)
        
        self.ax3.clear()

        self.ax3.plot(rollTotals3, rollSeq3, color='#FF5733')
                # self.ax3.stackplot(rollSeq,color='orange',alpha=0.1)
        # self.ax3.yaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))
        xlim = len(rollSeq3)
        self.ax3.set_xlim(xlim - 30, xlim)
        # self.ax3.set_ylim(0, 10)
        self.ax4.clear()
        self.ax4.plot(rollTotals4, rollSeq4, color='#FF5733', label='Roll', linestyle='-')  # Solid line
        self.ax4.plot(rollTotals5, rollSeq5, color='#00FF00', label='Pitch', linestyle='--') # Dotted line
        self.ax4.plot(rollTotals6, rollSeq6, color='#03c2fc', label='Yaw', linestyle='-.') # Dash-dot line
        self.ax4.legend(loc='upper left', frameon=False, bbox_to_anchor=(0.0, 1.0), facecolor='white', edgecolor='black', framealpha=1.0)
                # self.ax6.stackplot(rollSeq,color='orange',alpha=0.1)
        xlim = max(len(rollSeq6),len(rollSeq5),len(rollSeq4))
        self.ax4.set_xlim(xlim - 30, xlim)
        self.ax5.clear()
        self.ax5.plot(rollTotals7, rollSeq7, color='#FF5733',label='Roll')
                # self.ax4.stackplot(rollSeq,color='orange',alpha=0.1)
        self.ax5.plot(rollTotals8, rollSeq8, color='#00FF00',label='Pitch')
                # self.ax5.stackplot(rollSeq,color='orange',alpha=0.1)
        self.ax5.plot(rollTotals9, rollSeq9, color='#03c2fc',label='Yaw')
                # self.ax6.stackplot(rollSeq,color='orange',alpha=0.1)
        self.ax5.legend(loc='upper left', frameon=False, bbox_to_anchor=(0.0, 1.0), facecolor='white', edgecolor='black', framealpha=1.0)
        xlim = max(len(rollSeq7),len(rollSeq8),len(rollSeq9))
        self.ax5.set_xlim(xlim - 30, xlim)

        self.ax6.clear()
        self.ax6.plot(rollTotals10, rollSeq10, color='#FF5733')
               
        xlim = len(rollSeq10)
        self.ax6.set_xlim(xlim - 30, xlim)
        # self.ax6.set_ylim(0, 30)
            # Set subplot titles
        self.ax1.set_title("Altitude(m) vs Time(s)",
                        fontsize=14)
        self.ax2.set_title("Pressure(Pa) vs Time(s)",
                        fontsize=14)
        self.ax3.set_title("Voltage(V) vs Time(s)",
                        fontsize=14)
        self.ax4.set_title("Gyro(°/s) vs Time(s)",
                        fontsize=14)
        self.ax5.set_title("Accel(m/s²) vs Time(s)",
                        fontsize=14)
        self.ax6.set_title("Velocity(m/s) vs Time(s)",
                        fontsize=14)
        
        # end_time = time.time()
        # print(f"execution time: {end_time - start_time} seconds")

    def graph(self,command):
        global pointer
        global rollSeq1, rollTotals1, index1
        global rollSeq2, rollTotals2, index2
        global rollSeq3, rollTotals3, index3
        global rollSeq4, rollTotals4, index4
        global rollSeq5, rollTotals5, index5
        global rollSeq6, rollTotals6, index6
        global rollSeq7, rollTotals7, index7
        global rollSeq8, rollTotals8, index8
        global rollSeq9, rollTotals9, index9
        global rollSeq10, rollTotals10, index10
        global command_act
        # command_act=0
       
        
        
        command_act = command
        pointer = 1
        numRolls=40000

        if command=='a':
            intv=0.00001
        if command=='r':
            intv=0.00001

        index1 = count() 
        index2 = count()
        index3 = count()
        index4 = count()
        index5 = count()
        index6 = count()
        index7 = count()
        index8 = count()
        index9 = count()
        index10 = count()
        rollTotals1 = []
        rollTotals2 = []
        rollTotals3 = []
        rollTotals4 = []
        rollTotals5 = []
        rollTotals6 = []
        rollTotals7 = []
        rollTotals8 = []
        rollTotals9 = []
        rollTotals10 = []
        rollSeq1 = []
        rollSeq2 = []
        rollSeq3 = []
        rollSeq4 = []
        rollSeq5 = []
        rollSeq6 = []
        rollSeq7 = []
        rollSeq8 = []
        rollSeq9 = []
        rollSeq10 = []

        self.figure_graph = plt.figure()
        self.canvas_graph = FigureCanvas(self.figure_graph)
                # self.canvas.setStyleSheet("background-color:transparent")
                # canvas end
                # adding canvas
        self.horizontalLayout_graph.addWidget(self.canvas_graph)

        # Create a figure with two subplots
        self.ax1 = self.figure_graph.add_subplot(3, 2, 1)
        self.ax2 = self.figure_graph.add_subplot(3, 2, 2)
        self.ax3 = self.figure_graph.add_subplot(3, 2, 3)
        self.ax4 = self.figure_graph.add_subplot(3, 2, 4)
        self.ax5 = self.figure_graph.add_subplot(3, 2, 5)
        self.ax6 = self.figure_graph.add_subplot(3, 2, 6)

                #  Adjust spacing between plots
        plt.subplots_adjust(top=0.93, bottom=0.07, hspace=0.45, wspace=0.3)
        global pointer_act
        pointer_act=0
        # global alti_array,c
        # alti_array = [0]
        # c = 0
                # ports = serial.tools.list_ports.comports()
                # global serialInst
                # serialInst = serial.Serial()

                # portList = []

                # for onePort in ports:
                #     portList.append(str(onePort))
                #     print(str(onePort))

                # serialInst.baudrate = 9600
                # serialInst.port = "COM3"
                # serialInst.open()
        # global start_time
        # start_time = datetime.now()
        # self.fig=figure_graph
        global ctr
        ctr=0
        if command_act=='a':
            # time.sleep(0.4)
            self.ser.write(command_act.encode())

        
        # cProfile.run(self.animate)

        self.ani = animation.FuncAnimation(
            self.figure_graph, self.animate, frames=numRolls, interval=intv, repeat=False)
        
        
        # print(ctr)
        # # ani.save("animation.mp4")
        # if(ctr==7) :
        #     self.figure_graph.clf()
        
        self.canvas_graph.draw()
        
        # plt.close()
        
    def live_location(self):
        # map detecting live location
        loc=[23.1147,72.5013]
        if os.path.exists(r'C:\Users\DELL\OneDrive\Desktop\cansat\pfrcsv.csv'):
            with open(r'C:\Users\DELL\OneDrive\Desktop\cansat\pfrcsv.csv', 'r') as file:
                reader = csv.reader(file)
                last_row = None
                for row in reader:
                    last_row = row

            if last_row is not None:
                last_row_values = last_row
                loc[0]=last_row[8]
                loc[1]=last_row[9]

        if loc==['0.0000', '0.0000']:
            loc=[23.1147,72.5013]

        self.layout = QtWidgets.QVBoxLayout(self.frame_14)
        print(loc)
        m = folium.Map(
            tiles='OpenStreetMap',
            zoom_start=13,
            location=loc
        )

        folium.Marker(location=loc).add_to(m)
        # save map data to data object
        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())

        self.layout.addWidget(webView)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # print(cProfile.run(self.animate))
        self.label_16.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#b6b6b6;\">Set Time</span></p></body></html>"))
        self.label_15.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#b6b6b6;\">Callibrate</span></p></body></html>"))
        self.label_11.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#b6b6b6;\">SIM Enable</span></p></body></html>"))
        self.label_12.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#b6b6b6;\">SIM Disable</span></p></body></html>"))
        self.label_14.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#b6b6b6;\">SIM Activate</span></p></body></html>"))
        self.label_13.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#b6b6b6;\">On/Off</span></p></body></html>"))
        self.label_19.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#b6b6b6;\">CX</span></p></body></html>"))
        self.label_6.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:white;\">Team Id: 2022ASI-049</span></p></body></html>"))
        self.label_5.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:white;\">Team Kalpana</span></p></body></html>"))
        self.label_61.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:white;\">GNSS</span></p></body></html>"))
        self.label_71.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#505050;\">ALTITUDE</span></p></body></html>"))
        self.label_8.setText(_translate(
            "MainWindow", f"<html><head/><body><p align=\"right\">{initial[10]}</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14px; font-weight:496; font-style:normal;\">\n"
                                        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:400; color:#ffaa00;\">meters</span></p></body></html>"))
        self.label_10.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#505050;\">LATITUDE</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", f"          {initial[8]}°"))
        self.label_18.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:7pt; font-weight:400; color:#ffaa00;\"> north</span></p></body></html>"))
        self.label_22.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#505050;\">LONGITUDE</span></p></body></html>"))
        self.label_mtime_title.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#505050;\">AQI</span></p></body></html>"))
        self.label_mtime_val.setText(_translate(
            "MainWindow", "<html><head/><body ><p align=\"center\"><span style=\" color:white;\">0</span></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", f"          {initial[9]}°"))
        self.label_24.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:7pt; font-weight:400; color:#ffaa00;\">  east</span></p></body></html>"))
        self.label_34.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#505050;\">TIME</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", f"               {initial[7]}"))
        self.label_36.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:7pt; font-weight:400; color:#ffaa00;\">IST</span></p></body></html>"))
        self.label_37.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#505050;\">GNSS SATS</span></p></body></html>"))
        self.label_38.setText(_translate("MainWindow", f"                 {initial[11]}"))
        self.label_39.setText(_translate(
            "MainWindow", "<html><head/><body><p><br/></p><p><br/></p></body></html>"))
        self.pushButton_6.setText(_translate("MainWindow", "LAUNCH_PAD"))
        self.pushButton_5.setText(_translate("MainWindow", "ASCENT"))
        self.pushButton_4.setText(_translate("MainWindow", "ROCKET_DEPLOY"))
        self.pushButton_3.setText(_translate("MainWindow", "DESCENT"))
        self.pushButton_2.setText(_translate(
            "MainWindow", "AEROBRAKE_RELEASE (L)"))
        self.pushButton.setText(_translate("MainWindow", "TEST_MODE"))
        self.pushButton_7.setText(_translate("MainWindow", "IMPACT (U)"))
        self.pushButton_9.setText(_translate("MainWindow", "BOOT (R)"))
        self.label_2.setText(_translate(
            "MainWindow", "                  SOFTWARE STATE"))
        self.pushButton_21.setText(_translate("MainWindow", "DETECT LOCATION"))
        self.pushButton_csv.setText(_translate("MainWindow", "ACCESS LOG CSV"))
        self.pushButton_pfr.setText(_translate("MainWindow", "GENERATE POST FLIGHT ANALYSIS"))
        self.label_25.setText(_translate(
            "MainWindow", f"                    TIME STAMPING                     :                       {initial[1]}                       "))
        self.label_27.setText(_translate(
            "MainWindow", f"                    PACKET COUNT                     :                       {initial[2]}                        "))
        self.label_28.setText(_translate(
            "MainWindow", f"                    ALTITUDE                  :                       {initial[3]} meters                "))
        self.label_30.setText(_translate(
            "MainWindow", f"                    PRESSURE                     :                       {initial[4]} Pa                       "))
        self.label_29.setText(_translate(
            "MainWindow", f"                    VOLTAGE                     :                       {initial[6]} V                     "))
        self.label_26.setText(_translate(
            "MainWindow", f"                    TEMPERATURE                     :                       {initial[5]} ℃                             "))
        self.label_51.setText(_translate(
            "MainWindow", f"                    ACCEL_R                     :                       {initial[12]} m/s²                      "))
        self.label_52.setText(_translate(
            "MainWindow", f"                    ACCEL_P                     :                       {initial[13]} m/s²                       "))
        self.label_53.setText(_translate(
            "MainWindow", f"                    ACCEL_Y                     :                       {initial[14]} m/s²                "))
        self.label_54.setText(_translate(
            "MainWindow", f"                    GYRO_R                     :                       {initial[15]} rad/s                       "))
        self.label_55.setText(_translate(
            "MainWindow", f"                    GYRO_P                     :                       {initial[16]} rad/s                    "))
        self.label_56.setText(_translate(
            "MainWindow", f"                    GYRO_Y                     :                       {initial[17]} rad/s                            "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # ui.indicator(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
