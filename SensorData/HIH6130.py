'''
Created on 24.01.2015

@author: fiona
'''
from i2cSensor import i2cSensor
import time

class HIH6130(i2cSensor):
    '''
    HIH6130 temperature and humidity sensor
    '''
    
    ADDR = 0x27
    READ_REQUEST = 0x0


    def __init__(self, name, sensorType):
        '''
        Constructor
        '''
    
    def initCommunication(self, firmata):
        # enable the sensor
        #firmata.i2c_write(self.ADDR, self.COMMAND_BIT | self.WORD_BIT | self.REGISTER_CONTROL)
        #firmata.i2c_write(self.ADDR, self.CONTROL_POWERON)
        pass
        

    def rawToTemperature(self, data):
        # TODO: check if values are correct
        # use bitshift
        temperature = float(data[1] * 2**6 + data[0] / 4) / float(2**14 - 1) * 165.0 - 40.0;
        
        return temperature
    
    def rawToHumidity(self, data):
        humidity = (((data[1] & 0x3f) /2**8) | data[0]) * 100 / float((2**14) - 1);
        return humidity

    
    def read(self, firmata):
        firmata.i2c_write(self.ADDR, self.READ_REQUEST)
        firmata.i2c_read(self.ADDR, 0, 4, firmata.I2C_READ)
        time.sleep(0.5)
        
        data = firmata.i2c_get_read_data(self.ADDR)
        
        if (data is not None):
            humidity = self.rawToHumidity(data[1:3])
            temperature = self.rawToTemperature(data[2:-1])
        
            return (humidity, temperature)
        
        else:
            return -1