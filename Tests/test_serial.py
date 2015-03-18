'''
Created on 12.03.2015

@author: fiona
'''

import serial

def main():
    #### Arduino and i2c setup ####
    # for Fiona's computer
    ser = serial.Serial('/dev/tty.usbmodemfa141', 9600)
    
    while True:
        print ser.readline()

if __name__ == '__main__':
    main()