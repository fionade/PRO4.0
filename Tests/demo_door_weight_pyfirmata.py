# show welcome message
# connct to board
# enable reporting
# lopp: print data per pin

from pyfirmata import Arduino, util
import time
#import Adafruit_CharLCD as LCD

if __name__ == '__main__':
    
    # Initialize the LCD using the pins
    #lcd = LCD.Adafruit_CharLCDPlate()
    
    # Show intro
    #lcd.set_color(0.0, 0.0, 1.0)
    #lcd.clear()
    #lcd.message('PIP: Team Pro4.0\nDoor&Floormat')
    time.sleep(2.0)
    
    # config
    arduinoAddress = "/dev/tty.usbmodemfa141"
    
    # Seems necessary when using analog boards. See pyfirmata readme on github
    board = Arduino(arduinoAddress)
    it = util.Iterator(board)
    it.start()
    
    # Initialise pins
    pin = list();
    for x in range(0, 4):
        pin.append(board.get_pin('a:' + str(x) + ':a'))
        pin[x].enable_reporting()
    
    #Wait for pins to init
    time.sleep(0.5)
    
    time.sleep(1)

    while True:
        out = "Door " + str(pin[0].read())
        print(out)
        #lcd.clear()
        #lcd.message(out)
        time.sleep(1)
