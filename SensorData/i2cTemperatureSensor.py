'''
Created on 22.01.2015

@author: fiona
'''
from i2cSensor import i2cSensor

class i2cTemperatureSensor(i2cSensor):
    '''
    i2c temperature sensor
    '''


    def __init__(self, name, sensorType, firmata):
        '''
        Constructor
        '''
        
        # call parent constructor
        i2cSensor.__init__(self, name, sensorType, firmata)
    
    
    def initCommunication(self):
        raise NotImplementedError("Not implemented")
        