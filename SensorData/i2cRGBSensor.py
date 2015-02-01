# '''
# Created on 23.01.2015
# 
# @author: fiona
# '''
# https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/blob/master/Adafruit_TCS34725/Adafruit_TCS34725.py
 
from i2cSensor import i2cSensor
import time
 
TCS34725_ADDRESS = 0x29
 
TCS34725_ID = 0x12  # 0x44 = TCS34721/TCS34725, 0x4D = TCS34723/TCS34727
 
TCS34725_COMMAND_BIT = 0x80
 
TCS34725_ENABLE = 0x00
# TCS34725_ENABLE_AIEN = 0x10  # RGBC Interrupt Enable
# TCS34725_ENABLE_WEN = 0x08  # Wait enable - Writing 1 activates the wait timer
TCS34725_ENABLE_AEN = 0x02  # RGBC Enable - Writing 1 actives the ADC, 0 disables it
TCS34725_ENABLE_PON = 0x01  # Power on - Writing 1 activates the internal oscillator, 0 disables it
 
TCS34725_ATIME = 0x01  # Integration time
TCS34725_WTIME = 0x03  # Wait time (if TCS34725_ENABLE_WEN is asserted)
TCS34725_WTIME_2_4MS = 0xFF  # WLONG0 = 2.4ms   WLONG1 = 0.029s
TCS34725_WTIME_204MS = 0xAB  # WLONG0 = 204ms   WLONG1 = 2.45s
# TCS34725_WTIME_614MS = 0x00  # WLONG0 = 614ms   WLONG1 = 7.4s
 
TCS34725_AILTL = 0x04  # Clear channel lower interrupt threshold
TCS34725_AILTH = 0x05
TCS34725_AIHTL = 0x06  # Clear channel upper interrupt threshold
TCS34725_AIHTH = 0x07
 
TCS34725_PERS = 0x0C  # Persistence register - basic SW filtering mechanism for interrupts
TCS34725_PERS_NONE = 0b0000  # Every RGBC cycle generates an interrupt
TCS34725_PERS_1_CYCLE = 0b0001  # 1 clean channel value outside threshold range generates an interrupt
TCS34725_PERS_2_CYCLE = 0b0010  # 2 clean channel values outside threshold range generates an interrupt
TCS34725_PERS_3_CYCLE = 0b0011  # 3 clean channel values outside threshold range generates an interrupt
TCS34725_PERS_5_CYCLE = 0b0100  # 5 clean channel values outside threshold range generates an interrupt
TCS34725_PERS_10_CYCLE = 0b0101  # 10 clean channel values outside threshold range generates an interrupt
TCS34725_PERS_15_CYCLE = 0b0110  # 15 clean channel values outside threshold range generates an interrupt
TCS34725_PERS_20_CYCLE = 0b0111  # 20 clean channel values outside threshold range generates an interrupt
TCS34725_PERS_25_CYCLE = 0b1000  # 25 clean channel values outside threshold range generates an interrupt
TCS34725_PERS_30_CYCLE = 0b1001  # 30 clean channel values outside threshold range generates an interrupt
TCS34725_PERS_35_CYCLE = 0b1010  # 35 clean channel values outside threshold range generates an interrupt
TCS34725_PERS_40_CYCLE = 0b1011  # 40 clean channel values outside threshold range generates an interrupt
TCS34725_PERS_45_CYCLE = 0b1100  # 45 clean channel values outside threshold range generates an interrupt
TCS34725_PERS_50_CYCLE = 0b1101  # 50 clean channel values outside threshold range generates an interrupt
TCS34725_PERS_55_CYCLE = 0b1110  # 55 clean channel values outside threshold range generates an interrupt
TCS34725_PERS_60_CYCLE = 0b1111  # 60 clean channel values outside threshold range generates an interrupt
 
TCS34725_CONFIG = 0x0D
TCS34725_CONFIG_WLONG = 0x02  # Choose between short and long (12x) wait times via TCS34725_WTIME
TCS34725_CONTROL = 0x0F  # Set the gain level for the sensor
TCS34725_ID = 0x12  # 0x44 = TCS34721/TCS34725, 0x4D = TCS34723/TCS34727
TCS34725_STATUS = 0x13
TCS34725_STATUS_AINT = 0x10  # RGBC Clean channel interrupt
TCS34725_STATUS_AVALID = 0x01  # Indicates that the RGBC channels have completed an integration cycle
 
TCS34725_CDATAL = 0x14  # Clear channel data
TCS34725_CDATAH = 0x15
TCS34725_RDATAL = 0x16  # Red channel data
TCS34725_RDATAH = 0x17
TCS34725_GDATAL = 0x18  # Green channel data
TCS34725_GDATAH = 0x19
TCS34725_BDATAL = 0x1A  # Blue channel data
TCS34725_BDATAH = 0x1B
 
TCS34725_INTEGRATIONTIME_2_4MS = 0xFF  #  2.4ms - 1 cycle    - Max Count: 1024
TCS34725_INTEGRATIONTIME_24MS = 0xF6  # 24ms  - 10 cycles  - Max Count: 10240
TCS34725_INTEGRATIONTIME_50MS = 0xEB  #  50ms  - 20 cycles  - Max Count: 20480
TCS34725_INTEGRATIONTIME_101MS = 0xD5  #  101ms - 42 cycles  - Max Count: 43008
TCS34725_INTEGRATIONTIME_154MS = 0xC0  #  154ms - 64 cycles  - Max Count: 65535
TCS34725_INTEGRATIONTIME_700MS = 0x00  #  700ms - 256 cycles - Max Count: 65535
 
TCS34725_GAIN_1X = 0x00  #  No gain
TCS34725_GAIN_4X = 0x01  #  2x gain
TCS34725_GAIN_16X = 0x02  #  16x gain
TCS34725_GAIN_60X = 0x03  #  60x gain
 
__integrationTimeDelay = {
    0xFF: 0.0024,  # 2.4ms - 1 cycle    - Max Count: 1024
    0xF6: 0.024,  # 24ms  - 10 cycles  - Max Count: 10240
    0xEB: 0.050,  # 50ms  - 20 cycles  - Max Count: 20480
    0xD5: 0.101,  # 101ms - 42 cycles  - Max Count: 43008
    0xC0: 0.154,  # 154ms - 64 cycles  - Max Count: 65535
    0x00: 0.700  # 700ms - 256 cycles - Max Count: 65535
}
 
class i2cRGBSensor(i2cSensor):
    '''
    i2c RGB sensor
    '''
     
    def __init__(self, name, sensorType):
        '''
        Constructor
        '''
        i2cSensor.__init__(self, name, sensorType)
     
         
    def getCurrentData(self):
        raise NotImplementedError("Not implemented")
     
    def initCommunication(self, firmata):
                 
        firmata.i2c_write(TCS34725_ADDRESS, TCS34725_COMMAND_BIT | TCS34725_ID)
        time.sleep(5)
        
#         firmata.i2c_write(TCS34725_ADDRESS, TCS34725_ENABLE_PON)
#         time.sleep(5)
        
#         firmata.i2c_read(TCS34725_ADDRESS, TCS34725_ID, 1, firmata.I2C_READ)
#         time.sleep(5)

        ver = firmata.i2c_get_read_data(TCS34725_ADDRESS)
        time.sleep(5)

        if (ver == 0x44):
            print ("found it")
        else :
            print ("did not find it")
             
    

          

         
          
#         firmata.i2c_write(TCS34725_ADDRESS, TCS34725_ENABLE, (TCS34725_ENABLE_PON |TCS34725_ENABLE_AEN))
         
#         imcool = firmata.i2c_read(TCS34725_ADDRESS, TCS34725_ID, 1, firmata.I2C_READ)
#         print (" firmata.i2c_read(TCS34725_ID) " + str( imcool))
 
 
     
    def read(self, firmata):
        color =  {}
#         firmata.i2c_write(TCS34725_ADDRESS, TCS34725_RDATAL)
#         time.sleep(1)
#         firmata.i2c_read(TCS34725_ADDRESS, TCS34725_RDATAL, 1, firmata.I2C_READ)
#         time.sleep(1)
#         color["r"] = firmata.i2c_get_read_data(TCS34725_ADDRESS)
         
#         i2c_map = {}
#         firmata.i2c_reply(color["r"]) 
#         
#         firmata.i2c_write(TCS34725_ADDRESS, TCS34725_GDATAL)
#         time.sleep(1)
#         firmata.i2c_read(TCS34725_ADDRESS, TCS34725_GDATAL, 1, firmata.I2C_READ)
#         time.sleep(1)
#         color["g"] = firmata.i2c_get_read_data(TCS34725_ADDRESS)
#         
#         firmata.i2c_write(TCS34725_ADDRESS, TCS34725_BDATAL)
#         time.sleep(1)
#         firmata.i2c_read(TCS34725_ADDRESS, TCS34725_BDATAL, 1, firmata.I2C_READ)
#         time.sleep(1)
#         color["b"] = firmata.i2c_get_read_data(TCS34725_ADDRESS)
#         
#          
#         time.sleep(1)
# 
#         if (len(color) != 0):
#             
#             return i2c_map
#         
#         return -1
  
 
        if (len(color) != 0):
             
            return color
         
        return -1
     
     
     
     
     
