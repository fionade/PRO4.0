'''
Created on 22.01.2015

@author: fiona
'''
from PyMata.pymata import PyMata
#from i2cTemperatureSensor import i2cTemperatureSensor
from i2cLightSensor import i2cLightSensor
import time
from i2cRGBSensor import i2cRGBSensor
from HIH6130 import HIH6130

class Main(object):
    
    def __init__(self, arduinoAddress, dbAddress, sensors):
        # database/file
        self.__database = self.initDatabase(dbAddress)
        
        # board setup
        self.__firmata = PyMata(arduinoAddress)
        # initialise for i2c calls
        self.__firmata.i2c_config(0, self.__firmata.DIGITAL, 21, 20)
        
        # sensors
        # TODO: differentiate between different types of sensors
        self.__sensors = self.initSensors(sensors)
        
    
    def initDatabase(self, dbAddress):
        pass

    
    def initSensors(self, sensors):
        for s in sensors:
            # TODO: some sensor init function
            # on the sensor instance or globally for all?
            # how to get a device's address?
            print ("Setting up " + str(s))
            s.initCommunication(self.__firmata)
        time.sleep(0.5)

    
    def writeToDatabase(self, data):
        raise NotImplementedError("Not implemented")
 
    
    def loop(self):
        # iterate through all sensors, get their data (they should all implement a getData function, depending on their type
        # and write to file
        # print('listening')
        for s in sensors:
            data = s.read(self.__firmata)
            print(data)
        time.sleep(1)


'''
Main functionality:
read configurations, initialise database and sensors
start loop to collect sensor data and write to database/file
'''
if __name__ == '__main__':
    
    # config
    arduinoAddress = "/dev/tty.usbmodemfa141"
    dbAddress = ""
    
    # list all attached sensors
    sensors = []
    #sensors.append(i2cTemperatureSensor("id", "type"))
    #sensors.append(i2cLightSensor(1, "light"))
    sensors.append(HIH6130(1, "humidity_temperature"))
    #sensors.append(i2cRGBSensor(2, "rgb"))
    
    run = Main(arduinoAddress, dbAddress, sensors)
    
    while True:
        run.loop()

