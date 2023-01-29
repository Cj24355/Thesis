import machine
from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)     #initializing the I2C method for ESP32
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)       #initializing the I2C method for ESP8266

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

# Define the up and down button pins
up_button = Pin(12, Pin.IN, Pin.PULL_UP)
down_button = Pin(13, Pin.IN, Pin.PULL_UP)

# Define the menu options
menu_options = ["Option 1", "Option 2"]

# Set the initial menu index
current_option = 0


# Clear the LCD screen
lcd.clear()
# Print the menu options with a cursor indicating the current option

    # Check if the up button is pressed
    
while True:
    for i, option in enumerate(menu_options):
        if i == current_option:
            lcd.move_to(i*16, 0)
            lcd.putstr("> " + option)
        else:
            lcd.move_to(i*16, 0)
            lcd.putstr("  " + option)
    sleep(10)
    if not up_button.value():
        current_option = max(current_option - 1, 0)
    if not down_button.value():
        current_option = min(current_option + 1, len(menu_options) - 1)