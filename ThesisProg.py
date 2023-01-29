from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep

# Initiate The Size and the Address of the LCD

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)     #initializing the I2C method for ESP32
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)       #initializing the I2C method for ESP8266

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

button_up = Pin(12, Pin.IN)
button_down = Pin(14, Pin.IN)
button_select = Pin(27, Pin.IN)


menu = ["TIME OF FEEDING", "KILOGRAM/GRAMS", "START OPERATION"]
options_menu = 0

while True:
    if button_up.value() == True:
        lcd.clear()
        options_menu = max(options_menu - 1, 0)
        lcd.move_to(0, 0)
        lcd.putstr(f"{menu[options_menu]}")
    if button_down.value() == True:
        lcd.clear()
        options_menu = min(options_menu + 1, len(menu) -1)
        lcd.move_to(0, 0)
        lcd.putstr(f"{menu[options_menu]}")
