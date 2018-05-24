from matplotlib import pyplot as plt
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

    def updateData(self, temperature, humidity, time):
        self.axes[0].clear()
        self.axes[1].clear()

        self.axes[0].plot(time, temperature)
        self.axes[1].plot(time, humidity)


        self.canvas.draw()
