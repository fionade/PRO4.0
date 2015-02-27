'''
Created on 06.02.2015

@author: fiona
'''

import time
from PyMata.pymata import PyMata


LSM303_ADDRESS_ACCEL         = (0x32 >> 1)         # 0011001x
LSM303_ADDRESS_MAG           = (0x3C >> 1)         # 0011110x
LSM303_ID                    = (0b11010100)

LSM303_REGISTER_ACCEL_CTRL_REG1_A         = 0x20   # 00000111   rw
LSM303_REGISTER_ACCEL_CTRL_REG2_A         = 0x21   # 00000000   rw
LSM303_REGISTER_ACCEL_CTRL_REG3_A         = 0x22   # 00000000   rw
LSM303_REGISTER_ACCEL_CTRL_REG4_A         = 0x23   # 00000000   rw
LSM303_REGISTER_ACCEL_CTRL_REG5_A         = 0x24   # 00000000   rw
LSM303_REGISTER_ACCEL_CTRL_REG6_A         = 0x25   # 00000000   rw
LSM303_REGISTER_ACCEL_REFERENCE_A         = 0x26   # 00000000   r
LSM303_REGISTER_ACCEL_STATUS_REG_A        = 0x27   # 00000000   r
LSM303_REGISTER_ACCEL_OUT_X_L_A           = 0x28
LSM303_REGISTER_ACCEL_OUT_X_H_A           = 0x29
LSM303_REGISTER_ACCEL_OUT_Y_L_A           = 0x2A
LSM303_REGISTER_ACCEL_OUT_Y_H_A           = 0x2B
LSM303_REGISTER_ACCEL_OUT_Z_L_A           = 0x2C
LSM303_REGISTER_ACCEL_OUT_Z_H_A           = 0x2D
LSM303_REGISTER_ACCEL_FIFO_CTRL_REG_A     = 0x2E
LSM303_REGISTER_ACCEL_FIFO_SRC_REG_A      = 0x2F
LSM303_REGISTER_ACCEL_INT1_CFG_A          = 0x30
LSM303_REGISTER_ACCEL_INT1_SOURCE_A       = 0x31
LSM303_REGISTER_ACCEL_INT1_THS_A          = 0x32
LSM303_REGISTER_ACCEL_INT1_DURATION_A     = 0x33
LSM303_REGISTER_ACCEL_INT2_CFG_A          = 0x34
LSM303_REGISTER_ACCEL_INT2_SOURCE_A       = 0x35
LSM303_REGISTER_ACCEL_INT2_THS_A          = 0x36
LSM303_REGISTER_ACCEL_INT2_DURATION_A     = 0x37
LSM303_REGISTER_ACCEL_CLICK_CFG_A         = 0x38
LSM303_REGISTER_ACCEL_CLICK_SRC_A         = 0x39
LSM303_REGISTER_ACCEL_CLICK_THS_A         = 0x3A
LSM303_REGISTER_ACCEL_TIME_LIMIT_A        = 0x3B
LSM303_REGISTER_ACCEL_TIME_LATENCY_A      = 0x3C
LSM303_REGISTER_ACCEL_TIME_WINDOW_A       = 0x3D


LSM303_REGISTER_MAG_CRA_REG_M             = 0x00
LSM303_REGISTER_MAG_CRB_REG_M             = 0x01
LSM303_REGISTER_MAG_MR_REG_M              = 0x02
LSM303_REGISTER_MAG_OUT_X_H_M             = 0x03
LSM303_REGISTER_MAG_OUT_X_L_M             = 0x04
LSM303_REGISTER_MAG_OUT_Z_H_M             = 0x05
LSM303_REGISTER_MAG_OUT_Z_L_M             = 0x06
LSM303_REGISTER_MAG_OUT_Y_H_M             = 0x07
LSM303_REGISTER_MAG_OUT_Y_L_M             = 0x08
LSM303_REGISTER_MAG_SR_REG_Mg             = 0x09
LSM303_REGISTER_MAG_IRA_REG_M             = 0x0A
LSM303_REGISTER_MAG_IRB_REG_M             = 0x0B
LSM303_REGISTER_MAG_IRC_REG_M             = 0x0C
LSM303_REGISTER_MAG_TEMP_OUT_H_M          = 0x31
LSM303_REGISTER_MAG_TEMP_OUT_L_M          = 0x32


LSM303_MAGGAIN_1_3                        = 0x20  # +/- 1.3
LSM303_MAGGAIN_1_9                        = 0x40  # +/- 1.9
LSM303_MAGGAIN_2_5                        = 0x60  # +/- 2.5
LSM303_MAGGAIN_4_0                        = 0x80  # +/- 4.0
LSM303_MAGGAIN_4_7                        = 0xA0  # +/- 4.7
LSM303_MAGGAIN_5_6                        = 0xC0  # +/- 5.6
LSM303_MAGGAIN_8_1                        = 0xE0  # +/- 8.1

if __name__ == '__main__':
    arduinoAddress = "/dev/tty.usbmodemfa141"
    
    firmata = PyMata(arduinoAddress)
    firmata.i2c_config(0, firmata.DIGITAL, 21, 20)
    
    time.sleep(1)
    
    #Enable the accelerometer
    # write8(LSM303_ADDRESS_ACCEL, LSM303_REGISTER_ACCEL_CTRL_REG1_A, 0x27);
    firmata.i2c_write(LSM303_ADDRESS_ACCEL, LSM303_REGISTER_ACCEL_CTRL_REG1_A, 0x27)
    
    time.sleep(1)
    
    #Enable the magnetometer
    #write8(LSM303_ADDRESS_MAG, LSM303_REGISTER_MAG_MR_REG_M, 0x00);
    firmata.i2c_write(LSM303_ADDRESS_MAG, LSM303_REGISTER_MAG_MR_REG_M, 0x00)
    
    while True:
    
        # Read the accelerometer
        #Wire.beginTransmission((byte)LSM303_ADDRESS_ACCEL);
        #Wire.write(LSM303_REGISTER_ACCEL_OUT_X_L_A | 0x80);
        #Wire.endTransmission();
        #Wire.requestFrom((byte)LSM303_ADDRESS_ACCEL, (byte)6);    
        firmata.i2c_write(LSM303_ADDRESS_ACCEL, LSM303_REGISTER_ACCEL_OUT_X_L_A, 0x80)
        
#           Wire.beginTransmission((byte)LSM303_ADDRESS_ACCEL);
#   Wire.write(LSM303_REGISTER_ACCEL_OUT_X_L_A | 0x80);
#   Wire.endTransmission();
#   Wire.requestFrom((byte)LSM303_ADDRESS_ACCEL, (byte)6);
        
        time.sleep(1)
        
        firmata.i2c_read(LSM303_ADDRESS_ACCEL, LSM303_REGISTER_ACCEL_OUT_X_L_A, 6, firmata.I2C_READ)
        
        time.sleep(1)
    
        print(firmata.i2c_get_read_data(LSM303_ADDRESS_ACCEL))
