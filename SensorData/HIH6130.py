'''
Created on 24.01.2015

@author: fiona
'''
from i2cSensor import i2cSensor
from Sensor import Sensor
import thread
import time

class HIH6130(i2cSensor):
    '''
    HIH6130 temperature and humidity sensor
    '''
    
    ADDR = 0x27
    READ_REQUEST = 0x0


    def __init__(self, name, sensorType, firmata, thread_lock):
        '''
        Constructor
        '''
        self.__thread_lock = thread_lock
        i2cSensor.__init__(self, name, sensorType, firmata)
    
    def initCommunication(self):
        # no initialisation needed for this sensor
        self._Sensor__running = True
        self._Sensor__thread = thread.start_new_thread(self.poll, (self.__thread_lock,))
        

    def rawToTemperature(self, data):
        # TODO: check if values are correct
        # use bitshift
        temperature = float(data[1] * 2**6 + data[0] / 4) / float(2**14 - 1) * 165.0 - 40.0;
        
        return temperature
    
    def rawToHumidity(self, data):
        # TODO: check if values are correct
        # use bitshift
        humidity = (((data[1] & 0x3f) /2**8) | data[0]) * 100 / float((2**14) - 1);
        return humidity
    
    def poll(self, thread_lock):
        while self._Sensor__running:
            thread_lock.acquire()
            self.firmata().i2c_write(self.ADDR, self.READ_REQUEST)
            self.firmata().i2c_read(self.ADDR, 0, 4, self.firmata().I2C_READ)
            time.sleep(0.3)
            data = self.firmata().i2c_get_read_data(self.ADDR)
            thread_lock.release()
            
            if (data is not None):
                # two bytes for humidity
                humidity = self.rawToHumidity(data[1:3])
                # two bytes for temperature
                temperature = self.rawToTemperature(data[2:-1])
            
                self._Sensor__value = (humidity, temperature)
                #return (self._Sensor__value)
            
            else:
                self._Sensor__value = -1
                #return -1
            time.sleep(0.8)