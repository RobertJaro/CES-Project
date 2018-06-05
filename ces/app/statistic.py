from datetime import datetime, timedelta

import numpy as np
from qtpy import QtWidgets

from ces.app.data import data_provider
from ces.ui.statistic import Ui_Statistic


class StatisticDialog(QtWidgets.QDialog):

    def __init__(self):
        QtWidgets.QDialog.__init__(self)

        self.ui = Ui_Statistic()
        self.ui.setupUi(self)


        now = datetime.utcnow()
        data_model = data_provider.loadData(now - timedelta(weeks=3), now)

        day = None
        days = {}
        for i, time in enumerate(data_model.time):
            if day is time.day:
                np.append(days[day], self._getData(data_model, i))
            else:
                day = time.day
                days[day] = np.array([self._getData(data_model, i)])

        avg_tmp = [np.average(np.append(d[:, 0].ravel(), d[:, 1].ravel())) for d in days.values()]
        avg_hum = [np.average(np.append(d[:, 2].ravel(), d[:, 3].ravel())) for d in days.values()]

        max_tmp = [np.max(np.append(d[:, 0].ravel(), d[:, 1].ravel())) for d in days.values()]
        max_hum = [np.max(np.append(d[:, 2].ravel(), d[:, 3].ravel())) for d in days.values()]

        min_tmp = [np.min(np.append(d[:, 0].ravel(), d[:, 1].ravel())) for d in days.values()]
        min_hum = [np.min(np.append(d[:, 2].ravel(), d[:, 3].ravel())) for d in days.values()]

        self.ui.avg.setWindowTitle('Average')
        self.ui.avg.updateData(avg_tmp, avg_hum, days.keys())

        self.ui.max.updateData(max_tmp, max_hum, days.keys())
        self.ui.min.updateData(min_tmp, min_hum, days.keys())

    def _getData(self, data_model, i):
        return [data_model.temperature_station1[i], data_model.temperature_station2[i], data_model.humidity_station1[i],
                data_model.humidity_station2[i]]
