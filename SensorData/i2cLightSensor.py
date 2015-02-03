'''
Created on 22.01.2015

@author: fiona
'''
from i2cSensor import i2cSensor
import time
import thread

class i2cLightSensor(i2cSensor):
    '''
    i2c light sensor
    '''
    
    # i2c definitions
    # refer to https://github.com/janheise/TSL2561/
    READBIT                   = 0x01
    COMMAND_BIT               = 0x80    # Must be 1
    CLEAR_BIT                 = 0x40    # Clears any pending interrupt (write 1 to clear)
    WORD_BIT                  = 0x20    # 1 = read/write word (rather than byte)
    BLOCK_BIT                 = 0x10    # 1 = using block read/write
    
    CONTROL_POWERON           = 0x03
    CONTROL_POWEROFF          = 0x00
    
    REGISTER_CONTROL          = 0x00
    REGISTER_TIMING           = 0x01
    
    INTEGRATIONTIME_402MS     = 0x02
    GAIN_16X                  = 0x10
    
    REG_CHAN0_WORD = 0xAC
    REG_CHAN1_WORD = 0xAE
    
    LUX_CHSCALE               = 10      # Scale channel values by 2^10
    LUX_RATIOSCALE            = 9       # Scale ratio by 2^9    
    LUX_LUXSCALE              = 14      # Scale by 2^14
    LUX_K1T                   = 0x0040   # 0.125 * 2^RATIO_SCALE
    LUX_B1T                   = 0x01f2   # 0.0304 * 2^    LUX_SCALE
    LUX_M1T                   = 0x01be   # 0.0272 * 2^    LUX_SCALE
    LUX_K2T                   = 0x0080   # 0.250 * 2^RATIO_SCALE
    LUX_B2T                   = 0x0214   # 0.0325 * 2^    LUX_SCALE
    LUX_M2T                   = 0x02d1   # 0.0440 * 2^    LUX_SCALE
    LUX_K3T                   = 0x00c0   # 0.375 * 2^RATIO_SCALE
    LUX_B3T                   = 0x023f   # 0.0351 * 2^    LUX_SCALE
    LUX_M3T                   = 0x037b   # 0.0544 * 2^    LUX_SCALE
    LUX_K4T                   = 0x0100   # 0.50 * 2^RATIO_SCALE
    LUX_B4T                   = 0x0270   # 0.0381 * 2^    LUX_SCALE
    LUX_M4T                   = 0x03fe   # 0.0624 * 2^    LUX_SCALE
    LUX_K5T                   = 0x0138   # 0.61 * 2^RATIO_SCALE
    LUX_B5T                   = 0x016f   # 0.0224 * 2^    LUX_SCALE
    LUX_M5T                   = 0x01fc   # 0.0310 * 2^    LUX_SCALE
    LUX_K6T                   = 0x019a   # 0.80 * 2^RATIO_SCALE
    LUX_B6T                   = 0x00d2   # 0.0128 * 2^    LUX_SCALE
    LUX_M6T                   = 0x00fb   # 0.0153 * 2^    LUX_SCALE
    LUX_K7T                   = 0x029a   # 1.3 * 2^RATIO_SCALE
    LUX_B7T                   = 0x0018   # 0.00146 * 2^    LUX_SCALE
    LUX_M7T                   = 0x0012   # 0.00112 * 2^    LUX_SCALE
    LUX_K8T                   = 0x029a   # 1.3 * 2^RATIO_SCALE
    LUX_B8T                   = 0x0000   # 0.000 * 2^    LUX_SCALE
    LUX_M8T                   = 0x0000   # 0.000 * 2^    LUX_SCALE
    
    ADDR = 0x39

    def __init__(self, name, sensorType, firmata):
        '''
        Constructor
        '''
        i2cSensor.__init__(self, name, sensorType, firmata)
    
    def initCommunication(self):
        # enable the sensor
        self.firmata().i2c_write(self.ADDR, self.COMMAND_BIT | self.WORD_BIT | self.REGISTER_CONTROL)
        self.firmata().i2c_write(self.ADDR, self.CONTROL_POWERON)
        
        # set gain and timing
        self.firmata().i2c_write(self.ADDR, self.COMMAND_BIT | self.REGISTER_TIMING, self.INTEGRATIONTIME_402MS | self.GAIN_16X)
        
        self._Sensor__running = True
        #self._Sensor__thread = thread.start_new_thread(self.poll, (firmata,))
        
    def rawToLUX(self, ch0, ch1):
        chScale = (1 << self.LUX_CHSCALE);
        ch0_data = 256 * ch0[2] + ch0[1]
        ch1_data = 256 * ch1[2] + ch1[1]
        
        # scale the channel values
        channel0 = (ch0_data * chScale) >> self.LUX_CHSCALE
        channel1 = (ch1_data * chScale) >> self.LUX_CHSCALE
        
        # find the ratio of the channel values (Channel1/Channel0)
        ratio = 0
        if channel0 != 0:
            ratio = (channel1 << (self.LUX_RATIOSCALE+1)) // channel0
        
        # round the ratio value
        ratio = (ratio + 1) >> 1
        
        if (ratio >= 0) and (ratio <= self.LUX_K1T):  
            b = self.LUX_B1T
            m = self.LUX_M1T
        elif ratio <= self.LUX_K2T:
            b = self.LUX_B2T
            m = self.LUX_M2T
        elif ratio <= self.LUX_K3T:
            b = self.LUX_B3T
            m = self.LUX_M3T
        elif ratio <= self.LUX_K4T:
            b = self.LUX_B4T
            m = self.LUX_M4T
        elif ratio <= self.LUX_K5T:
            b = self.LUX_B5T
            m = self.LUX_M5T
        elif ratio <= self.LUX_K6T:
            b = self.LUX_B6T
            m = self.LUX_M6T
        elif ratio <= self.LUX_K7T:
            b = self.LUX_B7T
            m = self.LUX_M7T
        elif ratio <= self.LUX_K8T:
            b = self.LUX_B8T
            m = self.LUX_M8T
            
        temp = ((channel0 * b) - (channel1 * m))
        # do not allow negative lux value
        if temp < 0:
            temp = 0
        # round lsb (2^(LUX_SCALE-1))
        temp += (1 << (self.LUX_LUXSCALE-1))

        # strip off fractional portion
        lux = temp >> self.LUX_LUXSCALE

        # Signal I2C had no errors
        return lux

    
    def read(self):
        #while self._Sensor__running:
        self.firmata().i2c_write(self.ADDR, self.REG_CHAN0_WORD)
        self.firmata().i2c_read(self.ADDR, self.REG_CHAN0_WORD, 2, self.firmata().I2C_READ)
        time.sleep(0.5)       
        ch0_data = self.firmata().i2c_get_read_data(self.ADDR)
        
        self.firmata().i2c_write(self.ADDR, self.REG_CHAN1_WORD)
        self.firmata().i2c_read(self.ADDR, self.REG_CHAN1_WORD, 2, self.firmata().I2C_READ)
        time.sleep(0.5)
        ch1_data = self.firmata().i2c_get_read_data(self.ADDR)
        
        
        if (ch0_data is not None):
            #ch0_raw = 256 * ch0_data[2] + ch0_data[1]
            self._Sensor__value = self.rawToLUX(ch0_data, ch1_data)
            return self.rawToLUX(ch0_data, ch1_data)
        
        else:
            self._Sensor__value = -1
        return -1