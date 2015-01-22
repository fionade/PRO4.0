'''
Created on 22.01.2015

@author: fiona
'''
from i2cSensor import i2cSensor

class i2cLightSensor(i2cSensor):
    '''
    i2c light sensor
    '''


    def __init__(self, name, sensorType, address):
        '''
        Constructor
        '''
        i2cSensor.__init__(self, name, sensorType, address)