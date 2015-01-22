'''
Created on 22.01.2015

@author: fiona
'''
from Sensor import Sensor

class i2cSensor(Sensor):
    '''
    Base class for all i2c sensors
    '''


    def __init__(self, name, sensorType, address):
        '''
        Constructor
        '''
        
        Sensor.__init__(self, name, sensorType, address)
        self.__address = address
        
    def getAddress(self):
        return self.__address