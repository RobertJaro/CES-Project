import random
import time
from datetime import datetime, timedelta
from threading import Thread

import numpy as np
from PyQt5.QtCore import pyqtSignal
from qtpy import QtCore

from ces.app import time_interval


class DataModel:
    def __init__(self):
        self.temperature_station1 = []
        self.temperature_station2 = []
        self.humidity_station1 = []
        self.humidity_station2 = []
        self.time = []

    @property
    def temperature(self):
        return np.mean([self.temperature_station1, self.temperature_station2], axis=0)

    @property
    def humidity(self):
        return np.mean([self.humidity_station1, self.humidity_station2], axis=0)


class DataFetcher(QtCore.QObject, Thread):
    loaded = pyqtSignal(object)

    def __init__(self):
        self.provider = MockDataProvider()

        QtCore.QObject.__init__(self)
        Thread.__init__(self)

    def run(self):
        while True:
            now = datetime.now()
            data_model = self.provider.loadData(now - timedelta(hours=2), now)
            self.loaded.emit(data_model)
            time.sleep(time_interval)


class MockDataProvider:
    mock_temp_1 = []
    mock_temp_2 = []
    mock_hum_1 = []
    mock_hum_2 = []
    mock_time = []

    def loadData(self, from_time, to_time) -> DataModel:
        model = DataModel()

        self._updateData(to_time, from_time)

        model.temperature_station1.extend(self.mock_temp_1)
        model.temperature_station2.extend(self.mock_temp_2)
        model.humidity_station1.extend(self.mock_hum_1)
        model.humidity_station2.extend(self.mock_hum_2)
        model.time.extend(self.mock_time)

        return model

    def _updateData(self, to_time, from_time):
        self.mock_temp_1.clear()
        self.mock_temp_2.clear()
        self.mock_hum_1.clear()
        self.mock_hum_2.clear()
        self.mock_time.clear()

        count = int((to_time - from_time) / timedelta(seconds=time_interval))
        for i in range(count):
            self.mock_temp_1.append(random.uniform(20, 30))
            self.mock_temp_2.append(random.uniform(20, 30))
            self.mock_hum_1.append(random.uniform(20, 70))
            self.mock_hum_2.append(random.uniform(20, 70))
            self.mock_time.append(from_time + i * timedelta(seconds=time_interval))
