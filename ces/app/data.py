import random
import time
from datetime import datetime, timedelta
from threading import Thread

import numpy as np
from PyQt5.QtCore import pyqtSignal
from qtpy import QtCore


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
        self.interval = 2

        QtCore.QObject.__init__(self)
        Thread.__init__(self)

    def run(self):
        while True:
            data_model = self.provider.loadData()
            self.loaded.emit(data_model)
            time.sleep(self.interval)


class MockDataProvider:
    mock_temp_1 = []
    mock_temp_2 = []
    mock_hum_1 = []
    mock_hum_2 = []
    time = []

    last_time = datetime.now()

    def loadData(self) -> DataModel:
        model = DataModel()

        now = datetime.now()
        diff = now - self.last_time
        self._updateData(diff)
        self.last_time = now

        model.temperature_station1.extend(self.mock_temp_1)
        model.temperature_station2.extend(self.mock_temp_2)
        model.humidity_station1.extend(self.mock_hum_1)
        model.humidity_station2.extend(self.mock_hum_2)
        model.time.extend(self.time)

        return model

    def _updateData(self, time_range):
        count = int(time_range / timedelta(seconds=2))
        for i in range(count):
            self.mock_temp_1.append(random.uniform(20, 30))
            self.mock_temp_2.append(random.uniform(20, 30))
            self.mock_hum_1.append(random.uniform(20, 70))
            self.mock_hum_2.append(random.uniform(20, 70))
            self.time.append(self.last_time + timedelta(seconds=2 * i))
