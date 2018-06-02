from typing import List

from matplotlib import dates as md
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from qtpy import QtWidgets


class PlotWidget(QtWidgets.QWidget):

    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self)
        self.v_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.v_layout)

        self.initMainCanvas()

    def initMainCanvas(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        FigureCanvas.setSizePolicy(self.canvas, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self.canvas)

        self.axes = self.figure.subplots(2, 1, sharex=True)
        self.figure.subplots_adjust(hspace=0)

        self.v_layout.addWidget(self.canvas)
        self.v_layout.addWidget(self.toolbar)

    def setTitle(self,title):
        self.axes[0].set_title(title)

    def updateData(self, temperature, humidity, time):
        self.axes[0].clear()
        self.axes[1].clear()


        self.axes[0].plot(time, temperature,color='r')
        self.axes[0].set_ylabel('Temperature [°C]')
        self.axes[0].set_xlabel('Time')
        self.axes[1].plot(time, humidity, color='c')
        self.axes[1].set_ylabel('Humidity [%]')

        xformatter = md.DateFormatter('%H:%M')
        xlocator = md.MinuteLocator(byminute=range(0, 60, 10), interval=1)
        self.axes[0].xaxis.set_major_locator(xlocator)
        self.axes[0].xaxis.set_major_formatter(xformatter)

        self.canvas.draw()


class BarWidget(QtWidgets.QWidget):

    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self)
        self.v_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.v_layout)

        self.initMainCanvas()

    def initMainCanvas(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        self.toolbar.hide()
        FigureCanvas.setSizePolicy(self.canvas, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self.canvas)

        self.axs = self.figure.subplots(2, 1)

        self.v_layout.addWidget(self.canvas)

    def updateData(self, temperature, humidity, days):
        self.axs[0].clear()
        self.axs[1].clear()

        self.axs[0].bar(days, temperature, color="r")
        plt.title('title')

        self.axs[1].bar(days, humidity, color='c')


        xformatter = md.DateFormatter('%d.%m.')
        xlocator = md.DayLocator()
        self.axs[0].xaxis.set_major_locator(xlocator)
        self.axs[0].xaxis.set_major_formatter(xformatter)
        self.axs[1].xaxis.set_major_locator(xlocator)
        self.axs[1].xaxis.set_major_formatter(xformatter)

        self.canvas.draw()
