'''
Created on 22.01.2015

@author: fiona
'''
from Sensor import Sensor

class i2cSensor(Sensor):
    '''
    Base class for all i2c sensors
    '''


    def __init__(self, name, sensorType):
        '''
        Constructor
        '''
        
        Sensor.__init__(self, name, sensorType)
    
    def read(self):
        raise NotImplementedError("Not implemented")
    
    def initCommunication(self, firmata):
        raise NotImplementedError("Not implemented")
    