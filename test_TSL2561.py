#Quick n dirty test, to see how PyMata works with I2C Sensors
#TSL2561 is a two channel (visible and IR) light sensor
#I used PyMata because it was way better documented than PyFirmata
#To-Do: Add conversion from raw values to lux

import time

from PyMata.pymata import PyMata

##Constants copied from https://github.com/janheise/TSL2561/blob/master/TSL2561.py
ADDR_LOW                  = 0x29
ADDR_NORMAL               = 0x39
ADDR_HIGH                 = 0x49

READBIT                   = 0x01
COMMAND_BIT               = 0x80    # Must be 1
CLEAR_BIT                 = 0x40    # Clears any pending interrupt (write 1 to clear)
WORD_BIT                  = 0x20    # 1 = read/write word (rather than byte)
BLOCK_BIT                 = 0x10    # 1 = using block read/write

CONTROL_POWERON           = 0x03
CONTROL_POWEROFF          = 0x00

REGISTER_CONTROL          = 0x00
REGISTER_TIMING           = 0x01
REGISTER_THRESHHOLDL_LOW  = 0x02
REGISTER_THRESHHOLDL_HIGH = 0x03
REGISTER_THRESHHOLDH_LOW  = 0x04
REGISTER_THRESHHOLDH_HIGH = 0x05
REGISTER_INTERRUPT        = 0x06
REGISTER_CRC              = 0x08
REGISTER_ID               = 0x0A
REGISTER_CHAN0_LOW        = 0x0C
REGISTER_CHAN0_HIGH       = 0x0D
REGISTER_CHAN1_LOW        = 0x0E
REGISTER_CHAN1_HIGH       = 0x0F

REG_CHAN0_WORD = 0xAC
REG_CHAN1_WORD = 0xAE

INTEGRATIONTIME_13MS      = 0x00    # 13.7ms
INTEGRATIONTIME_101MS     = 0x01    # 101ms
INTEGRATIONTIME_402MS     = 0x02    # 402ms

GAIN_0X                   = 0x00    # No gain
GAIN_16X                  = 0x10    # 16x gain


firmata = PyMata("COM4")

addr = ADDR_NORMAL
firmata.i2c_config(0, firmata.DIGITAL, 21, 20)

#The sensor needs to be turned on by sending a certain byte
firmata.i2c_write(addr, COMMAND_BIT | WORD_BIT | REGISTER_CONTROL)
firmata.i2c_write(addr, CONTROL_POWERON)
time.sleep(0.5)

while True:
    firmata.i2c_write(addr, REG_CHAN0_WORD)
    firmata.i2c_read(addr, REG_CHAN0_WORD, 2, firmata.I2C_READ)

    #sleep to wait for the sensor to send back data
    time.sleep(0.1)
    ch0_data = firmata.i2c_get_read_data(addr)

    #data comes back as list of 3 ints, first is useless, second is least significant byte and third MSB
    ch0_raw = 256 * ch0_data[2] + ch0_data[1]


    firmata.i2c_write(addr, REG_CHAN1_WORD)
    firmata.i2c_read(addr, REG_CHAN1_WORD, 2, firmata.I2C_READ)

    #sleep to wait for the sensor to send back data
    time.sleep(0.1)
    ch1_data = firmata.i2c_get_read_data(addr)

    #data comes back as list of 3 ints, first is useless, second is least significant byte and third MSB
    ch1_raw = 256 * ch1_data[2] + ch1_data[1]

    print("CH0: " + str(ch0_raw) + " - " + "CH1: " + str(ch1_raw))
    #The sensor takes one measurement every 413ms, so the sum of sleeps should be at least about 0.5 seconds
    time.sleep(0.3)
