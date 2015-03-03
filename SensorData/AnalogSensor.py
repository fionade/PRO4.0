'''
Created on 02.03.2015

@author: fiona
'''
from Sensor import Sensor

class AnalogSensor(Sensor):
    '''
    classdocs
    '''


    def __init__(self, name, sensorType, pinNr, firmata):
        '''
        Constructor
        '''
        
        Sensor.__init__(self, name, sensorType, firmata)
        self.__pinNr = pinNr
        firmata.enable_analog_reporting(pinNr)
    
    
    def getValue(self):
        self._Sensor__value = self.firmata().analog_read(self.__pinNr)
        return(self._Sensor__value)
    
    def getPinNr(self):
        return self.__pinNr