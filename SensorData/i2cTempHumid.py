'''
Created on 09 Mar 2015

@author: dorienhuysmans
'''
# reference:https://github.com/DexterInd/GrovePi/blob/master/Software/Python/grovepi.py
############################################################################/
###        Including Files                                               ###/
############################################################################/

from i2cSensor import i2cSensor
import time
# import thread

############################################################################/
###        Macro Definitions                                             ###/
############################################################################/

TH02_I2C_DEV_ID  =    0x40
REG_STATUS        =   0x00 
REG_DATA_H        =   0x01
REG_DATA_L         =  0x02
REG_CONFIG          = 0x03
REG_ID              = 0x11
 
STATUS_RDY_MASK    =  0x01    #poll RDY,0 indicate the conversion is done
 
CMD_MEASURE_HUMI  =   0x01    #perform a humidity measurement
CMD_MEASURE_TEMP  =   0x11    #perform a temperature measurement
 
TH02_WR_REG_MODE   =   0xC0
TH02_RD_REG_MODE   =   0x80

############################################################################/
###        Class Definition                                              ###/
############################################################################/


class i2cTempHumid(i2cSensor):

    def __init__(self, name, sensorType, firmata):
        '''
        Constructor
        '''
        i2cSensor.__init__(self, name, sensorType, firmata)
      
          
    def getCurrentData(self):
        raise NotImplementedError("Not implemented")
      
    def initCommunication(self):
        time.sleep(0.6)

        self._Sensor__running = True
        self.poll()    
        
    def poll(self):
        while self._Sensor__running:
            
            self.firmata().i2c_write(TH02_I2C_DEV_ID, TCS34725_COMMAND_BIT | TCS34725_ENABLE) # 0x00 = ENABLE register

            self.firmata().i2c_read(TH02_I2C_DEV_ID, TCS34725_COMMAND_BIT | TCS34725_ID, 1, self.firmata().I2C_READ)
            data = self.firmata().i2c_get_read_data(TH02_I2C_DEV_ID)






        self.firmata().i2c_read(TCS34725_ADDRESS, TCS34725_COMMAND_BIT | TCS34725_ID, 1, self.firmata().I2C_READ)
        time.sleep(1)
 
        ver = self.firmata().i2c_get_read_data(TCS34725_ADDRESS)
        time.sleep(1)
         
        ver = ver[1]
        print ("version is")
        print ver 
        print ("(decimal) ...")
 
        if (ver == 0x44):
            print ("Connection Established")
        else :
            print ("No Connection")
              
      
        self.firmata().i2c_write(TCS34725_ADDRESS, TCS34725_COMMAND_BIT | TCS34725_ENABLE) # 0x00 = ENABLE register
        self.firmata().i2c_write(TCS34725_ADDRESS, TCS34725_ENABLE_PON | TCS34725_ENABLE_AEN) # 0x01 = Power on, 0x02 RGB sensors enabled
        self.firmata().i2c_write(TCS34725_ADDRESS, TCS34725_COMMAND_BIT | TCS34725_CDATAL) # Reading results start register 14, LSB then MSB



    def read(self):





# Read and return temperature and humidity from Grove DHT Pro
def dht(pin, module_type):
    write_i2c_block(address, dht_temp_cmd + [pin, module_type, unused])

    # Delay necessary for proper reading fron DHT sensor
    time.sleep(.6)
    try:
        read_i2c_byte(address)
        number = read_i2c_block(address)
        if number == -1:
            return -1
    except (TypeError, IndexError):
        return -1
    # data returned in IEEE format as a float in 4 bytes
    f = 0
    # data is reversed
    for element in reversed(number[1:5]):
        # Converted to hex
        hex_val = hex(element)
        #print hex_val
        try:
            h_val = hex_val[2] + hex_val[3]
        except IndexError:
            h_val = '0' + hex_val[2]
        # Convert to char array
        if f == 0:
            h = h_val
            f = 1
        else:
            h = h + h_val
    # convert the temp back to float
    t = round(struct.unpack('!f', h.decode('hex'))[0], 2)

    h = ''
    # data is reversed
    for element in reversed(number[5:9]):
        # Converted to hex
        hex_val = hex(element)
        # Print hex_val
        try:
            h_val = hex_val[2] + hex_val[3]
        except IndexError:
            h_val = '0' + hex_val[2]
        # Convert to char array
        if f == 0:
            h = h_val
            f = 1
        else:
            h = h + h_val
    # convert back to float
    hum = round(struct.unpack('!f', h.decode('hex'))[0], 2)
    return [t, hum]