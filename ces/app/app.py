from qtpy import QtWidgets

from ces.app import setTimeInterval, getTimeInterval
from ces.app.data import DataFetcher, DataModel
from ces.app.statistic import StatisticDialog
from ces.ui.main import Ui_Main


class CESApp(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        self.ui.station1_plot.toolbar.hide()
        self.ui.station2_plot.toolbar.hide()
        self.ui.main_plot.setTitle("Average")
        self.ui.station1_plot.setTitle("Station 1")

        self.ui.station2_plot.setTitle("Station 2")


        self.ui.statusBar.showMessage("Disconnected")

        fetcher = DataFetcher()
        fetcher.loaded.connect(self._onRefresh)
        fetcher.connected.connect(lambda x: self.statusBar().showMessage("Connected") if x else self.statusBar().showMessage("Disconnected"))
        fetcher.start()

        self.ui.settings_action.triggered.connect(self._onSettings)
        self.ui.statistic_action.triggered.connect(self._onStatistic)

    def _onRefresh(self, data_model: DataModel):
        self.ui.main_plot.updateData(data_model.temperature, data_model.humidity, data_model.time)
        self.ui.station1_plot.updateData(data_model.temperature_station1, data_model.humidity_station1, data_model.time)
        self.ui.station2_plot.updateData(data_model.temperature_station2, data_model.humidity_station2, data_model.time)

    def _onSettings(self):
        item, ok = QtWidgets.QInputDialog.getDouble(self, "Set Refresh Interval", "Interval (sec):",
                                                    value=getTimeInterval(), min=0.001, max=5000)
        if ok:
            setTimeInterval(item)

    def _onStatistic(self):
        dlg = StatisticDialog()
        dlg.exec_()
