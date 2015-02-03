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
from MPL3115A2 import MPL3115A2

    
def initDatabase(dbAddress):
    pass


def initSensors(sensors, firmata):
    for s in sensors:
        # TODO: some sensor init function
        # on the sensor instance or globally for all?
        # how to get a device's address?
        print ("Setting up " + str(s))
        s.initCommunication()
    time.sleep(0.5)


def writeToDatabase(data):
    raise NotImplementedError("Not implemented")


def loop(sensors, firmata):
    # iterate through all sensors, get their data (they should all implement a getData function, depending on their type
    # and write to file
    # print('listening')
    for s in sensors:
        # TODO: one thread per sensor and then just read the last value.
        data = s.read()
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
    
    # board setup
    firmata = PyMata(arduinoAddress)
    # initialise for i2c calls
    firmata.i2c_config(0, firmata.DIGITAL, 21, 20)
    
    # TODO: add firmata to constructors
    
    # list all attached sensors
    sensors = []
    #sensors.append(i2cTemperatureSensor("id", "type"))
    sensors.append(i2cLightSensor(1, "light", firmata))
    sensors.append(HIH6130(2, "humidity_temperature", firmata))
    #sensors.append(MPL3115A2(3, "altitude"))
    #sensors.append(i2cRGBSensor(2, "rgb"))
    
    # database/file
    database = initDatabase(dbAddress)
    
    # sensors
    # TODO: differentiate between different types of sensors
    initSensors(sensors, firmata)
    
    #run = Main(arduinoAddress, dbAddress, sensors)
    
    while True:
        loop(sensors, firmata)

