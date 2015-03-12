'''
<<<<<<< HEAD
Created on 09.03.2015

@author: dorien
'''
from Sensor import Sensor
# from cmath import log
import math
import time

=======
Created on 05.03.2015

@author: fiona
'''
from Sensor import Sensor
>>>>>>> origin/master

class DigitalSensor(Sensor):
    '''
    classdocs
    '''


    def __init__(self, name, sensorType, pinNr, firmata):
        '''
        Constructor
        '''
<<<<<<< HEAD
        
        Sensor.__init__(self, name, sensorType, firmata)
        self.__pinNr = pinNr
        firmata.enable_digital_reporting(pinNr)  
    
        
    def getValue(self):
        self._Sensor__value = self.firmata().digital_read(self.__pinNr)   
        print (self._Sensor__value )

        
        
        if self._Sensor__type == "GD_temphumid":
            
            self.firmata().set_pin_mode (self.__pinNr, self.firmata().INPUT, self.firmata().DIGITAL)
            self.firmata().digital_write(self.__pinNr, self.firmata().HIGH )
            time.sleep(0.25)
            
            self.firmata().set_pin_mode (self.__pinNr, self.firmata().OUTPUT, self.firmata().DIGITAL)
            self.firmata().digital_write(self.__pinNr, self.firmata().LOW )
            time.sleep(0.020)
            self.firmata().digital_write(self.__pinNr, self.firmata().HIGH )
            time.sleep(0.040)
            self.firmata().set_pin_mode (self.__pinNr, self.firmata().INPUT, self.firmata().DIGITAL)            
            
            
            for  i in range (0,85):
                counter = 0
                laststate = self.firmata().digital_read(self.__pinNr)   

                while (self.firmata().digital_read(self.__pinNr)  == laststate) :
                    counter = counter +1
                    time.sleep(0.001)
                    if (counter == 255) :
                        break
                
                laststate = self.firmata().digital_read(self.__pinNr) 
                if (counter == 255):
                    break
     
            
            self._Sensor__value = self.firmata().digital_read(self.__pinNr)   

#             table = self.firmata().get_digital_response_table()
#             print (table)
        
            return (self._Sensor__value)
        
#         if self._Sensor__type == "GD_barometer" :
            




        
        else :
            return (self.firmata().digital_read(self.__pinNr))  

            
            
#         return(self._Sensor__value)
=======
                
        Sensor.__init__(self, name, sensorType, firmata)
        self.__pinNr = pinNr
        firmata.enable_digital_reporting(pinNr)
    
    
    def getValue(self):
        self._Sensor__value = self.firmata().digital_read(self.__pinNr)
        return(self._Sensor__value)
>>>>>>> origin/master
    
    def getPinNr(self):
        return self.__pinNr