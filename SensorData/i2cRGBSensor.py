'''
Created on 23.01.2015

@author: fiona
'''
from i2cSensor import i2cSensor

class i2cRGBSensor(i2cSensor):
    '''
    classdocs
    '''


    def __init__(self, name, sensorType):
        '''
        Constructor
        '''
        i2cSensor.__init__(self, name, sensorType)
    
    def getCurrentData(self):
        pass
    
    def initCommunication(self):
        pass