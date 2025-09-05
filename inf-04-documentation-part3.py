class temperatureMonitor:
    def __init__(self, k, vehicleName):
        if (type(k) == int):
            self.vehicleName = vehicleName
            self.__tableSize = k
            self.__readings = []
            vehicleName = ""

    def addReading(self, temperature):
        if (type(temperature) == float or type(temperature) == int):
            if (self.__tableSize > len(self.__readings)):
                self.__readings.append(temperature)

    def getLastReading(self):
        return self.__readings[len(self.__readings) - 1]

class temperatureMonitorOil(temperatureMonitor):
    def __init__(self, k, vehicleName, oilName):
        super().__init__(k, vehicleName)
        self.oilName = oilName

temperatureMonitor1 = temperatureMonitor(4, "40 TP")
temperatureMonitor1.addReading(120)
print(temperatureMonitor1.getLastReading())
temperatureMonitor1.addReading(50)
print(temperatureMonitor1.getLastReading())

oil = temperatureMonitorOil(2, "50 TP", "ABC")
oil.addReading(20)
print(oil.getLastReading())