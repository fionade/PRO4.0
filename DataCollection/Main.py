'''
Created on 11.03.2015

@author: fiona
'''

from PyMata.pymata import PyMata
import json
import mysql.connector as mariadb
import time
import sys
import signal
#from TSL2561 import TSL2561

def main():
    
    def loop():
        for aS in analogSensors:
            if (aS.getType() == "DTH22"):
                pass
            else:
                data = board.analog_read(analogSensors[aS])
            print(str(aS) + ": " + str(data))
            #writeToDatabase(str(aS), data)
            
        for dS in digitalSensors:
            data = board.digital_read(digitalSensors[dS])
            print(str(dS) + ": " + str(data))
            writeToDatabase(str(dS), data)
        
        time.sleep(1)
    
    def writeToDatabase(sensor_name, data):
        try:
            cursor.execute("INSERT INTO data (sensor,data) VALUES (%s,%s)", (sensor_name, data))
        except mariadb.Error as error:
            print("Error: {}".format(error))
            
        mariadb_connection.commit()
    
    def signal_handler(sig, frame):
        print('Quit')
        if board is not None:
            board.reset()
        if mariadb_connection is not None:
            mariadb_connection.close()
        sys.exit(0)

        
    #### main ####
    signal.signal(signal.SIGINT, signal_handler)
    
    
    sensors = []  
    with open("config_room.json") as json_file:
        try:
            sensors = json.load(json_file)
            
        except ValueError:
            print("Configuration error: JSON object could not be decoded.")
            exit()
    
    #### Arduino and i2c setup ####
    # for Fiona's computer
    arduinoAddress = "/dev/tty.usbmodemfa141"
    
    # for RaspPis. Make sure that the upper left USB socket is used
    #arduinoAddress = "/dev/ttyACM0"
    #arduinoAddress = "/dev/ttyACM1"
    
    # board setup
    board = PyMata(arduinoAddress)
    # initialise for i2c calls
    board.i2c_config(0, board.DIGITAL, 21, 20)
    #board.i2c_config(0, board.ANALOG, 4, 5)
    
    analogSensors = {}  
    for sensor in sensors["AnalogSensors"]:
        pinNr = int(sensor["pin"])
        analogSensors[sensor["name"] + "_" + sensor["type"]] = pinNr
        # enable reporting for the analog sensor
        board.set_pin_mode(pinNr, board.INPUT, board.ANALOG)
        
    digitalSensors = {}  
    for sensor in sensors["DigitalSensors"]:
        pinNr = int(sensor["pin"])
        digitalSensors[sensor["name"] + "_" + sensor["type"]] = pinNr
        # enable reporting for the analog sensor
        board.set_pin_mode(pinNr, board.INPUT, board.DIGITAL)
        
    #i2cSensors = {}
    for sensor in sensors["i2cSensors"]:
        if sensor["class"] is "TSL2561":
            pass
            # i2cSensors[sensor["name"] + "_" + sensor["type"]] = TSL2561(board, [])
        elif sensor["class"] is "TCS2600":
            pass
        elif sensor["class"] is "MPL3115A2":
            pass
        else:
            print("Unknown i2c sensor.")
    
    # database/file
    #mariadb_connection = mariadb.connect(user='room', host='192.168.0.10', password='room', database='room')
    #mariadb_connection = mariadb.connect(user='cnc', host='192.168.0.10', password='cnc', database='cnc')
    #mariadb_connection = mariadb.connect(user='laser', host='192.168.0.10', password='laser', database='laser')
    mariadb_connection = mariadb.connect(user='test', password='test', database='test', host='192.168.0.10')
    #mariadb_connection = mariadb.connect(user='test', password='test', database='test', host='localhost')
    cursor = mariadb_connection.cursor()
        
    while True:
        try:
            loop()
        
        except KeyboardInterrupt:
            mariadb_connection.close()

if __name__ == '__main__':
    main()