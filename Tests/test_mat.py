# !/usr/bin/python
# Continously display 4 analog inputs on LCD display to test weight sensor mat
# To test on laptop, remove all LCD commands and change serial port

import time

from pyfirmata import util

import Adafruit_CharLCD as LCD

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()

# Show intro
lcd.set_color(0.0, 0.0, 1.0)
lcd.clear()
lcd.message('PIP: Team Pro4.0\nWeight Sensormat')
time.sleep(2.0)

# Seems necessary when using analog boards. See pyfirmata readme on github
it = util.Iterator(board)
it.start()

# Initialise pins
pin = list();
for x in range(0, 4):
    pin.append(board.get_pin('a:' + str(x) + ':a'))
    pin[x].enable_reporting()

#Wait for pins to init
time.sleep(0.5)

#Display analog inputs 0..3 continously
while True:
    out = ""
    out = str.ljust(str(pin[0].read()), 6, "0") + "    " + str.ljust(str(pin[1])
    out += str.ljust(str(pin[2].read()), 6, "0") + "    " + str.ljust(str(pin[3])

    lcd.clear()
    lcd.message(out)
    time.sleep(1)