# show welcome message
# connct to board
# enable reporting
# lopp: print data per pin

from PyMata.pymata import PyMata
import time
#import Adafruit_CharLCD as LCD

if __name__ == '__main__':
    
    # Initialize the LCD using the pins
    #lcd = LCD.Adafruit_CharLCDPlate()
    
    # Show intro
    #lcd.set_color(0.0, 0.0, 1.0)
    #lcd.clear()
    #lcd.message('PIP: Team Pro4.0\nWeight Sensormat')
    print('PIP: Team Pro4.0\nWeight and Door')
    time.sleep(2.0)
    
    # config
    arduinoAddress = "/dev/tty.usbmodemfa141"
    
    # board setup
    firmata = PyMata(arduinoAddress)
    
    # door on pin A0
    firmata.enable_analog_reporting(0)
    # weight mat on pin A2
    firmata.enable_analog_reporting(2)
    
    time.sleep(1)

    while True:
        out = "Door " + str(firmata.analog_read(0)) + "\n"
        #out = "Weight " + str(firmata.analog_read(2))
        #lcd.clear()
        #lcd.message(out)
        print(out)
        time.sleep(1)