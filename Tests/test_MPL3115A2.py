'''
Created on 05.02.2015

@author: fiona
'''

from PyMata.pymata import PyMata
import time

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


if __name__ == '__main__':
    arduinoAddress = "/dev/tty.usbmodemfa141"
    
    firmata = PyMata(arduinoAddress)
    firmata.i2c_config(0, firmata.DIGITAL, 21, 20)
    
    
    firmata.i2c_write(MPL3115_ADDR, MPL3115_CTRL_REG1, 0xB8)
    
    firmata.i2c_write(MPL3115_ADDR, MPL3115_PT_DATA_CFG, 0x07)
    
    firmata.i2c_write(MPL3115_ADDR, MPL3115_CTRL_REG1, 0xB9)
    
    time.sleep(1)
    
    while True:
    
        firmata.i2c_read(MPL3115_ADDR, MPL3115_STATUS, 1, firmata.I2C_READ)
    
        time.sleep(3)
        ctrl = firmata.i2c_get_read_data(MPL3115_ADDR)
        
        print(ctrl)
        
    
    