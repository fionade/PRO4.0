'''
Created on 03.03.2015

@author: fiona
'''
from PyMata.pymata import PyMata
import time

if __name__ == '__main__':
    
    # config
    arduinoAddress = "/dev/tty.usbmodemfa141"
    
    # board setup
    firmata = PyMata(arduinoAddress)
    
    firmata.enable_analog_reporting(0)

    while True:
        print(firmata.analog_read(0))
        time.sleep(0.5)

