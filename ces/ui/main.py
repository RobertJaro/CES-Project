# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(861, 600)
        self.content = QtWidgets.QWidget(Main)
        self.content.setObjectName("content")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.content)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_plot = PlotWidget(self.content)
        self.main_plot.setObjectName("main_plot")
        self.verticalLayout.addWidget(self.main_plot)
        Main.setCentralWidget(self.content)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 861, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        Main.setMenuBar(self.menubar)
        self.station1_dock = QtWidgets.QDockWidget(Main)
        self.station1_dock.setObjectName("station1_dock")
        self.station1_plot = PlotWidget()
        self.station1_plot.setObjectName("station1_plot")
        self.station1_dock.setWidget(self.station1_plot)
        Main.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.station1_dock)
        self.station2_dock = QtWidgets.QDockWidget(Main)
        self.station2_dock.setObjectName("station2_dock")
        self.station2_plot = PlotWidget()
        self.station2_plot.setObjectName("station2_plot")
        self.station2_dock.setWidget(self.station2_plot)
        Main.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.station2_dock)
        self.statusBar = QtWidgets.QStatusBar(Main)
        self.statusBar.setObjectName("statusBar")
        Main.setStatusBar(self.statusBar)
        self.settings_action = QtWidgets.QAction(Main)
        self.settings_action.setObjectName("settings_action")
        self.quit_action = QtWidgets.QAction(Main)
        self.quit_action.setObjectName("quit_action")
        self.statistic_action = QtWidgets.QAction(Main)
        self.statistic_action.setObjectName("statistic_action")
        self.menuFile.addAction(self.settings_action)
        self.menuFile.addAction(self.statistic_action)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.quit_action)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(Main)
        self.quit_action.triggered['bool'].connect(Main.close)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "MainWindow"))
        self.menuFile.setTitle(_translate("Main", "File"))
        self.station1_dock.setWindowTitle(_translate("Main", "Station 1"))
        self.station2_dock.setWindowTitle(_translate("Main", "Station 2"))
        self.settings_action.setText(_translate("Main", "Settings"))
        self.quit_action.setText(_translate("Main", "Quit"))
        self.statistic_action.setText(_translate("Main", "Statistic"))

from ces.app.plot import PlotWidget
