'''
Created on 01.02.2015

@author: fiona
'''
from i2cSensor import i2cSensor
import time

class MPL3115A2(i2cSensor):
    '''
    classdocs
    '''
    MPL3115_ADDR = 0x60
    MPL3115_STATUS = 0x00
    MPL3115_PRESSURE_DATA = 0x01
    MPL3115_DR_STATUS = 0x06
    MPL3115_DELTA_DATA = 0x07
    MPL3115_WHO_AM_I = 0x0c
    MPL3115_FIFO_STATUS = 0x0d
    MPL3115_FIFO_DATA = 0x0e
    MPL3115_FIFO_SETUP = 0x0e
    MPL3115_TIME_DELAY = 0x10
    MPL3115_SYS_MODE = 0x11
    MPL3115_INT_SORCE = 0x12
    MPL3115_PT_DATA_CFG = 0x13
    MPL3115_BAR_IN_MSB = 0x14
    MPL3115_P_ARLARM_MSB = 0x16
    MPL3115_T_ARLARM = 0x18
    MPL3115_P_ARLARM_WND_MSB = 0x19
    MPL3115_T_ARLARM_WND = 0x1b
    MPL3115_P_MIN_DATA = 0x1c
    MPL3115_T_MIN_DATA = 0x1f
    MPL3115_P_MAX_DATA = 0x21
    MPL3115_T_MAX_DATA = 0x24
    MPL3115_CTRL_REG1 = 0x26
    MPL3115_CTRL_REG2 = 0x27
    MPL3115_CTRL_REG3 = 0x28
    MPL3115_CTRL_REG4 = 0x29
    MPL3115_CTRL_REG5 = 0x2a
    MPL3115_OFFSET_P = 0x2b
    MPL3115_OFFSET_T = 0x2c
    MPL3115_OFFSET_H = 0x2d
    
    MPL3115A2_CTRL_REG1_SBYB = 0x01
    MPL3115A2_CTRL_REG1_OS128 = 0x38
    MPL3115A2_CTRL_REG1_ALT = 0x80
    

    def __init__(self, name, sensorType, firmata):
        '''
        Constructor
        '''
        i2cSensor.__init__(self, name, sensorType, firmata)

    def initCommunication(self):

#         # Set to Altimeter with an OSR = 128
#         print(self.MPL3115_PRESSURE_DATA | 0x38 | 0x80)
#         self.firmata().i2c_write(self.MPL3115_ADDR, [self.MPL3115_CTRL_REG1, self.MPL3115_PRESSURE_DATA | 0x38 | 0x80])
#         # Enable Data Flags in PT_DATA_CFG
#         self.firmata().i2c_write(self.MPL3115_ADDR, self.MPL3115_PT_DATA_CFG, 0x07)
#         # Set Active (polling)
#         #firmata.i2c_write(self.MPL3115_ADDR, self.MPL3115_CTRL_REG1, 0xB9)
#         
#         time.sleep(1)
#         
#         self.firmata().i2c_read(self.MPL3115_ADDR, self.MPL3115_CTRL_REG1, 3, self.firmata().I2C_READ)
#         time.sleep(1)
#         print(self.firmata().i2c_get_read_data(self.MPL3115_ADDR))

        self.firmata().i2c_read(self.MPL3115_ADDR, 0, 1, self.firmata().I2C_READ)
        # TODO: check how this can be reduced
        time.sleep(3)
        ctrl = self.firmata().i2c_get_read_data(self.MPL3115_ADDR)
        #print(ctrl[1] & 0xfe)
        
        self.firmata().i2c_write(self.MPL3115_ADDR, self.MPL3115_CTRL_REG1, ctrl[1] & 0xfe)
        time.sleep(2)
        self.firmata().i2c_read(self.MPL3115_ADDR, 0, 1, self.firmata().I2C_READ)
        time.sleep(1)
        print(self.firmata().i2c_get_read_data(self.MPL3115_ADDR))
        
        time.sleep(1)
        self.firmata().i2c_write(self.MPL3115_ADDR, 0x26, 0xb8)
        
        time.sleep(1)
        self.firmata().i2c_read(self.MPL3115_ADDR, 0x26, 1, self.firmata().I2C_READ)
        time.sleep(1)
        print(self.firmata().i2c_get_read_data(self.MPL3115_ADDR))
        
#         
#         self.firmata().i2c_write(self.MPL3115_ADDR, 0x2d, 0x00)
#         self.firmata().i2c_write(self.MPL3115_ADDR, 0x26, 0xb8)
#         self.firmata().i2c_write(self.MPL3115_ADDR, 0x13, 0x07)
#         
#         self.firmata().i2c_write(self.MPL3115_ADDR, 0x26, 0xb9)
        
    def read(self):
        
        self.firmata().i2c_read(self.MPL3115_ADDR, 0, 1, self.firmata().I2C_READ)
        time.sleep(0.2)
        ctrl = self.firmata().i2c_get_read_data(self.MPL3115_ADDR)
        print(ctrl)
        
#         self.firmata().i2c_read(0x60, 0x01, 5, self.firmata().I2C_READ)
#         data = self.firmata().i2c_get_read_data(0x60)
#         
#         if (data is not None):
#             return data
        
        #firmata.i2c_write(self.MPL3115_ADDR, self.MPL3115_STATUS)
#         time.sleep(0.1)
#         self.firmata().i2c_read(self.MPL3115_ADDR, self.MPL3115_STATUS, 1, self.firmata().I2C_READ)
#         time.sleep(1)
#         STA = self.firmata().i2c_get_read_data(self.MPL3115_ADDR)
#         
#         #if (STA & 0x04) == 4:
#         # OUT_P
#         self.firmata().i2c_write(self.MPL3115_ADDR, 0x03)
#         time.sleep(0.1)
#         self.firmata().i2c_read(self.MPL3115_ADDR, 0x03, 3, self.firmata().I2C_READ)
#         time.sleep(1)
#         OUT_P_MSB = self.firmata().i2c_get_read_data(self.MPL3115_ADDR)
#         
#         return (STA, OUT_P_MSB)
#         
#         firmata.i2c_read(self.MPL3115_ADDR, 0x02, 1, firmata.I2C_READ)
#         time.sleep(1)
#         OUT_P_CSB = firmata.i2c_get_read_data(self.MPL3115_ADDR)
        
        #OUT_P_CSB = firmata.i2c_read(self.MPL3115_ADDR, 0x02)
        #OUT_P_LSB = firmata.i2c_read(self.MPL3115_ADDR, s0x04)
        # # OUT_T
        # OUT_T_MSB = readI2C(0x04)
        # OUT_T_LSB = readI2C(0x05)
        
        # print OUT_P_MSB
        # print OUT_P_CSB
        # print OUT_P_LSB
        
        # treat the bits to get the altitude
        #signedvalue = OUT_P_MSB + OUT_P_CSB[2:]
        # fraction = OUT_P_LSB[:3]
        
        # print int(signedvalue,16)
        # print int(fraction,16)
        
        #string = "signedvalue: %s" % signedvalue
        #return (OUT_P_CSB, OUT_P_MSB)
        
        return -1
            
