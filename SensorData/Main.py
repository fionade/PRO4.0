'''
Created on 22.01.2015

@author: fiona
'''
from PyMata.pymata import PyMata
#from i2cTemperatureSensor import i2cTemperatureSensor
from i2cLightSensor import i2cLightSensor
import time

# i2c definitions
ADDR_NORMAL               = 0x39

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

class Main(object):
    
    def __init__(self, arduinoAddress, dbAddress, sensors):
        # database/file
        self.__database = self.initDatabase(dbAddress)
        
        # board setup
        self.__firmata = PyMata(arduinoAddress)
        # initialise for i2c calls
        self.__firmata.i2c_config(0, self.__firmata.DIGITAL, 21, 20)
        
        # sensors
        # TODO: differentiate between different types of sensors
        self.__sensors = self.initSensors(sensors)
        
    
    def initDatabase(self, dbAddress):
        pass

    
    def initSensors(self, sensors):
        for s in sensors:
            # TODO: some sensor init function
            # on the sensor instance or globally for all?
            # how to get a device's address?
            print ("Setting up " + str(s))
            addr = s.getAddress()
            self.__firmata.i2c_write(addr, COMMAND_BIT | WORD_BIT | REGISTER_CONTROL)
            self.__firmata.i2c_write(addr, CONTROL_POWERON)
        time.sleep(0.5)

    
    def writeToDatabse(self, data):
        pass
 
    
    def loop(self):
        # iterate through all sensors, get their data (they should all implement a getData function, depending on their type
        # and write to file
        # print('listening')
        for s in sensors:
            addr = s.getAddress()
            self.__firmata.i2c_write(addr, REG_CHAN1_WORD)
            time.sleep(1)
            self.__firmata.i2c_read(addr, REG_CHAN1_WORD, 2, self.__firmata.I2C_READ)
            time.sleep(1)
            ch0_data = self.__firmata.i2c_get_read_data(addr)
            ch0_raw = 256 * ch0_data[2] + ch0_data[1]
            print(ch0_raw)
        time.sleep(1)


'''
PRELIMINARY AND SUBJECT TO CHANGE!!

Main functionality:
read configurations, initialise database and sensors
start loop to collect sensor data and write to database/file
'''
if __name__ == '__main__':
    
    # config
    arduinoAddress = "/dev/tty.usbmodemfa141"
    dbAddress = ""
    
    # list all attached sensors
    sensors = []
    #sensors.append(i2cTemperatureSensor("id", "type", "address"))
    sensors.append(i2cLightSensor(1, "light", 0x39))
    
    run = Main(arduinoAddress, dbAddress, sensors)
    
    while True:
        run.loop()

