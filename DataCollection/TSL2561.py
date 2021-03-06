'''
Created on 12.03.2015

@author: fiona
'''
from i2cSensor import i2cSensor

class TSL2561(object):
    '''
    Class for use of the light sensor TSL2561 with the pyMata library.
    '''
    
    
    # i2c definitions
    # refer to https://github.com/janheise/TSL2561/
    ADDR = 0x39

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
    INTEGRATIONTIME_101MS     = 0x01    # 101ms
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


    def __init__(self, board, params):
        '''
        Constructor
        '''
        i2cSensor.__init__(self, board, params)
        
    def initCommunication(self):
        board = self.getBoard()
        # enable the sensor
        board.i2c_write(self.ADDR, self.COMMAND_BIT | self.WORD_BIT | self.REGISTER_CONTROL)
        board.i2c_write(self.ADDR, self.CONTROL_POWERON)
        
        # set gain and timing
        board.i2c_write(self.ADDR, self.COMMAND_BIT | self.REGISTER_TIMING, self.INTEGRATIONTIME_402MS | self.GAIN_16X)
        
    def requestRead(self):
        board = self.getBoard()
        board.i2c_write(self.ADDR, self.REG_CHAN0_WORD)
        board.i2c_read(self.ADDR, self.REG_CHAN0_WORD, 4, self.firmata().I2C_READ)
    
    def getData(self):
        board = self.getBoard()
        return(board.i2c_get_read_data(self.ADDR))