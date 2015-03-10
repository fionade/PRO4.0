'''
Created on 02.03.2015

@author: fiona
'''
from Sensor import Sensor
# from cmath import log
import math


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
        
 
        if self._Sensor__type == "ga_light" :
#             TODO: LOOK UP TABLE FOR LU VALUES             
            if self._Sensor__value < 200:
                lux = 1             
            elif self._Sensor__value < 300:
                lux = 3               
            elif self._Sensor__value < 400:
                lux = 6                
            elif self._Sensor__value < 500:
                lux = 10                  
            elif self._Sensor__value < 600:
                lux = 15 
            elif self._Sensor__value < 700:
                lux = 35
            elif self._Sensor__value < 800:
                lux = 80                
            elif self._Sensor__value > 800:
                lux = 100
            else :
                lux = -1
            return(lux)
 
         
        if self._Sensor__type == "ga_temperature":
            B = 3975
            a = int(self._Sensor__value)
            degree_celcius = 0
            if (a != 0):
                resistance=(float)(1023-a)*10000/a
#                 degree_celcius=1/(math.log(resistance/10000)/B+1/298.15)-273.15
            return(resistance)
#         TODO: exception when resistance drops too low (math out of bounds)



        if self._Sensor__type == "ga_sound":
            sound = self._Sensor__value 
            return(sound)
        
        if self._Sensor__type == "ga_movement":
            movement = self._Sensor__value 
            return(movement)
        
        if self._Sensor__type == "GA_gas1.3b":
            sensorValue = self._Sensor__value 
            Vref = 4.95
            gas=(float)(sensorValue/1023)*Vref
            return(gas)
        
        if self._Sensor__type == "GA_gas1.4":
            sensorValue = self._Sensor__value 
            Vref = 4.95
            gas=(float)(sensorValue/1023)*Vref
            return(gas)
        
        
        if self._Sensor__type == "GA_airQuality":
            airQuality = self._Sensor__value 
            
            return(airQuality)

        
        
        else :
            return (self.firmata().analog_read(self.__pinNr))

            
            
#         return(self._Sensor__value)
    
    def getPinNr(self):
        return self.__pinNr