'''
Created on 22.01.2015

@author: fiona
'''
from i2cSensor import i2cSensor
import time

# i2c definitions
# TODO: check which definitions can be transferred to the parent class
READBIT                   = 0x01
COMMAND_BIT               = 0x80    # Must be 1
CLEAR_BIT                 = 0x40    # Clears any pending interrupt (write 1 to clear)
WORD_BIT                  = 0x20    # 1 = read/write word (rather than byte)
BLOCK_BIT                 = 0x10    # 1 = using block read/write

CONTROL_POWERON           = 0x03
CONTROL_POWEROFF          = 0x00

REGISTER_CONTROL          = 0x00

REG_CHAN0_WORD = 0xAC
REG_CHAN1_WORD = 0xAE

ADDR = 0x39

class i2cLightSensor(i2cSensor):
    '''
    i2c light sensor
    '''

    def __init__(self, name, sensorType):
        '''
        Constructor
        '''
        i2cSensor.__init__(self, name, sensorType)
    
        
    def getCurrentData(self):
        raise NotImplementedError("Not implemented")
    
    def initCommunication(self, firmata):
        firmata.i2c_write(ADDR, COMMAND_BIT | WORD_BIT | REGISTER_CONTROL)
        firmata.i2c_write(ADDR, CONTROL_POWERON)
 
    
    def read(self, firmata):
        firmata.i2c_write(ADDR, REG_CHAN0_WORD)
        time.sleep(1)
        firmata.i2c_read(ADDR, REG_CHAN0_WORD, 2, firmata.I2C_READ)
        time.sleep(1)
        ch0_data = firmata.i2c_get_read_data(ADDR)
        if (ch0_data is not None):
            ch0_raw = 256 * ch0_data[2] + ch0_data[1]
            return ch0_raw
        
        return -1