# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statistic.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_Statistic(object):
    def setupUi(self, Statistic):
        Statistic.setObjectName("Statistic")
        Statistic.resize(884, 345)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Statistic)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.avg = BarWidget(Statistic)
        self.avg.setObjectName("avg")
        self.horizontalLayout.addWidget(self.avg)
        self.max = BarWidget(Statistic)
        self.max.setObjectName("max")
        self.horizontalLayout.addWidget(self.max)
        self.min = BarWidget(Statistic)
        self.min.setObjectName("min")
        self.horizontalLayout.addWidget(self.min)

        self.retranslateUi(Statistic)
        QtCore.QMetaObject.connectSlotsByName(Statistic)

    def retranslateUi(self, Statistic):
        _translate = QtCore.QCoreApplication.translate
        Statistic.setWindowTitle(_translate("Statistic", "Dialog"))


from ces.app.plot import BarWidget
