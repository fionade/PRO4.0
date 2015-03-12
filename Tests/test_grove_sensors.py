'''
Created on 10.01.2015

@author: fiona
'''

import csv
import time
import pyfirmata
import math
from time import sleep
import os.path

PORT = '/dev/tty.usbmodemfa141'
#PINS = (0, 1, 2, 3)


def writeDataToFile(csvfile, csvwriter, temperature='NA', light='NA', sound='NA'):
    print()
    csvwriter.writerow([time.time(), temperature, sound])
    csvfile.flush()

if __name__ == '__main__':
    
    # init file for output
    # check if it exists
    fileExists = False
    if os.path.isfile('sensordata.csv'):
        fileExists = True
        
    csvfile = open('sensordata.csv', 'a')
    csvwriter = csv.writer(csvfile, delimiter=';')
    
    if not fileExists:
        csvwriter.writerow(['time', 'temperature', 'light', 'sound'])
    
    board = pyfirmata.ArduinoMega(PORT)
    print "Setting up the connection to the board ..."
    print(board)
    it = pyfirmata.util.Iterator(board)
    it.start()
    
    # Start reporting for defined pins
    # temperature at a0
    board.analog[0].enable_reporting()
    #sda = board.get_pin("d:20:p")
    #sda.enable_reporting()
    # temperature definitions
    B = 3975;
    
    # light at a1
    board.analog[1].enable_reporting()
    # sound at a2
    board.analog[2].enable_reporting()
    sleep(1)
    
    # Loop for reading the input.
    try:
        while True:

            #print(sda.read())
            # TEMPERATURE
            a = board.analog[0].read()
            if (a != 0.0):
                resistance=(float)((1 - a) * 10000/a)
                temperature = 1/(math.log(resistance/10000)/B + 1/298.15) - 273.15
                print(temperature)
            
            # LIGHT
            # 0 = low intensity, 1 high
            light = board.analog[1].read()
            # to bits
            # 900 > 100 LUX
            # 800 ~80
            
            # SOUND
            sound = board.analog[2].read()
                
            #writeDataToFile(csvfile, csvwriter, temperature, light, sound)
            
            board.pass_time(1)
    
    except KeyboardInterrupt:
        board.exit()
        csvfile.close()
        exit()