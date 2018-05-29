import pickle
import random
import socket
import time
from datetime import datetime, timedelta
from threading import Thread

import numpy as np
from PyQt5.QtCore import pyqtSignal
from dateutil import parser
from qtpy import QtCore

from ces.app import getTimeInterval

HOST = "10.0.0.5"
PORT = 50008


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
        QtCore.QObject.__init__(self)
        Thread.__init__(self)

    def run(self):
        while True:
            now = datetime.utcnow()
            data_model = data_provider.loadData(now - timedelta(hours=2), now)
            self.loaded.emit(data_model)
            time.sleep(getTimeInterval())


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

        count = int((to_time - from_time) / timedelta(seconds=getTimeInterval()))
        for i in range(count):
            self.mock_temp_1.append(random.uniform(20, 30))
            self.mock_temp_2.append(random.uniform(20, 30))
            self.mock_hum_1.append(random.uniform(20, 70))
            self.mock_hum_2.append(random.uniform(20, 70))
            self.mock_time.append(from_time + i * timedelta(seconds=getTimeInterval()))


class DataProvider:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((HOST, PORT))

    def loadData(self, from_time, to_time) -> DataModel:
        self.socket.sendall('{};{}'.format(from_time, to_time).encode())
        response = self.socket.recv(10000)
        data = pickle.loads(response)
        model = DataModel()
        for d in data:
            model.temperature_station1.append(d[0])
            model.temperature_station2.append(d[1])
            model.humidity_station1.append(d[2])
            model.humidity_station2.append(d[3])
            model.time.append(parser.parse(d[4]))
        return model


data_provider = MockDataProvider()
