from qtpy import QtWidgets

from ces.ui.main import Ui_Main


class CESApp(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
